# 105- create a vehicle class with max speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


some_model1 = Vehicle(220, 15)
print(some_model1.max_speed, some_model1.mileage)


# 106- create a vehicle class without any variables and methods.

class Vehicle:
    pass


# 107- create a child class Bus that will inherit all of the variables and methods
# of the vehicle class.

# given
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


school_bus = Bus("some Buss", 150, 12)
print(school_bus.name, school_bus.max_speed, school_bus.mileage)


# 108- create a Bus class that inherits from the Vehicle class. Give the capacity argument
# of Bus.seating_capacity() a default value of 50.
# use the following code for your parent vehicle class. you need to use method overriding.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers."


class Bus(Vehicle):

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


School_buss = Bus("Bussy Bus", 100, 10)
print(School_buss.seating_capacity())


# 109- Define property that should have the same value for every class instance.
# Define a class attribute "color" with a default value white. every vehicle should be white.

class Vehicle:

    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


schooll_bus = Bus("Benz", 110, 20)
print(schooll_bus.color)

# 110-
"""
create a Bus child class that inherits from the vehicle class. The default fare charge
of any vehicle is seating capacity * 100. if vehicle is Bus instance, we need to add
an extra 10% on full fare as a maintenance charge. so total fare for bus instance will
become the final amount = total fare + 10% of the total fare.

Note: the bus seating capacity is 50. so the final fare amount should be 5500. you need
to override the fare() method of a vehicle class in Bus class.

use the following code for your parent vehicle class. we need to access the parent class
from inside a method of a child class.
"""


class Vehicle:

    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):

    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount


Buss = Bus("volvo", 10, 50)
print(Buss.fare())


# 111- Determine if school_Bus is an instance of the vehicle class.
class Vehicle:

    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


school_Bus = Bus("Benz", 14, 35)

print(isinstance(school_Bus, Vehicle))
