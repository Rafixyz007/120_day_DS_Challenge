## 2. Micro Challenge: The Self Reference


## Goal: Explain why def method(self) is required.

class Car:
    speed = 0
    def drive(self):
        self.speed = 100

my_car = Car()
my_car.drive()

""" 
When an instance method is called in Python, Python automatically passes the object as the first argument.
The self parameter is required to receive this object.

my_car.drive() is actually executed internally as:
Car.drive(my_car)

Therefore, without self, the method cannot know which objects data it should work with.

"""
