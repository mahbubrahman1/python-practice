li = [6, 7, "Jack", 9, "Mark"]
print(type(li))

# integer type data
age = [18,17,34,23,56,32]
print(age)



# String type data
student_name = ['Nadim','Diya','Habib','Maisha','Rakib','Mahbub']
print(student_name)



value = [18,19.5,'mahbub',2011]
print(value)




# indexing
#          0       1      2       3       4
name = ['mahbub','mim','habib','rahim','sadi']
print(name[3])



 #         -5      -4     -3     -2      -1
name = ['mahbub','mim','habib','rahim','sadi']
print(name[-1])




car_name = ["audi a6", "toyota harrier", "honda civic", "nissan x-trail", "audi a8l", "bmw i8"]
print(car_name[4:]) # 0, 1, 2, 3 bade sob print korbe



car_name = ["audi a6", "toyota harrier", "honda civic", "nissan x-trail", "audi a8l", "bmw i8"]
print(car_name[2:]) # 0, 1, bade sob print korbe





# koyta gari ache amar ta gonona korar jonno len use kora hoy

my_car = ['Civic','Allion A15','Audi A6','Land Cruiser','Premio']
print(len(my_car))



student = ['Hasan','Mahbub','Noyon','Munna','Hridoy']
student.remove('Mahbub')
print(student)



age = [15,58,75,45,65,25]
age.remove(25)
print(age)



age = [15,58,75,45,65,25]
age.insert(2,96)
print(age)



values = [15,58,'jack',45,'jhon',25]
values.append(18)
print(values)



nums = [12,45,36,23,21]
print(min(nums))



nums = [12,45,36,23,21]
print(max(nums))



student_list = ['Rahi','Habib','Mariya','Mehzabeen','Rahim']
print('Rahim' in student_list)



student_list = ['Rahi','Habib','Mariya','Mehzabeen','Rahim']
print('Salman' in student_list)




num = [12,45,34,23,78]
num.pop()
print(num)



name = ['Jack','Rose','Harry','Jhon''Rock']
name.pop()
print(name)



alphabet = ['c','b','d','a','f','e']
alphabet.sort()
print(alphabet)



number = [2, 5, 1, 23, 3, 7, 4, 8, 9, 6, 10]
number.sort()
print(number)


li = []
for i in range(10):
    li.append(i)
print(li)



# li = [5, 3, 6, 2, 8, 4, 45, 64, 32]
# even_numbers = []
# for i in li:
#     if i % 2 == 0:
#         even_numbers.append(i)
#
# print(even_numbers)


numbers = [67, 23, 56, 30, 69, 34, 20, 21]
odd_numbers = []
for i in numbers:
    if i % 2 != 0:
        odd_numbers.append(i)

print(odd_numbers)


# - list from user

# list = []
# length = int(input("Enter the length of list: "))

# for i in range(length):
#     x = int(input("Enter the number: "))
#     list.append(x)

# print("list:", list)





# FOR MORE INFORMATION PLEASE CHECK PROGRAMMING ESSENTIALS BOOK 

# FOR MORE INFORMATION PLEASE This tutorials https://www.youtube.com/watch?v=V0zzqVn3Tn8&t=304s&ab_channel=AnisulIslam

# https://www.youtube.com/watch?v=YVov0H3JRkc&t=244s&ab_channel=AnisulIslam

