import sys
import pytest

sys.path.append(r"E:\ML\PHASE01\D_CalculusForML\core")
sys.path.append(r"E:\ML\PHASE01\E_ChainRuleAndAutomaticDifferentiation\core")
sys.path.append(r"E:\ML\PHASE01\E_ChainRuleAndAutomaticDifferentiation\practice")

from dual import Dual
from value import Value
from helper import cube

@pytest.fixture()
def forward_pass():
    x = Dual(real_number=2.0, dual_number=1.0)
    y = cube(x)
    return x, y

@pytest.fixture()
def backward_pass():
    x = Value(data=2.0)
    y = cube(x)
    return x,y

def test_dual(forward_pass, backward_pass):
    bx, by = backward_pass
    fx, fy= forward_pass

    by.backward()

    assert by.data == fy.real_number
    assert bx.grad == fy.dual_number