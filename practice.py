
# def addi(a, b):
#     result = a+b
#     return result

# print(addi(10, 30))


# car = {
#     "Brand" : "Honda",
#     "Model" : "Civic",
#     "Year" : 2018,
#     "Reg." : 2020
# }


# for i in car.values():
#     print(i)


# for x, y in car.items():
#     print(x, y)


# print(car["Model"])


# del car["Reg."]
# print(car)


# car ["Price"] = "40 lacs"
# print(car)


# car["Model"] = 2019
# print(car)


# cloths = []
# cloths.append("T-Shirt")
# cloths.append("Shirt")
# cloths.append("Sweater")
# cloths.append("Jacket")
# print(cloths)

# cloths = ["T-Shirt", "Shirt", "Sweater", "Jacket"]
# cloths.pop()
# print(cloths)

# cloths.pop(2)
# print(cloths)


# sum = 0
# for i in num:
#     sum += i
# print(sum)


# num = 3, 5, 6, 2, 8, 7, 4
# sum = 0

# for i in num:
#     sum += i
# print(sum)


# my_list = [5, 6, 3, 7, 2, 9]
# sum = 0
# for i in my_list:
#     sum += i
# print(sum)


# def addition(num):
#     sum = 0
#     for i in num:
#         sum += i
#     return sum

# num = [5, 4, 7, 2, 8, 9]
# result = addition(num)
# print("The summation is", result)


# num = 1
# while num <= 10:
#     print(num)
#     num += 1


# num = 2
# while num <= 20:
#     print(num, end = " ")
#     num += 2


# n = int(input("Enter a number: "))
# sum = 0
# i = 1

# while i <= n:
#     sum += 1
#     i += 1
# print(sum)


# n = int(input("Enter a number: "))
# sum = 0
# for i in range(n+1):
#     sum = sum + 1
# print(sum)


# i = 1
# while i <= 20:
#     print(i, end = " ")
#     i += 1


# a = 4, 5, 32, 6, 7, 234
# print(max(a))
# print(min(a))


# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("This number is Even")
# else:
#     print("This number is Odd")


# num = int(input("Enter a number: "))

# if num < 0:
#     print("It is negative number")
# else:
#     print("It is positive number")


# def check_number(num):
#     if num < 0:
#         return "it is negative number"
#     else:
#         return "it is positive number"

# num = int(input("Enter a number: "))
# print(check_number(num))


# bd_division = {}
# bd_division["Dhaka:"] = {"D" : 13, "U" : 93, "UC" : 1833}
# bd_division["Barisal:"] = {"D" : 6, "U" : 39, "UC" : 333}
# bd_division["Khulna:"] = {"D" : 10, "U" : 59, "UC" : 270}

# print(bd_division["Khulna"])

# del bd_division["Dhaka"]
# print(bd_division)

# for i, j in bd_division.items():
#     print(i, j)


# list = []
# length = int(input("Enther the length of list: "))

# for i in range(length):
#     x = int(input("Enter the next number: "))
#     list.append(x)

# print("List:", list)


# list = [3, 5, 6, 1, 7, 9]
# list.insert(4, 10)
# print(list)


# list = [3, 5, 6, 1, 7, 9]
# result = 6 in list
# print(result)


# list = [3, 5, 6, 1, 7, 9]
# result = 10 in list
# print(result)


# def swap_position(list, pos1, pos2):
#
#     list[pos1], list[pos2] = list[pos2], list[pos1]
#     return list
#
# list = [20, 80, 60, 70, 30]
# pos1, pos2 = 1, 4
#
# print(swap_position(list, pos1-1, pos2-1))


# def convert(celsius):
#    celsius = 29
#    fahrenheit = (celsius * 1.8) + 32
#    return fahrenheit


# def reverse(list):
#     return [ele for ele in reversed(list)]

# list = [10, 11, 12, 13, 14, 15]
# print(reverse(list))


# list = [10, 11, 12, 13, 14, 15]
# list.reverse()
# print(list)


# list2 = ['a', 'b', 'c', 'd', 'a', 'a']
# list2.reverse()
# print(list2)


# string = "abgedge"
# string.reverse()
# print(string)


# def reverse(list):
#     list.reverse()
#     return list

# list = [6, 7, 8, 9, 10, 11, 12]
# print(reverse(list))


# string = "mahbuburrahman"
# string.reverse()
# print(string)


# def maximum(e, f):
#     if e >= f:
#         return e
#     else:
#         return f

#total = maximum(100, 200)
# print(total)

#e = 500
#f = 400
#print(maximum(e, f))

#print(maximum(570, 950))

# total = maximum(200, 700)
# print("The maximum number is", total)


# a = 80
# b = 130

# #maximum = max(a, b)
# #print(maximum)

# print(max(a, b))


# def reverse_list(list):
#    list.reverse()
#    return list

#list = [10, 11, 12, 13, 14, 15]
# print(reverse_list(list))


# def odd_number(x):
#    if x % 2 == 0:
#        return x

#x = 10


# i = int(input("Enter the number: "))

# if i % 2 == 0:
#     print("This number is even")
# else:
#     print("This number is odd")


#list = [2, 7, 5, 64, 14]

# for retult in list:
#    if retult % 2 == 0:
#        print(retult)


#name = ["Mahbub", "Mim", "Rahim", "Ayan", "Oyon"]
# name.clear()
# print(name)

#name = ["Mahbub", "Mim", "Rahim", "Ayan", "Oyon"]
# name.pop()
# print(name)


#age = [18, 23, 45, 12, 53, 7]
# age.sort()
# print(age)


# age = [18, 23, 45, 12, 53, 7]
# age.append(100)
# print(age)


# #age = [18, 23, 45, 12, 53, 7]
# #age.insert(4, 70)
# #print(age)


# from array import *

# roll = ("i", [6, 5, 9, 3, 4, 5, 1, 2])
# roll.count(5)
# print(roll)


# age = [18, 23, 45, 12, 53, 7]
# age.append(100)
# print(age)


#car_name = ["audi a6", "toyota harrier", "honda civic", "nissan x-trail", "audi a8l", "bmw i8"]

# print(car_name[-1:])


#st = input("Enter string: ")

#result = st[-1 :: -1]

# if(st == result):
#    print("It's palindrome string")
# else:
#    print("It's no palindrome string")


#string = input("Enter string: ")

#result = string[-1 :: -1]

# if(string == result):
#    print("It's Palindrome string")
# else:
#    print("It's not Palondrome string")


# def isitPalindrome(string):
#    result = string[-1::-1]
#    return result

#string = "madam"
#ans = isitPalindrome(string)


#car_name = ["audi a6", "toyota harrier", "honda civic", "nissan x-trail", "audi a8l", "bmw i8"]

# print(car_name[4:])

#car_name = ["audi a6", "toyota harrier", "honda civic", "nissan x-trail", "audi a8l", "bmw i8"]

# print(car_name[4])


# model = ["a8", "a6", "r8", "a5", "q3", "a4", "a15"]

# print(model[3])

# print(model[2:])

# print(model[::1])


# name = "mahbubur rahman"

# print(name[::-1])


'''
string = input("Enter string: ")

result = string[-1 :: -1]

if(string == result):
    print("It's Palindrome string")
else:
    print("It's not Palondrome string")
'''


'''
string = "mahbuburrahman"

def isitPalindrome(string):
    return string == string[-1::-1]
    
ans = isitPalindrome(string)

if ans:
    print("It's palindrome string")
else:
    print("It's not palindrome string")
'''


# name = "mahbuburrahman"

# print(name[2:5:8])

# print(60%48)

# print(60 // 48)


# for i in range(50, 80):
#    print(i, end = " ")


'''
guess_number = int(input("Enter number between 1 to 10: "))
random_number = random.randint(1, 10)

if guess_number == random_number:
    print("You have won")
else:
    print("You have lost")
    # print("Random number was:", random_number)   # alternative

'''

# print(random.randint(2, 8))


# x = random.randint(8, 30)
# print(x)


# import random

# for i in range(1, 6):
#     guess_number = int(input("Enter the number between 1 to 15: "))
#     random_number = random.randint(1, 15)

#     if guess_number == random_number:
#         print("Hurrah! You have won")
#     else:
#         print("Oh! You have lost")

#         print("The random number is:", random_number) # alternative


# my_number = [8, 4, 9, 2, 1, 7, 6]
# for i in my_number:
#     print(i, end=" ")


# def fibo(x):
#     a = 0
#     b = 1
#     print(a)
#     print(b)

#     for i in range(2, x):
#         c = a + b
#         a = b
#         b = c
#         print(c)
# fibo(20)


'''
n = int(input("Enter number: "))

a = 0
b = 1
c = 0

while c <= n:
    print(c)
    a = b
    b = c
    c = a + b
'''


'''
age_list = [45, 67, 34, 89, 23, 83, 36]

age_list.remove(max(age_list))
second_big = max(age_list)
print(second_big)
'''


'''
my_list = [33, 56, 78, 34, 98, 39]
my_list.sort()
print(my_list[-4])
'''


# amount = int(input("Enter the amount: "))
# time = int(input("Enter the time: "))
# rate = int(input("Enter the rate: "))

# simple_interest = (amount * time * rate) / 100
# print(simple_interest)


# def simple_interest(a, t, r):
#    result = (a * t * r) / 100
#    return result
#
# a = int(input("Enter the amount: "))
# t = float(input("Enter the time: "))
# r = float(input("Enter the rate: "))
# print(simple_interest(a, t, r))


# def simple_interest(a, t, r):
#    print("The principle amount =", a)
#    print("The time preiod =", t)
#    print("The rate of interest =", r)

