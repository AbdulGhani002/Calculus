from sympy import *
def natural_log(x, n=1000):
    y = (x - 1) / (x + 1)
    ln_x = 0

    for i in range(1, n, 2):
        term = (2 * (y ** i)) / i
        ln_x += term

    return ln_x


x = symbols('x')
f = natural_log(x)
plot(f)