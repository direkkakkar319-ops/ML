"""
This files helps us compare the three algorithms used for finding
the minimal loss when building a neural netrwork

Output looks like:
GD     -> x=0.798131, y=0.636104, loss=0.04083385
SGD+M  -> x=0.940412, y=0.884127, loss=0.00355685
Adam   -> x=0.999974, y=0.999948, loss=0.00000000
"""
from sgd_momentum import SGDMomentum
from vanilla_gradient_descent import GradientDescent
from adam import Adam
from test_function import rosenbrock, rosenbrock_gradient

def optimize(optimizer, func, grad_func, start, steps=5000):
    params = list(start)
    history = [params[:]]
    for _ in range(steps):
        grads = grad_func(params)
        params = optimizer.step(params, grads)
        history.append(params[:])
    return history

start = [-1.0, 1.0]

gd_history = optimize(GradientDescent(lr=0.0005), rosenbrock, rosenbrock_gradient, start)
sgd_history = optimize(SGDMomentum(lr=0.0001, momentum=0.9), rosenbrock, rosenbrock_gradient, start)
adam_history = optimize(Adam(lr=0.01), rosenbrock, rosenbrock_gradient, start)

for name, history in [("GD", gd_history), ("SGD+M", sgd_history), ("Adam", adam_history)]:
    final = history[-1]
    loss = rosenbrock(final)
    print(f"{name:6s} -> x={final[0]:.6f}, y={final[1]:.6f}, loss={loss:.8f}")
