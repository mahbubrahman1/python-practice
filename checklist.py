# hello world...
# *************

# print("Hello, World!")


# * variables..
# ***********

# x = 50
# y = 70
# print(x)
# print(y)

# x = 10
# x = "Really"
# print(x)


# * type..
# ********

# x = 10
# print(type(x))

# check = True
# print(type(check))

# num = 10.5
# print(type(num))


# ? Many Values to Multiple Variables..
# num1, num2, num3 = 60, 40, 20
# print(num2)


# ? One Value to Multiple Variables..
# a = b = c = "hello"
# print(b)
# print(a)

# num1 = num2 = num3 = 100
# print(num3)


# * Unpack a Collection...
# **********************

# companies = ["Google", "Microsoft", "Apple", "Samsung"]
# c1, c2, c3, c4 = companies
# print(c3)
# print(c2)


# ? multiple variables, separated by a comma
# x = "How"
# y = "Are"
# z = "You?"
# print(x, y, z)

# x = "How"
# y = "Are"
# z = "You?"
# print(x + " " + y + " " + z)


# * Built-in Data Types....
# **********************

# x = 5
# print(type(x))

# num = 20
# print(type(num))

# x = True
# print(type(x))

# li = [5, 6, 3, 4, 9, 8]
# print(type(li))

# li = {
#     "Brand" : "Samsung",
#     "Model" : "Galaxy S8"
# }
#
# print(type(li))

# x = range(8)
# print(type(x))

# x = {"Samsung", "Google", "Apple", "Xiaomi"}
# print(type(x))

# name = None
# print(type(name))


# * Python Numbers.......
# ********************

# x = 10
# y = 4.5
# z = 1j
# print(type(x))
# print(type(y))
# print(type(z))

# ? int
# x = 1
# print(type(x))

# ? float
# a = 4.5
# print(type(a))

# ? complex
# m = 3h
# print(type(m))

# n = -5y
# print(type(n))


# * type conversion......
# *******************

# ? it means conver from one type to another type
# x = 5.5
# x = int(x)
# print(x)

# x = 5
# x = float(x)
# print(x)

# x = 13
# x = complex(x)
# print(x)

# a = complex(1 + 2j)
# print(a)


# * type casting......
# ******************

# x = int(15.5)
# print(x)

# n = 80
# convert = str(n)
# print(convert)


# * string........
# **************

# country_name = "Bangladesh"
# result = country_name[1]
# print(result)

# ? loop through
# name = "Canada"
# for i in name:
#     print(i)

# for i in "Canada":
#     print(i)

# ? String Length
# name = "Bangladesh"
# print(len(name))

# text = "I Love My Country"
# print(len(text))

# ? Check String
# text = "No one really cares"
# check = "one" in text
# print(check)

# text = "No one really cares"
# check = "Because" in text
# print(check)

# text = "No one really cares"
# check = "Because" not in text
# print(check)

# text = "No one really cares"
# check = "really" not in text
# print(check)

# ? use it in an if statement
# text = "No one really cares"
# if "because" not in text:
#     print("No, 'because' is not in the sentense")

#! slicing strings
# name = "Bangladesh"
# print(name[2:5]) #Get the characters from position 2 to position 5

# person = "Mahbubur"
# sl = person[:4] # Get the characters from the start to position 5 
# print(sl)

# sentense = "helloworld"
# print(sentense[4:])

# text = "helloworld"
# print(text[-4:-2])

# text = "howareyoujohn"
# print(text[2:5])

# text = "howareyoujohn"
# print(text[3:])

#! modify strings
# name = "mahbubur rahman"
# print(name.upper())

# name = "Mahbubur Rahman"
# print(name.lower())

# txt = "Hello World"
# print(txt.replace("H", "i"))

# txt = "How are you?"
# result = txt.split(" ")
# print(result)

#! String Concatenation
# first_name = "John"
# last_name = "Smith"
# print(first_name + last_name)

# first_name = "John"
# last_name = "Smith"
# print(first_name + " " + last_name)


# * python operators........
# **********************

#! Arithmetic Operators
# a = 50
# b = 60
# print(a + b)

# x = 50
# y = 30
# print(x - y)

# a = 6
# b = 2
# print(a * b)

# x = 100
# y = 5
# print(x / 5)

# x = 111
# y = 12
# print(x % y)
# etc etc

