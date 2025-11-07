# Mostly we use unicode string 
# Read about unicode and utf-8
# Character encoding


# String to List
chai = "Lemon, Ginger, Masala, Mint"
print(chai.split(', ')) # comma and space ke basis pe split karo mere bhai

chai = "Masala Chai"
print(chai.find("Chai"))

chai = "Masala Chai Chai Chai"
print(chai.find("Chai")) # first occurrence

print(chai.count("Chai"))

chai_type = "Masala Chai"
quantity=2

order_formatting = "I ordered {} cups of {} "

# curly braces are placeholders and you can add variables

print(order_formatting.format(quantity,chai_type))



chai_variety = ["Lemon","Masala","Ginger"]
# List to string
print(", ".join(chai_variety))


chai = "He said, \"Masala chai is awesome\""
print(chai)


# Windows has also \ , so what is the solution , what iF i WANT TO PRINT THE PATH
# easy solution is if you use raw string 
chai = "Masala\nChai"
print(chai)
chai = r"Masala\nChai"
print(chai)

chai = r"c:\user\pwd"
print(chai)

# what is unicodescaping here

# chai = "c:\user\pwd"
# print(chai)
# le "/Users/suyash/Desktop/Chai-aur-Python/01_basics/strings_in_python.py", line 50
#     chai = "c:\user\pwd"
#            ^^^^^^^^^^^^^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape

chai = "c:\\user\\pwd"
print(chai)

chai = "Masala Chai"
print("Masala" in chai)