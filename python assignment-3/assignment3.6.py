# Create the custom Python classes which have methods and attributes and implement single inheritance, multiple inheritance, and multilevel inheritance

# Base class - 1
class Vehicle:
    def __init__(self,vehicle):
        self.vehicle = vehicle

# Children of Vehicle - Intermediate class - 1
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__('Car')
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.brand} {self.model}"

# Base class - 2
class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        return f"{self.fuel_type} engine"
    
# Children of Car
class SUV(Car):
    def __init__(self,brand,model,doors):
        super().__init__(brand,model)
        self.doors = doors

    def display_info(self):
        return f"{super().display_info()}, {self.doors} doors"


class ElectricCar(Car,Engine):
    def __init__(self, brand, model,fuel_type,speed):
        Car.__init__(self,brand, model)
        Engine.__init__(self,fuel_type)
        self.speed = speed
    
    def display_info(self):
        return f"{Car.display_info(self)}, {Engine.start(self)}, speed: {self.speed} mph"

# Single Inheritance
car = Car('Tata','Safari')
print(car.display_info())

# Multilevel Inheritance
punch = SUV('Tata','Punch','4')
print(punch.display_info())

# Multiple Inheritance
tesla = ElectricCar('Tesla','Model 4','electric',200)
print(tesla.display_info())

