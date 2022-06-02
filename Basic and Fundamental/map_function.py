# def my_function(n):
#     return n * n
#
# my_list = [5, 9, 7, 8]
# new_list = map(my_function, my_list)
# print(new_list)


"""
def my_function(n):
    return n * n

my_list = [5, 9, 7, 8]

#convert the map into a list, for readability:
# new_list = list(map(my_function, my_list))
# print(new_list)

# you can also conver the map into a tuple or set
# new_list = tuple(map(my_function, my_list))
# print(new_list)

new_list = set(map(my_function, my_list))
print(new_list)
"""


# def addition(num):
#     return num + num
#
# numbers = [6, 3, 9, 2]
# result = map(addition, numbers)
# print(list(result))


# def my_function(n):
#     return len(n)
#
# my_list = map(my_function, ("hi", "hello", "hey"))
# print(list(my_list))


# using lambda expressions
# numbers = [6, 2, 9, 3]
# result = map(lambda x: x + x, numbers)
# print(tuple(result))


nums1 = [5, 6, 7]
nums2 = [2, 3, 4]

result = map(lambda a, b: a + b, nums1, nums2)
print(list(result))