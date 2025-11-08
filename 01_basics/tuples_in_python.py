all_tea = ('Herbal','Earl Grey','Black','Green','Oolong')

# if "Green" in all_tea:
    # print("Present Sir")

more_tea = ('Herbal','Earl Grey','Black','Green','Oolong')

print(all_tea is more_tea) # returns true 

print(more_tea.count("Herbal"))
tea_types = ('Black','Green','Oolong') 

# using tuples to unwrap tuples
(black,green,oolo) = tea_types

print(black)
print(green)

print(oolo)

print(type(tea_types))

# Nesting tuples , list and strings me bhi hoti , as well as dictionary