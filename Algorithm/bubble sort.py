

# def bubble_sort(list):
#     n = len(list)
#     for i in range(n):
#         for j in range(n-1):

#             if list[j] > list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]
#     return list


# list = [1, 2, 7, 9, 3, 5]

# print(bubble_sort(list))


# def bubble_sort(list):
#     n = len(list)
#     for i in range(n):
#         for j in range(n-1):

#             if list[j] > list[j+1]:
#                 temp = list[j]
#                 list[j] = list[j+1]
#                 list[j+1] = temp
#     return list


# list = [1, 2, 7, 9, 3, 5]
# print(bubble_sort(list))


# dhape dhape kivabe kaj koreche seita dekhar jonne
def bubble_sort(nums):

    print("Before_nums_list:", nums)
    n = len(nums)
    for x in range(n):
        for y in range(n-1):
            if nums[y] > nums[y+1]:
                temp = nums[y]
                nums[y] = nums[y+1]
                nums[y+1] = temp
                print(nums)
    return nums


nums = [5, 9, 6, 2, 3]
sorted_result = bubble_sort(nums)
print("After_nums_list:", nums)


def bubble_sort(nums):

    print("Before nums:", nums)
    n = len(nums)

    for x in range(0, n):

        for y in range(0, n-x-1):
            if nums[y] > nums[y+1]:
                nums[y], nums[y+1] = nums[y+1], nums[y]
    return nums


nums = [19, 16, 15, 20, 11, 13]
sorted_result = bubble_sort(nums)
print("After_nums_list:", sorted_result)


# def bubbleSort(array):

#     for i in range(len(array)):
#         swapped = False
#         for j in range(0, len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#                 swapped = True
#         if not swapped:
#             break


# data = [8, 3, 4, 1, 7]
# bubbleSort(data)
# print('Sorted Array in Ascending Order:')
# print(data)
