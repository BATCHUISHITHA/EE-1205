import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Load data from the "output.dat" file using numpy's loadtxt
data = np.loadtxt("output.dat")

# Extract x_values and Gt_values from the data
x_values = data[:, 0]
y_values = data[:, 1]

# Create a continuous plot
plt.plot(x_values, y_values, marker='', linestyle='-', label='Continuous Plot')

# Find the index where x = 1
index_x_1 = np.where(x_values == 1)[0][0]

# Plot a red dot at y(1)
plt.plot(x_values[index_x_1], y_values[index_x_1], 'ro', label='$y(1)$')

plt.xlabel('$x$')
plt.ylabel('$y(x)$')
plt.grid(True)
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.legend()
plt.savefig('../figs/g50fig1.png')
plt.show()

