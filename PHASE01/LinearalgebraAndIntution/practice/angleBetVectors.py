import numpy as np
class Vector:
    def __init__(self, components):
        self.components = list(components)
        self.dim = len(self.components)
    
    def dot(self, other):
        return sum(a*b for a,b in zip(self.components, other.components)) 
    
    def magnitude(self):
        return sum(x**2 for x in self.components)**0.5
    
    def anglebetween(self,other):
        dot_product = self.dot(other)
        mag_product = self.magnitude() * other.magnitude() 

        if mag_product ==0:
            raise ValueError("Cannot compute angle with zero vector")

        angle_between = dot_product/mag_product

        angle_between = max(-1, min(1, angle_between))

        angle = np.arccos(angle_between)
        return np.degrees(angle)
    
    def __repr__(self):
        return f"Vector({self.components})" 

a = Vector([1, 2, 3])
b = Vector([4, 5, 6])

print("a =", a)
print("b =", b)
print(f"Angle between a and b = {a.anglebetween(b):.2f} degrees")