

# def selection_sort(nums):

#     for i in range(5):
#         min = i

#         for j in range(i, 6):
#             if nums[j] < nums[min]:
#                 min = j

#         temp = nums[i]
#         nums[i] = nums[min]
#         nums[min] = temp


# nums = [5, 3, 8, 6, 7, 2]
# selection_sort(nums)
# print(nums)


# def selec_sort(nums):

#     n = len(nums)
#     for i in range(n):
#         min = i
#         for j in range(i+1, n):
#             if nums[min] > nums[j]:
#                 min = j

#         # swap elements
#         temp = nums[i]
#         nums[i] = nums[min]
#         nums[min] = temp
#     return nums

# nums = [64, 25, 12, 22, 11]
# print(selec_sort(nums))


# def selec_sort(nums):

#     n = len(nums)
#     for i in range(n):
#         min = i
#         for j in range(i+1, n):
#             if nums[min] > nums[j]:
#                 min = j

#         # swap elements
#         temp = nums[i]
#         nums[i] = nums[min]
#         nums[min] = temp

# if __name__ == "__main__":
#     nums = [6, 1, 4, 9, 2]
#     selec_sort(nums)
#     print(nums)


def selection_sort(list):

    n = len(list)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if list[j] < list[min_index]:
                min_index = j

        if min_index != i:
            temp = list[i]
            list[i] = list[min_index]
            list[min_index] = temp

            # how it work
            print(list)

    return list


list = [6, 1, 4, 9, 2]
selection_sort(list)
print(list)
