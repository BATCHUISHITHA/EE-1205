import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 0.4033*s**4/(12808.2143074517*s**8 + 1540.36196218564*s**7 + 10142.5317235527*s**6 + 908.330882226954*s**5 + 2971.12957485079*s**4 + 176.172736602623*s**3 + 381.536082298044*s**2 + 11.2384559425352*s + 18.1245431295882)

# Perform substitution
substitution = ((1 - z**(-1)) / (1 + z**(-1)))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)
