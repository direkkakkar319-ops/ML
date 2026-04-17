"""
Project the vector [1, 2, 3] onto [1, 1, 1].
What does the result represent geometrically ?
"""
class Vector:
    def __init__(self, components):
        self.components = components 
        self.dim=len(self.components)
    
    def dot(self,other):
        return sum(a*b for a,b in zip(self.components, other.components))

    def __sub__(self,other):
        return Vector([a-b for a,b in zip(self.components, other.components)])
    def __repr__(self):
        return f"{self.components}"

def projection(a,b):
    scalar = a.dot(b)/b.dot(b)
    return Vector([scalar*x for x in b.components])

a = Vector([1, 2, 3])
b = Vector([1, 1, 1])

proj = projection(a, b)

print("="*40)
print("Projection:", proj)
print("="*40)

geometry = a-proj

print("="*40)
print(f"Geometry: {geometry}") 
print("="*40)

dot_product=geometry.dot(geometry)

print("="*40)
print(f"Dot product of Geometry{dot_product}")
print("="*40)

distance = geometry.dot(geometry) ** 0.5

print("="*40)
print("Distance from line:", distance)
print("="*40)