#    si = (a * t * r) / 100

#    print("The simple interest =", si)
#    return si
# simple_interest(10000, 5, 5)


# p = float(input("Enter the principle amount: "))
# t = float(input("Enter the time: "))
# r = float(input("Enter the rate: "))

# a = p * (1 + r / 100) * t
# print(a)


# print(5 ** 3)


# print(pow(5, 3))


# def compound_interest(principle, rate, time):
#     amount = principle * (1+rate/100) ** time
#     CI = amount - principle
#     return CI

# principle = int(input("Enter principle amount: "))
# rate = float(input("Enter the interest rate: "))
# time = float(input("Enter the time: "))

# total = compound_interest(principle, rate, time)
# print("Compound Interest is", total)


# def compound_interest(principle, rate, time):
#     amount = principle * (1 + rate / 100) ** time
#     ci = amount - principle
#     return ci
#
# principle = int(input("Enter the amount: "))
# rate = int(input("Enter the rate: "))
# time = int(input("Enter the time: "))
#
#
#
#
#
# def compound_interest(principle, rate, time):
#     amount = principle * (1 + rate/100) ** time
#     ci = amount - principle
#     return ci
#
# principle = int(input("Enter the principle amount: "))
# rate = float(input("Enter the rate: "))
# time = float(input("Enter the time: "))
#
# total = compound_interest(principle, rate, time)
# print("Compound Interest =", total)
#
#
#
#
# def compound_interest(principle, rate, time):
#     print("Principle Amount =", principle)
#     print("Rate of interest =", rate)
#     print("Time =", time)
#
#     amount = principle * (1 + rate/100) ** time
#     ci = amount - principle
#     print("Compound Interest is", ci)
#
# compound_interest(10000, 5, 4)


# def check_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             print("It's not prime number")
#             break
#     else:
#         print("It is prime number")

# num = int(input("Enter your number: "))
# check_prime(num)


#age = 1
# while age <= 10:
#    print(age)
#    age = age + 1


# for i in range(1, 50, 3):
#    print(i, end = " ")


#n = 1
# while n <= 50:
#    print(n, end = " ")
#    n = n + 3


# def all_prime(num):


# start = int(input("Start: "))
# end = int(input("End: "))

# for i in range(start, end + 1):
#     if i > 1:

#         for x in range(2, i):
#             if i % x == 0:
#                 break
#         else:
#             print(i)


# def all_prime(start, end):
#     for i in range(start, end + 1):
#         if i > 0:

#             for x in range(2, i):
#                 if i % x == 0:
#                     break
#             else:
#                 print(i)

# start = int(input("Start: "))
# end = int(input("End: "))
# all_prime(start, end)


# m = [1, 2, 3, 4, 5, 6, 7, 8]
# m.reverse()
# print(m)


'''
def re(my_list):
    my_list.reverse()
    return my_list

my_list = [20, 30, 40, 50, 60, 70, 80]
print(re(my_list))
'''

# my = "mahbubur rahman"
# print(my[4:-2])
#
#
#
# my = "mahbuburrahman"
# print(my[4::-2])
#
#
# str = "Hello World"
# print(str[6:10])
#
#
# tr = "Hello World"
# print(str[3:-2])
#
#
#
# age = [1,2,3,4,5,6,7,8,9]
#
#
#
# nums = [1, 3, 2, 41, 9]
# x = len(nums) - 2
# y = nums[x]
# print(y)
#
#
#
#
# def add_num(first, second):
#     return first + second
#
# x = add_num(2, 3)
# y = add_num(4, 5)
# z = add_num(x, y)
# print(z)
#
#
#
# marks = 990
# if marks >= 80 and marks <= 100:
#     print("A+")
# elif marks >= 70 and marks <= 79:
#     print("A")
#
#
#
# def addition(x, y):
#     return x + y
#
# print(addition(10, 20))
#
#
# a = (lambda x, y: x + y)(2, 3)
# print(a)
#
#
#
# english = int(input("Enter the marks of English: "))
# bangla = int(input("Enter the marks of Bangla: "))
# history = int(input("Enter the marks of History: "))
# chemistry = int(input("Enter the marks of Chemictry: "))
# physics = int(input("Enter the marks of Physics: "))
# math = int(input("Enter the marks of Math: "))

# average = (english + bangla + history + chemistry + physics + math) / 6

# if average >= 80 and average <= 100:
#     print("A+")
# elif average >= 70 and average <= 79:
#     print("A")
# elif average >= 60 and average <= 69:
#     print("A-")
# elif average >= 50 and average <= 59:
#     print("B")
# elif average >= 40 and average <= 49:
#     print("C")
# elif average >= 33 and average <= 39:
#     print("D")
# else:
#     print("Oh! You are fail.")

#
#
# for i in range(5):
#     if i == 4:
#         print(i)
#

# def big(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
#         pass
#
# print(big(100, 200))
# print(a+b)
#
#
# num = 5
# if num > 10:
#     pass
#
#
#
# list = []
# length = int(input("Enter the length of list: "))
#
# for i in range(length):
#     x = int(input("Enter the number: "))
#     list.append(x)
#
# print("list:", list)
#

#
# def person(name, age):
#     print(name)
#     print(age)
#
# name = "Mahbubur Rahman"
# age = 18
# person(name, age)


# def student(*details):
#     print(details)
#
# student("Mahbub", 18, "CSE", 2022, "BUET")
#
#
# def student(name, age, dp, year, ins):
#     print(name, age, dp, year, ins)
#
# name = "Mahbub"
# age = 18
# dp = "CSE"
# year = 2022
# ins = "BUET"


# student(name, age, dp, year, ins)
#
#
#
# def mahbub(*your_skill):
#     print(your_skill)
#
# mahbub("Java", "Python", "C++", "C", "Swift")


# def add(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print(sum)
#
# add(10, 20, 30, 70)
# add(100, 200)
#
#
#
# a = 10
# def some():
#
#     a = 15
#     b = 8
#     print(a, b)
#
# some()
# print(a)


# year = int(input("Enter the year: "))
#
# if year % 400 == 0:
#     print(year,"is leap year")
# else:
#     print(year,"is not leap year")


# year = int(input("Enter the year: "))

# if year % 400 == 0:
#     print("Yes")
# elif year % 100 == 0:
#     print("No")
# elif year % 4 == 0:
#     print("Yes")
# else:
#     print("No")


# year = int(input("Enter the year: "))
#
# if year % 100 != 0 and year % 4 == 0:
#     print("yes, it is leap year")
# elif year % 100 == 0 and year % 400 == 0:
#     print("Yes, it is leap year")
# else:
#     print("It is not leap year")


# year = int(input("Enter the year: "))
#
# if year % 100 != 0 and year % 4 == 0:
#     print("It is leap year")
# elif year % 100 == 0 and year % 400 == 0:
#     print("It is leap year")
# else:
#     print("It is not leap year")


# year = int(input("Enter the year: "))
#
# if year % 400 == 0:
#     print("It is leap year")
# elif year % 100 == 0:
#     print("It is not leap year")
# elif year % 4 == 0:
#     print("It is leap year")
# else:
#     print("It is not leap year")


# year = int(input("Enter the year: "))
#
# if year % 100 != 0 and year % 4 == 0:
#     print("it is leap year")
# elif year % 100 == 0 and year % 400 == 0:
#     print("it is leap year")
# else:
#     print("it is not leap year")


#
# from turtle import *
#
# hex = Turtle()
# hex.shape("classic")
# hex.color("violet")
# hex.speed(2)
#
# hex.forward(60)
# hex.right(70)
# hex.forward(60)


# s = 0
# while s <= 10:
#     print(s)
#     s += 2


# num = [13, 56, 43, 67, 45]
# sum = 0
#
# for i in num:
#     sum = sum + i
# print(sum)


# sum = 0
# for i in range(50):
#     sum += i
# print(sum)


# import turtle
#
# turtle.color("red")
# turtle.speed(6)
#
# c = 0
# while c < 36:
#     for i in range(4):
#         turtle.forward(100)
#         turtle.right(90)
#     turtle.right(10)
#     c += 1
#
# turtle.exitonclick()


# num = int(input("Enter the number: "))
#
# i = 0
# while i <= 10:
#     print(num, "x", i, "=", num*i)
#     i += 1


# sum = 0
# i = 2
# while i <= 100:
#     sum += 1
#     i += 1
# print(sum)
#


# while True:
#     num = int(input("Enter a number: "))
#     if num < 0:
#         print("Only allow positive number. Please try again.")
#         continue
#     if num == 0:
#         break
#     print("squre is", num*num)


# mahbub = 18
# hira = 17
# print(mahbub, hira)
#
# mahbub, hira = hira, mahbub
#
# print(mahbub, hira)


# m = 20
# h = 40
# print(m, h)
#
# temp = m
# m = h
# h = temp
# print(m, h)


#
# m = 20
# n = 40
# print(m, n)
#
# temp = m
# m = n
# n = temp
# print(m, n)

# m = 100
# n = 200
# print(m, n)
#
# temp = m
# m = n
# n = temp
# print(m, n)


# year = int(input("Enter a year: "))

# if year % 100 != 0 and year % 4 == 0:
#     print("It is leap year")
# elif year % 100 == 0 and year % 400:
#     print("It is leap year")
# else:
#     print("It is not leap year")


# year = int(input("Enter the year: "))

# if year % 400 == 0:
#     print("It is leap year")
# elif year % 100 == 0:
#     print("It is not leap year")
# elif year % 4 == 0:
#     print("It is leap year")
# else:
#     print("It is not leap year")


# year = int(input("Enter the year: "))

