

# - check prime number

num = int(input("Enter your number: "))

for i in range(2, num):
    if num % i == 0:
        print("It's not prime number")
        break
else:
    print("It is prime number")





def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print("It's not prime number")
            break
    else:
        print("It is prime number")

num = int(input("Enter your number: "))
check_prime(num)


# for more explan please check my notes

