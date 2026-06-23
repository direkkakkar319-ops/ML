# %% 
"""
Used to construct or buildt a new method
"""
class React:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
React(2, 3)


# %% 
"""__add__()"""
str1 = "hello"
str2 = "world"
new_str = str1.__add__(str2)
print(new_str)


# %%
"""__len__()"""
new_str = str1.__len__()
print(new_str)