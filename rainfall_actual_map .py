import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()

gdf = gpd.read_file("Export_Output.shp")

gdf['District'] = gdf['NAME_2'].str.strip().str.upper()

# The data
df = pd.read_excel("rainfall_kerala_actual.xlsx")
df['District'] = df['District'].str.strip().str.upper()

merged = gdf.merge(df, on='District', how='left')

# select the month
rainfall_column = 'May'

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

merged.plot(
    column=rainfall_column,
    cmap='Blues',
    legend=True,
    edgecolor='black',
    linewidth=0.6,
    ax=ax,
    legend_kwds={
        'shrink': 0.6,
        'label': 'Actual Rainfall (mm)',
    },
    vmin=400, vmax=1100
)
ax.set_title(
    f"Kerala District-wise Actual Rainfall: {rainfall_column} 2025",
    fontsize=16)
ax.axis('off')
plt.tight_layout()

plt.savefig(f"kerala_actual_rainfall_{rainfall_column.lower()}_2025.png", dpi=300)
plt.show()
