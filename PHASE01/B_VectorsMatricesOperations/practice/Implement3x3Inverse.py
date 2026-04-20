import sys
import os
import numpy as np 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.matrix import Matrix


def numpy_inverse_check(matrix):
    np_A = np.array(matrix.data)

    np_inv = np.linalg.inv(np_A)

    my_inv = matrix.inverse_3x3().data

    if np.allclose(my_inv, np_inv, atol=1e-6):
        print("Correct")
    else:
        print("Incorrect") 

matrix = Matrix([[1, 2, 3],[0, 1, 4],[5, 6, 0]])
numpy_inverse_check(matrix)