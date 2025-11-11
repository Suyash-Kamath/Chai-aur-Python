"""
Problem 2: Debugging Function Calls
Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.
"""

def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args) # join method string me , aapko iterable list deta hai precisely 
        kwargs_value = ', '.join(f"{key}:{value}" for key,value in kwargs.items())
        print(f"calling:{func.__name__} with args {args_value} and {kwargs_value} kwargs")
        return func(*args,**kwargs)
    
    return wrapper

@debug
def hello():
    print("Hello")

@debug
def greet(name,greeting="Hello"):
    print(f"{greeting}, {name}")


hello()
greet("chai",greeting="haanji")