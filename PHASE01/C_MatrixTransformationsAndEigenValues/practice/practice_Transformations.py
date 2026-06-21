"""
Question
    Create a composition of three transformations 
    (rotate 30 degrees, scale by [1.5, 0.8], shear with kx=0.3)
    and apply it to 8 points arranged in a circle. Print before
    and after coordinates. Compute the determinant of the composed
    matrix and verify it equals the product of the individual
    determinants
"""
import sys
import os
import math

sys.path.append(r"E:\ML\PHASE01\C_MatrixTransformationsAndEigenValues\core")
from transformations import (
    rotation_2d,
    scaling_2d,
    shearing_2d,
    mat_mul,
    mat_vec_mul,
    determinant_2x2
)

# ----------------------------------
# creating transformation matrices
# -----------------------------------
R = rotation_2d(math.radians(30))
S = scaling_2d(1.5, 0.8)