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

plt.xlabel('$x$')
plt.ylabel('$y(x)$')
plt.grid(True)
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.legend()
plt.savefig('../figs/g50fig1.png')
plt.show()

