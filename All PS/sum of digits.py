num = int(input("Enter a big number: "))
sum = 0
while num > 0:
    last_digit = num % 10        
    sum = sum + last_digit                # ei sutro gula mukhosto rakhte hobe
    num = num // 10
print(sum)





def sum_digit(num):
    
    sum = 0
    while num > 0:
        last_digit = num % 10
        sum = sum + last_digit
        num = num // 10
    return sum

num = int(input("Enter a big number: "))
result = sum_digit(num)
print("Sum of digits:", result)





def sum_digit(num):
    sum = 0
    for x in range(num):
        if x > 0:
            last_digit = num % 10
            sum = sum + last_digit
            num = num // 10
    return sum

num = int(input("Enter a number: "))
result = sum_digit(num)
print("Sum of digit:", result)




num = int(input("Enter a number: "))
sum = 0
while num > 0:
    sum = sum + num % 10
    num = num // 10
print(sum)