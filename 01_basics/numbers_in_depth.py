# Numbers in python is very strong compared to other languages
# Number's paradigm is very openned as soon as you include numpy
# Strings are also strong but there is no match with Numbers

# Numbers are not single objects but they are group of objects
# Sets are also/almost part of numbers internally 

# Compiler which is underhood of python is of c/c++ , 
# double in c , almost the same precision is given by python, underhood woi apis connect karni hai
# coding in those language is slight tough , so wrappers of those languages are made 

# In python : higher precision is given value
# also if you want to perform activity first then use parantheses as everyone knows it is high priority
x=2
y=3
z=4
print((x+y)*z)

print(float(40+2.23)) # this is okay, but intention should be clear what you want , so added float

# print(float('suyash'+3)) => error

repr('suyash')
str('chai')
print('chai')

"""
The difference between repr('suyash'), str('chai'), and print('chai') lies in their purpose and the way they represent string data in Python. 
1. repr('suyash') 

• repr() provides a "developer-friendly" or "official" string representation of an object. 
• Its goal is to be unambiguous and, ideally, to return a string that could be used to recreate the object. 
• For a string literal, repr() will return the string enclosed in quotes, showing its literal representation. 

>>> repr('suyash')
"'suyash'"

2. str('chai') 

• str() provides a "user-friendly" or "informal" string representation of an object. 
• Its goal is to be readable and easily understandable by a human user. 
• For a string literal, str() will simply return the string itself without any enclosing quotes. 

>>> str('chai')
'chai'

3. print('chai') 

• print() is a function that outputs a string to the console. 
• When print() is used with an object, it implicitly calls the object's __str__() method to get its string representation before printing it. 
• Therefore, print('chai') will display the user-friendly representation of the string 'chai' to the console. 

>>> print('chai')
chai

In summary: 

• repr() provides a literal, unambiguous representation, often used for debugging and development. 
• str() provides a human-readable representation, suitable for display to users. 
• print() outputs the str() representation of an object to the console. 

AI responses may include mistakes.
"""


# Chained comparison

# x<y<z is same as x<y and y<z 

a = 5
b = 6
c =7

print(a<b>c)

#  This is important , you should know how the values are placed

1==2<3

# True or false literal value is 1 or 0 
# as soon as you write 1, it gets replaced by True
print(True==2<3)
# actually 1 is number but True's literal number value is 1 

# trunc function of math.trunc() will always take you towards 0
# in python , number precision is almost infiinite

print(0o20) # octol means base 8 , 0 to 7,so isliye 20 likha ,  0o likha means octal

print(0xFF)

print(0b1000)


print(int('64',8)) # 64 ka octal chaiye 

import random

print(random.randint(1,100)) # last is not included so it means 1 to 99

print(random.choice([1,2,3,4]))

l1= ["Suyash","Krishna","Ram"]
print(random.choice(l1))


random.shuffle(l1)
print(l1)

# The real problem with python is here

print((0.1+0.1+0.1)-0.3)
# The Decimal precision is itself problematic
# There is the thing called Decimal Context manager , so learn it 

from decimal import Decimal
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))

from fractions import Fraction

myFra = Fraction(2,7)
print(myFra)


setone = {1,2,3,4}
print(setone & {1,3})
print(setone | {1,3,7})

print(setone - {1,2,3,4})
# empty curly braces nahi aaya kyuki it means dictionary ,you output set() aayega 
# if you want to denote empty set then please denote this way set()

print(True is 1)
# objects are differenet but values are same internally