# Overwriting the `__repr__` and `__str__` methods
class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    
    def __repr__(self) -> str:
        """
        `__repr__` is meant to provide an unambiguous string representation of the object.
        It's often used for debugging and should ideally return a string that could be used
        to recreate the object.
        """
        return f"Person(name:{self.name!r}, age={self.age})"
    
    def __str__(self) -> str:
        """
        `__str__` is meant to provide a readable string representation of the object.
        It's what gets shown when you print the object or convert it to a string.
        """
        return f"{self.name}, {self.age} years old"


person_01 = Person("Direk", 19)
print(repr(person_01))
print(person_01)
