"""Minimal frame for a visual experiment."""

from psychopy import visual, monitors, core, event

# %%
""" Monitor """

# set monitor information used in the experimental setup
moni = monitors.Monitor('testMonitor', width=8.2, distance=60)  # in cm

# set screen (make 'fullscr = True' for fullscreen)
mywin = visual.Window(size=(800, 600), screen=0, winType='pyglet',
                      allowGUI=True, fullscr=False, monitor=moni,
                      color='grey', colorSpace='rgb', units='cm')

# %%
""" Stimulus """

stim_1 = visual.GratingStim(win=mywin, tex=None, units='deg',
                            size=(2, 2), pos=(-1, 0), color='green')

stim_2 = visual.GratingStim(win=mywin, tex=None, units='deg',
                            size=(1, 1), pos=(2, 0), color='blue')

text = visual.TextStim(win=mywin, text='Hello', color='red', height=0.3)

# %%
""" Time """

# parameters
total_time = 5.

# give the system time to settle
core.wait(0.5)

# create a clock
clock = core.Clock()
clock.reset()

# %%
""" Render Loop """

while clock.getTime() < total_time:

    stim_1.draw()
    stim_2.draw()

    # set test text
    text.text = clock.getTime()
    text.draw()

    mywin.flip()

    # handle key presses each frame
    for keys in event.getKeys():
        if keys[0]in ['escape', 'q']:
            mywin.close()
            core.quit()

mywin.close()
core.quit()
