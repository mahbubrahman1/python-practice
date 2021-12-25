num = int(input("Enter the last number: "))

sum = 0
for i in range(num + 1):
    sum = sum + i**2
print(sum)






num = int(input("Enter the last number: "))

sum = 0
for i in range(2, num + 1, 2):
    sum = sum + i**2
print(sum)






def sum_square(num):
    sum = 0
    for i in range(num + 1):
        sum = sum + (i**2)
    return sum

num = int(input("Enter the last number: "))
result = sum_square(num)
print("sum of square:", result)