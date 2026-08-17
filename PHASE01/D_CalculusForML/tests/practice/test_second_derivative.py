import sys

sys.path.append(r"E:\ML\PHASE01\D_CalculusForML\practice")
sys.path.append(r"E:\ML\PHASE01\D_CalculusForML\core")
import pytest
from helper import cube, square
from second_derivative import numerical_second_derivative


def test_square_numerical_second_derivative():
    result = numerical_second_derivative(square, 5)
    assert result == pytest.approx(2, rel=1e-6)


def test_cube_numerical_second_derivative():
    result = numerical_second_derivative(cube, 2)
    assert result == pytest.approx(12, abs=1e-6)
