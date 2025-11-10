"""
5. Polymorphism
Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
"""





class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_info):
        super().__init__(brand,model)
        self.batter_info = battery_info
    def fuel_type(self):
        return "Electric Charge"
    
my_car = Car("Tata", "Safari")
my_tesla = ElectricCar("Tesla", "Model S", "85 kWh")

cars = [my_car, my_tesla]
for vehicle in cars:
    print(f"{vehicle.brand} {vehicle.model} → {vehicle.fuel_type()}")