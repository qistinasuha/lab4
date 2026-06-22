# Lab 4 — Malaysia Population Distribution Map

TFB3133 / TEB3133 Data Visualization — Week 6
Interactive choropleth map of Malaysia built with Streamlit, GeoPandas, and Folium.

## Files

| File | Purpose |
|---|---|
| `app.py` | Base lab code (Section 3 of the slides) |
| `app_assignment.py` | Modified version with all Section 5.1 experiments |
| `malaysia_states.geojson` | State boundary shapes (required — must sit in repo root) |
| `requirements.txt` | Python dependencies for Streamlit Cloud |

## Important note on state names

The GeoJSON file uses **"Pulau Pinang"**, not "Penang", for that state's official
name property. The state list in both scripts was updated to match exactly —
otherwise that state would render uncoloured on the map.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
# or
streamlit run app_assignment.py
```

## Deploy on Streamlit Cloud

1. Push all 4 files above to a GitHub repo (keep them in the root folder).
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**.
3. Select your repo, branch `main`, and set the main file to `app.py`
   (or `app_assignment.py` for the assignment version).
4. Click **Deploy**.

## Assignment experiments (`app_assignment.py`)

- **Task 2:** Population range widened to 1,000,000 – 10,000,000.
- **Task 3:** Sidebar toggle to switch between Population and GDP datasets.
- **Task 4:** Sidebar selector for colour scheme (YlOrRd, BuGn, Blues, Greens).
- **Task 5:** Checkbox to add two imaginary states ("New Selangor", "Westmalaya")
  and observe that they appear in the data table but not on the map, since no
  matching boundary exists in the GeoJSON.
