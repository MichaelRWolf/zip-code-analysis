
import sys
import csv
from collections import defaultdict

# Dictionary to store city occurrences across states
city_state_count = defaultdict(set)

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
    
    # Use city as the key and add (state, county) to the set
    city_state_count[city].add((state, county))

# Output cities that exist in more than 10 states
print(f"State/County Count, City Name, List of State/Counties")
for city, states_counties in city_state_count.items():
    states = {state for state, county in states_counties}
    if len(states) > 0:
        states_counties_list = [f"{state}/{county}" for state, county in states_counties]
        print(f"{len(states)},{city},{' '.join(states_counties_list)}")
