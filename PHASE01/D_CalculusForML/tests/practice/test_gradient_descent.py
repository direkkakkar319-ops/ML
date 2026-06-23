import sys
import numpy as np
import pytest

sys.path.append(r"E:\ML\PHASE01\D_CalculusForML\practice")
from gradient_descent import f , gradient_descent


def test_gradient_descent():
    point = [0.0, 0.0]
    output = gradient_descent(f, point)

    assert output == pytest.approx([3.0, -1.0], rel=1e-3)