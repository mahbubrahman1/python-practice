
x = int(input("Enter the number of x: "))
y = int(input("Enter the number of y: "))
z = int(input("Enter the number of z: "))

result = (x + y + z) / 3
print("Average number = %0.2f"% result)





n = int(input("How many numbers do you enter: "))
total = 0

for i in range(n):
    number = float(input("Enter number: "))
    total = total + number

avg = total / n
print("Average number is: %0.2f"% avg)





def avg_num(num):
    total = 0
    for i in range(num):
        nxt_num = float(input("Enter the next value: "))
        total = total + nxt_num
    average = total / num
    return average

num = int(input("how many number do you enter: "))
result = avg_num(num)
print("Average this number: %0.2f" % result)