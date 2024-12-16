import streamlit as st
import geopandas as gpd
import folium
import leafmap.foliumap as leafmap
import json
from shapely.geometry import mapping  # Import mapping from shapely

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
        parks_url = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/parks_gdf%20(1).geojson"
        zoning_url = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/zoning_gdf.geojson"

        # Load the data into GeoDataFrames
        parks_gdf = gpd.read_file(parks_url)
        zoning_gdf = gpd.read_file(zoning_url)

        # Create centroid for parks and add a buffer zone for zoning
        parks_gdf['centroid'] = parks_gdf.geometry.centroid
        zoning_gdf['buffer'] = zoning_gdf.geometry.buffer(1000)  # 1000 meters buffer
        parks_centroids_gdf = gpd.GeoDataFrame(parks_gdf, geometry='centroid')
        zones_gdf_buffered = zoning_gdf.set_geometry('buffer')

        # Spatial join to count parks within buffer zones
        intersects = gpd.sjoin(parks_cent
