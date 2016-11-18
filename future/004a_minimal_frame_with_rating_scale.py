"""Rating scale example, press 'q' to quit."""

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

stim = visual.GratingStim(win=mywin, tex=None, units='deg',
                          size=(2, 2), pos=(0, 0),
                          color='green'
                          )

# %%
""" Response Stimulus """

scale = visual.RatingScale(win=mywin, pos=(0, 0),
                           low=1, high=100,
                           precision=1,
                           markerStart=50,
                           marker='triangle',
                           markerColor='DarkRed',
                           tickHeight=0,
                           showValue=True,
                           showAccept=True,
                           leftKeys='1', rightKeys = '2',
                           acceptKeys=['4', 'return']
                           )

# %%
""" Time """

total_time = 20  # seconds
stim_time = 2 # seconds

# give the system time to settle
core.wait(0.5)

# create a clock
clock = core.Clock()
clock.reset()

# %%
""" Render Loop """

accum_time = 0

while clock.getTime() < total_time:

    while clock.getTime() < stim_time + accum_time:
        stim.draw()
        mywin.flip()
    
        # handle key presses each frame during stimulus
        for keys in event.getKeys(timeStamped=True):
            if keys[0]in ['escape', 'q']:
                mywin.close()
                core.quit()
    
    scale.reset()
    while scale.noResponse:
        scale.draw()
        mywin.flip()
        accum_time = clock.getTime()  # accumulated time
                    
    print 'Final rating: ' + str(scale.getRating())
    print 'Response time: ' + str(scale.getRT())
    
mywin.close()
core.quit()
