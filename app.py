from flask import Flask, render_template
import folium
import json

app = Flask(__name__)

@app.route('/')
def pendant_map():
    """
    Main page displaying medieval pendants on an interactive map
    Similar to Spurlock Museum blog posts but with embedded map
    """
    
    # Load pendant data
    with open('data/pendants.json', 'r') as f:
        pendants = json.load(f)
    
    # Create the map centered on Europe (adjust as needed)
    m = folium.Map(
        location=[48.0, 10.0],  # Central Europe
        zoom_start=4,
        tiles='OpenStreetMap'
    )
    
    # Add markers for each pendant
    for pendant in pendants:
        popup_html = f"""
        <div style="width: 200px;">
            <h4>{pendant['name']}</h4>
            <p><strong>Period:</strong> {pendant['period']}</p>
            <p><strong>Origin:</strong> {pendant['origin']}</p>
            <p>{pendant['description']}</p>
            <a href="{pendant['collection_link']}" target="_blank">View in Collection</a>
        </div>
        """
        
        folium.Marker(
            location=[pendant['lat'], pendant['lon']],
            popup=folium.Popup(popup_html, max_width=250),
            tooltip=pendant['name'],
            icon=folium.Icon(color='orange', icon='info-sign')
        ).add_to(m)
    
    # Generate map HTML
    map_html = m._repr_html_()
    
    return render_template(
        'pendant_map.html',
        map_html=map_html,
        pendants=pendants,
        title="Medieval Pendants: A Geographic Journey",
        author="David [Your Name]",
        date="January 2026",
        reading_time="10 minute read"
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
