# In List , ordered rehta hai and indexes are key but the keys are predefined

chai_types = {"Masala":"Spicy","Ginger":"Zesty",
              "Green":"Mild"}

print(chai_types)

chai_types["Green"]="Fresh"

print(chai_types)

# for chai in chai_types:
#     print(chai,chai_types[chai])

# key value pair is called items 
for key,value in chai_types.items():
    print(key,value)

if "Masala" in chai_types:
    print("I have Masala Chai")


chai_types["Earl Grey"] = "Citrus"

print(chai_types)
# List me there is no need to pass key because sequential tha lekin this is not sequential so pass the key to pop
chai_types.pop("Ginger")
print(chai_types)

chai_types.popitem()
# removes the last added
print(chai_types)

del chai_types["Green"] # memory se reference delete karta hai
print(chai_types)

# copy

chai_types_copy = chai_types.copy()


squarred_num = {x:x**2 for x in range(6)}
print(squarred_num)

squarred_num.clear()
print(squarred_num)

keys = ["Masala","Ginger","Lemon"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys,keys)

print(new_dict)