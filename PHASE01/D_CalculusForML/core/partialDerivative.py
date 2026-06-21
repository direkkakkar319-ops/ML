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

# -----------------------------
# Gradient Descent 
# -----------------------------
x = 5.0 # any value of x
lr = 0.1 # learning rate
steps = 50

for step in range(steps):
    grad = 2 * x
    x = x - lr * grad
    print(f"step {step:2d}  x={x:8.4f}  f(x)={x**2:10.6f}")