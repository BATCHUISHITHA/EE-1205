import soundfile as sf
from scipy import signal

# read.wavfile
input_signal,fs=sf.read('ishitha.wav')

#sampling frequency of input signal
sampl_freq=fs

#order of the filter
order=4

#cutoff frequency 
cutoff_freq=10000.0


#digital frequency
Wn=2*cutoff_freq/sampl_freq

#b and a are numerator and denominator polynomials respectively
b,a=signal.butter(order,Wn,'low')

#filter the input signal with butterworth filter
output_signal=signal.filtfilt(b,a,input_signal,padlen=1)

#output_signal=signal.lfilt(b,a,input_signal)

#write the output signal into .wav file
sf.write('ishithareducednoise.wav',output_signal,fs)
