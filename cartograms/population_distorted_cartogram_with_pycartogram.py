
import geopandas as gpd
import matplotlib.pyplot as plt
from pycartogram.cartogram import cartogram_geoprocessing
from shapely.geometry import Polygon, MultiPolygon

# Load the shapefile
shp_file_name = 'ne_110m_admin_1_states_provinces/ne_110m_admin_1_states_provinces.shp'
us_states = gpd.read_file(shp_file_name)

# Create synthetic population data (replace with real data if available)
us_states['population'] = us_states['NAME'].apply(lambda x: 1000 if 'New York' in x else 100)  # Example data

# Extract polygons and population data for cartogram creation
geometries = us_states['geometry'].tolist()
populations = us_states['population'].tolist()

# Create the cartogram using pycartogram
cartogram_geoms = cartogram_geoprocessing(geometries, populations, iterations=10)

# Plot the original and distorted cartogram side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

# Plot original map
us_states.boundary.plot(ax=ax1, color='blue')
ax1.set_title('Original Map')

# Plot distorted cartogram
for geom in cartogram_geoms:
    if isinstance(geom, Polygon):
        ax2.plot(*geom.exterior.xy, color='red')
    elif isinstance(geom, MultiPolygon):
        for poly in geom.geoms:
            ax2.plot(*poly.exterior.xy, color='red')

ax2.set_title('Population-Distorted Cartogram')
plt.show()
