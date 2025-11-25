import math

class Shape:
    def area(self):
        print("Area not defined")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


square = Square(5)
circle = Circle(3)

print("Square area:", square.area())
print("Circle area:", circle.area())