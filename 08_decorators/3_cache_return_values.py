"""
Problem 3: Cache Return Values
Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

"""


import time


def cache(func):
    cache_value={}
    def wrapper(*args,**kwargs):
        key = (args,frozenset(kwargs.items()))
        if key in cache_value:
            return cache_value[key]
        
        result = func(*args,**kwargs)
        cache_value[key] = result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(2,b=6))
print(long_running_function(2,b=6))
print(long_running_function(4,3))
print("Done")

# Dictionary cannot be used as key due to it can be easily changed , so used frozen set 