import math

def factorial(num):
    return math.factorial(num)

num = 4
result = factorial(num)
print("Factorial of", num, "is", factorial(num))


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

print(factorial(4))


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

n = 5
print(fact(n))


def fact(num):
    if (num == 1):
        return 1
    else:
        return num * fact(num-1)

print(fact(10))
