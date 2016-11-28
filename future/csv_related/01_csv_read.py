"""Basic text read."""

import csv

csv_name = 'Test_01.csv'

# read & display csv
file = open(csv_name)
data = csv.DictReader(file)

for row in data:
    print row
#    print row['trigger'], row['stimulus'], row['duration']

file.close()
