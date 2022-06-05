# method overriding bolte bujhay aki methot abar define kora
# class Phone:

#     def __init__(self) -> None:
#         print("I am Phone")

# class Samsung(Phone):
    
#     def __init__(self) -> None:
#         print("I am Samsung")
    
# my = Samsung()




class Phone:

    def __init__(self) -> None:
        print("I'm Phone")
    
class Samsung(Phone):

    def __init__(self) -> None:
        super().__init__()
        print("I'm Samsung")
    
my = Samsung()



class Shape:

    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2
   
class Triangle(Shape):

    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        return area
    
class Rectangle(Shape):
    
    def area(self):
        area = self.dim1 * self.dim2
        return area


tri = Triangle(20, 30)
rec = Rectangle(20, 30)

print("Triangle Area =", tri.area())
print("Ractangle Area =", rec.area())
    




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



















