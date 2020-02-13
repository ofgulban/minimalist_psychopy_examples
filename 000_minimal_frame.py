"""Minimal frame for a visual experiment."""

from psychopy import core, event, monitors, visual

# =============================================================================
# MONITOR

# Set monitor information used in the experimental setup
moni = monitors.Monitor('testMonitor', width=8.2, distance=60)  # in cm

# Set screen (make 'fullscr = True' for fullscreen)
mywin = visual.Window(size=(800, 600), screen=0, winType='pyglet',
                      allowGUI=True, fullscr=False, monitor=moni,
                      color='grey', colorSpace='rgb', units='cm')

# =============================================================================
# STIMULUS

stim_1 = visual.GratingStim(win=mywin, tex=None, units='deg',
                            size=(2, 2), pos=(-1, 0), color='green')

stim_2 = visual.GratingStim(win=mywin, tex=None, units='deg',
                            size=(1, 1), pos=(2, 0), color='blue')

text = visual.TextStim(win=mywin, text='Hello', color='red', height=0.3)

# =============================================================================
# TIME

# Parameters
total_time = 5.

# Give the system time to settle
core.wait(0.5)

# Create a clock
clock = core.Clock()
clock.reset()

# =============================================================================
# RENDER LOOP

while clock.getTime() < total_time:

    stim_1.draw()
    stim_2.draw()

    # Set text
    text.text = clock.getTime()
    text.draw()

    mywin.flip()

    # Handle key presses each frame
    for keys in event.getKeys():
        if keys[0]in ['escape', 'q']:
            mywin.close()
            core.quit()

mywin.close()
core.quit()
