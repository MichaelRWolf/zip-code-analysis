import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter

# Load the detailed shapefile of U.S. states; adjust the path to match your shapefile
shp_file_name='ne_110m_admin_1_states_provinces/ne_110m_admin_1_states_provinces.shp'

us_states = gpd.read_file(shp_file_name)

# Population data for all 50 states based on 2020 estimates (in millions)
population_data = {
    'Alabama': 5.03, 'Alaska': 0.73, 'Arizona': 7.28, 'Arkansas': 3.03, 'California': 39.24,
    'Colorado': 5.77, 'Connecticut': 3.60, 'Delaware': 1.00, 'Florida': 21.48, 'Georgia': 10.62,
    'Hawaii': 1.46, 'Idaho': 1.84, 'Illinois': 12.67, 'Indiana': 6.79, 'Iowa': 3.19,
    'Kansas': 2.94, 'Kentucky': 4.51, 'Louisiana': 4.62, 'Maine': 1.36, 'Maryland': 6.18,
    'Massachusetts': 7.03, 'Michigan': 10.05, 'Minnesota': 5.71, 'Mississippi': 2.96,
    'Missouri': 6.15, 'Montana': 1.08, 'Nebraska': 1.96, 'Nevada': 3.14, 'New Hampshire': 1.38,
    'New Jersey': 9.29, 'New Mexico': 2.11, 'New York': 19.84, 'North Carolina': 10.49,
    'North Dakota': 0.77, 'Ohio': 11.80, 'Oklahoma': 3.96, 'Oregon': 4.24, 'Pennsylvania': 12.78,
    'Rhode Island': 1.10, 'South Carolina': 5.12, 'South Dakota': 0.89, 'Tennessee': 6.91,
    'Texas': 29.53, 'Utah': 3.28, 'Vermont': 0.64, 'Virginia': 8.64, 'Washington': 7.71,
    'West Virginia': 1.79, 'Wisconsin': 5.89, 'Wyoming': 0.58
}

# Merge population data with GeoDataFrame
us_states['population'] = us_states['name'].map(population_data)

# Normalize population for cartogram effect
us_states['scaled_population'] = us_states['population'] / us_states['population'].max()

# Create a plot with Gaussian blur to simulate cartogram distortion
fig, ax = plt.subplots(1, 1, figsize=(15, 10))

# Plot using Gaussian filter to create a pseudo-cartogram effect
for _, state in us_states.iterrows():
    geometry = state['geometry']
    scaled_pop = state['scaled_population'] * 10  # Scaling factor for effect
    x, y = geometry.exterior.xy
    ax.fill(gaussian_filter(x, sigma=scaled_pop), gaussian_filter(y, sigma=scaled_pop), alpha=0.7)

ax.set_title('US States Population Cartogram (Pseudo-Effect)', fontsize=16)
plt.axis('off')
plt.show()
import geopandas as gpd
import matplotlib.pyplot as plt
from cartogram_geopandas import make_cartogram

# Load the detailed shapefile of U.S. states; adjust the path to match the location of your downloaded shapefile
us_states = gpd.read_file('/path_to_your_downloaded_shapefile/ne_110m_admin_1_states_provinces.shp')

