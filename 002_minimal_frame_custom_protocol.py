"""Minimal frame. 3 stimuli with custom protocol."""

from psychopy import visual, monitors, core, event
import numpy as np

#
"""MONITOR"""

# set monitor information used in the experimental setup
moni = monitors.Monitor('testMonitor', width=8.2, distance=60)  # in cm

# set screen (make 'fullscr = True' for fullscreen)
mywin = visual.Window(size=(1024, 768), screen=0, winType='pyglet',
                      allowGUI=True, allowStencil=True,
                      fullscr=False,
                      monitor=moni,
                      color='grey',
                      colorSpace='rgb',
                      units='cm'
                      )

#
"""STIMULUS"""

# Squares
testStim1 = visual.GratingStim(win=mywin, tex=None, units='deg',
                               size=(4, 4),
                               color='red',
                               )

# Text
testText = visual.TextStim(win=mywin, color='black', height=0.5)

#
"""BLOCKS"""

# try changing these numbers ans see what happens
blocks = np.array([1, 2, 3, 1, 2])

#
"""BLOCK_DURATIONS"""

# try changing these numbers ans see what happens
blockDur = np.array([4, 2, 5, 1, 3])

#
"""TIME"""

# parameters
totalTime = np.sum(blockDur)
print 'Total Time: %i' % totalTime  # '%i' means integer here

# give the system time to settle
core.wait(0.5)

# create a clock
clock = core.Clock()
clock.reset()

#
"""RENDER_LOOP"""

i = 0

while clock.getTime() < totalTime:

    if blocks[i] == 1:
        testStim1.setColor('red')
        testStim1.setSize((2, 2))

    elif blocks[i] == 2:
        testStim1.setColor('green')
        testStim1.setSize((3, 3))

    elif blocks[i] == 3:
        testStim1.setColor('blue')
        testStim1.setSize((4, 4))

    while clock.getTime() < np.sum(blockDur[0:i+1]):

        t = clock.getTime()

        # condition
        testStim1.draw()

        # set test text
        testText.setText(t)
        testText.draw()

        mywin.flip()

        # handle key presses each frame
        for keys in event.getKeys(timeStamped=True):
            if keys[0]in ['escape', 'q']:
                mywin.close()
                core.quit()
    i = i+1

    # '%i' inside the string means "integer" and it is different than the
    # variable 'i' that we iterate after each block
    print 'Block counter: %i' % i

mywin.close()
core.quit()
