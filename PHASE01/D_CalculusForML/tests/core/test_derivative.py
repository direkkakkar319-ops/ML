import pytest
import sys
sys.path.append(r"E:\ML\PHASE01\D_CalculusForML\core")
from derivative import numerical_derivative
from helper import square, cube 

@pytest.mark.parametrize(
        "num, expected",
        [
            (-2, -4),
            (-1, -2),
            (0, 0.0),
            (1, 2.0),
            (2, 4.0),
        ],
    )
def test_derivative_square(num, expected):
    assert numerical_derivative(square, num) == pytest.approx(expected)


@pytest.mark.parametrize(
        "num, expected",
        [
            (-2, 12),
            (-1, 3),
            (0, 0),
            (1, 3),
            (2, 12),
        ],
    )
def test_derivative_cube(num, expected):
    assert numerical_derivative(cube, num) == pytest.approx(expected, abs=1e-7)
