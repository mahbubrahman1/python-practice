

num = int(input("Enter a big number: "))
reverse = 0
while num > 0:
    last_digit = num % 10                # ei sutro gula mukhosto rakhte hobe
    reverse = reverse*10 + last_digit   # ei sutro gula mukhosto rakhte hobe
    num = num // 10                     # ei sutro gula mukhosto rakhte hobe
print(reverse)








def rev_num(num):

    reverse = 0
    while num > 0:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        num = num // 10
    return reverse

num = int(input("Enter a big number: "))
result = rev_num(num)
print("After reverse =", result)






def reverse_number(num):
    
    reverse = 0
    for i in range(num):
        if num > 0:
            last_digit = num % 10
            reverse = reverse * 10 + last_digit
            num = num // 10
    return reverse

num = int(input("Enter a big number: "))
result = reverse_number(num)
print("After reverse:", result)








num = int(input("Enter a big number: "))
reverse = 0
while num > 0:
    reverse = reverse*10 + num%10
    num = num // 10
print(reverse)
