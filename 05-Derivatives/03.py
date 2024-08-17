from sympy import *
from sympy.plotting import plot3d
x,y = symbols('x y')
f = 4*x**5 + 3*y**2
# Calculate the partial derivatives for x and y
dx_f = diff(f, x)
dy_f = diff(f, y)
print(dx_f) 
print(dy_f) 
plot3d(f)
