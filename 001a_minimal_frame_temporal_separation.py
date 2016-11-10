"""Minimal frame for two stimuli separated in time."""

from psychopy import visual, monitors, core, event

# %%
""" Monitor """

# set monitor information used in the experimental setup
moni = monitors.Monitor('testMonitor', width=8.2, distance=60)  # in cm

# set screen (make 'fullscr = True' for fullscreen)
mywin = visual.Window(size=(800, 600), screen=0, winType='pyglet',
                      allowGUI=True,
                      fullscr=False,
                      monitor=moni,
                      color='grey',
                      colorSpace='rgb',
                      units='cm'
                      )

# %%
""" Stimulus """

# Squares
stim_1 = visual.GratingStim(win=mywin, tex=None, units='deg',
                            size=(1, 1),
                            color='red',
                            )

stim_2 = visual.GratingStim(win=mywin, tex=None, units='deg',
                            size=(2, 2),
                            color='green',
                            )

# Text
text = visual.TextStim(win=mywin, color='black', height=0.4)

# %%
""" Time """

# parameters
total_time = 10.
block_time = 6.

# give the system time to settle
core.wait(0.5)

# create a clock
clock = core.Clock()
clock.reset()

# %%
""" Render Loop """

while clock.getTime() < total_time:

    t = clock.getTime()

    # determine block
    if t < block_time:
        stim_1.draw()

    elif t >= block_time:
        stim_2.draw()

    # set test text
    text.text = t
    text.draw()

    mywin.flip()

    # handle key presses each frame
    for keys in event.getKeys(timeStamped=True):
        if keys[0]in ['escape', 'q']:
            mywin.close()
            core.quit()

mywin.close()
core.quit()
