# Medieval Pendants Map - Spurlock Museum Style

This Flask application creates an interactive map page for medieval pendants, styled to match the Spurlock Museum website.

## Project Structure

```
pendant_map_project/
├── app.py                          # Main Flask application
├── templates/
│   ├── base.html                   # Base template with header/footer
│   └── pendant_map.html            # Main pendant map page
├── static/
│   ├── css/
│   │   └── spurlock_style.css      # CSS matching Spurlock Museum design
│   └── images/                     # Place pendant images here
├── data/
│   └── pendants.json               # Pendant data (location, description, etc.)
└── README.md                       # This file
```

## Setup Instructions

### 1. Install Required Packages

```bash
pip install flask folium
```

### 2. Run the Application

Navigate to the project directory and run:

```bash
cd pendant_map_project
python app.py
```

The application will start on `http://localhost:5000`

### 3. View in Browser

Open your browser and go to:
```
http://localhost:5000
```

## Customization

### Adding Your Pendant Data

Edit `data/pendants.json` to add your actual pendant information:

```json
{
    "name": "Your Pendant Name",
    "period": "12th Century",
    "origin": "Location, Country",
    "lat": 48.8566,
    "lon": 2.3522,
    "description": "Description of the pendant",
    "collection_link": "/collections/your-pendant-id"
}
```

### Adding Images

1. Place images in `static/images/`
2. Uncomment and update the hero image line in `pendant_map.html`
3. Replace the placeholder divs in the gallery with actual images

### Modifying Colors

The CSS uses CSS variables for easy customization. Edit `spurlock_style.css`:

```css
:root {
    --illinois-orange: #FF5F05;
    --illinois-blue: #13294B;
    /* Adjust these to match exact colors */
}
```

## Integration with Live Spurlock Site

When ready to deploy to the actual Spurlock website:

1. **Extract the HTML**: The templates generate static HTML that can be integrated into the existing CMS
2. **CSS Integration**: Copy the CSS rules from `spurlock_style.css` into the site's existing stylesheet
3. **Map Generation**: You can generate the map HTML offline and embed it as static content
4. **Backend**: If the Spurlock site uses PHP, you can convert the Flask routes to PHP equivalents

## Features Matching Spurlock Design

- ✅ University of Illinois color scheme (orange/blue)
- ✅ Blog post layout with metadata (date, author, reading time)
- ✅ Tag system
- ✅ Breadcrumb navigation
- ✅ Image gallery with captions
- ✅ Collection object links
- ✅ Resources section
- ✅ Responsive design
- ✅ Interactive map with popups

## Development Workflow

1. **Prototype in Colab** (if desired):
   - Test Folium map generation
   - Experiment with marker styles
   - Export map HTML

2. **Build Locally with Flask**:
   - Use PyCharm or VS Code
   - Run `python app.py` to test
   - Iterate on design

3. **Deploy to Production**:
   - Coordinate with Spurlock web team
   - Provide generated HTML/CSS
   - Integrate into existing CMS

## Next Steps

- [ ] Replace sample data with actual pendant information
- [ ] Add real pendant images
- [ ] Get exact color codes from Spurlock's brand guidelines
- [ ] Add more interactive features to the map
- [ ] Create additional pages if needed
- [ ] Test on different screen sizes
- [ ] Coordinate deployment with museum IT

## Contact

For questions about deployment to the live Spurlock site, contact the museum's web administrator.
