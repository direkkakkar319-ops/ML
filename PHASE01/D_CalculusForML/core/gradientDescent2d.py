from partialDerivative import numerical_gradient

from helper import f_2d

point = [4.0, 3.0]
lr = 0.1 
steps = 50

for step in range(steps):
    grad = numerical_gradient(f_2d, point)
    point = [p-lr*g for p, g in zip(point , grad)]
    # `zip(point, grad)` pairs the coordinates with their corresponding gradients
    loss = f_2d(point)

    if step % 5 == 0 or step == 49:
        print(f"step{step:2d}  point=({point[0]:7.4f}, {point[1]:7.4f}) f={loss:.6f}")
