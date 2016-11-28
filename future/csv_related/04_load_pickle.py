"""Load pickle."""

import pickle


pickle_name = 'Test_01.pickle'

file = open(pickle_name, 'rb')
pickle_file = pickle.load(file)
file.close()

# Put some prints to see/remember the data structure
print pickle_file
print type(pickle_file)
print pickle_file['Stimulus']
print pickle_file['Duration']
