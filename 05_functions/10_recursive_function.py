"""
10. Recursive Function
Problem: Create a recursive function to calculate the factorial of a number.

"""


def factorial(num):

    if num ==0:
        return 1
    else:
        return num*factorial(num-1)

print(factorial(4))