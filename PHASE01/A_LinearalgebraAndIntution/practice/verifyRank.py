"""
Verify rank of a matrix using rank() function
"""
class Vector:
    def __init__(self, components):
        self.components = components
        self.dim = len(self.components)
    
    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.components, other.components)])
    
    def dot(self, other):
        return sum(a*b for a,b in zip(self.components, other.components))

    def magnitude(self):
        return sum(x**2 for x in self.components)**0.5

    def normalize(self):
        mag = self.magnitude()
        return Vector([x/mag for x in self.components])
    
    def cosine_similarity(self, other):
        return self.dot(other)/(self.magnitude()*other.magnitude())

def projection(a,b):
    scalar=a.dot(b)/b.dot(b)
    return Vector([scalar*x for x in b.components])

def gram_schmit(vectors):
    orthogonal=[]
    for v in vectors:
        w=v 
        for u in orthogonal:
            proj = projection(w,u)
            w=w-proj 
        if w.magnitude()<1e-10:
            continue 
        orthogonal.append(w.normalize())
    return orthogonal

def rank(vectors):
    rank = len(gram_schmit(vectors))
    return rank 

"""Vector of 3x3 and rank 2"""
vectors = [
    Vector([1,2,3]),
    Vector([4,5,6]),
    Vector([5,7,9])
]

print("="*40)
print(f"rank of matrix is:{rank(vectors)}")
print("="*40)