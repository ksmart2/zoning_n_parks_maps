import streamlit as st
import leafmap.foliumap as leafmap
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

st.title("Interactive Bubble Map for Count of Residential Zones That Intersect A Park Location")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[35.9606, -83.9207], zoom=12)
        geojson_url = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/i_counts_geom_gdf.geojson"
        i_counts_geom_gdf = gpd.read_file(geojson_url)

        for _, row in i_counts_geom_gdf.iterrows():
            folium.CircleMarker(
                location=[row.geometry.centroid.y, row.geometry.centroid.x],
                radius=row['Count'] * 3,
                color="green",
                fill=True,
                fill_color="green",
                fill_opacity=0.6,
                popup=f"Park: {row['NAME']}<br>Count: {row['Count']}",
            ).add_to(m)


m.to_streamlit(height=700)
