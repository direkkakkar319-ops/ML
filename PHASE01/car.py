class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year 
    
    """this method is used for the user otuput mostly"""
    def __str__(self):
        return f"{self.make}, {self.model}, {self.year}"
    
    """
    this method is used for developer or debug the output 
    as it is more detailed output helping the devs for 
    understandin the code better
    """
    def __repr__(self):
        return f"Car(make=`{self.make}`, model=`{self.model}`, year=`{self.year}`)"

make_car = Car("Toyota", "Corolla", 2018)

print(str(make_car))  # Toyota, Corolla, 2018
print(repr(make_car)) # Car(make=`Toyota`, model=`Corolla`, year=`2018`)
