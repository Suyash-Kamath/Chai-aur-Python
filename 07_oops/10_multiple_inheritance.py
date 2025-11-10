# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.




# Parent class 1
class Battery:
    def battery_info(self):
        return "This car has a lithium-ion battery."


# Parent class 2
class Engine:
    def engine_info(self):
        return "This car has an electric motor instead of a fuel engine."
    
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    

# Child class (inherits from all three)
class ElectricCar(Battery, Engine, Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Calls Car’s __init__ (based on MRO)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"
    
my_tesla = ElectricCar("Tesla", "Model S", "85 kWh")

print(my_tesla.full_name())      # From Car
print(my_tesla.fuel_type())      # From ElectricCar
print(my_tesla.battery_info())   # From Battery
print(my_tesla.engine_info())    # From Engine
