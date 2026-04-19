class Vector:
    def __init__(self, components):
        self.components = components
        self.dim = len(self.components)
    
    def __repr__(self):
        return f"Vector({self.components})"

    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.components, other.components)])
    
    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.components, other.components)])
    
    def __mul__(self, other):
        return Vector([a*b for a,b in zip(self.components, other.components)])

    def dot(self,other):
        return sum(a*b for a,b in zip(self.components, other.components))

    def magnitude(self):
        return sum(x**2 for x in self.components)**0.5