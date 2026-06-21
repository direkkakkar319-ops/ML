"""
Numerical derivative vs Analytical derivative
"""
import math
from derivative import numerical_derivative

test_functions = [
    ("x^2", lambda x: x**2, lambda x: 2*x),
    ("x^3", lambda x: x**3, lambda x: 3*x**2),
    ("sin(x)", lambda x: math.sin(x), lambda x: math.cos(x)),
    ("e^x", lambda x: math.exp(x), lambda x: math.exp(x)),
    ("1/x", lambda x: 1/x, lambda x: -1/x**2),
]
x = 2.0

print(f"{'Function':<12} {'Numerical':>12} {'Analytical':>12} {'Error':>12}")
print("-"*40)

for name, f, df in test_functions:
    num = numerical_derivative(f ,x)
    ana = df(x)
    err = abs(num-ana)
    print(f"{name:<12} {num:12.6f} {ana:12.6f} {err:12.2e}")