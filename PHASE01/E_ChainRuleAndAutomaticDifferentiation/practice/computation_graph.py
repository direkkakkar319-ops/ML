"""
Question
    Build a computation graph for a single neuron:
        y = relu(w1x1 + w2x2 + b).
    Compute all five gradients and verify against PyTorch.
"""
import sys
import math
import random

sys.path.append(
    r"E:\ML\PHASE01\E_ChainRuleAndAutomaticDifferentiation\core"
    )
from value import Value

def computational_graph(
        x1_val,
        x2_val,
        w1_val,
        w2_val,
        b_val
        ):
    x1 = Value(data=x1_val)
    x2 = Value(data=x2_val)
    w1 = Value(data=w1_val)
    w2 = Value(data=w2_val)
    b = Value(data=b_val)

    exp = (w1 * x1 + w2 * x2 + b)
    y = exp.relu()
    y.backward()
    
    return x1, x2, w1, w2, b, y

print(computational_graph(
        x1_val=1,
        x2_val=2,
        w1_val=-3,
        w2_val=2,
        b_val=6.5343532532
))