import numpy as np 

A = np.array([[1, 2], [2, 4]])
print("="*40) 
print(f"Rank: {np.linalg.matrix_rank(A)}")
print("="*40) 
print() 

a = np.array([3, 4])
b = np.array([1, 0])
proj = (np.dot(a, b) / np.dot(b, b)) * b

print("="*40) 
print(f"Projection of {a} onto {b}: {proj}")
print("="*40)
print() 

Q, R = np.linalg.qr(np.random.randn(3, 3))

print("="*40)
print(f"Q is orthogonal: {np.allclose(Q @ Q.T, np.eye(3))}")
print("="*40)
print()

print("="*40)
print(f"R is upper triangular: {np.allclose(R, np.triu(R))}")
print("="*40)
print() 