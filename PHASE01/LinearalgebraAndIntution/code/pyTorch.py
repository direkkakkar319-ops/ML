import torch

x = torch.randn(3, requires_grad=True)
y = torch.tensor([1.0, 0.0, 0.0])

similarity = torch.dot(x, y)
similarity.backward()

print("="*40) 
print(f"x = {x.data}")
print("="*40)
print()

print("="*40)
print(f"y = {y.data}")
print("="*40)
print()

print("="*40)
print(f"dot product = {similarity.item():.4f}")
print("="*40)
print()

print("="*40)
print(f"d(dot)/dx = {x.grad}")
print("="*40)
print()