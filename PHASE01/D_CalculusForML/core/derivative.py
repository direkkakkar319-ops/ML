"""
Numerical Derivative 
Analytical Derivative
"""
from helper import square, cube

def numerical_derivative(f, x, h=1e-4):
    return (f(x + h) - f(x - h)) / (2 * h)

if __name__ == "__main__":
    nums = [-2, -1, 0, 1, 2]
    print("="*40)
    print("SQUARE")
    print("="*40)
    for num in nums:
        numerical = numerical_derivative(square, num)
        analytical = 2 * num 
        print(f"x={num:2d} f'(x) numerical={numerical:.6f}  analytical={analytical:.1f}")
    
    print()

    print("="*40)
    print("CUBE")
    print("="*40)
    for num in nums:
        numerical = numerical_derivative(cube, num)
        analytical = 3 * (2*num) 
        print(f"x={num:2d} f'(x) numerical={numerical:.6f}  analytical={analytical:.1f}")
