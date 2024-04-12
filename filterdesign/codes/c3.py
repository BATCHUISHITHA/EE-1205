import numpy as np

# Given parameters
s1 = -0.4523 - 0.4261j
s2 = -0.4523 + 0.4261j
s3 = -0.1874 + 1.0287j
s8 = -0.1874 - 1.0287j
epsilon = 0.31
Omega_Lp = 1

# Define denominator polynomial
den = np.poly([s1, s2, s3, s8])

# Define frequency range
w = np.arange(-2, 2.01, 0.01)

num = 0.4033

# Define parameters for transformation
B = 0.094
Omega0 = 0.4404

# Perform transformation to get s_L
s_L = (1j * 0.3959)**2 + Omega0**2
s_L /= B * (1j * 0.3959)

H = num / np.polyval(den, s_L)
print(1 / abs(H))
