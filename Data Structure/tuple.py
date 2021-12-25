
x = (3, 5, 7)
print(type(x))




tuple = (1, 2, 3, 4)
print(tuple[2])




# list er man change kora jay but tuple er man change kkora jay na....
my_tup = (43, 34, 78, 10, 74)
my_tup[3] = 18  
print(my_tup)




num = (50, 40, 10, 90, 70)
a, b, c, d, e = num

print(b)

print(a, d)




items = (1, 2, 5.5, ["a", "b", "c"], ("apple", "mango"))

for i in items:
    print(i, type(i))




items = (10, 50.4, "hanif", ["x", "y", "z"], ("honda", "audi", "bmw"))

for i in items:
    print(i, type(i))

print(items[3])

print(items[4][2])




"=== convert list from tuple"

tuple = (3, 6, 2, 9)
print(list(tuple)) 


tuple = (3, 6, 2, 9)
lst = list(tuple)
print(lst)



