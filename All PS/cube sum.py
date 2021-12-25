

num = int(input("Enter the last number: "))
sum = 0

for i in range(num+1):
    sum = sum + i ** 3
print(sum)





def cube_sum(num):
    sum = 0
    for i in range(num+1):
        sum = sum + i**3
    return sum

num = int(input("Enter the last number: "))
result = cube_sum(num)
print("The sum in this cube =", result)




