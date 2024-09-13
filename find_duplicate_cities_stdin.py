
import pandas as pd
import sys

# Load the dataset from standard input
df = pd.read_csv(sys.stdin)

# Group by state and city, and count occurrences
duplicates = df.groupby(['state', 'city']).size().reset_index(name='count')

# Filter to find cities with more than one ZIP code in the same state
duplicates = duplicates[duplicates['count'] > 1]

# Merge with the original data to get ZIP codes for the duplicate cities
result = pd.merge(df, duplicates[['state', 'city']], on=['state', 'city'])

# Display the result
print(result)
