class Matrix:
    def __init__(self, data):
        self.data = [list(row) for row in data]
        self.cols = len(self.data[0])
        self.rows = len(self.data)
        self.shape = (self.rows, self.cols)
    
    def __repr__(self):
        rows_str = "\n".join(str(row) for row in self.data)
        return f"Matrix({self.shape}):\n {rows_str}"
    
    def __add__(self,other):
        return Matrix([
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)  
        ])
    
    def __sub__(self,other):
        return Matrix([
            [self.data[i][j]-other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def scalar_multiply(self,scalar):
        return Matrix([
            [self.data[i][j] * scalar for j in range(self.cols)]
            for i in range(self.rows) 
        ])
    
    def element_wise_multiply(self,other):
        return Matrix([
            [self.data[i][j]*other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows) 
        ])

    def __matmul__(self,other):
        return self.matmul(other)

    def matmul(self,other):
        return Matrix([
            [
                sum(self.data[i][k]*other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows) 
        ])
    
    def transpose(self):
        return Matrix([
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols) 
        ])
    
    def determinant(self):
        if self.shape == (1,1):
            return self.data[0][0]
        if self.shape == (2,2):
            return self.data[0][0]*self.data[1][1]-self.data[0][1]*self.data[1][0]
        det=0 
        for j in range(self.cols):
            minor = Matrix([
                [self.data[i][k] for k in range(self.cols) if k!=j]
                for i in range(1,self.rows)
            ])
            det+=((-1)**j)*self.data[0][j]*minor.determinant()
        return det 

    def inverse_2x2(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular no inverse exists")
        return Matrix([
            [self.data[1][1]/det, -self.data[0][1]/det],
            [-self.data[1][0]/det, self.data[0][0]/det]
        ])
    def inverse_3x3(self):
        A = self.data

        # Step 1: determinant
        det = (
            A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
            - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
            + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0])
        )

        if abs(det) < 1e-9:
            raise ValueError("Matrix is not invertible")

        # Step 2: cofactors
        cof = [[0]*3 for _ in range(3)]

        cof[0][0] =  (A[1][1]*A[2][2] - A[1][2]*A[2][1])
        cof[0][1] = -(A[1][0]*A[2][2] - A[1][2]*A[2][0])
        cof[0][2] =  (A[1][0]*A[2][1] - A[1][1]*A[2][0])

        cof[1][0] = -(A[0][1]*A[2][2] - A[0][2]*A[2][1])
        cof[1][1] =  (A[0][0]*A[2][2] - A[0][2]*A[2][0])
        cof[1][2] = -(A[0][0]*A[2][1] - A[0][1]*A[2][0])

        cof[2][0] =  (A[0][1]*A[1][2] - A[0][2]*A[1][1])
        cof[2][1] = -(A[0][0]*A[1][2] - A[0][2]*A[1][0])
        cof[2][2] =  (A[0][0]*A[1][1] - A[0][1]*A[1][0])

        # Step 3: transpose (adjugate)
        adj = [[cof[j][i] for j in range(3)] for i in range(3)]

        # Step 4: divide by determinant
        inv = [[adj[i][j] / det for j in range(3)] for i in range(3)]

        return Matrix(inv)
    
    @staticmethod
    def identity(n):
        return Matrix([
            [1 if i==j else 0 for j in range(n)]
            for i in range(n)
        ])