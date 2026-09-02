"""
Question
    Saddle point escape.
    Define the function f(x, y) = x^2 - y^2 (a saddle point at the origin).
    Start at (0.01, 0.01).
    Compare how vanilla GD, SGD with momentum, and Adam behave.
    Which escapes the saddle point?
"""

import sys

import matplotlib.pyplot as plt

sys.path.append(r"E:\ML\PHASE01\H_Optimization\core")
sys.path.append(r"E:\ML\PHASE01\D_CalculusForML\core")

from adam import Adam
from compare import optimize
from helper import f_2d_negative
from partial_derivative import make_grad_func
from sgd_momentum import SGDMomentum
from vanilla_gradient_descent import GradientDescent

start_point = [0.01, 0.01]

grad_func = make_grad_func(f_2d_negative)

VGD_history = optimize(
    optimizer=GradientDescent(lr=0.05),
    func=f_2d_negative,
    grad_func=grad_func,
    start=start_point,
)

SGD_history = optimize(
    optimizer=SGDMomentum(lr=0.05, momentum=0.9),
    func=f_2d_negative,
    grad_func=grad_func,
    start=start_point,
)

ADAM_history = optimize(
    optimizer=Adam(lr=0.1),
    func=f_2d_negative,
    grad_func=grad_func,
    start=start_point,
)


def plot_trajectories(histories: dict):
    # --- Figure 1: trajectory in (x, y) space ---
    fig1, ax1 = plt.subplots(figsize=(6, 5))
    for name, history in histories.items():
        xs = [p[0] for p in history]
        ys = [p[1] for p in history]
        ax1.plot(xs, ys, label=name)
        ax1.scatter(xs[0], ys[0], marker="o", s=30)  # start
        ax1.scatter(xs[-1], ys[-1], marker="x", s=60)  # end
    ax1.scatter(0, 0, color="black", marker="*", s=100, label="saddle (0,0)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_title("Trajectory in parameter space")
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    fig1.tight_layout()
    fig1.savefig(
        r"E:\ML\PHASE01\H_Optimization\practice\graphs\saddle_trajectory.png", dpi=150
    )

    # --- Figure 2: |y| vs step, log scale ---
    fig2, ax2 = plt.subplots(figsize=(6, 5))
    for name, history in histories.items():
        ys = [abs(p[1]) for p in history]
        ax2.plot(ys, label=name)
    ax2.set_yscale("log")
    ax2.set_xlabel("step")
    ax2.set_ylabel("|y| (log scale)")
    ax2.set_title("Escape speed along the descending direction")
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    fig2.tight_layout()
    fig2.savefig(
        r"E:\ML\PHASE01\H_Optimization\practice\graphs\saddle_escape_speed.png", dpi=150
    )

    plt.show()


plot_trajectories(
    {
        "GD": VGD_history,
        "SGD+M": SGD_history,
        "Adam": ADAM_history,
    }
)
