# %%
# Libraries
import numpy as np 
import matplotlib.pyplot as plt 

# Python functions and classes
from value import Value
from visualise import draw_dot


# %%
plt.plot(np.arange(-5, 5, 0.25), np.tanh(np.arange(-5, 5, 0.25))); plt.grid()


# %%
x1 = Value(2.0, label="x1")
x2 = Value(0.0, label="x2")
w1 = Value(-3.0, label="w1")
w2 = Value(1.0, label="w2")
b = Value(6.7, label="b")

x1w1 = x1 * w1; x1w1.label="x1 * w1"
x2w2 = x2 * w2; x2w2.label="x2 * w2"

x1w1x2w2 = x1w1 + x2w2; x1w1x2w2.label="(x1 * w1) + (x2 * w2)" 
n = x1w1x2w2 + b; n.label="n"
# ----------------------
O = n.tanh(); O.label="o"
# ----------------------


# %%
# # dO/dn = d(tanh(n))/dn = sech(n)**2 = 1-tanh(n)**2
# # 1-O**2 = 1-(O.data)**2
# n.grad = 1 - (O.data)**2

# x1w1x2w2.grad = n.grad # due to the `+` it will have the same gradient
# b.grad = n.grad

# x1w1.grad = x1w1x2w2.grad
# x2w2.grad = x1w1x2w2.grad

# # PRACTICE
# # x1.grad = do/dx1
# # x1.grad = do/dx1 = (do/dx1w1) * (dx1w1/dx1)
# # x1.grad = do/dx1 = (do/dx1w1) * (dx1w1/dx1) = (x1w1.grad) * (w1.data)
# x1.grad = x1w1.grad * w1.data
# w1.grad = x1w1.grad * x1.data

# x2.grad = x2w2.grad * w2.data
# w2.grad = x2w2.grad * x2.data

# backpropagation one-by-one
# O._backward()
# n._backward()
# b._backward()
# x1w1x2w2._backward()
# x2w2._backward()
# x1w1._backward()

# backpropagation all at once
O.backward()


# %%
print("-"*40)
print(".tanh()")
print("-"*40)

print(f"x1: {x1}")
print(f"w1: {w1}")
print(f"x2: {x2}")
print(f"w2: {w2}")
print(f"b: {b}")
print()

dot = draw_dot(root=O)
filename = dot.render("graph_neural_net_tanh", cleanup=True)


# %%
x1 = Value(2.0, label="x1")
x2 = Value(0.0, label="x2")
w1 = Value(-3.0, label="w1")
w2 = Value(1.0, label="w2")
b = Value(6.7, label="b")

x1w1 = x1 * w1; x1w1.label="x1 * w1"
x2w2 = x2 * w2; x2w2.label="x2 * w2"

x1w1x2w2 = x1w1 + x2w2; x1w1x2w2.label="(x1 * w1) + (x2 * w2)" 
n = x1w1x2w2 + b; n.label="n"
# ----------------------
e = (2*n).exp(); e.label="e"
O = (e-1) / (e+1); O.label="o"
# ----------------------


# %%
O.backward()

# %%
print("-"*40)
print(".exp()")
print("-"*40)

print(f"x1: {x1}")
print(f"w1: {w1}")
print(f"x2: {x2}")
print(f"w2: {w2}")
print(f"b: {b}")
print()


# %%
dot = draw_dot(root=O)
filename = dot.render("graph_neural_net_exp", cleanup=True)


# %%
import torch as th


# %%
print("-"*40)
print("PyTorch-->.tanh()")
print("-"*40)


# %%
x1 = th.tensor([2.0], dtype=th.double, requires_grad=True)
w1 = th.tensor([0.0], dtype=th.double, requires_grad=True)
x2 = th.tensor([-3.0], dtype=th.double, requires_grad=True)
w2 = th.tensor([1.0], dtype=th.double, requires_grad=True)
b = th.tensor([6.881373587], dtype=th.double, requires_grad=True)
n = x1 * w1 + x2 * w2 + b
O = th.tanh(n)


# %%
print(f"O.data: {O.data.item()}")
O.backward()


# %%
print(f"x1: {x1.grad.item()}")
print(f"w1: {w1.grad.item()}")
print(f"x2: {x2.grad.item()}")
print(f"w2: {w2.grad.item()}")
print()


# %%'
th.tensor([[1, 2, 3], [4, 5, 6]]).dtype
