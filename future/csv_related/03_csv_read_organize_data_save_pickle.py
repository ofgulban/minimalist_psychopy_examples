"""Basic text read, organize by column, create pickle."""

import csv
import pickle

csv_name = 'Test_01.csv'
pickle_name = 'Test_01.pickle'

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

print 'Stimulus types    : ', state_ide
print 'Stimulus durations: ', state_dur

# I prefer dictionary data structures for pickles
dictionary = {'Stimulus': state_ide, 'Duration': state_dur}
print dictionary

# Save the pickle
out = open(pickle_name, 'wb')
pickle.dump(dictionary, out)
out.close()
print 'Saved as: ' + pickle_name
