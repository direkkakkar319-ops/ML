class Matrix:
    def __init__(self, rows):
        self.rows = [list (row) for row in rows]
        self.shape = (len(self.rows), len(self.rows[0]))

    def mul_vector(self, vector):    
        if len(vector)!=self.shape[1]:
            raise ValueError("Vector size must match the number of matrix columns")
        
        result = []
        for row in self.rows:
            value = sum(row[i]*vector[i] for i in range(len(vector)))
            result.append(value) 
        
        return result

    def __repr__(self):
        return f"matrix({self.rows})"

m = Matrix([[2,0],[0,3]])
v=[1, 1]
print("="*40)
print("MATRIX APPLIED TO VECTOR -->",m.mul_vector(v))
print("="*40)