# if year % 400 == 0:
#     print("It is leap year")
# elif year % 100 == 0:
#     print("It is not leap year")
# elif year % 4 == 0:
#     print("It is leap year")
# else:
#     print("It is not leap year")


# year = int(input("Enter the year: "))

# if year % 400 == 0:
#     print("It is leap year")
# elif year % 100 == 0:
#     print("It is not leap year")
# elif year % 4 == 0:
#     print("It is leap year")
# else:
#     print("It is not leap year")

# celsius = float(input("Enter the Celsius temperature: "))

# fahrenheit = (celsius * 1.8) + 32
# print("%0.2f Degree Celsius = %0.2f Degree Fahrenheit"%(celsius,fahrenheit))


# num = int(input("Enter a number: "))

# for i in range(2, num):
#     if num % i == 0:
#         print("It is not prime number")
#         break
# else:
#     print("It is prime number")


# def check_prime(num):
#     for x in range(2, num):
#         if num % x == 0:
#             print()

# num = int(input("Enter a number: "))


# roll = {
#     "Jack" : 56,
#     "Mark" : 98,
#     "Gats" : 53,
#     "Cook" : 48,
#     "Jhon" : 18
# }
# del roll["Gats"]
# print(roll)


# roll = {
#     "Mahbub:" : 163895,
#     "Sakib:" : 163885,
#     "Sumaiya:" : 163894,
#     "Khokon:" : 163900,
#     "Siddik" : 163877
# }
# for i, j in roll.items():
#     print(i, j)


# my_list = [10, 50, 60, 90, 30, 20, 70]
# x = max(my_list)
# print(x)


# my_list = [10, 50, 60, 90, 30, 20, 70]
# lar = my_list[0]

# for i in my_list:
#     if i > lar:
#         lar = i
# print("largest number is", lar)


# def check_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             print("It is not a prime number")
#             break
#     else:
#         print("It's prime number")

# num = int(input("Enter a number: "))
# check_prime(num)


# num = 1, 5, 7, 8, 3, 9
# sum = 0
# for i in num:
#     sum += i
# print(sum)


# num = int(input("Enter number when you start from: "))
# sum = 0

# for i in range(num+1):
#     sum = sum + 1
# print(sum)


# num = int(input("Enter a number: "))
# sum = 0

# for i in range(num+1):
#     sum = sum + i**2
# print(sum)


# def count_vowels(sentense):
#     count = 0
#     vowels = ["a", "e", "i", "o", "u"]
#     for i in sentense:
#         if i in vowels:
#             count = count + 1
#     return count

# sentense = input("Enter your sentense: ")
# total = count_vowels(sentense)
# print(total)


# sentense = input("Enter your sentence: ")
# count = 0
# vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
# for x in sentense:
#     if x in vowels:
#         count = count + 1
# print("Total vowels in this sentense:", count)


# def count_word(string):
#     count = 0
#     for i in string:
#         if i == " ":
#             count = count + 1
#     count = count + 1
#     return count

# string = "I want to be a Software Engineer at Google"
# print(count_word(string))


# def count_vowels(string):
#     count = 0
#     vowels = "a", "e", "i", "o", "u"
#     for i in string:
#         if i in vowels:
#             count = count + 1
#     return count

# string = "I want to be a Software Engineer at Google"
# total = count_vowels(string)
# print("Total vowels in this sentense:", total)


# import math

# a = 524
# b = 5
# result = math.floor(a / b)
# print("The result is", result)


# list = [50, -56, 60, 90, 30, 20, 70]
# largest = list[0]

# for x in list:
#     if x > largest:
#         largest = x
# print("Largest number in this list =", largest)


# def largest_element(list):
#     largest = list[0]

#     for x in list:
#         if x > largest:
#             largest = x
#     return largest

# list = [5, 6, 2, 10, 60, -3, 40]
# result = largest_element(list)
# print("Largest number in this list:", result)


# def largest_element(list):
#     largest = list[0]
#     for i in list:
#         if i > largest:
#             largest = i
#     return largest

# list = [4, 5, 3, 7, 9, 2, 1, 2]
# print(largest_element(list))


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# result = pow(num1, num2)
# print(result)

# print(pow(5, 2))

# import random

# x = random.randint(1, 10)
# print(x)


# list = [34, 56, 29, 34, 29, 70, 56, 34, 29]

# empty = []
# for i in list:
#     if i not in empty:
#         empty.append(i)
# print(empty)


# list = [45, 34, 7, 45, 7, 8, 34, 56]
# empty = []
# for i in list:
#     if i not in empty:
#         empty.append(i)
# print(empty)


# def remove_dublicates(list):
#     print("Before remove dublicates:", list)
#     unique = []
#     for i in list:
#         if i not in unique:
#             unique.append(i)
#     return unique

# list = [4, 5, 2, 4, 5, 8, 9, 6, 6, 4, 2]
# result = remove_dublicates(list)
# print("After remove dublicates:", result)


# def remove_duplicates(list):
#     unique = []
#     for i in list:
#         if i not in unique:
#             unique.append(i)
#     return unique

# list = [4, 5, 2, 4, 5, 8, 9, 6, 6, 4, 2]
# result = remove_duplicates(list)
# print(result)


# string = "mahbuburrahman"
# print(string[-1::-1])


# my_list = [4, 6, 3, 7, 1, 8, 5, 3]
# result = sum(my_list)
# print(result)


# my_list = [4, 6, 3, 7, 1, 8, 5, 3]
# sum = 0

# for x in my_list:
#     sum = sum + x
# print(sum)


# def sum_elements(list):
#     sum = 0
#     for i in list:
#         sum = sum + i
#     return sum

# list = [3, 5, 2, 9, 1, 8]
# print(sum_elements(list)


# a = 40
# b = 30
# print(a, b)

# temp = a
# a = b
# b = temp
# print(a, b)


# def swap_numbers(a, b):
#     print(a, b)
#     a, b = b, a
#     print(a, b)

# a = 400
# b = 300
# swap_numbers(a, b)


# num = int(input("How many numbers do you enter: "))
# total = 0

# for i in range(num):
#     next_number = float(input("Enter the next number: "))
#     total = total + next_number

# average = total / num
# print("Average number is: %0.2f" % average)


# start = int(input("Start: "))
# end = int(input("End: "))

# for i in range(start, end+1):
#     if i > 1:
#         for x in range(2, i):
#             if i % x == 0:
#                 break
#         else:
#             print(i)


# import random

# def guessing_num(guess_num):
#     random_number = random.randint(1, 10)
#     if random_number == guess_num:
#         print("You have won")
#     else:
#         print("You are lost")


# guess_num = int(input("Enter number between 1 to 10: "))
# guessing_num(guess_num)


# my_list = [3, 5, 6, 2, 10]
# # print(my_list[3])
# my_list[3] = 11
# print(my_list)


# num = int(input("How many number do you enter: "))
# total = 0
# for i in range(num):
#     next_num = float(input("Enter the next number: "))
#     total = total + next_num

# average = total / num
# print("Average number: %0.2f" % average)


# def avg_num(num):
#     total = 0
#     for i in range(num):
#         nxt_num = float(input("Enter the next value: "))
#         total = total + nxt_num
#     average = total / num
#     return average

# num = int(input("how many number do you enter: "))
# result = avg_num(num)
# print("Average this number: %0.2f" % result)


# def grades(*datials):
#     print(datials)

#     total = (english + bangla + history + chemistry + physics + math) / 6

#     if total >= 80 and total <= 100:
#         print("He got A+")
#     elif total >= 70 and total <= 79:
#         print("He got A")
#     elif total >= 60 and total <= 69:
#         print("He got A-")
#     elif total >= 50 and total <= 59:
#         print("He got B")
#     elif total >= 40 and total <= 49:
#         print("He got C")
#     elif total >= 33 and total <= 39:
#         print("He got D")
#     else:
#         print("He is fail")
#     return total

# english = int(input("Enter the marks of English: "))
# bangla = int(input("Enter the marks of Bangla: "))
# history = int(input("Enter the marks of History: "))
# chemistry = int(input("Enter the marks of Chemictry: "))
# physics = int(input("Enter the marks of Physics: "))
# math = int(input("Enter the marks of Math: "))

# grades(english, bangla, history, chemistry, physics, math)


# string = "madam"
# result = string[-1::-1]

# if string == result:
#     print("It is palindrome string")
# else:
#     print("It is not palindrome string")


# num = int(input("Enter a number: "))
# for i in range(2, num):
#     if num % 2 == 0:
#         print("It is not prime number")
#         break
# else:
#     print("It is prime number")


# def check_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             print("It is not prime number")
#             break
#     else:
#         print("It is prime number")

# num = int(input("Enter a number: "))
# check_prime(num)


# def check_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# num = int(input("Enter a number: "))
# result = check_prime(num)

# if result:
#     print("It is a prime number")
# else:
#     print("It is not a prime number")


# def com_int(p, r, t):
#     amount = p*(1+r/100)**t
#     ci = amount - p
#     return ci

# p = int(input("Enter principle amount: "))
# r = float(input("Enter the rate of interest: "))
# t = float(input("Enter the time of interest: "))

# print(com_int(p, r, t))


# def count_vowels(sentence):
#     vowels = ["a", "e", "i", "o", "u"]
#     count = 0
#     for i in sentence:
#         if i in vowels:
#             count += 1
#     return count


# sentence = input("Enter the sentence: ")
# result = count_vowels(sentence)
# print("Vowels in this sentence", result)


# start = int(input("start: "))
# end = int(input("End: "))

# for i in range(start, end+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)


