
# protected
# class Bank:
#
#     def __init__(self) -> None:
#         self._name = "One_bank"
#
# account = Bank()
# print(account._name)


# # private
# class Bank:
#
#     def __init__(self) -> None:
#         self.__name = "One_Bank"
#
# account = Bank()
# print(account.__name)


# class Bank:

#     def __init__(self):
#         self.__balance = 1000

# account = Bank("Mahbub")
# print(account.name)
# print(account.__balance)


# class Bank:

#     def __init__(self, name) -> None:
#         self.name = name
#         self.__balance = 1000

#     def get_balance(self):
#         return self.__balance

# account = Bank("Mahbub")
# print(account.name)
# print(account.get_balance())


# class Shape:

#     def __init__(self, a, b):
#         self.__a = a
#         self.__b = b


# class Triangle(Shape):

#     def area(self):
#         area = 0.5 * self.__a * self.__b
#         return area

# tri = Triangle(20, 30)
# print("Triangle area =", tri.area())


class Shape:

    def __init__(self, a, b):
        self._a = a
        self._b = b


class Triangle(Shape):

    def area(self):
        area = 0.5 * self._a * self._b
        return area


tri = Triangle(20, 30)
print("Triangle area =", tri.area())
