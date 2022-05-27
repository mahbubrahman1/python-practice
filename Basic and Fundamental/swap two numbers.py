
# x = 10
# y = 50
# print(x, y)
#
# tempo = x
# x = y
# y = tempo
# print(x, y)
#
#
#
# m = int(input("Enter the number of m: "))
# n = int(input("Enter the number of n: "))
# print(m, n)
#
# temp = m
# m = n
# n = temp
# print(m, n)
#
#
#
# a = 40
# b = 10
# print(a, b)
#
# a, b = b, a
# print(a, b)
#


def swap_numbers(a, b):
    print(a, b)
    a, b = b, a
    print(a, b)

a = 400
b = 300
swap_numbers(a, b)