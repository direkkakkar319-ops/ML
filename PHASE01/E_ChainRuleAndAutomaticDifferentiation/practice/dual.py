"""
Question
    Implement forward-mode autodiff using dual numbers.
    Create a Dual class and verify it gives the same 
    derivatives as your reverse-mode engine.
"""
class Dual:
    def __init__(self, real_number, dual_number=0.0):
        self.real_number = real_number
        self.dual_number = dual_number
    

    def __repr__(self):
        return f"Dual number: {self.dual_number}, Real Number: {self.real_number}"
    

    def __add__(self, other):
        other = other if (other, Dual) else Dual(real_number=other)

        return Dual(
            real_number=self.real_number + other.real_number,
            dual_number=self.dual_number + other.dual_number
        )
    

    def __mul__(self, other):
        other = other if (other, Dual) else Dual(real_number=other)

        return Dual(
            real_number=self.real * other.real,
            dual_number=self.real * other.dual + self.dual * other.real 
        )
    
    def __pow__(self, n):
        return Dual(
            real_number=self.real_number**n,
            dual_number=n*self.real_number ** (n-1) * self.dual_number
        )
    

    def relu(self):
        if self.real_number>0:
            return Dual(
                real_number=self.real_number,
                dual_number=self.dual_number
                )
        else:
            return Dual(
                real_number=0.0, 
                dual_number=0.0
                )        


if __name__ == "__main__":
    import sys
    sys.path.append(r"E:\ML\PHASE01\D_CalculusForML\core")
    from helper import cube
    x_val = Dual(
        real_number=2.0,
        dual_number=1.0
    )

    y = cube(x=x_val)

    print(y)