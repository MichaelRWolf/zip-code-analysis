
import pandas as pd

# Load the dataset from CSV file
df = pd.read_csv('zip_codes.csv')

# Group by state and city, and count occurrences
duplicates = df.groupby(['state', 'city']).size().reset_index(name='count')

# Filter to find cities with more than one ZIP code in the same state
duplicates = duplicates[duplicates['count'] > 1]

# Merge with the original data to get ZIP codes for the duplicate cities
result = pd.merge(df, duplicates[['state', 'city']], on=['state', 'city'])

# Display the result
print(result)