#! Comparison Operators
# a = 50
# b = 50
# print(a == b)

# a = 60
# b = 50
# print(a != b)

# a = 60
# b = 60
# print(a != b)

# a = 70
# b = 30
# print(a > b)

# a = 60
# b = 100
# print(a > b)

# a = 60
# b = 100
# print(a < b)

#    >=
#    <=

#! logical operators
# ? and - ei khtre duita condition e true hote hobe
# a = 100
# print(a > 10 and a < 200)

# x = 20
# print(x > 30 and x < 40)

# ? or - ei khtre duitar moddhe jekunu ekta condition true hote hobe
# x = 40
# print(x > 60 or x < 100)

# ? not - negative korbe. ulta thakbe
# print(not True)

# print(not False)

# x = 2
# y = 5
# print(not x > y)

#! Identity Operators
#? is
# x = 50
# y = 60
# x = y
# print(x is y)

# a = [5, 7, 3, 9, 1]
# b = [5, 7, 3, 9, 1]
# print(a is b) # two references refer to the same object
# print(a == b) # two objects have the same value

#? is not
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is not z)

#! Membership Operators
#? in
# string = "How are you"
# print("How" in string) 

# string = "How are you"
# print("Hello" in string) 

# companies = ["Apple", "Google", "Microsoft", "Amazon"]
# check = "Meta" in companies
# print(check)

# companies = ["Apple", "Google", "Microsoft", "Amazon"]
# check = "Asus" in companies
# print(check)

#? not in
# companies = ["Apple", "Google", "Microsoft", "Amazon"]
# check = "Asus" not in companies
# print(check)

# companies = ["Apple", "Google", "Microsoft", "Amazon"]
# check = "Google" not in companies
# print(check)

# * python Lists........
# **********************

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# companies = ["Apple", "Microsoft", "Amazon", "Meta"]
# print(len(companies))

# my_list = ["John", 19, True, "Male"]
# print(my_list)

#? creating a list
# this_list = list(("apple", "samsung", "google"))
# print(this_list)

#? Access List Items
# companies = ["Apple", "Microsoft", "Amazon", "Meta"]
# print(companies[2])

# companies = ["Apple", "Microsoft", "Amazon", "Meta"]
# print(companies[-1])

# companies = ["Apple", "Microsoft", "Amazon", "Meta", "Samsung", "Google", "Asus", "Dell"]
# print(companies[2:6])
#TODO NOTE-[ekhane 2 index a ache amazon so protome amazon theke print kora shuru korbe. ebong 6 index a ache Asus kintu asus print korbe na karon sobsomoy sesherta theke 1 biyug hobe 6 theke 1 bihug korle 5 hobe so index 5 porjonto print korbe]

# companies = ["Apple", "Microsoft", "Amazon", "Meta", "Samsung", "Google", "Asus", "Dell"]
# print(companies[3:])

# companies = ["Apple", "Microsoft", "Amazon", "Meta", "Samsung", "Google", "Asus", "Dell"]
# print(companies[-6 : -2])

#? Change List Items
# companies = ["Apple", "Microsoft", "Amazon", "Meta"]
# companies[1] = "Samsung"
# print(companies)

# companies = ["Apple", "Microsoft", "Amazon", "Meta", "Google", "Samsung"]
# companies[1:4] = ["Dell", "Asus"]
# print(companies)

#? Insert Items
# companies = ["Apple", "Microsoft", "Amazon", "Meta", "Google", "Samsung"]
# companies.insert(3, "Asus")
# print(companies)

#? Append Items
# companies = ["Apple", "Microsoft", "Amazon"]
# companies.append("Samsung")
# print(companies)

#? Extend List - mane ektar sathe arekta jug kora..
# top_brand = ["Apple", "Samsung", "Google"]
# mid_brand = ["Xiaomi", "Oneplus", "Huawei"]
# top_brand.extend(mid_brand)
# print(top_brand)

#? Remove List Items
# top_brand = ["Apple", "Samsung", "Google"]
# top_brand.remove("Google")
# print(top_brand)

# top_brand = ["Apple", "Samsung", "Google"]
# top_brand.pop(0)
# print(top_brand)

# top_brand = ["Apple", "Samsung", "Google"]
# top_brand.pop(1)
# print(top_brand)

