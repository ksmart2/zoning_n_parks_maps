import streamlit as st
import geopandas as gpd
import folium
import leafmap.foliumap as leafmap

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
        buffer = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/buffer_zones.%20(2).geojson"

        

        m.add_geojson(buffer, layer_name="Buffer Zones with Park Counts")
      

m.to_streamlit(height=700)
