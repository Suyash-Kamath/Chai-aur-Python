# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

# Input from user
species = input("Enter the pet species (Dog/Cat): ").strip().lower()
age = float(input("Enter the pet's age (in years): "))

# Logic using conditionals
if species == "dog":
    if age < 2:
        print("Recommended food: Puppy food")
    elif 2 <= age <= 5:
        print("Recommended food: Adult dog food")
    else:
        print("Recommended food: Senior dog food")

elif species == "cat":
    if age < 2:
        print("Recommended food: Kitten food")
    elif 2 <= age <= 5:
        print("Recommended food: Adult cat food")
    else:
        print("Recommended food: Senior cat food")

else:
    print("Sorry, recommendation not available for this species.")
