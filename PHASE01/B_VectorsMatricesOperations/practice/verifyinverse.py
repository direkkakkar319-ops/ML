import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.matrix import Matrix

def to_inverse(matrix):
    return matrix@matrix.inverse_2x2()

def is_identity(B):
    try: 
        A = B.data 
        n=len(A)   

        for row in A:
            if len(row)!=n:
                return False 
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    if abs(A[i][j]-1) > 1e-6:
                        return False
                else:
                    if abs(A[i][j])> 1e-6:
                        return False 
        return True 

    except Exception:
        return False 


def verify_inverse(matrix):
    try:
        result = to_inverse(matrix)
        if is_identity(result):
            return "Inverse is correct"
        else:
            return "inverse is wrong"
    except Exception:
        return "Matrix is Not invertable"

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[2, 5], [1, 3]])
C = Matrix([[1, 2], [2, 4]])

print(verify_inverse(A))
print(verify_inverse(B))
print(verify_inverse(C))