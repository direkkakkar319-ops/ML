import sys
import os
import math
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.matrix import Matrix

def sigmoid(x):
    return 1 / (1 + math.exp(-x))
    
"""Input for the network"""
A = Matrix([[1, 2, 3],[4, 5, 6]])

"""Initializing the weights"""
W1 = Matrix.random(3,4)
b1 = Matrix.random(1,4)

W2 = Matrix.random(4,2)
b2 = Matrix.random(1,2)

"""Step-forward pass""" 
b1_expanded = b1.repeat_rows(A.rows)
Z1 = A @ W1 + b1_expanded # layer 1
A1 = Z1.apply(sigmoid)

b2_expanded = b2.repeat_rows(A1.rows)
Z2 = A1 @ W2 + b2_expanded # layer 2
A2 = Z2.apply(sigmoid)

"""Printing shapes""" 
print("A(Matrix):", A.shape)
print("W1:", W1.shape)
print("Z1:", Z1.shape)
print("A1:", A1.shape)
print("W2:", W2.shape)
print("Z2:", Z2.shape)
print("A2:", A2.shape)

print("="*40)
print(f"{A.shape}--->{Z1.shape}--->{Z2.shape}")
print("="*40) 