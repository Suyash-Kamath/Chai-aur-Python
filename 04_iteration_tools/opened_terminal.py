# Iterable Objects

"""
list, file
"""

# Iteration tools
"""
for,comprehensions
"""

# response

"""
__next__

"""

"""
you can make iterable or non-iterable depending upon it has whether __next__ internal property or not 
"""


# whenever you want to open file then please open()

f=open('main.py')
# f.readline()
# readline(), har line pe kuch na kuch likha hai , ek array jaise hi hai

# this is the core syntax which makes the thing iterable f.__next__(), but this is the raw way of the behaviour of how python works internally to get the files
# raw way is not nicely handled but , crashing wala part aa sakta hai

# readline handles the execption of StopIteration and returns empty string

# for line in open('main.py').readlines():
# .readlines() was used earlier but it was very heavier for the memory so now no one uses it 

# for line in open('main.py'):
#     print(line,end="")

# ek extra line aaya kyuki print ke andhar /n thik se read nahi hota hai 

# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line,end='')

# test = ""
# if not test:
#     print("Chai")


# file ka khud ka bhi iter tool hota hai , f = open() me iter tool khud aata hai

myList = [1,2,3,4]

I = iter(myList)

print(I) # memory ka first starting point

print(I.__next__())
print(I)
"""
Doubt :

<list_iterator object at 0x1010a0c10>
1
<list_iterator object at 0x1010a0c10>


here the memory reference is not changed because , it is done by __next__ internally 
I be like me toh first ko hi point kar lunga , lekin internally ek pointer hai jisko me rakh raha hu , first ho chuka hai , abh , second me apne aap jayega 

memory reference jo list iterator  hai wo hamesha starting pe point karta hai 


"""

# print(I.__next__())
# print(I.__next__())
# print(I.__next__())
# print(I.__next__())


f = open('main.py')
# here is not need to do the same for the file , I = iter(myList)

# f behind the scene has already worked like this iter(f)

# print(iter(f) is f)
# print(iter(f) is f.__iter__())
#  all are same no matter aapne ye boldiya : iter(f), __iter__() or f

# remember : only for file : iter(f) and f are same 

# myNewList=[1,2,3]

# I = iter(myNewList)

# print(I is myNewList) # False

"""
File ko agar variabe ke andhar store karte ho , uska refernece leke , then wo apne aap me iterable object hai , but list me agar aapne memory reference me uska naam diya hai to wo nahi iterable object , wo bass actual object ka reference hai 


Dictinonary are also iterables

"""

D = {'a':1,'b':2}

# for key in D.keys():
#     print(key)

# let us do it manually , iter is manual iteration, and object diya jo actually iterable hai then reference aa jayega
I=iter(D)
# you can also use next() instead of __next__()

# print(next(I))
# print(next(I))
# print(next(I))

R = range(5)
print(R)

# range is also iterable
I = iter(R)
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))