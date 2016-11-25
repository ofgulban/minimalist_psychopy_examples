"""Basic text read, organize by column, create pickle."""

import csv, pickle

csvName = 'Test_01.csv'
pickleName = 'Test_01.pickle'

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

print 'Stimulus types    : ', stimType
print 'Stimulus durations: ', stimDur

# I prefer dictionary data structures for pickles
dictionary = {'Stimulus':stimType, 'Duration':stimDur}
print dictionary

# Save the pickle
pickle.dump(dictionary, open(pickleName, 'wb'))
print 'Saved as: ' + pickleName
