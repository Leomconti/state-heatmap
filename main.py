import folium
import pandas as pd
from folium.plugins import HeatMap

# Load your dataset
df = pd.read_csv("dataset_with_lat_lon.csv")

# Initialize a folium map
m = folium.Map(location=[-27.2423, -50.2189], zoom_start=7)

# Add a heatmap layer
HeatMap(data=df[["Latitude", "Longitude", "Population"]].values, radius=15).add_to(m)

# Save map to an HTML file
m.save("santa_catarina_heatmap.html")