# def divisible(num):
#     empty = []
#     for i in range(num):
#         if i % 3 == 0 and i % 5 == 0:
#             empty.append(i)
#     return empty

# num = int(input("Enter you number: "))
# result = divisible(num)
# print(result, "this number are divisibel by 3 and 5")


# def divisible(num):
#     empty = []
#     for i in range(num):
#         if i % 3 == 0 and i % 5 == 0:
#             empty.append(i)
#     return empty


# num = int(input("enter the last number: "))
# print(divisible(num))


# def divisible(num):
#     empty = []
#     for i in range(num):
#         if i % 3 == 0 and i % 5 == 0:
#             empty.append(i)
#     return empty

# num = int(input("How many numbers will end before that: "))
# result = divisible(num)
# print("3 and 5 divisible number are:", result)


# def count_vowels(sentence):
#     vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
#     count = 0
#     for x in sentence:
#         if x in vowels:
#             count = count + 1
#     return count

# sentence = input("Enter your sentence: ")
# result = count_vowels(sentence)
# print("The number of vowels in this sentence =", result)


# def gra_force(m1, m2, r):
#     G = 6.673* 10 ** -11
#     force = G*m1*m2/r**2
#     return force

# m1 = int(input("Enter the mess1: "))
# m2 = int(input("Enter the mess2: "))
# r = float(input("distance between center of the masses: "))
# print(gra_force(m1, m2, r))


# def lar_ele(my_list):
#     largest = my_list[0]
#     for i in my_list:
#         if i > largest:
#             largest = i
#     return largest

# my_list = [10, 50, 90, 150, 80, 20]
# print(lar_ele(my_list))


# def large(list):
#     largest = list[0]
#     for x in list:
#         if x > largest:
#             largest = x
#     return largest

# list = [5, 6, 4, 9, 2, 1]
# result = large(list)
# print("Largest elements in this list =", result)


# list = [18, 20, 25, 10, 19]
# largest = list[0]

# for i in list:
#     if i > largest:
#         largest = i
# print(largest)


# import random

# for i in range(1, 6):
#     number = int(input("Enter number between 10 to 20: "))
#     guess_number = random.randint(10, 20)

#     if number == guess_number:
#         print("you are win")
#     else:
#         print("You are loss")
#     print("Random number was:", guess_number)


# import random

# print("To stop anytime, enter: q")

# score = 0
# while True:
#     number = random.randint(0, 10)
#     guess = input("Guess a number between 0 to 10: ")
#     if guess == "q":
#         print("GAME OVER")
#         break
#     guess_number = int(guess)

#     if guess_number is number:
#         print("Congratulations, you gessed the number currectly")
#         score = score + 1
#         print("Your new score:", score)
#     else:
#         print("Your guess did not match")
#         print("Actually, the number was", number)


# def remove_duplicates(my_list):
#     print("Before list:", my_list)

#     empty = []
#     for i in my_list:
#         if i not in empty:
#             empty.append(i)
#     return empty

# my_list = ["e", "y", "a", "c", "e", "y"]
# result = remove_duplicates(my_list)
# print("After removing duplicates:", result)


# def reverse_number(num):

#     reverse = 0
#     while num > 0:
#         last_digit = num % 10
#         reverse = reverse * 10 + last_digit
#         num = num // 10
#     return reverse

# num = int(input("Enter a big number: "))

# result = reverse_number(num)
# print("After reverse:", result)


# def reverse_number(num):

#     reverse = 0
#     for i in range(num):
#         if num > 0:
#             last_digit = num % 10
#             reverse = reverse * 10 + last_digit
#             num = num // 10
#     return reverse

# num = int(input("Enter a big number: "))

# result = reverse_number(num)
# print("After reverse:", result)


# my_list = [4, 5, 2, 8, 9]
# sum = 0
# for i in my_list:
#     sum = sum + i
# print(sum)


# def sum_of_digits(number):

#     sum = 0
#     while number > 0:
#         last_digit = number % 10
#         sum = sum + last_digit
#         number = number // 10
#     return sum

# number = int(input("Enter a big number: "))
# print(sum_of_digits(number))


# student = {"Name" : "Mahbub", "Age" : 18, "Department": "CSE"}
# print(student["Department"])


# car = {
#     "Brand:" : "Audi",
#     "Model:" : "A8L",
#     "Year:" : 2020,
#     "CC:" : 2500
# }
# for x, y in car.items():
#     print(x, y)


# def sum_digit(num):

#     sum = 0
#     while num > 0:
#         last_digit = num % 10
#         sum = sum + last_digit
#         num = num // 10
#     return sum

# num = int(input("Enter a big number: "))
# result = sum_digit(num)
# print("Sum of digits:", result)


# def sum_digits(num):

#     sum = 0
#     while num > 0:
#         last_digit = num % 10
#         sum = sum + last_digit
#         num = num // 10
#     return sum

# num = int(input("Enter a big number: "))
# print(sum_digits(num))


# def word_count(sentence):

#     sum = 0
#     for i in sentence:
#         if i == " ":
#             sum = sum + 1
#     sum = sum + 1
#     return sum

# sentence = "I am a student"
# print(word_count(sentence))


# def average_number(num):

#     total = 0
#     for x in range(num):
#         next_number = float(input("Enter the next number: "))
#         total = total + next_number
#     average = total / num
#     return average

# num = int(input("How many number do you enter: "))
# print(average_number(num))


# def average_number(number):

#     total = 0
#     while number > 0:
#         next_number = float(input("Enter the next number: "))
#         total = total + next_number
#     average = total / number
#     return average

# number = int(input("How many number do you enter: "))
# result = average_number(number)
# print("Average number =", result)


# celsius = float(input("Enter the celsius temperature: "))
# fahrenheit = (celsius * 9) / 5+32

# print("%0.2f Degree Celsius = %0.2f Degree Fahrenheit" % (celsius, fahrenheit))


# def check_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             print("It is not a prime number")
#             break
#     else:
#         print("It is a prime number")

# num = int(input("Enter a number: "))
# check_prime(num)


# def check_prime(num):
#     for x in range(2, num):
#         if num % x == 0:
#             print("It is not prime number")
#             break
#     else:
#         print("It is a prime number")

# num = int(input("Enter a number: "))
# check_prime(num)


# def check_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return True
#     return False

# num = int(input("Enter a number: "))
# check_prime(num)

# if check_prime:
#     print("It is a prime number")
# else:
#     print("It is not prime number")


# class Laptop:

#     name = " "
#     brand = " "
#     color = " "

# Laptop.name = "Galaxy Book Pro"
# Laptop.brand = "Samsung"
# Laptop.color = "Black"

# print("Name of Laptop:", Laptop.name)
# print("Name of brand:", Laptop.brand)
# print("Name of color:", Laptop.color)


# class Bus:
#     Name = "Hanif"
#     Color = "Sky Blue"

# my_bus = Bus()
# print(my_bus.Name)


# class Bus:

#     Name = ""
#     Color = ""

# my_bus = Bus()
# my_bus.Name = "Shohag"
# my_bus.Color = "White"
# print(my_bus.Name)
# print(my_bus.Color)


# class Friends_laptop:

#     Model_Name = " "
#     Brand = " "
#     RAM = " "

# Mahbub_laptop = Friends_laptop()
# print("Mahbub's Laptop--")
# Mahbub_laptop.Model_Name = "Galaxy Book Pro"
# Mahbub_laptop.Brand = "Samsung"
# Mahbub_laptop.RAM = "8GB"
# print("Name:", Mahbub_laptop.Model_Name)
# print("Brand:", Mahbub_laptop.Brand)
# print("RAM:", Mahbub_laptop.RAM)

# Habib_laptop = Friends_laptop()
# print("Habib's Laptop--")
# Habib_laptop.Model_Name = "Vivobook S15"
# Habib_laptop.Brand = "Asus"
# Habib_laptop.RAM = "8GB"
# print("Name:", Habib_laptop.Model_Name)
# print("Brand:", Habib_laptop.Brand)
# print("RAM:", Habib_laptop.RAM)

# Nila_laptop = Friends_laptop()
# print("Nila's Laptop--")
# Nila_laptop.Model_Name = "Pavilion 601"
# Nila_laptop.Brand = "HP"
# Nila_laptop.RAM = "16GB"
# print("Name:", Nila_laptop.Model_Name)
# print("Brand:", Nila_laptop.Brand)
# print("RAM:", Nila_laptop.RAM)


# class Friends_laptop:

#     Model_Name = " "
#     Brand = " "
#     RAM = " "

#     def info(self):
#         print("Name:", self.Model_Name)
#         print("Brand:", self.Brand)
#         print("RAM:", self.RAM)

# Mahbub_laptop = Friends_laptop()
# Mahbub_laptop.Model_Name = "Galaxy Book Pro"
# Mahbub_laptop.Brand = "Samsung"
# Mahbub_laptop.RAM = "8GB"
# Mahbub_laptop.info()

# Habib_laptop = Friends_laptop()
# Habib_laptop.Model_Name = "Vivobook S15"
# Habib_laptop.Brand = "Asus"
# Habib_laptop.RAM = "8GB"
# Habib_laptop.info()

# Nila_laptop = Friends_laptop()
# Nila_laptop.Model_Name = "Pavilion 601"
# Nila_laptop.Brand = "HP"
# Nila_laptop.RAM = "16GB"
# Nila_laptop.info()


# class Phone:
#     Name = " "
#     Brand = " "
#     RAM = " "
#     Made_in = " "

#     def set_info(self, Name, Brand, RAM, Made_in):
#         self.Name = Name
#         self.Brand = Brand
#         self.RAM = RAM
#         self.Made_in = Made_in

