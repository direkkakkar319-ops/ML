"""
Question
    Use gradient descent to find the minimum
    of f(x, y) = (x - 3)^2 + (y + 1)^2.
    Start from (0, 0).
    The answer should converge to (3, -1).
"""
import sys
import random
sys.path.append(r"E:\ML\PHASE01\D_CalculusForML\core")
from partialDerivative import numerical_gradient

def f(point):
    x, y = point
    return (x - 3)**2 + (y + 1)**2


def gradient_descent(f, point, steps, lr):
    for step in range(steps):
        gradient = numerical_gradient(f, point)
        point = [
            p - lr * g
            for p, g in zip(point , gradient)
        ]
        loss = f(point)
    return point

if __name__ == "__main__":
    point = [0.0, 0.0]
    lr = 0.01
    steps = 400
    print(f"lowest point for the function is {gradient_descent(f, point, steps, lr)}")