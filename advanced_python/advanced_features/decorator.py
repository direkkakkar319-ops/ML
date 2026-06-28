def my_decorator(func):
    """
    A simple decorator that prints a message before and after 
    the execution of the function.
    """

    def wrapper(*args, **kwargs):
        print("-"*40)
        result = func(*args, **kwargs)
        print("-"*40)
        return result
    
    return wrapper

@my_decorator
def say_hello(name):
    """
    A simple function that generates the user.
    """
    print(f"Hello {name}")

@my_decorator
def add(a, b):
    """
    A simple function that returns the sume of two numbers.
    """
    sum = a+b 
    print(f"Sum of a:{a} and b:{b} is {sum}")

if __name__ == "__main__":
    say_hello("Direk")
    add(13, 13)