#     def phone_info(self):
#         print(f"Phone Name:", self.Name, "Brand:", self.Brand, "RAM:", self.RAM, "Made in", self.Made_in)

# A50 = Phone()
# A50.set_info("Galaxy A50", "Samsung", "4GB", "China")
# A50.phone_info()

# A70 = Phone()
# A70.set_info("Galaxy A70", "Samsung", "6GB", "India")
# A70.phone_info()

# A30 = Phone()
# A30.set_info("Galaxy A30", "Samsung", "3GB", "Vietnam")
# A30.phone_info()


# class Calculator:
#     Brand = "CAsio"

#     def multiply(self, m, n):
#         total = m * n
#         return total

# my_cle = Calculator()
# result = my_cle.multiply(2, 10)
# print("Result =", result)


# class Student:
#     info = "All Student"

#     def get_info(self):
#         return self.info

# my_name = Student()
# result = my_name.get_info()
# print(result)


# class Friends_laptop:

#     Model_Name = " "
#     Brand = " "
#     RAM = " "

#     def __init__(self, Model_name, Brand, RAM):
#         self.Model_Name = Model_name
#         self.Brand = Brand
#         self.RAM = RAM

#     def info(self):
#         print("Name:", self.Model_Name)
#         print("Brand:", self.Brand)
#         print("RAM:", self.RAM)

# Mahbub_laptop = Friends_laptop("Galaxy Book Pro", "Samsung", "8GB")
# Mahbub_laptop.info()


# class Student:

#     name = " "
#     department = ""
#     roll = " "

#     def __init__(self, name, department, roll):
#        self.name = name
#        self.department = department
#        self.roll = roll

#     def info(self):
#         print("Name:", self.name)
#         print("Department:", self.department)
#         print("Roll:", self.roll)

# mahbub = Student("Mahbubur Rahman", "CSE", 163895)
# mahbub.info()


# class Phone:

#     def __init__(self, Brand, Model):
#         self.Brand = Brand
#         self.Model = Model

# my_phone = Phone("Samsung", "Galaxy S21")
# print(my_phone.Brand)
# print(my_phone.Model)


# class Student:

#     def __init__(self, Name, Roll, Department):
#         self.Name = Name
#         self.Roll = Roll
#         self.Department = Department

# MR = Student("M.R.", 95, "CSE")
# print(MR.Name)
# print(MR.Roll)
# print(MR.Department)


# class Car:

#     name = " "
#     color = " "

# my_car = Car()
# my_car.name = "Allion"
# print(my_car.name)


# class Car:

#     def __init__(self, name, color) -> None:
#         self.name = name
#         self.color = color

# my_car = Car("Premio", "White")
# print(my_car.name)
# print(my_car.color)


# class Car:

#     def __init__(self, n, c, y):
#         self.name = n
#         self.color = c
#         self.year = y

# my_car = Car("Allion", "White Pearl", 2012)
# print("Model_name:", my_car.name)
# print("Color:", my_car.color)
# print("Year:", my_car.year)


# class Student:

#     def __init__(self, n, r) -> None:
#         self.name = n
#         self.roll = r

# mahbub = Student("Mahbubur Rahman", 95)
# print(f"Name:", mahbub.name, "Roll:", mahbub.roll)

# siddik = Student("Siddikur Rahman", 76)
# print(f"Name:", siddik.name, "Roll:", siddik.roll)

# marzan = Student("Marzan Rahman", 72)
# print(f"Name:", marzan.name, "Roll:", marzan.roll)


# class Car:

#     def __init__(self, n, c, y) -> None:
#         self.name = n
#         self.color = c
#         self.year = y

#     def info(self):
#         print("Name:", self.name)
#         print("Color:", self.color)
#         print("Year:", self.year)

# my_car = Car("Allion", "Sky Blue", 2008)
# my_car.info()

# mahfuj_car = Car("Premio", "White Pearl", 2010)
# mahfuj_car.info()

# rahi_car = Car("Civic", "Red", 2022)
# rahi_car.info()

# mahi_car = Car("CRV", "Gray", 2010)
# mahi_car.info()


# class Car:

#     def __init__(self, n, c) -> None:
#         self.name = n
#         self.color = c

# xcar = Car("civic", "red")
# xcar.year = 2022
# print(xcar.name, xcar.color, xcar.year)


# class Student:

#     def __init__(self, r, g):
#         self.roll = r
#         self.gpa = g

#     def info(self):
#         print("roll:", self.roll)
#         print("gpa:", self.gpa)

# mahbub = Student(163895, 3.15)
# mahbub.info()


# class Triangle:

#     def calculate_area(self, base, height):
#         return base * height

# total = Triangle()
# x = total.calculate_area(10, 20)
# print(x)


# class Triangle:

#     def __init__(self, b, h) -> None:
#         self.base = b
#         self.height = h

#     def calculate_area(self):
#         print("Area =", 0.5 * self.base * self.height)

# total1 = Triangle(10, 20)
# total1.calculate_area()

# total2 = Triangle(20, 30)
# total2.calculate_area()


# class Triangle:

#     def __init__(self, b, h) -> None:
#         self.base = b
#         self.height = h

#     def calculate_area(self):
#         return 0.5 * self.base * self.height

# total1 = Triangle(10, 20)
# print("Area =", total1.calculate_area())

# total2 = Triangle(20, 30)
# print("Area =", total2.calculate_area())


# import math

# class Circle:

#     def __init__(self, r) -> None:
#         self.radius = r

#     def calculate_area(self):
#         return math.pi * self.radius * self.radius

# total_area = Circle(4)
# print("Area = %0.2f" % total_area.calculate_area())


# class Addition:

#     def __init__(self, a, b) -> None:
#         self.a = a
#         self.b = b

#     def calculate(self):
#         return self.a + self.b

# total1 = Addition(10, 20)
# print(total1.calculate())

# # caile amra aro add korte pari

# total2 = Addition(100, 500)
# print(total2.calculate())
# total3 = Addition(100, 200)
# print(total3.calculate())


# import math

# class Sphere:

#     def __init__(self, r) -> None:
#         self.radius = r

#     def calculate_area(self):
#         return 4 * math.pi * self.radius * self.radius

# total = Sphere(5)
# print("Sphere area = %0.2f" % total.calculate_area())


# class Shopping:
#     cart = [ ]

#     def __init__(self, item1, item2):
#         self.item1 = item1
#         self.item2 = item2

#     def add_to_cart(self):
#         self.cart.append(self.item1)
#         self.cart.append(self.item2)

# cus1 = Shopping("T-Shirt")
# print(cus1.add_to_cart())


# class Shopping:

#     def __init__(self):
#         self.cart = [ ]

#     def add_to_cart(self, item):
#         self.cart.append(item)

# cus1 = Shopping()
# cus1.add_to_cart("T-Shirt")
# print(cus1.cart)

# cus2 = Shopping()
# cus2.add_to_cart("Shoes")
# print(cus2.cart)


# class Shopping:

#     def __init__(self) -> None:
#         self.cart = []

#     def add_to_cart(self, item):
#         self.cart.append(item)

# customer1 = Shopping()
# customer1.add_to_cart("Shirt")
# print(customer1.cart)

# customer2 = Shopping()
# customer2.add_to_cart("Sandle")
# print(customer2.cart)


# class Marketing:

#     def __init__(self) -> None:
#         self.cart = []

#     def add_to_cart(self, item):
#         self.cart.append(item)

#         print("")


# def word_count(sentence):

#     count = 0
#     for c in sentence:
#         if c == " ":
#             count = count + 1
#     count = count + 1
#     return count

# sentence = input("Enter your sentence: ")
# total = word_count(sentence)
# print("The number of words in this sentence:", total)


# def word_count(sentence):

#     count = 0
#     for i in sentence:
#         if i == " ":
#             count = count + 1
#     count = count + 1
#     return count

# sentence = "i am student in cse at mpbi"
# print(word_count(sentence))


# def sum_digit(digit):

#     total = 0
#     while digit > 0 :
#         last_digit = digit % 10
#         total = total + last_digit
#         digit = digit // 10
#     return total

# digit = int(input("Enter a big number: "))
# print(sum_digit(digit))


# def sum_digit(digit):

#     sum = 0
#     for i in range(digit):
#         if i > 0:
#             last_digit = digit % 10
#             sum = sum + last_digit
#             digit = digit // 10
#     return sum
# digit = int(input("Enter your digit: "))
# print(sum_digit(digit))


# def sum_of_digits(number):

#     sum = 0
#     while number > 0:
#         last_digit = number % 10
#         sum = sum + last_digit
#         number = number // 10
#     return sum

# number = int(input("Enter your number: "))
# print(sum_of_digits(number))

# def simple_interest(amount, rate, time):

#     si = (amount * rate * time) / 100
#     return si

# amount = int(input("Enter amount of interest: "))
# rate = float(input("Enter rate of interest: "))
# time = float(input("Enter time of interest: "))

# total = simple_interest(amount, rate, time)
# print("Simple Interest =", total)


# def reverse_string(string):

#     reverse = ""
#     for char in string:
#         reverse = char + reverse
#     return reverse

# string = input("Enter your string: ")
# print(reverse_string(string))


# def reverse_string(string):

#     reverse = ""
#     for c in string:
#         reverse = c + reverse
#     return reverse

# string = input("Enter your string: ")
# result = reverse_string(string)
# print("After reverse:", result)


# def reverse_string(string):

#     reverse = ""
#     for i in string:
#         reverse = i + reverse
#     return reverse

# string = input("Enter your string: ")
# result = reverse_string(string)
# print("After reverse:", result)


