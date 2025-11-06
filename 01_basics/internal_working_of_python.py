a_score = 10
score = 10

print(id(a_score))
print(id(score))
# same reference as python internally optimises it 

# Object becomes Object when it passes the reference

# Python is number powerful programming language
# there is reference_count which counts the reference whenever memory allocation happens

# Can we get to know the reference count ? , yes but there is actual problem

import sys
print(sys.getrefcount(24601))
# But I did not assign this , so how come output is 3 ?
# same for this 
print(sys.getrefcount("hitesh"))

# Internally compiler optimisation loop gets on , so every time it returns 3 
# There are pointers but this is not possible to reach as closely as possible to memory and get the ref_count
# you get the output same , so there is proof that there is no mechanism of counting

#  there is thing of ref_count but cannot be proven via print statement

#  Datatype goes into memory , never goes with the variable

#  So Python ke paas koi data type nahi hai kyuki variable ke andhar aap assign nahi karte , memory ke andhar datatype hota hai and it gets assigned in memory, so memory ke andhar jo reference hai uska datatype hota haii

a = 3  
#  it means 3 ka ek object aaya , uska assignment ho gaya a ke andhar 

# Python ke andhar ek exception hai in case of garbage collector
# Python numbers and strings which uses majorly, doesn't collect immediately , it takes time , what is 3's ref is taken again in the code , 
# Python doesn't wastes assign and re-assign computation power
#  Number and string ka late garbage collection hota hai
#  you can forcefully call garbage collection 

a="chaiaurcode"
a = 3.14
a=5
b=2
# Types of object is in object not in variables 
a=a+2

# 5 me garbage collector late hit hota hai and 7 object variable ko assign hota hai 

myListOne = [1,2,3]
myListTwo = myListOne
myListOne = 'chai'
print(myListTwo)

myListOne = [1,2,3]
print(myListTwo)
print(myListOne)
myListOne[0]=10
print(myListTwo)
print(myListOne)
print(id(myListTwo))
print(id(myListOne))

# List is mutable 

print("==============")

a= 500
b = 500
print(f"A's memory {id(a)} and B's memory {id(b)}")

print("==============")

l1 = [1,2,3]
l2=l1

#  List me agar same value bhi assign karoge naa toh naya reference banta hai 

# So here comes the immutability and mutability concept why list even though same value but different reference

# let's move onto the next topic 

h1 = [1,2,3]
h2 = h1[:]
#  here the reference is not passed , copy is passed , so pass by value
#  Slicing kiya hai to copy banta hai and uska reference deta hai 

#  Copy ka library hota hai

import copy
h2 = copy.copy(h1)

# deepcopy karke bhi hoti hai , matlab list ke andhar ek list hoti toh wo nahi hogi copy , toh deepcopy use karnaa padega 

# Usually copy me ek hi level ki list aati hai , deepcopy se nested bhi laate hai

print("==============")

listBolte = [1,2,3,[4,5,6]]
listHiBolte = copy.copy(listBolte)
print(listHiBolte)

listHameshaBolo = copy.deepcopy(listBolte)

print(listHameshaBolo)

print("================")

# Diff between == and is operator

n = [1,2,3]
m=n

print(m==n)
print(m is n)

#  == checks the value and is checks the memory reference

# Python me Dynamic reference type aata hai , apne aap pata lagata hai konsi datatype aane waala hai 
#  Definations memory ke andhar rakhi jaati , variables ke paas nahi hoti hai ye informations 