"""
TFB3133 / TEB3133 Data Visualization — Lab 4
Visualizing Population Distribution using Streamlit
Map file: malaysia_states.geojson (16 states/territories)
"""

import numpy as np
import pandas as pd
import geopandas as gpd
import folium
import streamlit as st
from streamlit_folium import folium_static

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Malaysia Population Distribution Map",
    layout="wide",
)

# NOTE: The GeoJSON file labels Penang as "Pulau Pinang" (its official Malay name),
# not "Penang". The state list below matches the GeoJSON exactly so every state
# gets coloured on the choropleth map.
STATES = [
    "Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", "Pahang",
    "Pulau Pinang", "Perak", "Perlis", "Sabah", "Sarawak", "Selangor",
    "Terengganu", "Kuala Lumpur", "Labuan", "Putrajaya",
]

IMAGINARY_STATES = ["New Selangor", "Westmalaya"]


# ── 3.1 Generate sample population data ──────────────────────────────────────
def generate_population_data():
    population = np.random.randint(500_000, 5_000_000, size=len(STATES))
    data = pd.DataFrame({"State": STATES, "Population": population})
    return data
    


# ── 3.2 Load the Malaysia map ─────────────────────────────────────────────────
@st.cache_data
def load_map():
    malaysia_map = gpd.read_file("malaysia_states.geojson")
    return malaysia_map


# ── 3.3 Plot the choropleth map ───────────────────────────────────────────────
def plot_map(malaysia_map, data):
    m = folium.Map(location=[4.2105, 101.9758], zoom_start=6)
    folium.Choropleth(
        geo_data=malaysia_map,
        name="Population Distribution",
        data=data,
        columns=["State", "Population"],
        key_on="feature.properties.name",
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Population Distribution",
    ).add_to(m)
    return m


# ── 3.4 Main Streamlit application ────────────────────────────────────────────
def main():
    st.title("Malaysia Population Distribution Map")

    population_data = generate_population_data()
    st.write("Sample Population Data for States:")
    st.dataframe(population_data, use_container_width=True)

    malaysia_map = load_map()
    folium_map = plot_map(malaysia_map, population_data)
    folium_static(folium_map)


if __name__ == "__main__":
    main()


def plot_map(malaysia_map, data, value_column, fill_color="YlOrRd"):
    m = folium.Map(location=[4.2105, 101.9758], zoom_start=6)

    # 1. Draw the choropleth (colour fill) as before
    folium.Choropleth(
        geo_data=malaysia_map,
        name=f"{value_column} Distribution",
        data=data,
        columns=["State", value_column],
        key_on="feature.properties.name",
        fill_color=fill_color,
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=f"{value_column} Distribution",
    ).add_to(m)

    # 2. Merge the data into the map's GeoDataFrame so each shape
    #    carries the value needed for the tooltip
    merged = malaysia_map.merge(data, left_on="name", right_on="State", how="left")

    # 3. Add an invisible GeoJson layer just for hover tooltips
    folium.GeoJson(
        merged,
        name="Tooltips",
        style_function=lambda feature: {
            "fillColor": "transparent",
            "color": "transparent",
            "weight": 0,
        },
        tooltip=folium.GeoJsonTooltip(
            fields=["name", value_column],
            aliases=["State:", f"{value_column}:"],
            localize=True,
            sticky=True,
            labels=True,
            style="""
                background-color: white;
                color: #333333;
                font-family: arial;
                font-size: 13px;
                padding: 6px;
            """,
        ),
    ).add_to(m)

    return m
