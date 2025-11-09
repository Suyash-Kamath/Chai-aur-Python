username = "chaiaurcode"

# we are not concerned about if-else scopes , because they are only conditional check

# scope ko namespace bhi bolte hai

# every language follows the system upar upar jaatey jao. , means agar variable andhar na mile toh bahar milegaa hii

# python me poori file ko global maana jata hai 


username = "chaiaurcode"

def func():
    # username = "chai"
    print(username)

print(username)
func()


x = 99 
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x # global keyword apne aap global reference de raha hai ki me jis x ki baat kar raha hu, ye x me naya declare nahi kar raha hu, meh chahta hu ki aap global space me jaana  aur wahape x dekho and usko leke aao memory references me and saare jo changes hai and usage hai wo uss x ka kardo
#     x = 12
    
# func3()
# print(x)



def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()
# agar line 41 to 42 ka reference hi stored hai toh , usko pata kaise chala iski value kya thi x ki , this is called closure concept , defination of function ke saath saath   associated variables hai, unke references bhi jaate hai , this is bag theory 


# python me factory function ki naam se jaana jata hai ,also jyadatar closures 


"""
About closure:

How it works:
When the outer function is called and returns the inner function, the inner function "closes over" 
the environment of the outer function. This means it retains a reference to the values of the variables 
from the outer function's scope, even though the outer function's execution has completed and its local 
variables would normally be destroyed. When the returned inner function is later called, it can still 
access and use those "remembered" variables.

"""

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual



f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))