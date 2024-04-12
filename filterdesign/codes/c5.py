from sympy import symbols, simplify

# Define symbolic variable s
s = symbols('s')

# Constants
omega0_val = 0.4404
B_val = 0.094

# Define s_L in terms of s, omega0, and B
s_L = (s**2 + omega0_val**2) / (B_val * s)

# Given roots
s1 = -0.4523 - 0.4261j
s2 = -0.4523 + 0.4261j
s3 = -0.1874 + 1.0287j
s8 = -0.1874 - 1.0287j

# Define the given polynomial expression
polynomial_expr = 0.4033 / ((s_L - s1) * (s_L - s2) * (s_L - s3) * (s_L - s8))

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
