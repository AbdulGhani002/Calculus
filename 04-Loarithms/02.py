import sympy as sp
x = sp.symbols('x')
f=1/x
result = sp.limit(f, x, sp.oo) 
# sp.oo is the representation of infinity in sympy
print(result)
sp.plot(f)
