
# function binary_search(list, find_value):
    
#     low = 0
#     high = length of the list
    
#     while low <= high:
#         mid = average of low and high
#         if mid element < find_value
#             element will be on the right side
#             low = mid

#         elif mid element > find_value
#             element will be on the left side
#             high = mid

#         else
#             you got the element
#             return the mid




def binary_search(list, find_value):

    low = 0
    high = len(list)

    while low <= high:
        mid = (low + high) // 2
        if list[mid] < find_value:
            low = mid
        elif list[mid] > find_value:
            high = mid
        else:
            return mid
        
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = binary_search(list, 8)
print(index)









