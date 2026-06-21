"""
Question
    Find the eigenvalues of the matrix [[4, 2], [1, 3]] by hand
    using the characteristic equation. Then verify with your
    from-scratch function and with NumPy.
"""
import sys
import os
import numpy as np

sys.path.append(r"E:\ML\PHASE01\C_MatrixTransformationsAndEigenValues\core")
from eigenValues import eigenvalues_2x2

A = [[4, 2], [1, 3]] # matrix


# ----------------
# From Scratch
# ----------------
values = eigenvalues_2x2(A)

print(f"matrix: {A}")
print(f"Eigen vlaues: {values}")


# ----------------
# NumPy
# ----------------
np_values = np.linalg.eig(np.array(A))

print(f"Numpy: {np_values}")


# ----------------
# By hand
# ---------------
a, b = A[0]
c, d = A[1]

trace = a + d
det = a*d - b*c 

print(f"Characterstic Equation:λ² - ({trace})λ + ({det}) = 0")