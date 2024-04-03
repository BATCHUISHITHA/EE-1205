import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy import signal

# Read the audio file
input_signal, fs = sf.read('ishitha.wav')

# Define the filter parameters
order = 4
cutoff_freq = 10000.0
Wn = 2 * cutoff_freq / fs

# Design the Butterworth filter
b, a = signal.butter(order, Wn, 'low')

# Custom filtering function using the difference equation
def custom_filter(b, a, input_signal):
    output_signal = signal.lfilter(b, a, input_signal)
    return output_signal

# Apply the custom filter to the input signal
output_signal_custom = custom_filter(b, a, input_signal)

# Apply the inbuilt filter to the input signal
output_signal_builtin = signal.lfilter(b, a, input_signal)

# Time axis for plotting
time = np.arange(len(input_signal)) / fs

# Plotting the verification plot with dots
plt.figure(figsize=(10, 6))

plt.plot(time, output_signal_custom, 'bo', label='output of audio signal without using built in function')
plt.plot(time, output_signal_builtin, 'ro', label='output of audio signal using built in function')
plt.title('Verification of outputs of Audio Filter')
plt.legend()

plt.tight_layout()

# Save the plot as an image
plt.savefig('6.1.png')

plt.show()

