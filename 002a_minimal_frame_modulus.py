"""Minimal frame with modulus usage."""

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
                      units='cm',
                      blendMode='avg',
                      )

# %%
""" Stimulus """

stim = visual.GratingStim(win=mywin, tex=None, units='deg')

# Text
text = visual.TextStim(win=mywin, color='black', height=0.4)

# %%
""" Time """

# parameters
total_time = 12  # seconds
block_time = 2  # seconds
loop_dur = block_time * 3  # because we have 3 different stimuli)

# give the system time to settle
core.wait(0.5)

# create a clock
clock = core.Clock()
clock.reset()

# %%
""" Render Loop """

i = 0  # used to count how many blocks are completed

while clock.getTime() < total_time:

    t = clock.getTime()

    if t % loop_dur < block_time:
        stim.setColor('red')
        stim.setSize((1, 1))

    elif t % loop_dur >= block_time and t % loop_dur < 2 * block_time:
        stim.setColor('green')
        stim.setSize((2, 2))

    elif t % loop_dur >= 2 * block_time:
        stim.setColor('blue')
        stim.setSize((3, 3))

    while clock.getTime() < block_time * (i + 1):

        t = clock.getTime()

        stim.draw()

        # set test text
        text.text = t
        text.draw()

        mywin.flip()

        # handle key presses each frame
        for keys in event.getKeys(timeStamped=True):
            if keys[0]in ['escape', 'q']:
                mywin.close()
                core.quit()

    i = i + 1

mywin.close()
core.quit()
