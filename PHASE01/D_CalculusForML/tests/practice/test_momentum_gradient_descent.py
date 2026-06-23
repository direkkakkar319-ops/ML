import sys
sys.path.append(r"E:\ML\PHASE01\D_CalculusForML\practice")
from momentum_gradient_descent import f, momentum_gradient_descent
import pytest
import math

def test_momentum_gradient_descent():
    output = momentum_gradient_descent(f, point=[10.0], steps=500, lr=0.0001)
    expected = math.sqrt(3/2)

    assert abs(output[0]) == pytest.approx(expected, rel=1e-2) 