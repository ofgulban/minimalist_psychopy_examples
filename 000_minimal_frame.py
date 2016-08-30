"""Minimal frame for a visual experiment."""

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

testStim1 = visual.GratingStim(win=mywin, tex=None, units='deg',
                               size=(3, 3), pos=(-1, 0),
                               color='green',
                               )

testStim2 = visual.GratingStim(win=mywin, tex=None, units='deg',
                               size=(2, 2), pos=(2, 0),
                               color='blue',
                               )

testText = visual.TextStim(win=mywin, text='HELLO', color='red', height=0.5)

#
"""TIME"""

# parameters
totalTime = 5.

# give the system time to settle
core.wait(0.5)

# create a clock
clock = core.Clock()
clock.reset()

#
"""RENDER_LOOP"""

while clock.getTime() < totalTime:

    # set test text
    testText.setText(clock.getTime())

    testStim1.draw()
    testStim2.draw()
    testText.draw()

    mywin.flip()

    # handle key presses each frame
    for keys in event.getKeys(timeStamped=True):
        if keys[0]in ['escape', 'q']:
            mywin.close()
            core.quit()

mywin.close()
core.quit()
