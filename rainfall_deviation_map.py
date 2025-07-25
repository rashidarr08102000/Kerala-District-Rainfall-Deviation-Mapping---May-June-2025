
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file("Export_Output.shp")
gdf['District'] = gdf['NAME_2'].str.strip().str.upper()

df_actual = pd.read_excel("rainfall_kerala_actual.xlsx")
df_normal = pd.read_excel("rainfall_kerala_normal.xlsx")

# Standardize district names
df_actual['District'] = df_actual['District'].str.strip().str.upper()
df_normal['District'] = df_normal['District'].str.strip().str.upper()

df = df_actual.merge(df_normal, on='District', suffixes=('_actual', '_normal'))

# Calculating deviation
df['May_deviation'] = df['May_actual'] - df['May_normal']

# Merge with shapefile
merged = gdf.merge(df, on='District', how='left')

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

merged.plot(
    column='May_deviation',
    cmap='Blues',  
    legend=True,
    edgecolor='black',
    linewidth=0.7,
    ax=ax,
    legend_kwds={
        'shrink': 0.6,
        'label': 'Rainfall Deviation (mm)'
    },
    vmin=400, vmax=1100 
)

ax.set_title("Kerala Rainfall Deviation: May 2025", fontsize=16)
ax.axis('off')
plt.tight_layout()
plt.savefig("kerala_rainfall_deviation_may_2025.png", dpi=300)
plt.show()
