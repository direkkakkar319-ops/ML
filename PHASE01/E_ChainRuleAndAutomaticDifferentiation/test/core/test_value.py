import pytest
import sys

sys.path.append(r"E:\ML\PHASE01\E_ChainRuleAndAutomaticDifferentiation\core")
from value import Value


@pytest.fixture()
def function_is_two():
    x = Value(2)
    y = x ** 3
    return x,y


def test_value(function_is_two):
    x, y = function_is_two

    assert y.data == 8


def test_pow(function_is_two):
    """
    Question
        Verify that d/dx(x^3) at x=2 equals 12.0.
    """
    x, y = function_is_two
    y.backward()

    assert x.grad == 12


def test_tanh():
    """
    Question
        Verify that tanh'(0) = 1 and tanh'(2) = 0.0707 (approx).
    """