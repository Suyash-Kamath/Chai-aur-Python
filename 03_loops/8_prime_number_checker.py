"""

8. Prime Number Checker
Problem: Check if a number is prime.


A prime number is a natural number greater than 1 that has only two factors: 1 and itself.


"""

number = 28

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)