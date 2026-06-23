"""
Question
    Implement `numerical_second_derivative(f, x)` using
    numerical_derivative called twice.
    Verify that the second derivative of x^3 at x=2 is 12.
"""
import sys
sys.path.append(r"E:\ML\PHASE01\D_CalculusForML\core")
from derivative import numerical_derivative
from helper import square, cube

def numerical_second_derivative(f, x):
    def first_derivative(z):
        return numerical_derivative(f, z)
    
    second_derivative = numerical_derivative(first_derivative, x)

    return second_derivative

x=2

print(f"Second Derivative of x^2 when x={x}:  {numerical_second_derivative(square, x)}")
print(f"Second Derivative of x^3 when x={x}:  {numerical_second_derivative(cube, x)}")