# def reverse_string(string):

#     reverse = ""
#     for c in string:
#         reverse = c + reverse
#     return reverse

# string = input("Enter your string: ")
# result = reverse_string(string)
# print("After reverse:", result)


# def reverse_number(num):

#     reverse = 0
#     while num > 0:
#         last_digit = num % 10
#         reverse = reverse * 10 + last_digit
#         num = num // 10
#     return reverse

# num = int(input("Enter a your number: "))
# print(reverse_number(num))


# def reverse_number(number):

#     reverse = 0
#     while number > 0:
#         last_number = number % 10
#         reverse = reverse * 10 + last_number
#         number = number // 10
#     return reverse

# number = int(input("Enter your number: "))
# result = reverse_number(number)
# print("After reverse=", result)


# def remove_duplicate(str):

#     empty = []
#     for i in str:
#         if i not in empty:
#             empty.append(i)
#     return empty

# str = ["h", "i", "u", "i", "h", "e", "a"]
# result = remove_duplicate(str)
# print(result)


# def remove_duplicates(num):

#     empty = []
#     for x in num:
#         if x not in empty:
#             empty.append(x)
#     return empty

# num = 4, 5, 3, 3, 5, 6, 9, 2, 4, 6
# result = remove_duplicates(num)
# print("After remove duplicates:", result)


# def leap_year(year):

#     if year % 100 != 0 and year % 400 == 0:
#         print("It is leap year")
#     elif year % 100 == 0 and year % 4 == 0:
#         print("It is leap year")
#     else:
#         print("It not leap year")

# year = int(input("Enter year: "))
# leap_year(year)


# def leap_year(year):

#     if year % 100 != 0 and year % 4 == 0:
#         print("It is leap year")
#     elif year % 100 == 0 and year % 400 == 0:
#         print("It is leap year")
#     else:
#         print("It is not leap year")

# year = int(input("Enter year: "))
# leap_year(year)


# year = int(input("Enter year: "))

# if year % 400 == 0:
#     print("It is leap year")
# elif year % 100 == 0:
#     print("It is not leap year")
# elif year % 4 == 0:
#     print("It is leap year")
# else:
#     print("It is not leap year")


# def leap_year(year):

#     if year % 100 != 0 and year % 400:
#         print("It is leap year")
#     elif year % 100 and year % 4:
#         print("It is leap year")
#     else:
#         print("It is not leap year")

# year = int(input("Enter the year: "))
# leap_year(year)


# def reverse_string(string):

#     reverse = ""
#     for i in string:
#         reverse = i + reverse
#     return reverse

# string = input("Enter your string: ")
# result = reverse_string(string)
# print("After reverse:", result)


# a = int(input("Enter the number a: "))
# b = int(input("Enter the number b: "))
# c = int(input("Enter the number c: "))

# average = (a + b + c) / 3
# print(average)


# def average_number(num):

#     total = 0
#     for i in range(num):
#         next_num = float(input("Enter the next number: "))
#         total = total + next_num
#     average = total / num
#     return average

# num = int(input("How many number do you enter: "))
# print(average_number(num))


# num = int(input("How many number do you enter: "))

# total = 0
# for i in range(num):
#     next_value = float(input("Enter the next value: "))
#     total = total + next_value

# average = total / num
# print("Average of number= %0.2f" % average)


# english = int(input("ENter the marks of english: "))
# banglaa = int(input("ENter the marks of bangla: "))
# islam = int(input("ENter the marks of islam: "))

# average = (english + banglaa + islam) / 3

# if average >= 80 and average <= 100:
#     print("You got A+")
# elif average >= 70 and average <= 79:
#     print("You got A")
# else:
#     print("You are fail")


# def check_prime(num):

#     for i in range(2, num):
#         if num % i == 0:
#             print("It is not prime number")
#             break
#     else:
#         print("It is prime number")

# num = int(input("Enter a number: "))
# check_prime(num)


# def check_prime(num):

#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# num = int(input("Enter a number: "))
# result = check_prime(num)

# if result:
#     print("It is prime number")
# else:
#     print("It is not prime number")


# def check_palindrome(string):
#     return string == string[-1::-1]

# string = input("Enter your string: ")
# result = check_palindrome(string)z

# if result:
#     print("It is palindrome string")
# else:
#     print("It is not palindrome")


# class Bank:

#     def __init__(self) -> None:
#         self.balance = 1000

#     def get_balance(self):
#         return self.balance

#     def withdraw(self, amount):
#         self.balance = self.balance - amount
#         return amount

# # now use the class
# my_bank = Bank()
# my_bank.withdraw(100)
# balance = my_bank.get_balance()
# print(balance)

# my_bank.withdraw(50)
# balance = my_bank.get_balance()
# print(balance)


# class Shopping:

#     def __init__(self) -> None:
#         self.cart = []

#     def add_to_cart(self, item):
#         self.cart.append(item)

# cus1 = Shopping()
# cus1.add_to_cart("T-Shirt")
# print(cus1.cart)

# cus2 = Shopping()
# cus2.add_to_cart("Pant")
# print(cus2.cart)

# cus3 = Shopping()
# cus3.add_to_cart("Shoes")
# print(cus3.cart)


# class Shopping:

#     def __init__(self):
#         self.cart = []

#     def add_to_cart(self, item):
#         self.cart.append(item)

# cus1 = Shopping()
# cus1.add_to_cart("Sandle")
# print(cus1.cart)

# cus2 = Shopping()
# cus2.add_to_cart("Shirt")
# print(cus2.cart)

# cus3 = Shopping()
# cus3.add_to_cart("T-Shirt")
# print(cus3.cart)

# cus4 = Shopping()
# cus4.add_to_cart("Pant")
# print(cus4.cart)

# cus5 = Shopping()
# cus5.add_to_cart("Shoes")
# print(cus5.cart)

# cus6 = Shopping()
# cus6.add_to_cart("Mask")
# print(cus6.cart)

"""===-----------==="""


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


# class Dhaka_Bank:

#     def __init__(self) -> None:
#         self.minimum = 100
#         self.balance = 5000

#     def get_balance(self):
#         return self.balance

#     def withdraw(self, amount):
#         if amount < self.minimum:
#             print("No money for you")
#         else:
#             self.balance = self.balance - amount
#             return amount
# my_bank = Dhaka_Bank()
# my_bank.withdraw(98)
# print(my_bank.get_balance())


# class Bank:

#     def __init__(self) -> None:
#         self.minimum = 100
#         self.balance = 10000

#     def get_balance(self):
#         return self.balance

#     def withdraw(self, amount):
#         if amount < self.minimum:
#             print("No money for you")
#         elif amount > self.balance:
#             print("You are broke! No money!")
#         else:
#             self.balance = self.balance - amount
#             return amount

# # now use class
# my_bank = Bank()
# my_bank.withdraw(990)
# balance = my_bank.get_balance()
# print("Now my balance:", balance)

# my_bank.withdraw(1200)
# balance = my_bank.get_balance()
# print("after that:", balance)


# class Shopping:

#     def __init__(self) -> None:
#         self.cart = []

#     def add_to_cart(self, item):
#         self.cart.append(item)

# #now use object
# cus1 = Shopping()
# cus1.add_to_cart("Watch")
# print(cus1.cart)

# cus2 = Shopping()
# cus2.add_to_cart("Ring")
# print(cus2.cart)

# cus3 = Shopping()
# cus3.add_to_cart("Mouse")
# print(cus3.cart)

# cus4 = Shopping()
# cus4.add_to_cart("Phone case")
# print(cus4.cart)


# class Laptop:

#     def cpu(self):
#         print("It is cpu")

#     def ram(self):
#         print("It is ram")

#     def ssd(self):
#         print("It is ssd")

# class PC:

#     def psu(self):
#         print("It is psu")

#     def mb(self):
#         print("It is mb")

# my_pc = PC()
# my_pc.cpu()
# my_pc.ram()
# my_pc.ssd()
# my_pc.psu()
# my_pc.mb()


# class SmartDevice:

#     def recharge(self):
#         print("Eating electricity")
#         print("Electrons are yummy!")

# class Phone(SmartDevice):

#     video_call = True

#     def __init__(self, brand, price, network):
#         self.brand = brand
#         self.price = price
#         self.network = network

# my_phone = Phone("Samsung", "$100", "Airtel")
# my_phone.recharge()


# class Shopping:

#     def __init__(self):
#         self.cart = []

#     def add_to_cart(self, item):
#         self.cart.append(item)

# mahbub = Shopping()
# mahbub.add_to_cart("Shirt")
# print(mahbub.cart)

# rahi = Shopping()
# rahi.add_to_cart("T-Shirt")
# print(rahi.cart)

# mahi = Shopping()
# mahi.add_to_cart("Watch")
# print(mahi.cart)


# class Bank:

#     def __init__(self):
#         self.balance = 5000

#     def get_balance(self):
#         return self.balance

#     def withdraw(self, amount):
#         self.balance = self.balance - amount
#         return amount

# my_bank = Bank()
# my_bank.withdraw(3000)
# print(my_bank.get_balance())


# class Bank:

#     def __init__(self) -> None:
#         self.minimum = 100
#         self.balance = 5000

#     def get_balance(self):
#         return self.balance

#     def withdraw(self, amount):
#         if amount < self.minimum:
#             print("No money for you")
#         elif amount > self.balance:
#             print("You are broke! No money")
#         else:
#             self.balance = self.balance - amount
#             return amount

# # now time to use class with object
# my_bank = Bank()
# my_bank.withdraw(800)
# balance = my_bank.get_balance()
# print("Now my balance:", balance)


