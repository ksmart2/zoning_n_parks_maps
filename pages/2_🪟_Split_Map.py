import streamlit as st
import folium
import geopandas as gpd
from streamlit_folium import st_folium

# URL to the GeoJSON file in your GitHub repo (replace this with your actual URL)
geojson_url = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/parks_gdf.geojson"

# Load the GeoDataFrame from the URL
gdf = gpd.read_file(geojson_url)

# Create a folium map centered on a specific location (for example, Knoxville, TN)
m = folium.Map(location=[35.9606, -83.9207], zoom_start=12)

# Add the GeoDataFrame to the map as a layer
folium.GeoJson(gdf).add_to(m)

# Display the map in Streamlit using st_foliu
st.title("Interactive Map of Parks & Zoning Datasets")
st_folium(m, width=700, height=500)

