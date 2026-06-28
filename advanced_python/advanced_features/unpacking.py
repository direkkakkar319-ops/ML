# %%
"""
Unpacking
    It refers to splitting up an iterable object and grabbing
    individual elements
"""
# %%
# Basic unpacking
a, b, c = [1, 2, 3]
print(f"a: {a}, b: {b}, c: {c}\n")

# %%
# Extended iterable unpacking with *
a, b, *c = [1, 2, 3, 4, 5, 6]
print(f"a: {a}, b: {b}, c: {c}\n")

# %%
# Ignoring values using unpacking
a, _, c = [1, 2, 3]

# %%
# Unpacking nested structure
data = ("Alice", (25, "Engineer"))
name, (age, profession)= data

# %%
# Unpacking in Funcntion Arguments
def print_names(*names):
    for name in names:
        print(name)
print_names("Alice", "Bob", "Tim")

# %%
# Combining lists with unpacking
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = [*list1, *list2]
print(f"Combined list {combined_list}")
print(*list1) # print without brackets

# %%
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined_dict = {**dict1, **dict2}
print(f"Combined dictionary: {combined_dict}")

# %%
x = 10
y = 20
print(f"Before swap: x:{x}, y:{y}")
x, y = y, x 
print(f"After swap: x:{x}, y:{y}")
