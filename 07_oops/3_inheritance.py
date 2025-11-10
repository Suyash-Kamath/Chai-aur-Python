"""

3. Inheritance
Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

"""


class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} and {self.model}"
    


class ElectricCar(Car):
    def __init__(self,brand,model,battery_info):
        self.batteryinfo = battery_info
        super().__init__(brand,model)

    def battery_size(self):
        return f"Battery Size - {self.batteryinfo}"
    


my_tesla = ElectricCar("Tesla","Model S","85 kwH")

print(my_tesla.full_name())
print(my_tesla.battery_size())