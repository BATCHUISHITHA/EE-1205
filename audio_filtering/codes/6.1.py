import soundfile as sf
from scipy import signal
import numpy as np
from matplotlib import pyplot as plt

def myfiltfilt(b, a, input_signal):
    # Perform zero-phase filtering using FFT
    output_signal = signal.filtfilt(b, a, input_signal, padlen=1)
    return output_signal

# Read the input .wav file
input_signal, fs = sf.read('ishitha.wav')

# Sampling frequency of input signal
sampl_freq = fs

# Order of the filter
order = 4

# Cutoff frequency 
cutoff_freq = 10000.0

# Digital frequency
Wn = 2 * cutoff_freq / sampl_freq

# Design Butterworth filter
b, a = signal.butter(order, Wn, 'low')

# Filter the input signal with Butterworth filter using filtfilt
output_signal = myfiltfilt(b, a, input_signal)


op1 = myfiltfilt(b, a, input_signal)

# Verify outputs by plotting
x_plt = np.arange(len(input_signal))
plt.plot(x_plt[1000:10000], output_signal[1000:10000], 'b.',label='Output by built in function')
plt.plot(x_plt[1000:10000], op1[1000:10000], 'r.',label='Output by not using built in function')
plt.title("Verification of outputs of Audio Filter")
plt.grid()
plt.legend()
plt.savefig("6.1.png")
plt.show()

