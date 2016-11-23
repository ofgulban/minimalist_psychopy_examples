# -*- coding: utf-8 -*-
"""Load pickle, organize indices per condition and custom text file."""

import pickle
import numpy as np

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
                'White_stim' : [2],
                'Task_stim' : [3,4]}

# Seems familiar?
blocks = pickleFile['Stimulus']
blockDur = pickleFile['Duration']

# Some useful prints
print '---------------'
print 'blocks = np.' + repr(blocks)
print 'blockDur = np.' +  repr(blockDur)
print '---------------'

# Please take a deep breath now.

# Defining a function will reduce the code length significantly.
def idxAppend(iteration, enumeration, dictName, outDict):
     if int(enumeration) in range(stimTypeDict[dictName][0],
                                  stimTypeDict[dictName][-1]+1
                                  ):
        outDict = outDict.setdefault(dictName, [])
        outDict.append( iteration )

# Reorganization of the protocol array (finding and saving the indices)
outIdxDict = {}  # an empty dictionary

# Please take a deeper breath.
for i, j in enumerate(blocks):
    for k in stimTypeDict:  # iterate through each key in dict
        idxAppend(i, j, k, outIdxDict)

print outIdxDict

# Creation of the Brainvoyager .prt custom text file
prtName = 'Test_01.prt'

file = open(prtName,'w')
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

# Conditions/predictors
for i in stimTypeDict:  # iterate through each key in stim. type dict

    # Write the condition/predictor name and put the Nr. of repetitions   
    file.writelines(['\n', i+'\n', str(len(outIdxDict[i]))])
                     
    # iterate through each element in indices dict for a specific stim. type    
    for j in outIdxDict[i]:
        onset = int( sum(blockDur[0:j+1]) - blockDur[j] + 1 )
        file.write('\n')
        file.write(str( onset ))
        file.write(' ')
        file.write(str( onset + blockDur[j]-1 ))
    # contiditon color (same for all for simplicity reasons)
    file.write('\nColor: 255 000 000\n')

file.close()
