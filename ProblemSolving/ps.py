
# - Python program to swap two elements in a list


# two variables
a = 78
b = 63
print(a, b)
a, b = b, a 
print(a, b)


# List

def swap_position(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

Number_List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swap_position(Number_List, pos1-1, pos2-1))

#                 OR

Number_List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

def swap_position(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

print(swap_position(Number_List, pos1-1, pos2-1))





list = [1, 2, 3, 4, 5]
pos1, pos2 = 2, 5

def swap_position(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

print(swap_position(list, pos1-1, pos2-1))




Number_List = [23, 65, 19, 90]
print(Number_List)

pos1, pos2 = 1, 3

Number_List[pos1], Number_List[pos2] = Number_List[pos2], Number_List[pos1]
print(Number_List)





