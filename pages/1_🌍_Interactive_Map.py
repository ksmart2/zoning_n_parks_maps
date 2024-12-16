import streamlit as st
import geopandas as gpd
import folium
import leafmap.foliumap as leafmap
import json

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
        intersects = gpd.sjoin(parks_centroids_gdf, zones_gdf_buffered, predicate='within')
        park_counts = intersects.groupby('index_right').size()

        # Replace NaN values for zones with no parks
        zoning_gdf['park_counts'] = zoning_gdf.index.map(park_counts).fillna(0)

        # Remove the buffer column
        zones_gdf = zoning_gdf.drop(columns='buffer')

        # Reproject back into EPSG:4326 for proper lat/lon coordinates
        zones_gdf = zones_gdf.to_crs(epsg=4326)

        # Convert the geometries to GeoJSON format (solves the serialization issue)
        parks_geojson = parks_gdf.geometry.apply(lambda x: json.loads(x.to_json())).to_list()
        zoning_geojson = zoning_gdf.geometry.apply(lambda x: json.loads(x.to_json())).to_list()

        # Add zoning data to the map, styled by park_counts
        folium.GeoJson(zoning_geojson).add_to(m)

        # Add parks data (centroids) to the map
        folium.GeoJson(parks_geojson).add_to(m)

# Display the map in Streamlit
m.to_streamlit(height=700)
