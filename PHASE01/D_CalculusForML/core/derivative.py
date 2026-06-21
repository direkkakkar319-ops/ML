"""
Numerical Derivative 
Analytical Derivative
"""
def numirical_derivative(f, x, h=1e-7):
    return (f(x + h) - f(x - h)) / (2 * h)


def f(x): # return square of `x`
    return x ** 2


nums = [-2, -1, 0, 1, 2]

for num in nums:
    numerical = numirical_derivative(f, num)
    analytical = 2 * num 
    print(f"x={num:2d} f'(x) numerical={numerical:.6f}  analytical={analytical:.1f}")

