"""

9. Class Inheritance and isinstance() Function
Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.


"""

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # ✅ Call parent constructor
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"
    

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(my_tesla.full_name())
print(my_tesla.fuel_type())

# 🔍 Checking instance relationships
print(isinstance(my_tesla, ElectricCar))   # ✅ True
print(isinstance(my_tesla, Car))           # ✅ True (because ElectricCar inherits Car)
print(isinstance(my_tesla, object))        # ✅ True (everything in Python inherits from object)


print(issubclass(ElectricCar, Car))     # ✅ True
print(issubclass(Car, ElectricCar))     # ❌ False
