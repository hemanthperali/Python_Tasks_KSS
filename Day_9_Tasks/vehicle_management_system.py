'''A transport company manages different vehicles. Create a base class Vehicle with
attributes like brand and speed. Create derived classes Car and Bike that inherit from
Vehicle and display their details.'''

class Vehicle:
    brand = "Hyundai"
    speed = "160 Kmph"

    def display(self):
        print("Brand:",self.brand)
        print("Speed:",self.speed,"\n")

class Car(Vehicle):
    brand = "BMW"
    speed = 200

    def show(self):
        print("Car Details:")
        self.display()

class Bike(Vehicle):
    brand = "TVS"
    speed = 80

    def show(self):
        print("Bike Details:")
        self.display()

c = Car()
b = Bike()
c.show()
b.show()
