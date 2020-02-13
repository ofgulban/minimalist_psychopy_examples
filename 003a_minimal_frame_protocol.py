"""Minimal frame for showing three stimuli with custom protocol."""

import numpy as np
from psychopy import visual, monitors, core, event

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
stim = visual.GratingStim(win=mywin, tex=None, units='deg')

# Text
text = visual.TextStim(win=mywin, color='black', height=0.4)

# =============================================================================
# BLOCK IDENTIFIERS AND DURATIONS

# Try changing these numbers ans see what happens
block_ide = np.array([1, 2, 3, 2, 3, 1])
block_dur = np.array([2, 3, 2, 1, 4, 4])

# =============================================================================
# TIME

# Parameters
total_time = np.sum(block_dur)
print('Total Time: {}'.format(total_time))

# Give the system time to settle
core.wait(0.5)

# Create a clock
clock = core.Clock()
clock.reset()

# =============================================================================
# RENDER LOOP

i = 0

while clock.getTime() < total_time:

    # Determine block
    if block_ide[i] == 1:
        stim.color = 'red'
        stim.size = (1, 1)

    elif block_ide[i] == 2:
        stim.color = 'green'
        stim.size = (2, 2)

    elif block_ide[i] == 3:
        stim.color = 'blue'
        stim.size = (3, 3)

    while clock.getTime() < np.sum(block_dur[0:i+1]):

        stim.draw()

        # Set test text
        text.text = clock.getTime()
        text.draw()

        mywin.flip()

        # Handle key presses each frame
        for keys in event.getKeys(timeStamped=True):
            if keys[0] in ['escape', 'q']:
                mywin.close()
                core.quit()
    i = i + 1
    print('Block counter: {}'.format(i))

mywin.close()
core.quit()
