import streamlit as st
import geopandas as gpd
import folium
import leafmap.foliumap as leafmap
from folium import LinearColormap

# Set up Streamlit
st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
The accessibility of the public parks in
the City of Knoxville, Tennessee within
the different residential zones.
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Density Map")
st.markdown("""
This map was designed to display the density of park locations within 400 meters of each residential zone. To calculate the park density for each residential area, a buffer was created around each residential zone using .buffer(). The buffer size was set to 400 meters, which is a reasonable walking distance to access a park. Since parks are represented as polygons and multipolygons, the centroid of each park was calculated to transform the geometry type into a POINT type. The POINT type is required for spatial joins. A spatial join was performed between the park centroids and the buffered residential zones. To do this, gpd.sjoin was used with the parameter predicate=’within’ to only count parks that are within the 1 kilometer buffer zone for each residential zone. After the join, each residential zone now has a count of how many parks are within 400 meters,  creating the density measure to be plotted on the map. On the map, the darker colors represent higher density of park locations per residential zone, while the lighter zones in red and orange have lower density, and zones in yellow have 0 parks within 400 meters.
""")

with st.expander("See source code"):
    with st.echo():
        
        # Initialize the map centered on Knoxville
        m = leafmap.Map(center=[35.9606, -83.9207], zoom=12)

        # Link to the raw data for buffer zones
        buffer_url = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/buffer_zones.%20(2).geojson"

        # Read the GeoJSON as a GeoDataFrame to assign color scale values
        buffer_gdf = gpd.read_file(buffer_url)

        # Apply a color scale to the park_counts values 
        color_scale = LinearColormap(['gray', 'yellow', 'green', 'blue'], vmin=buffer_gdf['park_counts'].min(), vmax=buffer_gdf['park_counts'].max())

        # Convert GeoDataFrame to GeoJSON
        buffer_geojson = buffer_gdf.to_json()

        # Add the GeoJSON layer to the map 
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

        # Add the park data for park reference 
        parks = "https://raw.githubusercontent.com/ksmart2/zoning_n_parks_maps/refs/heads/main/parks_gdf%20(1).geojson"
        m.add_geojson(parks, layer_name="Park Locations", style={"color": "orange"})
        legend = {
                    "Parks": "orange",
                }
        m.add_legend(title="Map Legend", legend_dict=legend)


m.to_streamlit(height=700)
