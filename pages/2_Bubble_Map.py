import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import folium


st.set_page_config(layout="wide")

markdown = """
The accessibility of the public parks in
the City of Knoxville, Tennessee within
the different residential zones.
"""

st.sidebar.title("About")
st.sidebar.info(markdown)


st.title("Interactive Bubble Map for Count of Residential Zones That Intersect A Park Location")
st.markdown("""
An interactive bubble map was created to visualize the count of residential zones that intersect park locations. This map utilizes the count of residential zone intersects per park location. The bubble size provides a visual representation of the usefulness of each park. The size of each circle is proportional to the number of residential zones that intersect a park boundary. The map was made to be interactive so the user can click each circle to view the park name and the count of residential zones it services. This map reveals several patterns. The first, is that areas closer to downtown Knoxville tend to have more park locations. Additionally, parks in South Knoxville appear to service, on average, a larger number of residential zones than those in other parts of the city. This highlights a geographic trend in park accessibility. 
""")
with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[35.9606, -83.9207], zoom=12)
        geojson_url = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/i_counts_geom_gdf%20(1).geojson"
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
