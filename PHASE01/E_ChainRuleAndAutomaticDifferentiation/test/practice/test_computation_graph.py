"""
Question
    Build a computation graph for a single neuron:
        y = relu(w1x1 + w2x2 + b).
    Compute all five gradients and verify against PyTorch.
"""
import sys
import pytest
import torch

sys.path.append(
    r"E:\ML\PHASE01\E_ChainRuleAndAutomaticDifferentiation\practice"
    )
sys.path.append(
    r"E:\ML\PHASE01\E_ChainRuleAndAutomaticDifferentiation\core"
    )
from computation_graph import computational_graph
from value import Value


def test_with_torch():
    x1, x2, w1, w2, b, y = computational_graph(
        x1_val=1.0,
        x2_val=2.0,
        w1_val=-3.0,
        w2_val=2.0,
        b_val=6.5343532532
        )
    
    tx1 = torch.tensor(data=1.0, requires_grad=True)
    tx2  = torch.tensor(data=2.0, requires_grad=True)
    tw1  = torch.tensor(data=-3.0, requires_grad=True)
    tw2  = torch.tensor(data=2.0, requires_grad=True)
    tb = torch.tensor(data=6.5343532532, requires_grad=True)
    
    exp = (tw1 * tx1 + tw2 * tx2 + tb)

    ty = exp.relu()
    ty.backward()

    assert y.data == pytest.approx(ty.item())

    assert x1.grad == pytest.approx(tx1.grad.item())
    assert x2.grad == pytest.approx(tx2.grad.item())
    assert w1.grad == pytest.approx(tw1.grad.item())    
    assert w2.grad == pytest.approx(tw2.grad.item())    
    assert b.grad == pytest.approx(tb.grad.item())    
