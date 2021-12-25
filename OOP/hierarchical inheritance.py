import math


class Shape:

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b


class Triangle(Shape):

    def area(self):
        area = 0.5 * self.a * self.b
        return area


class Rectangle(Shape):

    def area(self):
        area = self.a * self.b
        return area


class Circle(Shape):

    def area(self):
        area = math.pi * self.a * self.a
        return area


tri = Triangle(8, 6)
rec = Rectangle(9, 2)
cir = Circle(7, 3)

print("Triangle area =", tri.area())
print("Ractangle area =", rec.area())
print("Circle area = %0.2f" % cir.area())
