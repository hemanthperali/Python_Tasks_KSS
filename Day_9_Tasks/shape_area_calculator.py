'''A graphics application needs to calculate the area of different shapes. Create classes
Circle, Rectangle, and Triangle, each having an area() method. Demonstrate
polymorphism by calling the same method for different objects.'''

class Circle:
    def area(self):
        r = 5
        print("Area of Circle:",3.14*r*r)

class Rectangle(Circle):
    def area(self):
        l = 4
        b = 6
        print("Area of Rectangle:",l*b)

class Triangle(Circle):
    def area(self):
        b = 5
        h = 10
        print("Area of Triangle:",0.5*b*h)

c = Circle()
r = Rectangle()
t = Triangle()

c.area()
r.area()
t.area()
