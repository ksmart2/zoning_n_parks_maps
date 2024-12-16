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

        # URLs for the GeoJSON data
        buffer_url = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/buffer_zones.%20(2).geojson"

        # Load the data into GeoDataFrames
        buffer_gdf = gpd.read_file(buffer_url)

        # Check the range of values in 'park_counts'
        st.write(buffer_gdf['park_counts'].describe())  # Check the range and distribution

        # Apply a color scale to the park_counts values
        # Define the color scale (adjust min/max values based on your data distribution)
        color_scale = LinearColormap(['gray', 'yellow', 'green', 'blue'], vmin=buffer_gdf['park_counts'].min(), vmax=buffer_gdf['park_counts'].max())

        # Convert GeoDataFrame to GeoJSON
        buffer_geojson = buffer_gdf.to_json()

        # Add the GeoJSON layer to the map with custom color styling
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

# Display the map in Streamlit
m.to_streamlit(height=700)
