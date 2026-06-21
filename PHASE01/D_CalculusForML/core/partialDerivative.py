def numerical_gradient(f, point, h=1e-7):
    gradient = []
    for i in range(len(point)):
        point_plus = list(point)
        point_minus = list(point)
        
        point_plus[i] += h
        point_minus[i] -= h

        partial = (f(point_plus) - f(point_minus)) / (2 * h)

        gradient.append(partial)

    return gradient


def f_multi(point):
    x, y = point 
    return x**2 + 3*x*y + y**2

point = [1.0, 2.0]
grad = numerical_gradient(f_multi, point)

print(f"Numerical Gradient at (1, 2): {[f'{g:.4f}' for g in grad]}")
print(f"Analytical Gradient at (1, 2): [{2*1+3*2}, {3*1+2*2}]") # [(2x + 3y), (3x + 2y)]
print()
