
# - Remove Duplicates from list



numbers = [34, 56, 29, 34, 29, 70, 56, 34, 29]

unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)

print("After removing duplicates:", unique)



my_list = [1,1,2,3,2,2,4,5,6,2,1]
print("List before =", my_list)

uniq = []
for x in my_list:
    if x not in uniq:
        uniq.append(x)

print("The list after removing duplicates: ", uniq)


# using function


def remo_dup(items):
    uniq = []
    for i in items:
        if i not in uniq:
            uniq.append(i)
    return uniq

items = [2, 3, 5, 3, 2, 9, 7, 0, 9, 3, 5]
print(remo_dup(items))




def remove_duplicates(my_list):
    print("List Before:", my_list)

    unique = []
    for i in my_list:
        if i not in unique:
            unique.append(i)
    return unique

my_list = [3, 5, 5, 6, 4, 3, 8, 9, 8, 3]

result = remove_duplicates(my_list)
print("The list after removing duplicates: ", result)






# example..............



my_list = [3, 5, 6, 3, 5, 6, 6, 3, 9, 2]
print("List before =", my_list)

emt = []

for i in my_list:
    if i not in emt:
        emt.append(i)

print("The list after removing duplicates:", emt)






def remove_duplicates(my_list):
    print("List before =", my_list)
    emt = []
    for x in my_list:
        if x not in emt:
            emt.append(x)
    return emt

my_list = [3, 5, 6, 3, 5, 6, 6, 3, 9, 2]

result = remove_duplicates(my_list)
print("The list after removing duplicates =", result)