# import math


# class Shape:

#     def __init__(self, a, b) -> None:
#         self.a = a
#         self.b = b


# class Triangle(Shape):

#     def area(self):
#         area = 0.5 * self.a * self.b
#         return area


# class Rectangle(Shape):

#     def area(self):
#         area = self.a * self.b
#         return area


# class Circle(Shape):

#     def area(self):
#         area = math.pi * self.a * self.a
#         return area


# tri = Triangle(8, 6)
# rec = Rectangle(9, 2)
# cir = Circle(7, 3)

# print("Triangle area =", tri.area())
# print("Ractangle area =", rec.area())
# print("Circle area = %0.2f" % cir.area())


# class Addition:

#     def __init__(self, a, b) -> None:
#         self.a = a
#         self.b = b

#     def result(self):
#         return self.a + self.b

# total = Addition(50, 100)
# print(total.result())


# class A:

#     def display(self):
#         print("I am display 1")


# class B(A):

#     def display(self):
#         print("I am display 2")


# class C(A,B):

#     def display(self):
#         print("I am display 3")


# class Bank:

#     def __init__(self) -> None:
#         self._name = "One_bank"

# account = Bank()
# print(account._name)


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


# class Shape:

#     def __init__(self, a, b):
#         self._a = a
#         self._b = b


# class Triangle(Shape):

#     def area(self):
#         area = 0.5 * self._a * self._b
#         return area

# tri = Triangle(20, 30)
# print("Triangle area =", tri.area())


# class Base:

#     def __init__(self) -> None:
#         self.a = "GeeksforGeeks"
#         self.__c = "GeeksforGaaks"

# my = Base()
# print(my.a)
# print(my.__c)


# x = int(5)
# print(x)


# x = "Hello"[0]
# print(x)


# x = "Hello".sub(0, 1)
# print(x)


# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")
# print(fruits)


# fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# print(fruits[2:5])


# car = {"A6", "allion", "premio", "A8L"}

# print(car)


# print(len(car))
# print(type(car))
# print(car)

# car.add("Q8")
# print(car)


# print("yes") if 5 > 2 else print("No")


# i = 1
# while i < 6:
#     print(i)
#     i = i + 1


# i = 1
# while i < 6:
#     if i == 3:
#         break
#     i = i + 1
#     print(i)


# i = 0
# while i < 6:
#     i = i + 1
#     if i == 3:
#         continue
#     print(i)


# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)


# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")


# car = ["a5", "a6", "a8", "r8"]

# for x in car:
#     if x == "a6":
#         continue
#     print(x)


# car = ["a5", "a6", "a8", "r8"]

# for x in car:
#     if x == "a6":
#         break
#     print(x)


# def my_function():
#     print("Hello from a function")

# my_function()


# def my_function(fname, lname):
#     print(fname)

# my_function()


# def my_function(x):
#     return x + 5

# print(my_function(15)


# x = lambda a: a+10
# print(x(20))


# class MyClass:

#     x = 5

# p1 = MyClass()
# print(p1.x)


# class Person:

#     def __init__(self, fname) -> None:
#         self.first_name = fname

#     def printname(self):
#         print(self.first_name)

# class Student(Person):
#     pass

# x = Student("Mike")
# x.printname()


# class Person:

#     def __init__(self, fname) -> None:
#         self.first_name = fname

#     def name(self):
#         print(self.first_name)

# class Student(Person):
#     pass

# x = Student("Mahbub")
# x.name()


# n = 3
# t = 100

# if n % 2 == 0:
#     print("Even")
# elif t %
# else:


# target = "Google", "FB", "MS", "Amazon"
# # print(target)


# for my_target in target:
#     print(my_target, end = " ")


# t = int(input())

# for i in range(t):
#     x = int(input())

#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")


# size = int(input("Enter size: "))
# a = []

# for i in range(size):
#     numbers = int(input("Enter number list: "))
#     a.append(numbers)

# for x in range(size):
#     for y in range(0,size-x-1):
#         if a[y] > a[y+1]:
#             temp = a[y]
#             a[x] = a[y+1]
#             a[y+1] = temp

# print(a)


# def bubble_sort(nums):

#     print("Before list:", nums)
#     n = len(nums)
#     for x in range(n):
#         for y in range(n-1):
#             if nums[y] > nums[y+1]:
#                 temp = nums[y]
#                 nums[y] = nums[y+1]
#                 nums[y+1] = temp
#     return nums

# nums = [6, 7, 3, 9, 1]
# sorted_result = bubble_sort(nums)
# print("After list:", nums)


# t = int(input())

# for i in range(t):
#     x = int(input())

#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")


# addition = lambda mahbub, nira : mahbub + nira
# print(addition(18, 17))


# import turtle
# turtle.shape("classic")
# turtle.speed(2)
# turtle.color("red")

# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)

# turtle.exitonclick()


# import turtle
# turtle.shape("turtle")

# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)

# turtle.exitonclick()


# def factorial(num):

#     fact = 1
#     for i in range(1, num+1):
#         fact = fact * i
#     return fact


# print(factorial(4))


# def average_number(nums):

#     total = 0
#     for i in range(nums):
#         next_num = float(input("Enter the next value: "))
#         total = total + next_num
#     average = total / nums
#     return average


# nums = int(input("How many number do you enter: "))
# print(average_number(nums))


# celsius = float(input("Enter Celsius temperature: "))
# result = (celsius*9) / 5 + 32

# print("%0.2f degree Celsius = %0.2f degree Fahrenheit" % (celsius, result))


# celsius = float(input("Enter celsius temperature: "))
# result = (celsius * 9) / 5 + 32

# print("%0.2f degree Celsius = %0.2f degree Fahrenheit" % (celsius, result))


# start = int(input("Start: "))
# end = int(input("End: "))

# for i in range(start, end + 1):
#     if i > 1:
#         for x in range(2, i):
#             if i % x == 0:
#                 break
#         else:
#             print(i)


# def palindrome(string):

# string = "geek"


# Optimized Bubble sort in Python

# def bubbleSort(array):

#     for i in range(len(array)):
#         swapped = False
#         for j in range(0, len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#                 swapped = True
#         if not swapped:
#             break


# data = [8, 3, 4, 1, 7]
# bubbleSort(data)
# print('Sorted Array in Ascending Order:')
# print(data)


# def selec_sort(nums):

#     n = len(nums)
#     for i in range(n):
#         min = i
#         for j in range(i+1, n):
#             if nums[min] > nums[j]:
#                 min = j

#         # swap elements
#         temp = nums[i]
#         nums[i] = nums[min]
#         nums[min] = temp


# if __name__ == "__main__":
#     nums = [6, 1, 4, 9, 2]
#     selec_sort(nums)
#     print(nums)


# class Student_info:

#     Roll = " "
#     Department = " "


# Mahbub = Student_info()
# Mahbub.Roll = 95
# Mahbub.Department = "CSE"

# print("Roll:", Mahbub.Roll)
# print("Department:", Mahbub.Department)


# class Calculator:

#     Brand = "Casio"

#     def sub(self, x, y):
#         total = x - y
#         return total


# my = Calculator()
# result = my.sub(30, 10)
# print(result)


# class Phone:

#     Model = ""
#     Brand = ""
#     Price = ""

#     def info(self):

#         print("Model:", self.Model)
#         print("Brand:", self.Brand)
#         print("Price:", self.Price)


# my_phone = Phone()
# my_phone.Model = "Galaxy Note20 Ultra"
# my_phone.Brand = "Samsung"
# my_phone.Price = "$1020"
# my_phone.info()


# class Student:

#     def __init__(self, roll, department):
#         self.roll = roll
#         self.department = department

#     def text(self):
#         print("Roll:", self.roll)
#         print("Department:", self.department)


# Mahbub = Student(163895, "CSE")
# Mahbub.text()

# Rahim = Student(156734, "EEE")
# Rahim.text()

# Adnan = Student(356734, "RAC")
# Adnan.text()


# class Triangle:

#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height


# Triangle_area = Triangle(5, 6)
# print(Triangle_area.area())


# import math
# class Circle:

#     def __init__(self, radius) -> None:
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius * self.radius


# total_area = Circle(5)
# print("Area = %0.2f" % total_area.area())


# class First_shift:

#     def class1(self):
#         print("this is class one")

#     def class2(self):
#         print("this is class two")


# class Second_shift(First_shift):

#     def class3(self):
#         print("this is class three")

#     def class4(self):
#         print("this is class four")


# both_shift = Second_shift()
# both_shift.class1()
# both_shift.class2()
# both_shift.class3()
# both_shift.class4()


# class Result:

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b


# class Addition(Result):

#     def add(self):
#         return self.a + self.b


# class Multiply(Result):

#     def multi(self):
#         return self.a * self.b


# class Subtraction(Result):

#     def sub(self):
#         return self.a - self.b


# ax = Addition(5, 9)
# bx = Multiply(6, 7)
# cx = Subtraction(10, 2)

# print("Addition =", ax.add())
# print("Multiply =", bx.multi())
# print("Subtraction =", cx.sub())

# print(5, 10)
# print(Multiply.multi(3, 7))
# print(Subtraction.sub(10, 2))


# class A:

#     def class1(self):
#         print("this is class one")

#     def class3(self):
#         print("this is class three")


# class B(A):

#     def class5(self):
#         print("this is class five")

#     def class4(self):
#         print("this is class four")


# class C(B):

#     def class6(self):
#         print("this is class six")

#     def class10(self):
#         print("this is class ten")


# both = C()
# both.class1()
# both.class3()
# both.class10()


# text = "bangladesh is beautiful country and I love my country very much"
# count = 0

