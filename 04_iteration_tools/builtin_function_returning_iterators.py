it = map(lambda x: x*2, [1, 2, 3])
for x in it:
    print(x)

print(list(it))
print(list(it))


"""
Important Behavior of map():

map() is lazy → it does NOT compute all values at once.

The values are only created when iterating.

Once exhausted, the iterator cannot be reset or reused.
"""