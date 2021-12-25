


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# sum = num1 + num2 + num3
# result = sum / 3
# print("Average number =", result)






num = int(input("How many number do you enter: "))
total = 0

for i in range(num):
    numbers = float(input("Enter number: "))
    total = total + numbers
avg = total / num
print("Average number:", avg)