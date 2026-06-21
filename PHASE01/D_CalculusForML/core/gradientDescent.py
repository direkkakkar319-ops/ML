from partialDerivative import numerical_gradient, f_multi

point = [1.0, 2.0]
grad = numerical_gradient(f_multi, point)

x = 5.0 # any value of x
lr = 0.1 # learning rate
steps = 50

for step in range(steps):
    grad = 2 * x
    x = x - lr * grad
    print(f"step {step:2d}  x={x:8.4f}  f(x)={x**2:10.6f}")