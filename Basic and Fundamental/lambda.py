# normal function
# def add(a, b):
#     return a + b
#
# print(add(50, 30))


# using lambda function
# add = lambda a, b : a + b
# print(add(50, 40))

print((lambda a, b: a + b)(20, 50))


"""
x = lambda a : a + 10
print(x(20))
#ekhane a hocche peramiter/argument and ei peramiter a ami 20 pass korechi


x = lambda a, b : a * b
print(x(4, 5))


# tinti sonkher moddhe jug o kora jay sohoje

sum = lambda a, b, c : a + b + c
print(sum(10,20,30))


def fun(n):
    return lambda a : a * n

dob = fun(2)
print(dob(11))


def multi(num):
    return lambda a : a * num

double = multi(2)
tripler = multi(3)

print(double(10))
print(tripler(10))
"""