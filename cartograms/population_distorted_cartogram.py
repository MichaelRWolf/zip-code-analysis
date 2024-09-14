
import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon
import matplotlib.pyplot as plt
from cartopy import crs as ccrs
import numpy as np

# Load the shapefile
shp_file_name = 'ne_110m_admin_1_states_provinces/ne_110m_admin_1_states_provinces.shp'
us_states = gpd.read_file(shp_file_name)

# Assume population column exists, normalize the population for distortion
# For demonstration, we'll create synthetic population data
us_states['population'] = np.random.randint(1, 1000, len(us_states))  # Replace with actual population data

# Normalize population for visual distortion effect
us_states['pop_norm'] = us_states['population'] / us_states['population'].max()

# Plotting the population-distorted cartogram
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw={'projection': ccrs.PlateCarree()})

# Iterate through each state and plot distorted boundaries
for _, row in us_states.iterrows():
    geometry = row['geometry']
    scale_factor = row['pop_norm']  # Scale based on population

    if isinstance(geometry, Polygon):
        # Distort the polygon using the population scale factor
        distorted = geometry.buffer(scale_factor)
        ax.add_geometries([distorted], crs=ccrs.PlateCarree(), edgecolor='blue', facecolor='none')
    elif isinstance(geometry, MultiPolygon):
        # For MultiPolygon, iterate through each Polygon inside it
        for poly in geometry.geoms:
            distorted = poly.buffer(scale_factor)
            ax.add_geometries([distorted], crs=ccrs.PlateCarree(), edgecolor='blue', facecolor='none')

# Set the title and show the plot
ax.set_title('Population-Distorted US States Cartogram')
plt.show()
