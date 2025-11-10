"""
6. Class Variables Problem: Add a class variable to Car that keeps track of the number of cars created.

"""


class Car:
    total_cars =0

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

        Car.total_cars+=1

    def full_name(self):
        return f"{self.brand} and {self.model}"
    
car1 = Car("Tata", "Nexon")
car2 = Car("Toyota", "Corolla")
car3 = Car("Tesla", "Model S")

print("Total cars created:", Car.total_cars)