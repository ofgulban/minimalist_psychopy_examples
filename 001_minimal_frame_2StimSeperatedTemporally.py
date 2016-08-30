"""Minimal frame for 2 stimuli separated in time."""

from psychopy import visual, monitors, core, event

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
                               size=(2, 2),
                               color='green',
                               )

# Instead of creating another visual object we manipulated the testStim1 by
# using setColor() and setSize().
testStim2 = visual.GratingStim(win=mywin, tex=None, units='deg',
                               size=(4, 4),
                               color='blue',
                               )

# Text
testText = visual.TextStim(win=mywin, color='black', height=0.5)

#
"""TIME"""

# parameters
totalTime = 10.
blockTime = 6.

# give the system time to settle
core.wait(0.5)

# create a clock
clock = core.Clock()
clock.reset()

#
"""RENDER_LOOP"""

while clock.getTime() < totalTime:

    t = clock.getTime()

    if t < blockTime:
        testStim1.setColor('red')
        testStim1.setSize((2, 2))

    elif t >= blockTime:
        testStim1.setColor('green')
        testStim1.setSize((3, 3))

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

mywin.close()
core.quit()
