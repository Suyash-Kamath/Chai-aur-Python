"""

8. Property Decorators
Problem: Use a property decorator in the Car class to make the model attribute read-only.



"""

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model

    @property
    def model(self):
        return self.__model
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    

my_car = Car("Tata", "Safari")

# Accessing model (works fine)
print(my_car.model)     # ✅ "Safari"

# Trying to change model (will fail)
my_car.model = "Nexon"  # ❌ Raises AttributeError