# Population data for all 50 states based on 2020 estimates (in millions)
population_data = {
    'Alabama': 5.03, 'Alaska': 0.73, 'Arizona': 7.28, 'Arkansas': 3.03, 'California': 39.24,
    'Colorado': 5.77, 'Connecticut': 3.60, 'Delaware': 1.00, 'Florida': 21.48, 'Georgia': 10.62,
    'Hawaii': 1.46, 'Idaho': 1.84, 'Illinois': 12.67, 'Indiana': 6.79, 'Iowa': 3.19,
    'Kansas': 2.94, 'Kentucky': 4.51, 'Louisiana': 4.62, 'Maine': 1.36, 'Maryland': 6.18,
    'Massachusetts': 7.03, 'Michigan': 10.05, 'Minnesota': 5.71, 'Mississippi': 2.96,
    'Missouri': 6.15, 'Montana': 1.08, 'Nebraska': 1.96, 'Nevada': 3.14, 'New Hampshire': 1.38,
    'New Jersey': 9.29, 'New Mexico': 2.11, 'New York': 19.84, 'North Carolina': 10.49,
    'North Dakota': 0.77, 'Ohio': 11.80, 'Oklahoma': 3.96, 'Oregon': 4.24, 'Pennsylvania': 12.78,
    'Rhode Island': 1.10, 'South Carolina': 5.12, 'South Dakota': 0.89, 'Tennessee': 6.91,
    'Texas': 29.53, 'Utah': 3.28, 'Vermont': 0.64, 'Virginia': 8.64, 'Washington': 7.71,
    'West Virginia': 1.79, 'Wisconsin': 5.89, 'Wyoming': 0.58
}

# Merge population data with GeoDataFrame, adjusting the column name to match your shapefile's state name column
us_states['population'] = us_states['name'].map(population_data)  # Use 'name' or another appropriate column name

# Generate the cartogram, scaling states by population
cartogram = make_cartogram(us_states, 'population', scale_factor=1.0)

# Plot the cartogram
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
cartogram.plot(ax=ax, column='population', legend=True, cmap='OrRd', edgecolor='black')

# Adjust display settings
ax.set_title('US States Population Cartogram', fontsize=16)
plt.axis('off')
plt.show()
import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Load the Natural Earth shapefile provided by geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filter for United States
us_states = world[world['iso_a3'] == 'USA']

# Population data for all 50 states based on 2020 estimates (in millions)
population_data = {
    'Alabama': 5.03, 'Alaska': 0.73, 'Arizona': 7.28, 'Arkansas': 3.03, 'California': 39.24,
    'Colorado': 5.77, 'Connecticut': 3.60, 'Delaware': 1.00, 'Florida': 21.48, 'Georgia': 10.62,
    'Hawaii': 1.46, 'Idaho': 1.84, 'Illinois': 12.67, 'Indiana': 6.79, 'Iowa': 3.19,
    'Kansas': 2.94, 'Kentucky': 4.51, 'Louisiana': 4.62, 'Maine': 1.36, 'Maryland': 6.18,
    'Massachusetts': 7.03, 'Michigan': 10.05, 'Minnesota': 5.71, 'Mississippi': 2.96,
    'Missouri': 6.15, 'Montana': 1.08, 'Nebraska': 1.96, 'Nevada': 3.14, 'New Hampshire': 1.38,
    'New Jersey': 9.29, 'New Mexico': 2.11, 'New York': 19.84, 'North Carolina': 10.49,
    'North Dakota': 0.77, 'Ohio': 11.80, 'Oklahoma': 3.96, 'Oregon': 4.24, 'Pennsylvania': 12.78,
    'Rhode Island': 1.10, 'South Carolina': 5.12, 'South Dakota': 0.89, 'Tennessee': 6.91,
    'Texas': 29.53, 'Utah': 3.28, 'Vermont': 0.64, 'Virginia': 8.64, 'Washington': 7.71,
    'West Virginia': 1.79, 'Wisconsin': 5.89, 'Wyoming': 0.58
}

# Merge population data with GeoDataFrame
us_states['population'] = us_states['name'].map(population_data)

# Normalize population for scaling in the cartogram
us_states['scaled_population'] = us_states['population'] / us_states['population'].max()

# Create plot
fig, ax = plt.subplots(1, 1, figsize=(15, 10), subplot_kw={'projection': ccrs.Mercator()})

# Plotting the states with scaling based on population
us_states.boundary.plot(ax=ax, linewidth=1, color='black')
us_states.plot(column='scaled_population', ax=ax, legend=True, cmap='OrRd', edgecolor='black')

# Adjust display settings
ax.set_title('US States Population Cartogram', fontsize=16)
plt.show()
