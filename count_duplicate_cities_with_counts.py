
import sys
import csv
from collections import defaultdict

# Dictionary to store unique city-county pairs within each state
city_count = defaultdict(set)

# Reading CSV data from stdin
reader = csv.reader(sys.stdin)

# Skip the header row
header = next(reader)

# Find the indexes for city, state_id, and county_name to ensure correct column usage
city_index = header.index('city')
state_index = header.index('state_id')
county_index = header.index('county_name')

# Process each row in the CSV data
for row in reader:
    city = row[city_index]
    state = row[state_index]
    county = row[county_index]
    
    # Use (state, city) as the key and add county to the set to ensure uniqueness
    city_count[(state, city)].add(county)

# Output cities that are not unique within a state
print(f"Count, State, City, Counties")
for (state, city), counties in city_count.items():
    # Check if a city is associated with more than one distinct county, indicating it's not unique within the state
    if len(counties) > 1:
        print(f"{len(counties)}, {state}, {city}, {', '.join(counties)}")
