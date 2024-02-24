import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Load data from the "output.dat" file using numpy's loadtxt
data = np.loadtxt("output.dat")

# Extract t_values and Gt_values from the data
x_values = data[:, 0]
fx_values = data[:, 1]
fs_values = data[:,2]

# Create a continuous plot
plt.plot(x_values, fx_values, marker='',color='red', linestyle='-', label='f(x) values')
plt.plot(x_values, fs_values, marker='',color='green', linestyle='-', label='Fourier Series values')

plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.grid(True)
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.legend()
plt.savefig('../figs/f.png')
plt.show()

