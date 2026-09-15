"""
Question
    Implement learning rate decay.
    Add an exponential decay schedule to the GradientDescent class: lr = lr_0 * 0.999^step.
    Compare convergence with and without decay on the Rosenbrock function.
"""
import sys

sys.path.append(r"E:\ML\PHASE01\H_Optimization\core")

from vanilla_gradient_descent import GradientDescent
