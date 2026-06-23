class ArithematicOperators: 
    def __init__(self, name, quantity):
        self.name = name 
        self.quantity = quantity 

    def __repr__(self):
        return f"ArithimaticOperators(name=`{self.name}`, quantity=`{self.quantity}`)"    
    
    """addition"""
    def __add__(self, other):
        if isinstance(other,ArithematicOperators) and self.name == other.name:
            return ArithematicOperators(self.name,  self.quantity+other.quantity)
        raise ValueError("Cannot add items of different types")
    
    """Subtraction"""
    def __sub__(self, other):
        if isinstance(other, ArithematicOperators) and self.name == other.name:
            if self.quantity>other.quantity:
                return ArithematicOperators(self.name, self.quantity - other.quantity)
    
    """Multiplication"""
    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return ArithematicOperators(self.name, int(self.quantity * factor))
        raise ValueError("Multiplication factor must be an integer")
     
    """floor division"""
    def __truediv__(self, factor):
        if isinstance(factor, (int, float)) and factor != 0:
            return ArithematicOperators(self.name, int(self.quantity / factor))
        raise ValueError("Division factor must be non-zero")
    
    """Equal to"""
    def __eq__(self, other):
        if isinstance(other , ArithematicOperators):
            return self.name == other.name and self.quantity == other.quantity
        return False
    
    """Less than"""
    def __lt__(self, other):
        if isinstance(other, ArithematicOperators) and self.name == other.name:
            return self.quantity > other.quantity
        raise ValueError("Two different values can't be compared")
    
    """Greater than"""
    def __gt__(self, other):
        if isinstance(other, ArithematicOperators) and self.name == other.name:
            return self.quantity < other.quantity
        raise ValueError("Two different values can't be compared")
    
    """Greater than or equal to"""
    def ___gte___(self, other):
        if isinstance(other, ArithematicOperators) and self.name == other.name:
            return self.quantity <= other.quantity
        raise ValueError("Two different values can't be comapred")
    
    """Not equal to"""
    def __ne__(self, other):
        if isinstance(other, ArithematicOperators) and self.name == other.name:
            return self.quantity != other.quantity
        raise ValueError("Two different values can't be compared")

item1 = ArithematicOperators("Apple", 50)
item2 = ArithematicOperators("Apple", 100)
item3 = ArithematicOperators("Banana", 200)

item_add = item1 + item2
print(item_add)

item_sub = item2 - item1  
print(item_sub)

item_mul = item2 * 3 
print(item_mul)

item_div = item2 / 2 
print(item_div) 
