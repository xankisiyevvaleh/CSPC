import sympy as sp

t = sp.symbols('t')

s = t**3 + 2*t**2 + 5*t

v = sp.diff(s, t)
a = sp.diff(v, t)

print("Position s(t):", s)
print("Velocity v(t):", v)
print("Acceleration a(t):", a)  