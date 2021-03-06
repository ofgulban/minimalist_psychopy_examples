"""Load pickle. Organize indices per condition."""

import pickle


pickle_name = 'Test_01.pickle'

file = open(pickle_name, 'rb')
pickle_file = pickle.load(file)
file.close()

# Put some prints to see/remember the data structure.
print pickle_file
print type(pickle_file)
print pickle_file['Stimulus']
print pickle_file['Duration']

# Letter code the stimuli
stimTypeDict = {'Rest': [0],
                'Black_stim': [1],
                'White_stim': [2]}

# Seems familiar?
blocks = pickle_file['Stimulus']
blockDur = pickle_file['Duration']

# Some useful prints
print '---------------'
print 'blocks = ' + str(blocks)
print 'blockDur = ' + str(blockDur)
print '---------------'


# Defining a function will reduce the code length significantly.
def idxAppend(iteration, enumeration, dictName, outDict):
    if int(enumeration) in range(stimTypeDict[dictName][0],
                                 stimTypeDict[dictName][-1]+1  # for multi-int
                                 ):
        outDict = outDict.setdefault(dictName, [])
        outDict.append(iteration)


# Reorganization of the protocol array (finding and saving the indices)
outIdxDict = {}  # an empty dictionary

# !
for i, j in enumerate(blocks):
    print i, j

    for k in stimTypeDict:  # iterate through each key in dict
        idxAppend(i, j, k, outIdxDict)

print outIdxDict
