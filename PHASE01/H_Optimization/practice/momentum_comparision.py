"""
Quesiton
    Momentum comparison.
        a. Run SGD with momentum values [0.0, 0.5, 0.9, 0.99] on the
        Rosenbrock function.
        b. Track the loss at every step.
        c. Which momentum value converges fastest? Which overshoots?
"""

import sys

sys.path.append(r"E:\ML\PHASE01\H_Optimization\core")

from compare import optimize
from sgd_momentum import SGDMomentum
from test_function import rosenbrock, rosenbrock_gradient

SGD_history = {}
momentum = [0.0, 0.5, 0.9, 0.99]
start = [-1.2, 1.0]

for m in momentum:
    try:
        SGD_history[m] = optimize(
            optimizer=SGDMomentum(momentum=m),
            func=rosenbrock,
            grad_func=rosenbrock_gradient,
            start=start,
        )
    except OverflowError:
        print(f"momentum={m} diverged (overflow)")
        history[m] = None

final_losses = {
    lr: history[-1][1] for lr, history in SGD_history.items() if history is not None
}

for key, values in final_losses.items():
    print(f"Momentum: {key} Loss: {values}")
