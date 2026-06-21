"""
Question
    1.  Create a composition of three transformations 
        (rotate 30 degrees, scale by [1.5, 0.8], shear with kx=0.3)
        and apply it to 8 points arranged in a circle .
    
    2.  Print before and after coordinates .
    
    3.  Compute the determinant of the composed matrix and verify
        it equals the product of the individual determinants .
"""
import sys
import os
import math

sys.path.append(r"E:\ML\PHASE01\C_MatrixTransformationsAndEigenValues\core")
from transformation import (
    rotation_2d,
    scaling_2d,
    shearing_2d,
    mat_mul,
    mat_vec_mul,
)
from detVolume import det_2x2

# ----------------------------------
# create transformation matrices
# -----------------------------------
R = rotation_2d(math.radians(30))
S = scaling_2d(1.5, 0.8)
SH = shearing_2d(0.3, 0)


# ----------------------------------
# create composition
# -----------------------------------
C = mat_mul(SH, mat_mul(S, R))


# ----------------------------------
# Generate 8 points
# -----------------------------------
points = []
for i in range(8):
    angle = math.radians(i*45)
    x = math.cos(angle)
    y = math.sin(angle)
    points.append([x,y])


# ----------------------------------
# Apply transformations
# -----------------------------------
print("Original -> Transformed")

for p in points:
    transformed = mat_vec_mul(C,p)
    
    print(
        f"{[round(x,4) for x in p]}"
        f"-->"
        f"{[round(x,4) for x in transformed]}"
    )


# ----------------
# Determinants
# ----------------
DR = det_2x2(R)
DS = det_2x2(S)
DSH = det_2x2(SH)
DC = det_2x2(C)

print(f"det(R) = {DR:.4f}")
print(f"det(S) = {DS:.4f}")
print(f"det(H) = {DSH:.4f}")
print(f"det(C) = {DC:.4f}")

product = DR * DS * DSH

print(f"Product of `rotated`, `scaled`, `sheared` matricx: {product}")
print(f"Transformed Matrices: {C}")
print(f"Verification: {abs(DC - product) < 1e-10}") # verification