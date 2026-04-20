import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.matrix import Matrix

def to_inverse2x2(matrix):
    return matrix@matrix.inverse_2x2()

def to_inverse3x3(matrix):
    return matrix@matrix.inverse_3x3()

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


def verify_inverse2x2(matrix):
    try:
        result = to_inverse2x2(matrix)
        if is_identity(result):
            return "Inverse is correct"
        else:
            return "inverse is wrong"
    except Exception:
        return "Matrix is Not invertable"

if __name__ == "__main__":
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[2, 5], [1, 3]])
    C = Matrix([[1, 2], [2, 4]])
    print("="*40) 
    print(verify_inverse2x2(A))
    print(verify_inverse2x2(B))
    print(verify_inverse2x2(C))
    print("="*40)

def verify_inverse3x3(matrix):
    try:
        result = to_inverse3x3(matrix)
        if is_identity(result):
            return "Inverse is correct"
        else:
            return "inverse is wrong"
    except Exception:
        return "Matrix is Not invertable" 

print() 

if __name__ == "__main__":
    A = Matrix([[1, 2, 3],[0, 1, 4],[5, 6, 0]])
    B = Matrix([[2, -1, 0],[1,  2, -1],[3,  0,  1]])
    C = Matrix([[1, 2, 3],[2, 4, 6],[1, 1, 1]])

    print("="*40)
    print(verify_inverse3x3(A))
    print(verify_inverse3x3(B))
    print(verify_inverse3x3(C))
    print("="*40) 