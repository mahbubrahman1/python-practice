# *** built in function/library function ***

print(type(18))
   # othoba
x = 18
print(type(x))

print(type('jhon'))

print(type(True))


from math import *

print(sqrt(25))
print(max(100,456,234))
print(min(453,123,45))
print(pow(2,3))

# othoba

num = 25, 34
print(max(num))


import math

print(max(60, 30, 80))
print(min(30, 70, 90))
print(math.sqrt(25))      # import math likhle math likhte hoy
print(math.ceil(2.8))
print(math.floor(6.7))
print(math.pow(3, 4))



from math import *

print(max(60, 30, 80))
print(min(30, 70, 90))
print(sqrt(25))             # from math import *  eita likhle ar math likhte hoy na
print(ceil(2.8))
print(floor(6.7))
print(pow(3, 4))


# *** User defined function ***

def message():
   print('I Love You')
   print('I Love My Car')
   print('I Love My Bycycle')
message()      # eta holo function ke call kora


def love():
    print("I Love My PC")
    print("I love My Cycle")
    print("I Love My Phone")

def message():
    print("I love you")
    print("I miss you")
    print("I cissed you")

love()
message()


def message():
   print('I Love You')
   print('I Love My Car')             # eta hocche perameter chara
   print('I Love My Bycycle')

message()


def add(m, n):
    result = m + n      # perameter soho (ekhane perameter hocche m,n)
    print(result)

add(10, 20)              #ekhane bosbe m,n er man


# aro clean/sundor kore likhle 
def add(m, n):
    result = m + n
    print(result)

add("The result is",10, 20)



def remove(p, q):
    result = p - q
    print(result)

def add(e, f):
    result = e + f
    print(result)

remove(90, 60)
add(70, 30)


def add(m, n):
    result = m + n
    print(result)

add(10, 50)
add(50, 40)
add(40, 80)


# function er sahajje 2 ti sonkher moddhe jog o biog

def add(m, n):
    result = m + n
    print(result)

add(10, 50)

def delete(m, n):
    result = m - n
    print(result)

delete(50, 10)

# othoba

def add(m, n):
    result = m + n
    print(result)

def delete(m, n):
    result = m - n
    print(result)

add(10, 50)
delete(50, 10)


def name(firstname):
    print(firstname + " Rahman")

name("Mahbubur")
name("Piyom")
name("Aayra")
name("Nafisa")


def cname(conuntry = "China"):
    print("I am from " + conuntry)

cname("England")
cname("Bangladesh")
cname("India")
cname("Japan")


def message(text):
    print("i love my " + text)

message("Car")
message("Bike")
message("PC")
message("Phone")
message("Bus")


# function er sahajje 3 ti sonkher moddhe jog

def add(x,y,z):
   result = x + y + z
   print(result)
add(20,40,60)    


def add(x,y):
    c = x+y
    print(c)

def name():
    print('Hello, Mahbub!')

add(10,20)
name()



# more information please check my notes and video: https://www.youtube.com/watch?v=yYR7WOdexDw&list=PLgH5QX0i9K3rz5XqMsTk41_j15_6682BN&index=11&ab_channel=AnisulIslamAnisulIslam
#                                                   https://www.youtube.com/watch?v=m9o9itPDjAs&list=PLgH5QX0i9K3rz5XqMsTk41_j15_6682BN&index=37&ab_channel=AnisulIslamAnisulIslamVerified