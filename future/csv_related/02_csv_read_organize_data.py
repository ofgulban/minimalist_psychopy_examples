"""Basic text read, organize by column."""

import csv

csv_name = 'Test_01.csv'


# create empty arrays to append elements later
state_ide = []
state_dur = []

# read & display csv
file = open(csv_name)
data = csv.DictReader(file)

# instead of simple prints, append each relevant element to a list, then print
for row in data:
    # change data type from string to integers (optional but will be useful)
    state_ide.append(int(row['stimulus']))
    state_dur.append(int(row['duration']))

file.close()

print 'Block types    : ', state_ide
print 'Block durations: ', state_dur
