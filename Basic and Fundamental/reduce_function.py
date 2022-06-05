from functools import reduce

myList = [6, 2, 9, 5, 8]

def addition(a, b):
    return a + b

sum = reduce(addition, myList)
print(sum)