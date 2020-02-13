"""Minimal frame for two stimuli separated in time."""

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

# Squares
stim_1 = visual.GratingStim(win=mywin, tex=None, units='deg',
                            size=(2, 2), color='green')

# Text
text = visual.TextStim(win=mywin, color='black', height=0.4)

# =============================================================================
# TIME

# Parameters
total_time = 10.
block_time = 6.

# Give the system time to settle
core.wait(0.5)

# Greate a clock
clock = core.Clock()
clock.reset()

# =============================================================================
# RENDER LOOP

while clock.getTime() < total_time:

    t = clock.getTime()

    # Determine block
    if t < block_time:
        stim_1.color = 'red'
        stim_1.size = (1, 1)

    elif t >= block_time:
        stim_1.color = 'green'
        stim_1.size = (2, 2)

    stim_1.draw()

    # Set text
    text.text = t
    text.draw()

    mywin.flip()

    # Handle key presses each frame
    for keys in event.getKeys():
        if keys[0] in ['escape', 'q']:
            mywin.close()
            core.quit()

mywin.close()
core.quit()
