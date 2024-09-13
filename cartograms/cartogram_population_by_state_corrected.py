
import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon
import matplotlib.pyplot as plt

# Load the shapefile
shp_file_name = 'ne_110m_admin_1_states_provinces/ne_110m_admin_1_states_provinces.shp'
us_states = gpd.read_file(shp_file_name)

# Plotting each state's exterior
fig, ax = plt.subplots(figsize=(10, 15))

# Iterate through each row in the GeoDataFrame
for _, row in us_states.iterrows():
    geometry = row['geometry']
    
    # Check if geometry is a Polygon or MultiPolygon
    if isinstance(geometry, Polygon):
        # For a single Polygon, directly access the exterior
        x, y = geometry.exterior.xy
        ax.plot(x, y, color='blue')
    elif isinstance(geometry, MultiPolygon):
        # For a MultiPolygon, iterate through each Polygon inside it using .geoms
        for poly in geometry.geoms:
            x, y = poly.exterior.xy
            ax.plot(x, y, color='blue')

# Set the title and show the plot
ax.set_title('US States Boundaries')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
