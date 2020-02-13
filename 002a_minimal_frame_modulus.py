"""Minimal frame with modulus usage."""

from psychopy import visual, monitors, core, event

# =============================================================================
# MONITOR

# Set monitor information used in the experimental setup
moni = monitors.Monitor('testMonitor', width=8.2, distance=60)  # cm,

# Set screen (make 'fullscr = True' for fullscreen)
mywin = visual.Window(size=(800, 600), screen=0, winType='pyglet',
                      allowGUI=True, fullscr=False, monitor=moni,
                      color='grey', colorSpace='rgb', units='cm',
                      blendMode='avg')

# =============================================================================
# STIMULUS

stim = visual.GratingStim(win=mywin, tex=None, units='deg')

text = visual.TextStim(win=mywin, color='black', height=0.4)

# =============================================================================
# TIME

# Parameters
total_time = 12  # seconds
block_time = 2  # seconds
loop_dur = block_time * 3  # because we have 3 different stimuli

# Give the system time to settle
core.wait(0.5)

# Create a clock
clock = core.Clock()
clock.reset()

# =============================================================================
# RENDER LOOP

i = 0  # Used to count how many blocks are completed

while clock.getTime() < total_time:

    t = clock.getTime() % loop_dur

    if t < block_time:
        stim.setColor('red')
        stim.setSize((1, 1))

    elif t >= block_time and t < 2 * block_time:
        stim.setColor('green')
        stim.setSize((2, 2))

    elif t >= 2 * block_time:
        stim.setColor('blue')
        stim.setSize((3, 3))

    while clock.getTime() < block_time * (i + 1):

        t = clock.getTime()

        stim.draw()

        text.text = t
        text.draw()

        mywin.flip()

        # Handle key presses each frame
        for keys in event.getKeys(timeStamped=True):
            if keys[0] in ['escape', 'q']:
                mywin.close()
                core.quit()

    i = i + 1

mywin.close()
core.quit()
