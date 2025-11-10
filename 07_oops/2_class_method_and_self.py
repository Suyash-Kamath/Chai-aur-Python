"""
2. Class Method and Self
Problem: Add a method to the Car class that displays the full name of the car (brand and model).
"""

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model=model

    def full_name(self):
        return f"returns {self.brand} and {self.model}"


my_car = Car("Mahindra","XUV700")

print(my_car.full_name())