'''A geometry application needs to calculate the area of rectangles. Create a Rectangle
class that uses a constructor to initialize length and width. Add a method to calculate
and display the area.'''

class Rectangle:

    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def calculate_area(self):
        print("Rectangle Area:",self.length * self.width)

r = Rectangle(10,5)
r.calculate_area()
        