import numpy as np
import matplotlib.pyplot as plt

# Define the DFT matrix
def dft_matrix(N):
    n = np.arange(N)
    k = n.reshape((N, 1))
    W = np.exp(-2j * np.pi * k * n / N)
    return W

# Define the signal x(n) and h(n)
xtemp = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
x = np.pad(xtemp, (0, 10), 'constant', constant_values=(0))

hn1 = np.pad((-1/2)**np.arange(6), (0, 2), 'constant', constant_values=(0))
hn2 = np.pad((-1/2)**np.arange(6), (2, 0), 'constant', constant_values=(0))
h = hn1 + hn2

# Compute DFT matrix for x(n)
N_x = len(x)
W_x = dft_matrix(N_x)

# Compute X(k) using DFT matrix for x(n)
X = np.dot(W_x, x)

# Compute Y(k) = X(k) * H(k) element-wise
Y = X * h

# Compute y(n) using inverse DFT
W_inv = np.conjugate(W_x.T)  # Inverse DFT matrix
y = np.dot(W_inv, Y) / N_x  # IDFT of Y(k) to get y(n)

# Plotting
plt.stem(range(N_x), np.real(y), markerfmt='C0o')
plt.title("y(n) by DFT Matrix (with h(n))")
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.show()

