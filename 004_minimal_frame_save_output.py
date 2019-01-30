"""Minimal frame with output file.

Press 5 repeatedly to emulate scanner triggers.

"""

import numpy as np
import pickle
from psychopy import visual, monitors, core, event

# %%
""" Monitor """

# set monitor information used in the experimental setup
moni = monitors.Monitor('testMonitor', width=8.2, distance=60)  # cm,

# set screen (make 'fullscr = True' for fullscreen)
mywin = visual.Window(size=(800, 600), screen=0, winType='pyglet',
                      allowGUI=True,
                      fullscr=False,
                      monitor=moni,
                      color='grey',
                      colorSpace='rgb',
                      units='cm')

# %%
""" Stimulus """

# Squares
stim = visual.GratingStim(win=mywin, tex=None, units='deg')

# Text
text = visual.TextStim(win=mywin, color='black', height=0.4)

#
""" Block Identifiers and Durations """

# try changing these numbers ans see what happens
block_ide = np.array([1, 2, 3, 1, 2])
block_dur = np.array([4, 2, 5, 1, 3])

# %%
""" Time """

# parameters
total_time = np.sum(block_dur)
print('Total Time: {}'.format(total_time)

# give the system time to settle
core.wait(0.5)

# create a clock
# clock=core.Clock()  # <----- No need anymore
# clock.reset()       # <----- No need anymore

# %%
""" Render loop """

i = 0
trig = 0  # <-----

while trig < total_time:  # <-----

    if block_ide[i] == 1:
        stim.color = 'red'
        stim.size = (1, 1)

    elif block_ide[i] == 2:
        stim.color = 'green'
        stim.size = (2, 2)

    elif block_ide[i] == 3:
        stim.color = 'blue'
        stim.size = (3, 3)

    while trig < np.sum(block_dur[0:i + 1]):  # <-----

        # condition
        stim.draw()

        # set test text
        text.text = 'Trigger: ' + str(trig)  # <-----
        text.draw()

        mywin.flip()

        # handle key presses each frame
        for keys in event.getKeys(timeStamped=True):
            if keys[0]in ['5']:  # <-----
                trig = trig + 1  # <-----

            if keys[0]in ['escape', 'q']:
                mywin.close()
#                core.quit()
    i = i + 1
    print('Block counter: {}'.format(i))

# %%
"""Saving output at the end of the experiment."""

# Dictionary data structure can be used
dictionary = {'Stimulus':block_ide, 'Duration':block_dur}
print(dictionary)

# Save the pickle
pickle_name = 'Test_01.pickle'
out = open(pickle_name, 'wb')
pickle.dump(dictionary, out)
out.close()
print('-----\n Saved as: {}\n-----'.format(pickle_name))

mywin.close()
#core.quit()
