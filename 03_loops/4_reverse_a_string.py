"""
Problem: Reverse a string using a loop.


Note:

🔹 Memory explanation

input_str = "Python"

When this runs, Python creates a string object "Python" in memory.

The variable input_str points to that object’s memory location.

So input_str → "Python"

reversed_str = ""

This creates another string object — the empty string "".

Even though it looks small, it’s still an independent object in memory.

So reversed_str → ""

✅ So yes — reversed_str has its own memory assigned, even if it’s just an empty string.

🧠 Extra concept: immutability

Strings in Python are immutable, meaning you can’t change them in place.
So if later you do something like:

reversed_str += "n"


Python doesn’t modify the old empty string.
Instead, it creates a new string "n" and reassigns reversed_str to point to that new object.

Each update creates a new memory object.
"""

input_str = "Python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str  

print(reversed_str)