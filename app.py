from flask import Flask, render_template, jsonify, request
import folium
from folium import plugins
import json

app = Flask(__name__)


def load_pendants():
    """Load pendant data from JSON file"""
    with open('data/pendants.json', 'r') as f:
        pendants = json.load(f)

    # Extract century information for each pendant
    for pendant in pendants:
        period = pendant['period']
        century = int(''.join(filter(str.isdigit, period.split()[0])))
        pendant['century'] = century

    return pendants


def get_filter_options(pendants):
    """Extract all unique filter options from pendant data"""
    shapes = sorted(list(set(p['shape'] for p in pendants)))
    materials = sorted(list(set(p['material'] for p in pendants)))
    regions = sorted(list(set(p['region'] for p in pendants)))
    sizes = sorted(list(set(p['size'] for p in pendants)))
    functions = sorted(list(set(p['function'] for p in pendants)))

    # Get all unique preservation statuses
    preservation_statuses = set()
    for p in pendants:
        preservation_statuses.update(p['preservation'])
    preservation_statuses = sorted(list(preservation_statuses))

    centuries = sorted(list(set(p['century'] for p in pendants)))

    return {
        'shapes': shapes,
        'materials': materials,
        'regions': regions,
        'sizes': sizes,
        'functions': functions,
        'preservation_statuses': preservation_statuses,
        'centuries': centuries,
        'min_century': min(centuries),
        'max_century': max(centuries)
    }


@app.route('/')
def pendant_map():
    """
    Main page displaying medieval pendants on an interactive map
    with comprehensive filtering options
    """
    pendants = load_pendants()
    filter_options = get_filter_options(pendants)

    # Create the map centered on Europe
    m = folium.Map(
        location=[48.0, 10.0],
        zoom_start=4,
        tiles='OpenStreetMap'
    )

    # Add all pendants to the map
    for pendant in pendants:
        # Create data attributes for filtering
        data_attrs = f"""data-century="{pendant['century']}" 
                        data-shape="{pendant['shape']}" 
                        data-material="{pendant['material']}" 
                        data-region="{pendant['region']}"
                        data-size="{pendant['size']}"
                        data-function="{pendant['function']}"
                        data-preservation="{','.join(pendant['preservation'])}" """

        popup_html = f"""
        <div style="width: 250px;">
            <h4>{pendant['name']}</h4>
            <p><strong>Period:</strong> {pendant['period']}</p>
            <p><strong>Origin:</strong> {pendant['origin']}</p>
            <p><strong>Shape:</strong> {pendant['shape']}</p>
            <p><strong>Material:</strong> {pendant['material']}</p>
            <p><strong>Size:</strong> {pendant['size'].capitalize()}</p>
            <p><strong>Function:</strong> {pendant['function'].replace('_', ' ').title()}</p>
            <p><strong>Preservation:</strong> {', '.join([s.capitalize() for s in pendant['preservation']])}</p>
            <p style="margin-top:10px;">{pendant['description']}</p>
            <a href="{pendant['collection_link']}" target="_blank">View in Collection</a>
        </div>
        """

        folium.Marker(
            location=[pendant['lat'], pendant['lon']],
            popup=folium.Popup(popup_html, max_width=280),
            tooltip=f"{pendant['name']} ({pendant['period']})",
            icon=folium.Icon(color='orange', icon='info-sign')
        ).add_to(m)

    # Generate map HTML
    map_html = m._repr_html_()

    return render_template(
        'pendant_map.html',
        map_html=map_html,
        pendants=pendants,
        pendants_json=json.dumps(pendants),
        filter_options=filter_options,
        title="Medieval Pendants: A Geographic Journey",
        author="David Eby",
        date="January 2026",
        reading_time="10 minute read"
    )


@app.route('/api/filter-pendants', methods=['POST'])
def filter_pendants():
    """
    API endpoint to filter pendants based on multiple criteria
    """
    filters = request.json
    pendants = load_pendants()

    filtered = []
    for pendant in pendants:
        # Check century
        if filters.get('century') and pendant['century'] != filters['century']:
            continue

        # Check shape
        if filters.get('shapes') and pendant['shape'] not in filters['shapes']:
            continue

        # Check material
        if filters.get('materials') and pendant['material'] not in filters['materials']:
            continue

        # Check region
        if filters.get('regions') and pendant['region'] not in filters['regions']:
            continue

        # Check size
        if filters.get('sizes') and pendant['size'] not in filters['sizes']:
            continue

        # Check function
        if filters.get('functions') and pendant['function'] not in filters['functions']:
            continue

        # Check preservation (pendant must have ALL selected preservation statuses)
        if filters.get('preservation_statuses'):
            if not all(status in pendant['preservation'] for status in filters['preservation_statuses']):
                continue

        filtered.append(pendant)

    return jsonify(filtered)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
