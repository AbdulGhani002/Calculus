'''For the function f x = 3x^2 +1.
What is the area under the curve for x between 0
and 2?'''
from sympy import *
def calculate_area_under_curve(lower_LIMIT,upper_LIMIT):
    x = symbols('x')
    f = (3*(x**2)) + 1
    integrated = integrate(f,(x,lower_LIMIT,upper_LIMIT))
    print(integrated)
    return integrated
calculate_area_under_curve(0,2)