import streamlit as st
st.title("_BlazeGuardian_")

st.write("""
## Explore the factors that contribute to the wildfires in Alberta and Beyond
This machine learning model not only displays to you how  much each factor
contributes to a wildfire, but also allows you to explore the data further by
segmenting it into various causes and possible factors to help mitigate the risk
of wildfires particularly in first nations communities. Please download the
dataset below for your reference.
""")

st.download_button("Alberta Wildfires Data Set", "/content/fp-historical-wildfire-data-2006-2021.csv", file_name = "fp-historical-wildfire-data-2006-2021.csv")

st.subheader("Access to Detailed Report")
st.write("Use the button below to acces a in-depth analysis of our findings.")
st.link_button("Access Report", "https://docs.google.com/document/d/1frUK1DXamQg05Hj76eCshZuxbO8vuOiJT_kCOUjOk_4/edit?usp=sharing")

st.sidebar.title("_Explore the dataset!_")
st.sidebar.subheader("Filters:")
fire_spread_rate = st.sidebar.slider("Fire Spread Rate", 4.0, 20.0, 12.0)
fuel_types = st.sidebar.multiselect("Fuel Types", ["C4", "O1A"])
fire_spread_rate = st.sidebar.multiselect("General Causes", ["Lightning", "Resident", "Forest Industry", "Agriculture Indusrtry"])
fire_spread_rate = st.sidebar.multiselect("Activity Class", ["Debris Disposal", "Arson", "Cooking and Warming", "Operations"])

import pandas as pd
import numpy as np
import pydeck as pdk

df1 = pd.read_csv("/content/fp-historical-wildfire-data-2006-2021.csv")

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=54.76,
        longitude=-111.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=df1,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df1,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))
