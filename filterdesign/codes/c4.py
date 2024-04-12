import numpy as np

# Given parameters
s1 = -0.4523 - 0.4261j
s2 = -0.4523 + 0.4261j
s3 = -0.1874 + 1.0287j
s8 = -0.1874 - 1.0287j
epsilon = 0.31
Omega_Lp = 1

# Generate the denominator polynomial
den = np.poly([s1, s2, s3, s8])
num = np.array([1])
s = 1j*1  # use Omega = 1
H = num / np.polyval(den, s)

req = 1 / np.sqrt(1 + epsilon**2)

Gain_LP = req / abs(H)
print(Gain_LP)
