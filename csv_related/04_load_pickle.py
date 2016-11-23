"""Load pickle."""

import pickle


pickleName = 'Test_01.pickle'

file = open(pickleName, 'rb')
pickleFile = pickle.load(file)
file.close()

# Put some prints to see/remember the data structure
print pickleFile
print type(pickleFile)
print pickleFile['Stimulus']
print pickleFile['Duration']
