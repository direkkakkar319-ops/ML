import random
from mlp import MLP

random.seed(42)
model = MLP(sizes=[2, 4, 1])

xs = [[0, 0], [0, 1], [1, 0], [1, 1]]
ys = [-1, 1, 1, -1]  # XOR pattern (using -1/1 for tanh)

for step in range(100):
    preds = [model(x) for x in xs]
    loss = sum((pred-y)**2 for pred, y in zip(preds, ys))

    for parameter in model.parameters():
        parameter.grad = 0.0 
    
    loss.backward()

    lr = 0.05
    for parameter in model.parameters():
        parameter.data -= lr * parameter.grad
    
    if step % 20 == 0:
        print(f"step{step} loss={loss.data:.4f}")

print("\nPredictions after training:")
for x, y in zip(xs, ys):
    print(f"  input={x}  target={y:2d}  pred={model(x).data:6.3f}")