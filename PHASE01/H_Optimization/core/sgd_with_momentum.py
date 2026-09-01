import sys

sys.path.append(r"E:\ML\PHASE01\D_CalculusForML\practice")
sys.path.append(r"E:\ML\PHASE01\D_CalculusForML\core")
sys.path.append(r"E:\ML\PHASE01\D_CalculusForML\core")

from gradient_descent import gradient_descent
from helper import biquadratic_equation
from momentum_gradient_descent import momentum_gradient_descent

if __name__ == "__main__":
    steps = 500
    lr = 0.0001
    point = [1.0]
    sgd_with_momentum = momentum_gradient_descent(
        biquadratic_equation, point, steps, lr
    )
    sgd_normal = gradient_descent(biquadratic_equation, point, steps, lr)
    print(f"SGD with momentum {sgd_with_momentum}")
    print(f"SGD without momentum {sgd_normal}")