# for i in text:
#     if i == " ":
#         count += 1
# count += 1
# print("The number of words in this text", count)



# sentence = "I am a student. I read in class ten"
# count = 0

# for x in sentence:
#     if x == " ":
#         count += 1
# count += 1
# print("the number of words in this sentence", count)


# num = int(input("Enter the last number: "))
# sum = 0
# for sq in range(num + 1):
#     sum = sum + (sq ** 2)
# print(sum)


# myList = [4, 5, 2, 1, 8]
# print(sum(myList))


# myList = [4, 5, 2, 1, 8]
# sum = 0
# for total in myList:
#     sum = sum + total
# print(sum)


# list = [10, 40, 20, 50, 90, 70]

# sum = 0
# for num in list:
#     sum = sum + num
# print(sum)




# def sumDigit(num):

#     sum = 0
#     for i in range(num):
#         if i > 0:
#             lastDigit = num % 10
#             sum += lastDigit
#             num = num // 10
#     return sum

# num = int(input("Enter a big number: "))
# print(sumDigit(num))


# num = 3456
# sum = 0

# for i in range(num):
#     if i > 0:
#         last_digit = num % 10
#         sum = sum + last_digit
#         num = num // 10
# print(sum)


# string = "student"
# reverse = " "
# for char in string:
#     reverse = char + reverse
# print(reverse)



# def reverse_string(string):

#     reverse = " "
#     for char in string:
#         reverse = char + reverse
#     return reverse

# string = "bangladesh"
# print(reverse_string(string))


# num = 12345
# reverse = 0

# while num > 0:
#     last_digit = num % 10
#     reverse = reverse * 10 + last_digit
#     num = num // 10

# print(reverse)


# def reverse_number(num):

#     print("Before reverse:", num)
#     reverse = 0
#     while num > 0:
#         last_digit = num % 10
#         reverse = reverse * 10 + last_digit
#         num = num // 10
#     return reverse

# num = 12345
# result = reverse_number(num)
# print("After reversed:", result)



# list = [10, 49, 10, 50, 69, 49, 50, 10, 69, 90]
# temp = []
# print("List before:", list)

# for i in list:
#     if i not in temp:
#         temp.append(i)

# print("List after:", temp)

# def removeDuplicates(myList):

#     emt = []
#     for i in  myList:
#         if i not in emt:
#             emt.append(i)
#     return emt

# myList = [5, 4, 4, 5, 6, 7, 2, 2]
# print(removeDuplicates(myList))



# year = int(input("Enter year: "))

# if year % 100 != 0 and year % 4 == 0:
#     print("It is leap year")

# elif year % 100 == 0 and year % 400 == 0:
#     print("It is leap year")

# else:
#     print("It is not leap year")


# def fibonacci(num):

#     x = 0
#     y = 1
#     print(x)
#     print(y)

#     for i in range(2, num):
#         result = x + y
#         x = y
#         y = result
#         print(result)

# fibonacci(10)


# def fibonacci(totalNum):

#     num1 = 0
#     num2 = 1
#     print(num1)
#     print(num2)

#     for i in range(2, totalNum):
#         result = num1 + num2
#         num1 = num2
#         num2 = result
#         print(result)

# fibonacci(20)



# def checkPrime(num):

#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return False

# num = int(input("Enter a number: "))
# result = checkPrime(num)

# if result:
#     print("It is a prime number")
# else:
#     print("It is not a prime number")



# def check_prime(num):

#     for x in range(2, num):
#         if num % 2 == 0:
#             print("It is not a prime number")
#             break
#     else:
#         print("It is a prime number")

# num = int(input("Enter a number: "))
# check_prime(num)



# from tkinter import *

# myRoot = Tk()

# myRoot.geometry("500x200")
# myRoot.minsize(200, 100)

# myRoot.title("My Information")

# def output():

#     print(f"Your Name: {name_info.get()}")
#     print(f"Your Roll: {roll_info.get()}")
#     print(f"Your Department: {department_info.get()}")

# name = Label(text="Name:", font=("helvetica 11"))
# roll = Label(text="Roll:", font=("helvetica 11"))
# department = Label(text="Department:", font=("helvetica 11"))
# name.grid(row=0)
# roll.grid(row=1)
# department.grid(row=2)

# name_info = StringVar()
# roll_info = StringVar()
# department_info = StringVar()
# name_enter = Entry(myRoot, textvariable=name_info)
# roll_enter = Entry(myRoot, textvariable=roll_info)
# department_enter = Entry(myRoot, textvariable=department_info)
# name_enter.grid(row=0, column=1)
# roll_enter.grid(row=1, column=1)
# department_enter.grid(row=2, column=1)

# Button(text="Submit", bd=2, command=output).grid()
# myRoot.mainloop()



"""
from tkinter import *

root = Tk()

root.geometry("300x400")

root.title("Google")

def answer():
    print("Submitted")

Label(text="Username").grid(row=0, column=1)
Label(text="Password").grid(row=1, column=1)

user_data = StringVar()
pass_data = StringVar()

Entry(root, textvariable=user_data).grid(row=0, column=2)
Entry(root, textvariable=pass_data).grid(row=1, column=2)

Button(text="Submit", command=answer).grid(row=2, column=2)

root.mainloop()
"""

# x = 0
# while(x < 100):
#     x += 2
# if (x % 33 == 0):
#     print('this is an awkward loop')

# a = 100
# b = 200
# c = 300

# def processor(arg):
#     print('processing stuffs!')
#     global a
#     global b
#     c += arg + b + a
#     print(c)
# processor(10)

# def mod_div_calculation(num1, num2, calc_type):
#     if calc_type == '%':
#         print(num1 % num2)
#     elif calc_type == '/':
#         print(num1 / num2)

# a = 60
# b = 70
# result = a + b
# print(result)

# a = 9
# b = 4
# print(a * b)

# name = "Mahbubur Rahman"
# print("His full name is " + name)

# numbers = [6, 4, 8, 3, 9, 2]
# for i in numbers:
#     print(i)

# numbers = [6, 8, 4, 6, 2, 9]
# find = numbers[4]
# print(find)

# numbers = [6, 8, 4, 6, 2, 9]
# print(numbers[2:])

# numbers = [6, 8, 4, 6, 2, 9]
# print(len(numbers))

# numbers = [6, 8, 4, 5, 2, 9]
# numbers.remove(6)
# print(numbers)

# numbers = [6, 8, 4, 5, 2, 9]
# numbers.insert(4, 10)
# print(numbers)

# numbers = [6, 8, 4, 5, 2, 9]
# numbers.append(3)
# print(numbers)

# numbers = [6, 8, 4, 5, 2, 9]
# check = 6 in numbers
# print(check)

# numbers = [6, 8, 4, 5, 2, 9]
# check = 7 in numbers
# print(check)

# numbers = [6, 8, 4, 5, 2, 9, 1]
# numbers.sort()
# print(numbers)

# li = []
# for i in range(10):
#     li.append(i)
#
# print(li)

# my_list = []
# for i in range(5):
#     my_list.append(i**2)
#
# print(my_list)

# li = [6, 7, "Jack", 9, "Mark"]
# print(type(li))

#-----------------------------------------------
#===============================================

# hello world...
# print("Hello, World!")


# variables..
# x = 50
# y = 70
# print(x)
# print(y)

# x = 10
# x = "Really"
# print(x)


# type...
# x = 10
# print(type(x))

# check = True
# print(type(check))

# num = 10.5
# print(type(num))


# Many Values to Multiple Variables
# num1, num2, num3 = 60, 40, 20
# print(num2)


# One Value to Multiple Variables
# a = b = c = "hello"
# print(b)

#==============================555

# def check_prime(num):
#
#     for i in range(2, num):
#         if num % i == 0:
#             print("It's not a prime number")
#             break
#     else:
#         print("It's a prime number")
#
# num = int(input("Enter a number: "))
# check_prime(num)

# def count_vowels(text):
#     c = 0
#     vowels = ["a", "e", "i", "o", "u"]
#     for i in text:
#         if i in vowels:
#             c = c + 1
#     return c
#
# text = input("Enter text: ")
# result = count_vowels(text)
# print("Total vowels in this text", result)

# fibonnacchi series..

# def fibo(num):
#     num1 = 0
#     num2 = 1
#
#     if (num == 1):
#         print(num1)
#     else:
#         print(num1)
#         print(num2)
#
#         for i in range(2, num):
#             result = num1 + num2
#             num1 = num2
#             num2 = result
#             print(result)
#
# fibo(10)

# def leap_year(year):
#     if year % 400 == 0:
#         print("It is leap year")
#     elif year % 100 == 0:
#         print("It is not leap year")
#     elif year % 4 == 0:
#         print("It is leap year")
#     else:
#         print("It is not leap year")
#
# for i in range(1, 5):
#     year = int(input("Enter year: "))
#     leap_year(year)


# nested_list = [['p','q','r'], 1, 2, 3, [100, 121, [11,12,13]]]
# print(nested_list[0][1])
# print(nested_list[4][2][2])


# li = [5, 10, 15, 25]
# print(li[::-2])


# import copy as cp
#
# s = [10, 20]
# s.append(60)
#
# n = cp.copy(s)
# n.append(60)
#
# x = cp.copy(n)
# x.append(60)
#
# print(s, n, x, sep='#')


# simple = [1, 2, 4, 5, 6]
# print(simple[:])
# print(simple[-1])

# print(simple[:-1])
# print(simple[-1])

import csv
file = open("test.csv")
csv_file_reader = csv.reader(file)
data = list(csv_file_reader)
print(csv_file_reader)