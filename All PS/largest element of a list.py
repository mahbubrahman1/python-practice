
# my_list = [10, 50, 60, 90, 30, 20, 70]
# x = max(my_list)
# print(x)




my_list = [10, 50, 60, 90, 30, 20, 70]
lar = my_list[0]

for i in my_list:
    if i > lar:
        lar = i
print("largest number is", lar)



def large(mylist):
    largest = mylist[0]
    for x in mylist:
        if x > largest:
            largest = x
    return largest

mylist = [5, 6, 3, 9, 4, 7, 8]
result = large(mylist)
print("Largest number in the list:", result)


















