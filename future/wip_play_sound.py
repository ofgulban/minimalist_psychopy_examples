"""Simple script to play sounds.

Notes
-----
Having trouble playing sounds correctly in debian so far. It seems that
Psychopy sound recommentations has changed. I need to have a closer look:
<https://www.psychopy.org/api/sound.html>

"""

import os
import psychtoolbox as ptb
from psychopy import prefs
prefs.hardware['audioLib'] = ['PTB']
from psychopy import core, sound, event

path_in = "/home/faruk/Git/minimalist_psychopy_examples/future/test"

# Print the sound files
sounds = sorted(os.listdir(path_in))

# Play sounds one by one
for i in sounds:
    sound_i = os.path.join(path_in, i)
    test_sound = sound.Sound(sound_i, volume=1, sampleRate=44100)
    now = ptb.GetSecs()
    test_sound.play()
    print(i)
    core.wait(2)

core.quit()
print("Finished.")
