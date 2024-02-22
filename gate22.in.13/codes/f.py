import numpy as np
import matplotlib.pyplot as plt

# Define the piecewise function
def f(x):
    if -1 <= x < 0:
        return -1 - x
    elif 0 < x <= 1:
        return 1 - x
    else:
        return None

# Generate x values
x_values = np.linspace(-1.5, 1.5, 400)

# Generate y values
y_values = [f(x) for x in x_values]

# Plot the graph with a solid line
plt.plot(x_values, y_values, label=r'$f(x)$', linestyle='-')

# Add scatter points at (-1, 0) and (1, 0)
plt.scatter([-1, 1], [0, 0], color='red', zorder=5)

# Add a dot at (0, 1) on the y-axis
plt.scatter([0], [1], color='red', zorder=5)

# Add a dotted line between -1 and 1 on the y-axis
plt.plot([0, 0], [-1, 1], color='red', linestyle='dotted')

# Add labels and title
plt.xlabel('$x$')
plt.ylabel('$f(x)$')


# Add grid and legend
plt.grid(True)
plt.legend()

# Save plot as f.png
plt.savefig('f.png')

# Show plot
plt.show()

