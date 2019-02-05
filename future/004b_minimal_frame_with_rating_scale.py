"""Rating scale example presented together with stimulus."""

import numpy as np
import pprint
from psychopy import visual, monitors, core

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

stim = visual.GratingStim(win=mywin, tex=None, units='deg',
                          size=(2, 2), pos=(0, 0), color='green')

# %%
""" Response Stimulus """

scale = visual.RatingScale(win=mywin, pos=(0, -0.7), low=1, high=100,
                           precision=1, markerStart=50, marker='triangle',
                           markerColor='DarkRed', tickHeight=0,
                           scale=None,  # text above the slider
                           showValue=False, showAccept=False)

# %%
""" Time """

total_time = 10  # seconds

# give the system time to settle
core.wait(0.5)

# create a clock
clock = core.Clock()
clock.reset()

# %%
""" Render Loop """

accum_time = 0

while clock.getTime() < total_time:

    stim.draw()
    scale.draw()
    mywin.flip()

print('Response history (Rating, RT):')
pprint.pprint(scale.getHistory())
history = np.array(scale.getHistory())
mean, std = np.mean(history[:, 0]), np.std(history[:, 0])
print('Average rating: {}'.format(mean))
print('Standard deviation: {}'.format(std))

mywin.close()
core.quit()
