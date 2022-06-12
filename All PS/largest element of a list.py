
# my_list = [10, 50, 60, 90, 30, 20, 70]
# x = max(my_list)
# print(x)




# my_list = [10, 50, 60, 90, 30, 20, 70]
# lar = my_list[0]
#
# for i in my_list:
#     if i > lar:
#         lar = i
# print("largest number is", lar)
#
#
#
# def large(mylist):
#     largest = mylist[0]
#     for x in mylist:
#         if x > largest:
#             largest = x
#     return largest
#
# mylist = [5, 6, 3, 9, 4, 7, 8]
# result = large(mylist)
# print("Largest number in the list:", result)






# def even_odd(list):
#     list = []
#     length = int(input("Enter the length of list: "))
#
#     for i in range(len(length)):
#         x = int(input("Enter the number: "))
#         list.append(x)
#
#     empty = ""
#
#     for i in range(len(list)):
#         num = list[i]
#         if (num % 2 == 0):
#             empty = empty + " 0"
#         else:
#             empty = empty + " 1"
#
#     return empty
#
# print(even_odd(list))





list = []
length_list = int(input("Enter the length of list: "))

for i in range(length_list):
    x = int(input("Enter the number: "))
    list.append(x)

empty = ""

for i in range(len(list)):
    num = list[i]
    if (num % 2 == 0):
        empty = empty + " 0"
    else:
        empty = empty + " 1"

print(empty)













