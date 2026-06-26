import pytest
import sys
import math

sys.path.append(r"E:\ML\PHASE01\E_ChainRuleAndAutomaticDifferentiation\core")
from value import Value


@pytest.fixture()
def power_function():
    x = Value(data=2)
    y = x ** 3
    return x,y


def test_value(power_function):
    x, y = power_function

    assert y.data == 8


def test_pow(power_function):
    """
    Question
        Verify that d/dx(x^3) at x=2 equals 12.0.
    """
    x, y = power_function
    y.backward()

    assert x.grad == 12


def test_tanh():
    """
    Question
        Verify that tanh'(0) = 1 and tanh'(2) = 0.0707 (approx).
    """
    x = Value(data=2.0)
    y = x.tanh()

    assert y.data == pytest.approx(math.tanh(2.0))

    x = Value(data=0.0)
    y = x.tanh()

    assert y.data == pytest.approx(math.tanh(0))