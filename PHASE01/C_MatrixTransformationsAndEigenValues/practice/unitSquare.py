"""
Question
    Apply `rotation`, `scaling`, and `shearing` to a unit square
    (corners at [0,0], [1,0], [1,1], [0,1]).
    Print the transformed corners for each. Verify that rotation 
    preserves distances between corners.
"""
import sys
import os
import math


sys.path.append(r"E:\ML\PHASE01\C_MatrixTransformationsAndEigenValues\core")
from transformation import rotation_2d, scaling_2d, shearing_2d, mat_vec_mul


squares = [[0,0], [1,0], [1,1], [0,1]]


# transformation matrices
R = rotation_2d(math.radians(45))
S = scaling_2d(2, 3)
SH = shearing_2d(1, 0)


# applied tranformations
rotated = [mat_vec_mul(R, p) for p in squares]
scaled = [mat_vec_mul(S, p) for p in squares]
sheared = [mat_vec_mul(SH, p) for p in squares]


# output
print(f"Oirignal squares: {squares}")
print(f"Rotated Squares: {rotated}")
print(f"Scaled squares: {scaled}")
print(f"Sheared Squares: {sheared}")


# verification
def distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0])** 2 + (p1[1] - p2[1]) ** 2
    )

print("Distance Verification (Rotation)")

pairs = [
    (0, 1),  # edges
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 2),  # diagonals
    (1, 3)
]

for i , j in pairs:
    before = distance(squares[i], squares[j])
    after = distance(rotated[i], rotated[j])

print(
    f"corners {i}-{j}:"
    f"Before = {before:.5f}"
    f"After = {after:.5f}"
    f"Preserved = {abs(before - after)< 1e-10}"
)