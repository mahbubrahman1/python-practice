
class Shopping:

    cart = []

    def add_to_cart(self, item):
        self.cart.append(item)


cus1 = Shopping()
cus1.add_to_cart("Shirt")
print(cus1.cart)


class Shopping:

    def __init__(self) -> None:
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)


cus1 = Shopping()
cus1.add_to_cart("Shirt")
print(cus1.cart)

cus2 = Shopping()
cus2.add_to_cart("Pant")
print(cus2.cart)


class Shopping:

    def __init__(self):
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)


cus1 = Shopping()
cus1.add_to_cart("Sandle")
print(cus1.cart)

cus2 = Shopping()
cus2.add_to_cart("Shirt")
print(cus2.cart)

cus3 = Shopping()
cus3.add_to_cart("T-Shirt")
print(cus3.cart)

cus4 = Shopping()
cus4.add_to_cart("Pant")
print(cus4.cart)

cus5 = Shopping()
cus5.add_to_cart("Shoes")
print(cus5.cart)

cus6 = Shopping()
cus6.add_to_cart("Mask")
print(cus6.cart)


# caile amra evabeo likhte pari

class Car_shop:

    def __init__(self):
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)

    def info(self):
        print(self.cart)


cus1 = Car_shop()
cus1.add_to_cart("Allion")
cus1.info()

cus2 = Car_shop()
cus2.add_to_cart("Premio")
cus2.info()

cus3 = Car_shop()
cus3.add_to_cart("Axio")
cus3.info()


"""=== === === === === === ==="""


class One_Bank:

    def __init__(self) -> None:
        self.balance = 5000

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return amount


# use class
my_bank = One_Bank()
my_bank.withdraw(3000)
print(my_bank.get_balance())


class Dhaka_Bank:

    def __init__(self) -> None:
        self.minimum = 100
        self.balance = 5000

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < self.minimum:
            print("No money for you")
        else:
            self.balance = self.balance - amount
            return amount


my_bank = Dhaka_Bank()
my_bank.withdraw(98)
print(my_bank.get_balance())


class Bank:

    def __init__(self) -> None:
        self.minimum = 100
        self.balance = 10000

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < self.minimum:
            print("No money for you")
        elif amount > self.balance:
            print("You are broke! No money!")
        else:
            self.balance = self.balance - amount
            return amount


# now use class
my_bank = Bank()
my_bank.withdraw(990)
balance = my_bank.get_balance()
print("Now my balance:", balance)

my_bank.withdraw(1200)
balance = my_bank.get_balance()
print("after that:", balance)
