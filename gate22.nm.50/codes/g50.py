import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Load data from the "output.dat" file using numpy's loadtxt
data = np.loadtxt("output.dat")

# Extract t_values and Gt_values from the data
t_values = data[:, 0]
y_values = data[:, 1]

# Create a continuous plot
plt.plot(t_values, y_values, marker='', linestyle='-', label='Continuous Plot')

# Find the index where t = 1
index_t_1 = np.where(t_values == 1)[0][0]

# Plot a red dot at y(1)
plt.plot(t_values[index_t_1], y_values[index_t_1], 'ro', label='$y(1)$')

plt.xlabel('$t$')
plt.ylabel('$y(t)$')
plt.grid(True)
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.legend()
plt.savefig('../figs/g50fig1.png')
plt.show()

