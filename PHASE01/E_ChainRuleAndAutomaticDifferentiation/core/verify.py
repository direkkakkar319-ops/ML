from value import Value


x1 = Value(data=2.0)
x2 = Value(data=3.0)

a = x1 * x2
b = a + Value(data=1.0)

y = b.relu()
y.backward()

print(f"y={y.data}")
print(f"dy/dx1 = {x1.grad}")
print(f"dy/dx2 = {x2.grad}")

# if we need a more complex expression
a = Value(data=2.0)
b = Value(data=-3.0)
c = Value(data=10.0)
f = (a*b+c).relu() 

f.backward()

print(f"df/da = {a.grad}")
print(f"df/db = {b.grad}")
print(f"df/dc = {c.grad}")