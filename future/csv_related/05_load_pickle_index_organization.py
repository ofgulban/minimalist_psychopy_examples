"""Load pickle. Organize indices per condition."""

import pickle


pickleName = 'Test_01.pickle'

file = open(pickleName, 'rb')
pickleFile = pickle.load(file)
file.close()

# Put some prints to see/remember the data structure.
print pickleFile
print type(pickleFile)
print pickleFile['Stimulus']
print pickleFile['Duration']

# Letter code the stimuli
stimTypeDict = {'Rest': [0],
                'Black_stim' : [1],
                'White_stim' : [2]}

# Seems familiar?
blocks = pickleFile['Stimulus']
blockDur = pickleFile['Duration']

# Some useful prints
print '---------------'
print 'blocks = ' + str(blocks)
print 'blockDur = ' +  str(blockDur)
print '---------------'

# Please take a deep breath now.

# Defining a function will reduce the code length significantly.
def idxAppend(iteration, enumeration, dictName, outDict):
     if int(enumeration) in range(stimTypeDict[dictName][0],
                                  stimTypeDict[dictName][-1]+1  # for multi-int 
                                  ):
        outDict = outDict.setdefault(dictName, [])
        outDict.append( iteration )

# Reorganization of the protocol array (finding and saving the indices)
outIdxDict = {}  # an empty dictionary

# Please take a deeper breath.
for i, j in enumerate(blocks):
    print i, j
    
    for k in stimTypeDict:  # iterate through each key in dict

        idxAppend(i, j, k, outIdxDict)

print outIdxDict
