# slicing dicing

tea_varieties = ["Masala","Ginger","Herbal","Milk"]

tea_varieties[1:2] = ['Lemon']
# Jaha slicing ho rahi hai , vaha value "string " karke assign karne ki koshish ki toh string ,array ki taraha treat ho gaya hai, so ek ek value individually gaya , so pass it like array 

print(tea_varieties)

tea_varieties[1:3] = ["Green","Masala"]

print(tea_varieties)

tea_varieties[1:1] # empty array , 1 se start karke 1 tak hi jaana hai lekin jo final value rehta hai wo excluding hota hai, so it means indexing me hamne kuch pass nahi kiya hai 

tea_varieties[1:1] = ["test","test"]
print(tea_varieties)

# delete operation
tea_varieties = ["Black","Green","Masala","White"]

tea_varieties[1:1] = ["test","test"]
print(tea_varieties)
tea_varieties[1:3] = []
print(tea_varieties)

# Copy

tea_varieties_copy=tea_varieties.copy()
tea_varieties_copy.append("Lemon")

print(tea_varieties_copy)
print(tea_varieties)


squarred_number = [x**2 for x in range(10)]
print(squarred_number)

cube_num = [x**3 for x in range(10)]
print(cube_num)