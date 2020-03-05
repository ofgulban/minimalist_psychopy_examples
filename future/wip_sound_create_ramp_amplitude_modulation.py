"""CreateTones_MM.m Python port.

Notes
-----
I have converted an old matlab script to python and actually never really used
it afterwards. Therefore anyone using this script should test whether sounds
are created properly.

"""

import os
import numpy as np
from scipy.io import wavfile

# Parameters
out_dir = "/home/faruk/Git/minimalist_psychopy_examples/future/test"
samp_freq = 44100  # Sampling frequency
sound_dur = 800  # Duration of sounds in ms

# -----------------------------------------------------------------------------
s = int(samp_freq * sound_dur / 1000)  # Nr. samples for sound duration
time_vector = np.arange(1, s + 1) / float(samp_freq)

nr_freq = 8
sound_freq_vector = 2 ** (np.linspace(np.math.log(200, 2),
                          np.math.log(10000, 2), nr_freq))

sound_freq_vector = np.insert(sound_freq_vector, 6, 6000, axis=0)

# -----------------------------------------------------------------------------
# Jitter main tones
for i in range(0, len(sound_freq_vector)):
    sourceFreq = sound_freq_vector[i*3]

    for j in range(0, 1):
        sound_freq_vector = np.insert(sound_freq_vector, i * 3 + j,
                                      sourceFreq / (2 ** 0.1), axis=0)
        sound_freq_vector = np.insert(sound_freq_vector, i * 3 + j + 2,
                                      sourceFreq * (2 ** 0.1), axis=0)

sound_freq_vector = np.round(sound_freq_vector)

# -----------------------------------------------------------------------------
# Amplitude modulation
amp_mod_freq = 8  # Amplitude modulation frequency
amp_mod_depth = 1  # Amplitude modulation depth (strenght, amplitude)
ampl = 0.95

full_time_vector = np.array([])
for i, freq in enumerate(sound_freq_vector):
    sound_i = ampl * np.sin(2 * np.pi * freq * time_vector)

    # Add amplitude modulation
    modulator = amp_mod_depth * np.sin(2 * np.pi * amp_mod_freq * time_vector)
    sound_i = ((1 + modulator) * sound_i) / 2
    full_time_vector = np.concatenate([full_time_vector, sound_i])

    # Save output
    out_path = os.path.join(out_dir, "TEST_{}.wav".format(str(i).zfill(2)))
    wavfile.write(out_path, samp_freq, sound_i)


# =============================================================================
def ramp_sound(in_vector, samp_freq, ramp_time):
    """RampSound.m implementation."""
    nr_samples = len(in_vector)
    ramp_nr_samples = round(ramp_time * samp_freq / 1000)
    ramp_on = np.linspace(0, 1, ramp_nr_samples)
    ramp_off = np.linspace(1, 0, ramp_nr_samples)

    in_vector_temp = np.copy(in_vector)

    # Add ramp
    in_vector_temp[0:ramp_nr_samples] = in_vector[0:ramp_nr_samples] * ramp_on
    in_vector_temp[nr_samples - ramp_nr_samples:nr_samples] = (
        in_vector[nr_samples - ramp_nr_samples:nr_samples] * ramp_off)
    in_vector = in_vector_temp
    return in_vector


# =============================================================================
# Preproc_sounds.mm implementation

# Parameters
energy = 200
ramp_time = 10

# Add ramp
for i in range(0, len(sound_freq_vector)):
    tmp = full_time_vector[i*s:i*s+s]
    tmp = ramp_sound(tmp, samp_freq, ramp_time)
    en_s = np.sum(tmp**2, axis=0)
    tmp = tmp * np.sqrt(energy / en_s)
    tmp = tmp - tmp.mean()

    out_name = 'TEST_{}_ramped.wav'.format(str(i).zfill(2))
    out_path = os.path.join(out_dir, out_name)
    wavfile.write(out_path, samp_freq, tmp)

print("Finished.")
