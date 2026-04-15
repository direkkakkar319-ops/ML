import numpy as np

a = np.array([1, 2, 3], dtype=float)
b = np.array([4, 5, 6], dtype=float)

print("="*40) 
print(f"ADDITION --> a + b = {a + b}")
print("="*40) 
print() 

print("="*40) 
print(f"DOT PRODUCT --> a · b = {np.dot(a, b)}")
print("="*40) 
print()

print("="*40) 
print(f"NORMALIZATION --> |a| = {np.linalg.norm(a):.4f}")
print("="*40) 
print()

print("="*40) 
print(f"COSINE SIMILARITY --> cosine = {np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)):.4f}")
print("="*40) 
print() 

W = np.random.randn(2, 3) * 0.1
x = np.array([1.0, 0.5, -0.3])
print("="*40) 
print(f"MATRIX MULTIPLICATION --> Wx = {W @ x}")
print("="*40) 