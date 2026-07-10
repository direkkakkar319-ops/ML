from value import Value
from visualise import draw_dot, trace
import numpy as np 
import matplotlib.pyplot as plt 

plt.plot(np.arange(-5, 5, 0.25), np.tanh(np.arange(-5, 5, 0.25))); plt.grid()

x1 = Value(2.0, label="x1")
x2 = Value(0.0, label="x2")
w1 = Value(-3.0, label="w1")
w2 = Value(1.0, label="w2")
b = Value(6.7, label="b")

x1w1 = x1 * w1; x1w1.label="x1 * w1"
x2w2 = x2 * w2; x2w2.label="x2 * w2"

x1w1x2w2 = x1w1 + x2w2; x1w1x2w2.label="(x1 * w1) + (x2 * w2)" 
n = x1w1x2w2 + b; n.label="n"

O = n.tanh(); O.label="o"

O.grad = 1.0
# dO/dn = d(tanh(n))/dn = sech(n)**2 = 1-tanh(n)**2
# 1-O**2 = 1-(O.data)**2
n.grad = 1 - (O.data)**2



dot = draw_dot(root=O)
filename = dot.render("graph_neural_net", cleanup=True)
