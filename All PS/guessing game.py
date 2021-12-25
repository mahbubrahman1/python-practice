
import random


guess_num = int(input("Enter number between 1 to 10: "))
random_num = random.randint(1, 10)

if guess_num == random_num:
    print("You have won")
else:
    print("You have lost")








guess_number = int(input("Enter number between 1 to 10: "))
random_number = random.randint(1, 10)

if guess_number == random_number:
    print("You have won")
else:
    print("You have lost")

    # show the random number
    print("Random number was:", random_number)







# random moudle import korte abar vule jeona. ekhane ami import korinai cause upore dekho kore felchi

for i in range(1, 6): # 5 bar colar jonno 
    guess_number = int(input("Enter the number between 1 to 15: "))
    random_number = random.randint(1, 15)

    if guess_number == random_number:
        print("Hurrah! You have won")
    else:
        print("Oh! You have lost")
    
        print("Actually the random number is:", random_number)


