import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Load data from the "output.dat" file using numpy's loadtxt
data = np.loadtxt("output.dat")

# Extract t_values and Gt_values from the data
t_values = data[:, 0]
Gt_values = data[:, 1]

# Create a continuous plot
plt.plot(t_values/10, Gt_values, marker='', linestyle='-', label='Continuous Plot')

plt.xlabel('$t$')
plt.ylabel('$G(t)$')
plt.grid(True)
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.legend()
plt.savefig('../figs/g44fig1.png')
plt.show()