# top_brand = ["Apple", "Samsung", "Google"]
# top_brand.pop()
# print(top_brand)

# top_brand = ["Apple", "Samsung", "Google"]
# del top_brand[0]
# print(top_brand)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

#? Loop Lists
# companies = ["Apple", "Microsoft", "Amazon"]
# for i in companies:
#     print(i)

#? List Comprehension
# my_list = []
# for i in range(10):
#     my_list.append(i)

# print(my_list)


# numbers = [2, 4, 8, 6, 10]
# square_numbers = []
# for number in numbers:
#     square_numbers.append(number * number)

# print(square_numbers)


# companies = ["apple", "samsung", "google", "amazon"]
# new_companies = []

# for company in companies:
#     if "a" in company:
#         new_companies.append(company)
    
# print(new_companies)

#? Sort Lists
# numbers = [5, 7, 3, 2, 1, 9]
# numbers.sort()
# print(numbers)

# numbers = [5, 7, 3, 2, 1, 9]
# numbers.reverse()
# print(numbers)

#? join lists
# list1 = [5, 6, 3, 2, 7]
# list2 = ["a", "e", "g"]
# result = list1 + list2
# print(result)

# list1 = [5, 6, 3, 2, 7]
# list2 = ["a", "e", "g"]

# for i in list2:
#     list1.append(i)

# print(list1)


# * python Tuples........
# **********************

# my_tup = ("Samsung", "Apple", "Xiaomi")
# print(my_tup)

# my_tup = ("Samsung", "Apple", "Xiaomi")
# print(type(my_tup))

#TODO NOTE-[Tuple items are ordered, unchangeable, and allow duplicate values]

# this_tuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(this_tuple)

# this_tuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(len(this_tuple))

# this_tuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(this_tuple[2])

# my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(my_tuple[2:5])

# my_tuple = ("Apple", "Banana", "Cherry")
# if "Apple" in my_tuple:
#     print("yes, 'apple' is in the fruits tuple")

#? Update Tuples
#TODO NOTE-[Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.]

# x = ("apple", "banana", "cherry")
# x[1] = "mango"
# print(x)


# my_list = ("apple", "banana", "cherry")
# his_list = list(my_list)
# his_list[2] = "mango"

#TODO NOTE-[Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.]
# my_tuple = ("apple", "banana", "cherry")
# x = list(my_tuple)
# x.append("orange")
# my_tuple = tuple(x)

#? Unpack Tuples
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# more check w3school...


# * python sets........
# **********************

# this_set = {"apple", "banana", "cherry"}
# print(this_set)
#todo NOTE-[Set items are unordered, unchangeable, and do not allow duplicate values ]

#? add set items
# my_set = {"Samsung", "Apple", "Xiaomi"}
# my_set.add("Google")
# print(my_set)

# my_set = {"apple", "banana", "cherry"}
# new_set = {"pineapple", "mango", "papaya"}
# my_set.update(new_set)
# print(my_set)

# more check w3school..

# * python dictionaries...
# ************************

#todo NOTE-[Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates. Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.]

# phone = {
#     "Brand" : "Samsung",
#     "Model" : "Galaxy S22",
#     "Price" : "$999"
# }

# print(phone)

# phone = {
#     "Brand" : "Samsung",
#     "Model" : "Galaxy S22",
#     "Price" : "$999"
# }

# print(phone["Model"])

# phone = {
#     "Brand" : "Samsung",
#     "Model" : "Galaxy S22",
#     "Price" : "$999",
#     "Launch Date" : "09 February 2022"
# }

# print(len(phone))

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# print(thisdict)

#! Access Dictionary Items
# phone = {
#     "Brand" : "Samsung",
#     "Model" : "Galaxy S22",
#     "Price" : "$999"
# }

# result = phone["Model"]
# print(result)

# result = phone.get("Price")
# print(result)

# show_keys = phone.keys()
# print(show_keys)

# show_values = phone.values()
# print(show_values)

# phone["Launch Date"] = "09 Fabruary 2022"
# print(phone)

# result = phone.items()
# print(result)

# if "Price" in phone:
#     print("Yes")

#? Change Dictionary Items
#! change values
# phone = {
#     "Brand" : "Samsung",
#     "Model" : "Galaxy S22",
#     "Price" : "$999",
#     "Launch Date" : "09 February 2022"
# }

