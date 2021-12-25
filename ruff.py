
# class Bank:

#     def __init__(self):
#         self.balance = 5000

#     def get_balance(self):
#         return self.balance

#     def withdraw(self, amount):
#         self.balance = self.balance - amount
#         return amount

# # now use class
# my_bank = Bank()
# my_bank.withdraw(500)
# balance = my_bank.get_balance()
# print(balance)

# my_bank.withdraw(100)
# balance = my_bank.get_balance()
# print(balance)

# my_bank.withdraw(400)
# balance = my_bank.get_balance()
# print(balance)


# class One_Bank:

#     def __init__(self) -> None:
#         self.balance = 5000

#     def get_balance(self):
#         return self.balance

#     def withdraw(self, amount):
#         self.balance = self.balance - amount
#         return amount

# # use class
# my_bank = One_Bank()
# my_bank.withdraw(3000)
# print(my_bank.get_balance())


# class Bank:

#     def __init__(self) -> None:
#         self.balance = 5000

#     def get_balance(self):
#         return self.balance

#     def withdraw(self, amount):
#         self.balance = self.balance - amount

# # now use class
# my_bank = Bank()
# my_bank.withdraw(2000)
# print("After withdraw:", my_bank.get_balance())


# class One_Bank:

#     def __init__(self) -> None:
#         self.minimum = 100
#         self.balance = 5000

#     def get_balance(self):
#         return self.balance

#     def withdraw(self, amount):
#         if amount < self.minimum:
#             print("You have to withdraw above 100tk")
#         else:
#             self.balance = self.balance - amount
#             return amount

# # now use class
# my_bank = One_Bank()
# my_bank.withdraw(1989)
# print(my_bank.get_balance())


# class School:

#     def class_one(self):
#         print("This is class 1")

#     def class_two(self):
#         print("This is class 2")

#     def class_three(self):
#         print("This is class 3")

#     def class_four(self):
#         print("This is class 4")

#     def class_five(self):
#         print("This is class 5")

# class High_School(School):

#     # school import in High_School
#     def class_six(self):
#         print("This is class 6")

#     def class_seven(self):
#         print("This is class 7")

#     def class_eight(self):
#         print("This is class 8")

#     def class_nine(self):
#         print("This is class 9")

#     def class_ten(self):
#         print("This is class 10")

# all_class = High_School()
# all_class.class_one()
# all_class.class_two()
# all_class.class_three()
# all_class.class_four()
# all_class.class_five()
# all_class.class_six()
# all_class.class_seven()
# all_class.class_eight()
# all_class.class_nine()
# all_class.class_ten()


# Python program to demonstrate
# method overriding


# # Defining parent class
# class Parent():

#     # Constructor
#     def __init__(self):
#         self.value = "Inside Parent"

#     # Parent's show method
#     def show(self):
#         print(self.value)

# # Defining child class
# class Child(Parent):

#     # Constructor
#     def __init__(self):
#         self.value = "Inside Child"

#     # Child's show method
#     def show(self):
#         print(self.value)


# # Driver's code
# obj1 = Parent()
# obj2 = Child()

# obj1.show()
# obj2.show()


# class Shape:

#     def __init__(self, dim1, dim2):
#         self.dim1 = dim1
#         self.dim2 = dim2

# class Triangle(Shape):

#     def area(self):
#         area = 0.5 * self.dim1 * self.dim2
#         return area

# class Rectangle(Shape):

#     def area(self):
#         area = self.dim1 * self.dim2
#         return area


# tri = Triangle(20, 30)
# rec = Rectangle(20, 30)

# print("Triangle Area =", tri.area())
# print("Ractangle Area =", rec.area())


# phone = {"Brand:" : "Apple", "Model:" : "iPhone 11Pro", "Color:" : "MidNight Green"}

# for x, y in phone.items():
#     print(x, y)


# num = [5, 4, 6, 3, 45, 6, 4, 7, 54, 67, 34, 21, 90]

# for i in num:
#     if i == 90:
#         print("I find it")
#         break
# else:
#     print("I can't find it")


# num = [5, 3, 4, 2, 6, 7]

# for x in num:
#     if x == 70:
#         print("found")
#         break
# else:
#     print("not fou


# if mid element is lower


# def factorial(n):

#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * 1
#     return fact

# print(factorial(5))


# def find_fib(n):
#     if n <= 2:
#         return 1

#     fib_x, fib_next = 1, 1

#     i = 3
#     while i <= n:
#         i = i + 1
#         fib_x, fib_next = fib_next, fib_x + fib_next

#     return fib_next

# for x in range(0, 10):
#     print(find_fib(x))


# def fibo(num):

#     a = 0
#     b = 1
#     print(0)
#     print(1)

#     for i in range(2, num):
#         result = a + b
#         a = b
#         b = result
#         print(result)

# fibo(10)


# t = int(input("How many number do you enter: "))

# for i in range(t):
#     x = int(input("enter number: "))

#     if x % 2 == 0:
#         print("this number is even")
#     else:
#         print("this number is odd")


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

result = a + b + c

print("Result =", result)
