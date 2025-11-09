"""

. Generator Function with yield
Problem: Write a generator function that yields even numbers up to a specified limit.

"""

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i



for num in even_generator(10):
    print(num)

# dhyaan rakhu ki return naa karu , bus value generate / yield karu and yaad rakhu ki me kaha ruka tha memory so that next time call kau toh yaad rakhu ki kahase values du 
# agar 2 loop call karega generator ko then python ko maalumn hota ha context

# what yield does is it returns value but memory me function ke saath saath state bhi rakhte ho