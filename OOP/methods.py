class Phone:
    Name = "Samsung Galaxy Note20 Ultra"

    def hard_work(self):
        print("Chat Chat Chat")
    
my_phone = Phone()
my_phone.hard_work()



class Car:
    Name = "Honda Civic"

    def start_car(self):
        print("Boom Boom......")

my_car = Car()
my_car.start_car()



class Calculator:
    Brand = "Casio"

    def add(self, a, b):
        return a + b
    
my_clc = Calculator()
print(my_clc.add(2, 4))




class Calculator:
    Brand = "casio"

    def deduct(self, a, b):
        return a - b
    
my_clc = Calculator()
result = my_clc.deduct(100, 20)
print(result)



class Calculator:
    Brand = "Citysun"

    def multiply(self, x, y):
        return x * y

my_calc = Calculator()
result = my_calc.multiply(5, 2)
print(result)




class Calculator:
    Brand = "Casio"

    def subtruc(self, m, n):
        total = m - n
        return total
    
my_calc = Calculator()

result = my_calc.subtruc(20, 10)
print("Result =", result)




class laptop:

    Model_Name = " "
    Brand = " "
    RAM = " "

    def info(self):
        print("Name:", self.Model_Name)
        print("Brand:", self.Brand)
        print("RAM:", self.RAM)

my_laptop = laptop()
my_laptop.Model_Name = "Galaxy Book Pro"
my_laptop.Brand = "Samsung"
my_laptop.RAM = "8GB"
my_laptop.info()



class Laptop:

    Model_Name = " "
    Brand = " "
    RAM = " "

    def laptop_info(self, Model_name, Brand, RAM):
        self.Model_Name = Model_name
        self.Brand = Brand
        self.RAM = RAM

    def info(self):
        print("Name:", self.Model_Name)
        print("Brand:", self.Brand)
        print("RAM:", self.RAM)

my_laptop = Laptop()
my_laptop.laptop_info("G.B. Pro", "Samsung", "8GB")
my_laptop.info()




class Student_info:

    name = " "
    roll = " "
    semester = " "

    def set(self, name, roll, semester):
        self.name = name
        self.roll = roll
        self.semester = semester
    
    def info(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Semester:", self.semester)
    
my_info = Student_info()
my_info.set("Mahbubur Rahman", 163895, "5th")
my_info.info()




class Friends_laptop:

    Model_Name = " "
    Brand = " "
    RAM = " "

Mahbub_laptop = Friends_laptop()
print("Mahbub's Laptop--")
Mahbub_laptop.Model_Name = "Galaxy Book Pro"
Mahbub_laptop.Brand = "Samsung"
Mahbub_laptop.RAM = "8GB"
print("Name:", Mahbub_laptop.Model_Name)
print("Brand:", Mahbub_laptop.Brand)
print("RAM:", Mahbub_laptop.RAM)

Habib_laptop = Friends_laptop()
print("Habib's Laptop--")
Habib_laptop.Model_Name = "Vivobook S15"
Habib_laptop.Brand = "Asus"
Habib_laptop.RAM = "8GB"
print("Name:", Habib_laptop.Model_Name)
print("Brand:", Habib_laptop.Brand)
print("RAM:", Habib_laptop.RAM)

Nila_laptop = Friends_laptop()
print("Nila's Laptop--")
Nila_laptop.Model_Name = "Pavilion 601"
Nila_laptop.Brand = "HP"
Nila_laptop.RAM = "16GB"
print("Name:", Nila_laptop.Model_Name)
print("Brand:", Nila_laptop.Brand)
print("RAM:", Nila_laptop.RAM)

# ekhane code onek likhte hoy but methode use korle aro sohoj hoy

class Friends_laptop:

    Model_Name = " "
    Brand = " "
    RAM = " "

    def info(self):
        print("Name:", self.Model_Name)
        print("Brand:", self.Brand)
        print("RAM:", self.RAM)

Mahbub_laptop = Friends_laptop()
Mahbub_laptop.Model_Name = "Galaxy Book Pro"
Mahbub_laptop.Brand = "Samsung"
Mahbub_laptop.RAM = "8GB"
Mahbub_laptop.info()

Habib_laptop = Friends_laptop()
Habib_laptop.Model_Name = "Vivobook S15"
Habib_laptop.Brand = "Asus"
Habib_laptop.RAM = "8GB"
Habib_laptop.info()

Nila_laptop = Friends_laptop()
Nila_laptop.Model_Name = "Pavilion 601"
Nila_laptop.Brand = "HP"
Nila_laptop.RAM = "16GB"
Nila_laptop.info()

# caile aro sohoje lekha jay----



class Friends_laptop:
    
    Model_Name = " "
    Brand = " "
    RAM = " "

    def laptop_info(self, Model_name, Brand, RAM):
        self.Model_Name = Model_name
        self.Brand = Brand
        self.RAM = RAM

    def info(self):
        print("Name:", self.Model_Name)
        print("Brand:", self.Brand)
        print("RAM:", self.RAM)

Mahbub_laptop = Friends_laptop()
Mahbub_laptop.laptop_info("G.B. Pro", "Samsung", "8GB")
Mahbub_laptop.info()

Habib_laptop = Friends_laptop()
Habib_laptop.laptop_info("V.B. S15", "Asus", "16GB")
Habib_laptop.info()

Nila_laptop = Friends_laptop()
Nila_laptop.laptop_info("M.Book D15", "Huawei", "32GB")
Nila_laptop.info()





# f use korle sob pashapashi dekhabe....

class Phone:
    Name = " "
    Brand = " "
    RAM = " "
    Made_in = " "

    def set_info(self, Name, Brand, RAM, Made_in):
        self.Name = Name
        self.Brand = Brand
        self.RAM = RAM
        self.Made_in = Made_in
    
    def phone_info(self):
        print(f"Phone Name:", self.Name, "Brand:", self.Brand, "RAM:", self.RAM, "Made in", self.Made_in)

A50 = Phone()
A50.set_info("Galaxy A50", "Samsung", "4GB", "China")
A50.phone_info()

A70 = Phone()
A70.set_info("Galaxy A70", "Samsung", "6GB", "India")
A70.phone_info()

A30 = Phone()
A30.set_info("Galaxy A30", "Samsung", "3GB", "Vietnam")
A30.phone_info()




""" === modify attributes === """

class Bank:
    account_balance = 5000

    def get_balance(self):
        return self.account_balance
    
my_account = Bank()
balance = my_account.get_balance()
print(balance) 



class Student:
    info = "All Student"

    def get_info(self):
        return self.info
    
my_name = Student()
result = my_name.get_info()
print(result)



















