

import math


class A:

    def features1(self):
        print("Feature 1 working")

    def features2(self):
        print("Feature 2 working")


class B(A):

    def features4(self):
        print("Feature 4 working")

    def features6(self):
        print("Feature 6 working")


my = B()
my.features1()
my.features2()
my.features4()
my.features6()

# # ekhane A holo parent class/super class and B holo child class/sub class


class Phone:

    def call(self):
        print("You can call")

    def message(self):
        print("You can message")


class Apple(Phone):

    def photo(self):
        print("You can take photo")


my_phone = Apple()
my_phone.message()
my_phone.call()
my_phone.photo()


class School:

    def class_one(self):
        print("This is class 1")

    def class_two(self):
        print("This is class 2")

    def class_three(self):
        print("This is class 3")

    def class_four(self):
        print("This is class 4")

    def class_five(self):
        print("This is class 5")


class High_School(School):

    # school import in High_School
    def class_six(self):
        print("This is class 6")

    def class_seven(self):
        print("This is class 7")

    def class_eight(self):
        print("This is class 8")

    def class_nine(self):
        print("This is class 9")

    def class_ten(self):
        print("This is class 10")


all_class = High_School()
all_class.class_one()
all_class.class_two()
all_class.class_three()
all_class.class_four()
all_class.class_five()
all_class.class_six()
all_class.class_seven()
all_class.class_eight()
all_class.class_nine()
all_class.class_ten()


# class Shape:
#
#     def __init__(self, dim1, dim2):
#         self.dim1 = dim1
#         self.dim2 = dim2
#
# class Triangle(Shape):
#
#     def area(self):
#         area = 0.5 * self.dim1 * self.dim2
#         return area
#
# class Rectangle(Shape):
#
#     def area(self):
#         area = self.dim1 * self.dim2
#         return area
#
#
# tri = Triangle(20, 30)
# rec = Rectangle(20, 30)
#
# print("Triangle Area =", tri.area())
# print("Ractangle Area =", rec.area())


class Phone():

    def __init__(self, brand, price, netwark) -> None:
        self.brand = brand
        self.price = price
        self.netwark = netwark

    def recharge(self):
        print("Eating Electricity:")
        print("Electrons are Yummy!")


my_phone = Phone("Apple", 100, "Airtel")
my_phone.recharge()


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
