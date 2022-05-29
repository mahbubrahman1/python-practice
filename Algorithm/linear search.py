
num = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]

for i in num:
    if i == 33:
        print("i find it")


my_car_list = ["civic", "allion", "premio", "a6", "axio", "a8l", "lc"]
for car in my_car_list:
    if car == "a8l":
        print("I find it")
        break
else:
    print("it's not in my car list")


def linear_search(my_list, find_num):
    n = len(my_list)

    for i in range(n):
        if my_list[i] == find_num:
            return "found!"

    return "not found!"

my_list = [10, 60, 40, 30, 90]
find_num = 30
print(linear_search(my_list, find_num))
