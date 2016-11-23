"""Basic text read."""

import csv

csvName = 'Test_01.csv'

# read & display csv
file = open(csvName)
data = csv.DictReader(file)

for row in data:
    print row
#    print row['trigger'], row['stimulus'], row['duration']

file.close()