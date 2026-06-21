import sys
import os
import pytest 
import numpy as np
sys.path.append(r"E:\ML\PHASE01\C_MatrixTransformationsAndEigenValues\core")
from transformation import (
    rotation_2d, 
    scaling_2d, 
    shearing_2d, 
    reflection_x, 
    reflection_y, 
    mat_vec_mul, 
    mat_mul
)


# ----------------
# Rotation
#-----------------
def test_rotation_2d():
    assert np.allclose(
        rotation_2d(0),
        np.array([[1.0, 0.0],
                  [0.0, 1.0]])
    )

    assert np.allclose(
        rotation_2d(np.pi / 6),      # 30
        np.array([[0.8660254, -0.5],
                  [0.5,        0.8660254]])
    )

    assert np.allclose(
        rotation_2d(np.pi / 4),      # 45
        np.array([[0.70710678, -0.70710678],
                  [0.70710678,  0.70710678]])
    )

    assert np.allclose(
        rotation_2d(np.pi / 3),      # 60
        np.array([[0.5,       -0.8660254],
                  [0.8660254,  0.5]])
    )

    assert np.allclose(
        rotation_2d(np.pi / 2),      # 90
        np.array([[0.0, -1.0],
                  [1.0,  0.0]])
    )


# ----------------
# Scaling
#-----------------
def test_scaling_2d():
    assert np.allclose(
        scaling_2d(1, 1),
        np.array([[1, 0],
                  [0, 1]])
    )

    assert np.allclose(
        scaling_2d(2, 1),
        np.array([[2, 0],
                  [0, 1]])
    )

    assert np.allclose(
        scaling_2d(1, 3),
        np.array([[1, 0],
                  [0, 3]])
    )

    assert np.allclose(
        scaling_2d(2, 3),
        np.array([[2, 0],
                  [0, 3]])
    )

    assert np.allclose(
        scaling_2d(-1, 1),
        np.array([[-1, 0],
                  [ 0, 1]])
    )

    assert np.allclose(
        scaling_2d(1, -1),
        np.array([[ 1, 0],
                  [ 0, -1]])
    )

    assert np.allclose(
        scaling_2d(0, 0),
        np.array([[0, 0],
                  [0, 0]])
    )


# ----------------
# Shearing
#-----------------
def test_shearing_2d():
    assert np.allclose(
        shearing_2d(1, 1),
        np.array([[1, 1],
                  [1, 1]])
    )

    assert np.allclose(
        shearing_2d(2, 1),
        np.array([[1, 2],
                  [1, 1]])
    )

    assert np.allclose(
        shearing_2d(1, 3),
        np.array([[1, 1],
                  [3, 1]])
    )

    assert np.allclose(
        shearing_2d(2, 3),
        np.array([[1, 2],
                  [3, 1]])
    )

    assert np.allclose(
        shearing_2d(-1, 1),
        np.array([[1, -1],
                  [ 1, 1]])
    )

    assert np.allclose(
        shearing_2d(1, -1),
        np.array([[ 1, 1],
                  [ -1, 1]])
    )

    assert np.allclose(
        shearing_2d(0, 0),
        np.array([[1, 0],
                  [0, 1]])
    )


# ----------------
# Reflection
#-----------------
def test_reflection_x():
    assert np.allclose(
        reflection_x(),
        np.array([[1, 0],
                  [0, -1]])
    )

def test_reflection_y():
    assert np.allclose(
        reflection_y(),
        np.array([[-1, 0],
                  [0, 1]])
    )


# ----------------------
# Matrix Multiplication
#-----------------------
def test_value_mat_mul():
    assert np.allclose(
        mat_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]]),
        np.array([
            [19, 22],
            [43, 50]
        ])
    )

    assert np.allclose(
        mat_mul(
            [[1, 2, 3], [4, 5, 6]],
            [[7, 8], [9, 10], [11, 12]]
        ),
        np.array([
            [58, 64],
            [139, 154]
        ])
    )

def test_error_mat_mul():
    with pytest.raises(ValueError, match="Incompatible dimensions"):
        mat_mul(
             [[1, 2, 3], [4, 5, 6]],
             [[1, 0], [0, 1]]
        )
    
    with pytest.raises(ValueError, match="Incompatible dimensions"):
        mat_mul(
            [[1, 2], [3, 4], [5, 6]],
            [[1, 2], [3, 4], [5, 6]]
        )


# -----------------------------
# Matrix Vector Multiplication
#------------------------------
def test_mat_vec_mul():
    assert np.allclose(
        mat_vec_mul(
            [[2,1],[0,3]],
            [4,5]
        ),
        np.array([13, 15])
    )

    assert np.allclose(
        mat_vec_mul(
            [[2, 0, 1],
             [1, 3, 0],
             [0, 1, 4]],
            [1, 2, 3]
        ),
        np.array([5, 7, 14])
    )

    assert np.allclose(
        mat_vec_mul(
            [[0, 0],
             [0, 0]],
            [5, 6]
        ),
        np.array([0, 0])
    )

    assert np.allclose(
        mat_vec_mul(
            [[2, 0, 1],
             [1, 3, 0],
             [0, 1, 4]],
            [1, 2, 3]
        ),
        np.array([5, 7, 14])
    )