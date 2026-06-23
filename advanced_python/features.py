# %%
"""
Unpacking
    It refers to splitting up an iterable object
    and grabbing individual elements
"""

# Basic unpacking
a, b, c = [1, 2, 3]
print(f"a: {a}, b: {b}, c: {c}\n")

# Extended iterable unpacking with *
a, b, *c = [1, 2, 3, 4, 5, 6]
print(f"a: {a}, b: {b}, c: {c}\n")

# Ignoring values
a, _, c = [1, 2, 3]

# 
# %%
