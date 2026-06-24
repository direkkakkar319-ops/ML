"""
Question
    Add momentum to the gradient descent loop:
    maintain a velocity vector that accumulates
    past gradients.
    Compare convergence speed with and without
    momentum on f(x) = x^4 - 3x^2.
"""
import sys
sys.path.append(r"E:\ML\PHASE01\D_CalculusForML\core")
from partialDerivative import numerical_gradient
from gradient_descent import gradient_descent


def f(point):
    x = point[0]
    return x**4 - 3*x**2


def momentum_gradient_descent(f, point, steps, lr, momentum=0.95):
    velocity = [0.0]   
    point = point.copy()

    for _ in range(steps):
        gradient = numerical_gradient(f, point)
        velocity = [
            momentum * v + lr * g
            for v, g in zip(velocity, gradient)
        ]
        point = [
            p - v
            for p, v in zip(point, velocity)
        ]

    return point

if __name__ == "__main__":
    steps = 500
    lr = 0.0001
    point = [1.0]

    normal = gradient_descent(f, point, steps, lr)
    momentum = momentum_gradient_descent(f, point, steps, lr)

    print(f"Gradient Descent done Normally: {normal}")
    print(f"Gradient Descent done using momentum:  {momentum}")