from sympy import *
x = symbols('x')
f = x**2
# Calculate the derivative of the function
dx_f = diff(f)
print(dx_f)