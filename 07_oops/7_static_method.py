"""
7. Static Method
Problem: Add a static method to the Car class that returns a general description of a car.

Static method is a method that belongs to a class rather than an instance of a class

"""

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport — they help"
    

# Create car objects
car1 = Car("Tata", "Nexon")
car2 = Car("Toyota", "Corolla")

# Calling static method
print(Car.general_description())     # ✅ Called using class name
print(car1.general_description())     # ✅ Also works, but not recommended
