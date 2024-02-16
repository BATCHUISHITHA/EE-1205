import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Load data from the "output.dat" file using numpy's loadtxt
data = np.loadtxt("output.dat")

# Extract n_values and y_values from the data
t_values = data[:, 0].astype(int)
Gt_values = data[:, 1]

# Create a stem plot
plt.stem(t_values, Gt_values, linefmt='|', markerfmt='o', basefmt='b', label='Stem Plot')

plt.xlabel('$t$')
plt.ylabel('$G(t)$')
plt.grid(True)
plt.yscale('log')
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.legend()
plt.savefig('../figs/g44fig1.png')
plt.show()
