import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Interactive Map of Knoxville Parks and Zoning Areas")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[35.9606, -83.9207], zoom=12)
        parks = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/parks_gdf.geojson"
        zoning = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/zoning_gdf.geojson"

        m.add_geojson(zoning, layer_name="Zoning Areas", style={"color": "blue"})
        m.add_geojson(parks, layer_name="Park Locations", style={"color": "pink"})

        legend = {
            "Parks": "pink",
            "Residential Zones": "blue"
        }
m.add_legend(title="Map Legend", legend_dict=legend)

m.to_streamlit(height=700)
