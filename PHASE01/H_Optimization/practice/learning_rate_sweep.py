"""
Question
    Learning rate sweep.
        a. Run vanilla gradient descent on the Rosenbrock function
        with learning rates [0.0001, 0.0005, 0.001, 0.005, 0.01].
        b. Plot or print the final loss after 5000 steps for each.
        c. Find the largest learning rate that still converges.
"""

import sys

import matplotlib.pyplot as plt

sys.path.append(r"E:\ML\PHASE01\H_Optimization\core")

from compare import optimize
from test_function import rosenbrock, rosenbrock_gradient
from vanilla_gradient_descent import GradientDescent

lrs = [0.0001, 0.0005, 0.001, 0.005, 0.01]
gd_history = {}

for lr in lrs:
    try:
        gd_history[lr] = optimize(
            optimizer=GradientDescent(lr=lr),
            func=rosenbrock,
            grad_func=rosenbrock_gradient,
            start=[-1.2, 1.0],
        )
    except OverflowError:
        print(f"lr={lr} diverged (overflow)")
        gd_history[lr] = None

final_losses = {
    lr: history[-1][1] for lr, history in gd_history.items() if history is not None
}
diverged_lrs = [lr for lr, history in gd_history.items() if history is None]
lrs_list = list(final_losses.keys())
losses_list = list(final_losses.values())

plt.figure(figsize=(5, 5))
plt.plot(lrs_list, losses_list, marker="o")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Learning Rate")
plt.ylabel("Final loss after 5000 steps")
plt.title("Learning rate sweep on Rosenbrock function")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.savefig(
    r"E:\ML\PHASE01\H_Optimization\practice\graphs\lr_sweep.png", dpi=150
)  # <-- added, before show()
plt.show()
