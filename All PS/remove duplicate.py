

my_list = [34, 56, 29, 34, 29, 70, 56, 34, 29]

unq = []
for i in my_list:
    if i not in unq:
        unq.append(i)

print("After removing duplicates:", unq)





list = [10, 49, 10, 50, 69, 49, 50, 10, 69, 90]
empty = []

for i in list:
    if i not in empty:
        empty.append(i)
print(empty)





def remove_duplicates(my_list):
    print("List before:", my_list)

    emp = []
    for i in my_list:
        if i not in emp:
            emp.append(i)
    return emp

my_list = [2, 4, 5, 2, 3, 6, 5, 4, 7, 8, 3]
x = remove_duplicates(my_list)
print("List after removing duplicates:", x)


# more explan- programming hero app
