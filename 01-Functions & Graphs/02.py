from sympy import *
from sympy.plotting import plot3d
x, y = symbols('x y')
f = x**2 + 3*y
plot3d(f)
