import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
The accessibility of the public parks in
the City of Knoxville, Tennessee within
the different residential zones.
"""

st.sidebar.title("About")
st.sidebar.info(markdown)


st.title("Interactive Map of Knoxville Parks and Zoning Areas")
st.markdown("""
This map is an interactive map plotted using folium. This map includes the residential zones and their boundaries in blue, and the park locations and their boundaries in red. The user is able to click each zone and see all the related information for that zone from each dataset. 
""")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[35.9606, -83.9207], zoom=12)
        parks = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/parks_gdf%20(1).geojson"
        zoning = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/zoning_gdf.geojson"

        m.add_geojson(zoning, layer_name="Zoning Areas", style={"color": "blue"})
        m.add_geojson(parks, layer_name="Park Locations", style={"color": "red"})

        legend = {
            "Parks": "red",
            "Residential Zones": "blue"
        }
m.add_legend(title="Map Legend", legend_dict=legend)

m.to_streamlit(height=700)