# phone["Model"] = "Galaxy S22 Ultra"
# print(phone)

# phone = {
#     "Brand" : "Samsung",
#     "Model" : "Galaxy S22",
#     "Price" : "$999",
#     "Launch Date" : "09 February 2022"
# }

# phone.update({"Model" : "Galaxy S8"})
# print(phone)

#? Adding Items
# phone = {
#     "Brand" : "Samsung",
#     "Model" : "Galaxy S22",
#     "Price" : "$999",
#     "Launch Date" : "09 February 2022"
# }

# phone["Colors"] = ["Phantom White", "Phantom Black", "Pink Gold", "Greem", "Graphite", "Cream", "Sky Blue", "Violet"]
# print(phone)

#? Removing Items
# phone = {
#     "Brand" : "Samsung",
#     "Model" : "Galaxy S22",
#     "Price" : "$999",
#     "Launch Date" : "09 February 2022"
# }

# phone.pop("Price")
# print(phone)

# del phone["Model"]
# print(phone)

# clear full dictionary
# phone.clear()
# print(phone)

#? Loop Through a Dictionary
phone = {
    "Brand" : "Samsung",
    "Model" : "Galaxy S22",
    "Price" : "$999",
    "Launch Date" : "09 February 2022"
}

# for i in phone:
#     print(i) # only show the Keys

# for i in phone:
#     print(phone[i]) # only show the Values

# for i in phone.keys():
#     print(i) # only show the Keys

# for i in phone.values():
#     print(i) # only show the Values

# for i, j in phone.items():
#     print(i, j) # show both keys and values

#? Nested Dictionaries
# my_laptop = {
#     "laptop1" : {
#         "Brand" : "Dell",
#         "Model" : "XPS 17"
#     },
#     "laptop2" : {
#         "Brand" : "Apple",
#         "Model" : "MacBook Pro"
#     },
#     "laptop3" : {
#         "Brand" : "Samsung",
#         "Model" : "Galaxy"
#     }
# }

# print(my_laptop)

# result = my_laptop["laptop2"]
# print(result)

# result = my_laptop["laptop2"]['Brand']
# print(result)

# my_laptop["laptop4"] = {
#     "Brand" : "Asus",
#     "Model" : "ROG Flow X15"
# }

# print(my_laptop)


# * python if...Else, Elif
# **********************

# a = 20
# b = 10
# if a > b:
#     print("a is greater than b")

# more more more.............


# * functions
# **********************

# def my_function():
#     print("Hello from a function")

# print(my_function())

# def my_function(a, b):
#     print(a + b)

# print(my_function(3, 5))

# def full_name(first_name, last_name):
#     print(first_name + " " + last_name)

# print(full_name("Mahbubur", "Rahman"))

#? default parameter
# def my_function(country = "Norway"):
#     print("I am from" + country)

# print(my_function("Finland"))
# print(my_function())

# def my_function(brand):
#     for i in brand:
#         print(i)
    
# brands = ["Apple", "Samsung", "Google", "Microsoft"]
# my_function(brands)


# * lambda............
# **********************
#todo NOTE-[ A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression. ]

# sum = lambda a : a + 20
# print(sum(5))


# * Python Scope..
#*****************
#todo NOTE-[A variable is only available from inside the region it is created. This is called scope.]

#? Local scope
#todo NOTE-[A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.]

# def my_function():
#     x = 40
#     print(x)

# my_function()

#? Global scope
#todo NOTE-[A variable created in the main body of the Python code is a global variable and belongs to the global scope. Global variables are available from within any scope, global and local.]

# x = 40

# def my_function():
#     print(x)

# my_function()
# print(x)

#? Global Keyword
#todo NOTE-[If you need to create a global variable, but are stuck in the local scope, you can use the global keyword. The global keyword makes the variable global.]

# def my_function():
#     global x
#     x = 30
#     print(x)

# my_function()

# def my_function():
#     global x
#     x = 30

# my_function()
# print(x)


#* Class and Object
# ****************

# class Myclass:
#     x = 5

# ob1 = Myclass()
# print(ob1.x)

# class Student:
#     name = "John Dalton"
#     id = 56

# info = Student()
# print(info.name)

class Student:
    name = "John Dalton"
    id = 56
    department = "CE"

info = Student()
print("Name:", info.name)
print("ID:", info.id)
print("Department:", info.department)