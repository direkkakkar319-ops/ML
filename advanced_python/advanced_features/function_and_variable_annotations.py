name: str = "Direk"
age: int = "19"
is_student: bool = True

# Funcrion annotations
def greet(person: str, age: int) -> str:
    """
    Greets a person by name and age.

    :param person: The name of the person (expected to be a string).
    :param age: The age of the person (expected to be an integer).
    :return: A greeting message (expected to be a string).
    """
    return f"Hello, {person}! You are {age} years old."

# Using the function
greeting_message = greet(person=name, age=age)
print(greeting_message)

print("\nFunction Annotations:", greet.__annotations__)
print("Variable Annotations:", globals().get("__annotations__", {}))
