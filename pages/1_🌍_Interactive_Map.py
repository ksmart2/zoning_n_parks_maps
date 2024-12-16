import streamlit as st
import geopandas as gpd
import folium
import leafmap.foliumap as leafmap
from folium import LinearColormap

# Set up Streamlit
st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Density Map")

with st.expander("See source code"):
    with st.echo():
        
        # Initialize the map centered on Knoxville
        m = leafmap.Map(center=[35.9606, -83.9207], zoom=12)

        # Link to the raw data for buffer zones
        buffer_url = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/buffer_zones.%20(2).geojson"

        # Read the GeoJSON as a GeoDataFrame to assign color scale values
        buffer_gdf = gpd.read_file(buffer_url)

        # Apply a color scale to the park_counts values 
        color_scale = LinearColormap(['gray', 'orange', 'pink', 'purple'], vmin=buffer_gdf['park_counts'].min(), vmax=buffer_gdf['park_counts'].max())

        # Convert GeoDataFrame to GeoJSON
        buffer_geojson = buffer_gdf.to_json()

        # Add the GeoJSON layer to the map 
        folium.GeoJson(
            buffer_geojson,
            name="Buffer Zones with Park Counts",
            style_function=lambda feature: {
                'fillColor': color_scale(feature['properties']['park_counts']),
                'color': 'black',
                'weight': 0.5,
                'fillOpacity': 0.6
            }
        ).add_to(m)

        # Add the color scale legend to the map
        color_scale.add_to(m)

        # Add the park data for park reference 
        parks = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/parks_gdf%20(1).geojson"
        m.add_geojson(parks, layer_name="Park Locations", style={"color": "yellow"})
        legend = {
                    "Parks": "yellow",
                }
        m.add_legend(title="Map Legend", legend_dict=legend)


m.to_streamlit(height=700)
