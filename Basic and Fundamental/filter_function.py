# def even_numbers(n):
#     return n % 2 == 0
#
# li = [10, 55, 66, 33, 22, 20, 90, 99]
# new_list = list(filter(even_numbers, li))
# print(new_list)


# using lambda expression
# my_list = [10, 55, 66, 33, 22, 20, 90, 99]
# new_list = list(filter(lambda n: n % 2 == 0, my_list))
# print(new_list)


"""
ages = [12, 18, 29, 10, 8, 31, 25]

def myFunction(x):
    if x > 18:
        return True
    else:
        return False

# adults = list(filter(myFunction, ages))
# print(adults)

# another way
adults = filter(myFunction, ages)

for i in adults:
    print(i)
"""


ages = (12, 18, 29, 10, 8, 31, 25)
adults = tuple(filter(lambda x: x > 18, ages))
print(f"Adults ages are: {adults}")