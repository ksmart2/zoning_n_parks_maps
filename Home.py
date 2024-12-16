import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
The accessibility of the public parks in
the City of Knoxville, Tennessee within
the different residential zones.
"""

st.sidebar.title("About")
st.sidebar.info(markdown)

# Customize page title
st.title("Park Accessibility for Residential Zones in Knoxville, TN")

st.markdown(
    """
    The goal of this project was to assess the accessibility of the public parks in the City of Knoxville, Tennessee within the different residential zones. By utilizing geographic data on parks and zoning areas, this study conducted spatial analysis methods to evaluate whether each residential zone has access to a park and to examine the overall distribution of parks throughout Knoxville. Unlike previous studies that primarily focus on general park availability, this project explores the geographic distribution of parks in relation to residential zones, with a focus on identifying any disparities in access for underserved communities within Knoxville. 
    """
)

st.header("Datasets")

markdown = """
- [Park and Zoning Data](https://knoxplanning.org/data/open-data)


"""

st.markdown(markdown)


