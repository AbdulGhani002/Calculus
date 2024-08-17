'''For the function f x = 3x^2 + 1.
What is the slope at x = 3?'''
from sympy import *
def calculate_slop(value):
    x = symbols('x')
    f = (3*(x**2))+1
    diff_x = diff(f)
    slope_at_value = diff_x.subs(x,value)
    print(slope_at_value)
    return slope_at_value
calculate_slop(3)