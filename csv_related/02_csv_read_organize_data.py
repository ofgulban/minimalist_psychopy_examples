"""Basic text read, organize by column."""

import csv

csvName = 'Test_01.csv'


# create empty arrays to append elements later
stimType =[]  
stimDur  =[]

# read & display csv
file = open(csvName)
data = csv.DictReader(file)

# instead of simple prints, append each relevant element to a list, then print
for row in data:   
    # change data type from string to integers (optional but will be useful)
    stimType.append(int(row['stimulus']))
    stimDur.append(int(row['duration']))

file.close()

print 'Block types    : ', stimType
print 'Block durations: ', stimDur
