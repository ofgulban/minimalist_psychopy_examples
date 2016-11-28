"""Load pickle, organize indices per condition and custom text file."""

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
                                 stimTypeDict[dictName][-1]+1
                                 ):
        outDict = outDict.setdefault(dictName, [])
        outDict.append(iteration)


# Reorganization of the protocol array (finding and saving the indices)
outIdxDict = {}  # an empty dictionary

# !
for i, j in enumerate(blocks):
    for k in stimTypeDict:  # iterate through each key in dict
        idxAppend(i, j, k, outIdxDict)

print outIdxDict

# Creation of the Brainvoyager .prt custom text file
prtName = 'Test_01.prt'

file = open(prtName, 'w')
strings = ['FileVersion: 2\n',
           'ResolutionOfTime: Volumes\n',
           'Experiment: Test protocol\n',
           'BackgroundColor: 0 0 0\n',
           'TextColor: 255 255 217\n',
           'TimeCourseColor: 255 255 255\n',
           'TimeCourseThick: 3\n',
           'ReferenceFuncColor: 255 255 51\n',
           'ReferenceFuncThick: 2\n'
           'NrOfConditions: 3\n'
           ]
file.writelines(strings)

file.close()
