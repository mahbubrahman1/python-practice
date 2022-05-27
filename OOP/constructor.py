import math


class Phone:

    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model


my_phone = Phone("Samsung", "Galaxy S21")
print(my_phone.Brand)
print(my_phone.Model)


class Student:

    def __init__(self, Name, Roll, Department):
        self.Name = Name
        self.Roll = Roll
        self.Department = Department


MR = Student("M.R.", 95, "CSE")
print("Name:", MR.Name)
print("Roll:", MR.Roll)
print("Department:", MR.Department)


class Car:

    def __init__(self, n, c, y):
        self.name = n
        self.color = c
        self.year = y


my_car = Car("Allion", "White Pearl", 2012)
print("Model_name:", my_car.name)
print("Color:", my_car.color)
print("Year:", my_car.year)
"""
এখানে যখন আমি my_car = Car(“Corolla”, “White”) লিখছি,
তখন __init__(self, n, c)-এর self-এ যাচ্ছে my_car অবজেক্টের র
েফারেন্স, n-এ যাচ্ছে “Corolla”, আর c-তে যাচ্ছে “White”। তারপর যখন
self.name = n স্টেটমেন্ট এক্সিকিউট হচ্ছে, তখন my_car অবজেক্টের name
নামে একটি অ্যাট্রিবিউট তৈরি হচ্ছে আর সেখানে n অ্যাসাইন হচ্ছে। একইভাবে
color অ্যাট্রিবিউট তৈরি হয়ে সেখানে c-তে যা পাঠিয়েছিলাম, তা অ্যাসাইন হচ্ছে।

Car ক্লাসে যে দুটি ডেটা অ্যাট্রিবিউট তৈরি করেছিলাম (name ও color),
সেগুলো কিন্তু আমি বাদ দিয়ে দিয়েছি। কারণ আমি অবজেক্ট তৈরি করার সময়
 init মেথডের ভেতরে self.name ও self.color যখন লিখছি, তখন
সেই অবজেক্টের জন্য name ও color নামে অ্যাট্রিবিউট তৈরি হয়ে যাচ্ছে।
একে বলে ইনস্ট্যান্স অ্যাট্রিবিউট, যা কেবল ওই ক্লাসের ইনস্ট্যান্সের (বা অবজেক্টের)
থাকে। তবে এখন কিন্তু আর ক্লাসের নাম লিখে ডট দিয়ে name (ও color)
একসেস করা যাবে না। আমরা যদি লিখি print(Car.name), তাহলে আমরা
এরর পাবো : AttributeError: type object ‘Car’ has no attribute ‘name’।
"""


class Car:

    def __init__(self, n, c, y) -> None:
        self.name = n
        self.color = c
        self.year = y

    def info(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Year:", self.year)


my_car = Car("Allion", "Sky Blue", 2008)
my_car.info()

# এখন আমরা চাইলে একাধিক কার অবজেক্ট তৈরি করতে পারি।


class Car:

    def __init__(self, n, c, y) -> None:
        self.name = n
        self.color = c
        self.year = y

    def info(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Year:", self.year)


my_car = Car("Allion", "Sky Blue", 2008)
my_car.info()

mahfuj_car = Car("Premio", "White Pearl", 2010)
mahfuj_car.info()

rahi_car = Car("Civic", "Red", 2022)
rahi_car.info()

mahi_car = Car("CRV", "Gray", 2010)
mahi_car.info()


class Student:

    def __init__(self, n, r) -> None:
        self.name = n
        self.roll = r


mahbub = Student("Mahbubur Rahman", 95)
print(f"Name:", mahbub.name, "Roll:", mahbub.roll)

siddik = Student("Siddikur Rahman", 76)
print(f"Name:", siddik.name, "Roll:", siddik.roll)

marzan = Student("Marzan Rahman", 72)
print(f"Name:", marzan.name, "Roll:", marzan.roll)


class Student:

    name = " "
    department = ""
    roll = " "

    def __init__(self, name, department, roll):
        self.name = name
        self.department = department
        self.roll = roll

    def info(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Roll:", self.roll)


mahbub = Student("Mahbubur Rahman", "CSE", 163895)
mahbub.info()

siddik = Student("Siddikur Rahman", "CSE", 163876)
siddik.info()

# more info check this video: https://www.youtube.com/watch?v=Yh8kivPAFZM&list=PLgH5QX0i9K3rz5XqMsTk41_j15_6682BN&index=54&ab_channel=AnisulIslam
# subeen website: http://pybook.subeen.com/object-class-python/
""" === trivujer ketrofol nirnoy"""


class Triangle:

    def calculate_area(self, base, height):
        return base * height


total = Triangle()
x = total.calculate_area(10, 20)
print(x)


class Triangle:

    def __init__(self, b, h) -> None:
        self.base = b
        self.height = h

    def calculate_area(self):
        print("Area =", 0.5 * self.base * self.height)


total1 = Triangle(10, 20)
total1.calculate_area()

total2 = Triangle(20, 30)
total2.calculate_area()


class Triangle:

    def __init__(self, b, h) -> None:
        self.base = b
        self.height = h

    def calculate_area(self):
        return 0.5 * self.base * self.height


total1 = Triangle(10, 20)
print("Area =", total1.calculate_area())

total2 = Triangle(20, 30)
print("Area =", total2.calculate_area())
"""=== britter ketrofol nirnoy"""


class Circle:

    def __init__(self, r) -> None:
        self.radius = r

    def calculate_area(self):
        return math.pi * self.radius * self.radius


total_area = Circle(4)
print("Area = %0.2f" % total_area.calculate_area())
"""=== duita songkhar moddhe jug"""


class Addition:

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def calculate(self):

        return self.a + self.b


total1 = Addition(10, 20)
print(total1.calculate())

# caile amra aro add korte pari

total2 = Addition(100, 500)
print(total2.calculate())
total3 = Addition(100, 200)
print(total3.calculate())
"""=== guloker ketrofol nirnoy"""


class Sphere:

    def __init__(self, r) -> None:
        self.radius = r

    def calculate_area(self):
        return 4 * math.pi * self.radius * self.radius


total = Sphere(5)
print("Sphere area = %0.2f" % total.calculate_area())
