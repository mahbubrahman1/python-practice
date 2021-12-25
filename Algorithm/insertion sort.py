

# def insertion_sort(list):

#     n = len(list)

#     for i in range(1, n):
#         item = list[i]
#         j = i - 1

#         while j >= 0 and list[j] > item:
#             list[j + 1] = list[j]
#             j = j - 1
#             list[j + 1] = item


# list = [6, 1, 4, 9, 2]

# insertion_sort(list)
# print(list)


# def insertion_sort(list):

#     n = len(list)

#     for i in range(1, n):
#         item = list[i]
#         j = i - 1

#         while j >= 0 and item < list[j]:
#             list[j + 1] = list[j]
#             j = j - 1

#         list[j + 1] = item


# list = [6, 1, 4, 9, 2]

# insertion_sort(list)
# print(list)


a = [7, 4, 3, 5, 1]

for i in range(1, size):
    t = a[i]
    j = i - 1

    while j >= 0 and t < a[j]:
        a[j + 1] = a[j]
        j = j - 1

    a[j + 1] = t
