def f(x): # return square of `x`
    return x ** 2

def f_2d(point):
    x, y = point 
    return x ** 2 + y ** 2

def f_multi(point):
    x, y = point 
    return x**2 + 3*x*y + y**2

def saddle(x, y):
    return x ** 2 - y ** 2

def bowl(x, y):
    return x ** 2 + y ** 2
