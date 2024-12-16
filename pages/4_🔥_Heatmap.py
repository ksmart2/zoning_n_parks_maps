import streamlit as st
import leafmap.foliumap as leafmap
import folium
import geopandas as gpd

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Heatmap")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map(center=[35.9606, -83.9207], zoom=12)
        geojson_url = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/i_counts_geom_gdf%20(1).geojson"
        i_counts_geom_gdf = gpd.read_file(geojson_url)

        
        m.add_heatmap(
            i_counts_geom_gdf,
            value="Count",
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)
