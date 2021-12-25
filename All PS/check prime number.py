


# num = 11
# for i in range(2, num):  # prime number a sobsomoy 2 ebong je number deya hobe se number er ag porjonto bhag korbe. ekhane 2 diye prothome vag korbe then 3 tarpor 11 er agporjonto colte thakbe.
#     if num % i == 0:  # ekhane i mean 2 diye 11 ke vag korbe tarpor jodi vagshesh 0 hoy tahole prime number. 2 diye jay na then dibe 3 diye then........
#         print("It is not prime number")
#         break
# else:
#     print("It is prime number")





# num = int(input("Enter a number: "))
# for i in range(2, num):
#     if num % i == 0:
#         print("It is not prime number")
#         break
# else:
#     print("It is prime number")




def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print("It's not a prime number")
            break
    else:
        print("It's prime number")

num = int(input("Enter a number: "))
check_prime(num)





def checkPrime(num):

    for i in range(2, num):
        if num % i == 0:
            return False
    return False

num = int(input("Enter a number: "))
result = checkPrime(num)

if result:
    print("It is a prime number")
else:
    print("It is not a prime number")






















# more info check this video: https://www.youtube.com/watch?v=nM1TRC0myws&t=216s