# my_list = [5, 9, 6, 7, 4]
# new_list = []
#
# for i in my_list:
#     new_list.append(i * i)
#
# print(new_list)


# my_list = [5, 9, 6, 7, 4]
# new_list = [i * i for i in my_list]
# print(new_list)


# squares of the odd numbers
# my_list = [5, 9, 6, 7, 4]
# new_list = []
#
# for i in my_list:
#     if i % 2 != 0:
#         new_list.append(i * i)
#
# print(new_list)


# my_list = [5, 9, 6, 7, 4]
# new_list = [i*i for i in my_list if i%2!=0]
# print(new_list)


# my_list = [5, 6, 3, 9, 2, 8]
# new_list = [i+1 for i in my_list]
# print(new_list)


# my_list = [5, 6, 3, 9, 2, 8]
# my_dict = {i:i*2 for i in my_list}
# print(my_dict)


my_dict = {
    "Brand": "Samsung",
    "Model": "Galaxy S22",
    "Price": "$999"
}

new_dict = [k for k, v in my_dict.items()]
print(new_dict)