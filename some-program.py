"""
name = input("Hi there! What's you name: ")
print("Nice to meet you! " + name)
age = int(input("How old are you: "))
birth_year = 2022 - age
ans = str(birth_year)
print("You were born in " + ans)
"""

"""
# different way
print("Hi there! What's you name?")
name = input()
print("Nice to meet you! " + name)
print("How old are you?")
age = int(input())
birth_year = 2022 - age
ans = str(birth_year)
print("You were born in " + ans)
"""

"""
# a simple program using infinite loop and break
while True:
    name = input("Enter you name: ")
    if name == "Mahbub":
        break

print("Thanks")

using continue
while True:
    name = input("Who are you? Answer: ")
    if name != "IronMan":
        continue
    print("Hi " + name)
    password = input("what's your password? Answer: ")
    if password == "superpower":
        break

print("Open the door!!")
"""

"""
# guess game
import random
sec_num = random.randint(1, 20)
flag = False

def game_function(guessed_num, secret):
    if guessed_num < secret:
        return "Too low"
    elif guessed_num > secret:
        return "Too high"
    else:
        return "CORRECT"

for i in range(1, 6):
    print('Take a guess. You have '+str(6-i)+' guesses left.')
    guess = input()
    if game_function(int(guess)), sec_num) == "CORRECT":
        print("YOU WON THE GAME")
        flag = True
        break

if not flag:
    print("You lost the game")
"""

"""
fav_movies = []

while True:
    print("Movie no "+ str(len(fav_movies)+1) +" or press ENTER to stop adding into the list.")
    movie = input()

    if movie == "":
        break

    fav_movies = fav_movies + [movie]

if len(fav_movies) != 0:
    print("The movies are: ")
    for i in  range(len(fav_movies)):
        print(fav_movies[i])
"""

"""
fav_tech_brand = ["Samsung", "Corsair", "Asus", "Dell", "Google"]
name = input("Enter a tech brand name: ")
if name not in fav_tech_brand:
    print("No. It's not in the list.")
else:
    print(name+" is in the list")
"""

# search item using Linear Search algorithom...
"""
n = 6

def searching(li, n):
    for i in range(len(li)):
        if li[i] == n:
            return "Found!"

    if i == len(li) - 1:
        return "Not Found!"

li = [5, 7, 3, 9, 1]
result = searching(li, n)
print(result)
"""


"""
def linear_search(li, x):
    n = len(li)

    for i in range(n):
        if li[i] == x:
            return "FOUND!"

    return "NOT FOUND!"

li = [6, 8, 3, 4, 5]
x = 7
result = linear_search(li, x)
print(result)
"""


"""
def linear_search(my_list, find_num):
    n = len(my_list)

    for i in range(n):
        if my_list[i] == find_num:
            return "found!"

    return "not found!"

my_list = [10, 60, 40, 30, 90]
find_num = 30
print(linear_search(my_list, find_num))
"""


"""
text = "bangladesh is a beautiful country"
letters = {}

for i in text:
    letters.setdefault(i, 0)
    letters[i] = letters[i] + 1

print(letters)
"""

"""
import pprint as serial

text = "bangladesh is a beautiful country"
letters = {}

for i in text:
    letters.setdefault(i, 0)
    letters[i] = letters[i] + 1

serial.pprint(letters)
"""

"""
contact_number = {
    "John" : 1799886655,
    "David" : 1944338899,
    "Marin" : 1633221177
}
n = 0

while n < 5:
    name = input("Enter your name or press Enter to exit: ")

    if name == "":
        break

    if name in contact_number:
        print("The contact number of "+name + " is " + str(contact_number[name]))
    else:
        add = input("There is no such name in the phone-book. Do you want to add it? ")

        if add == "yes":
            number = input("Enter the number: ")
            contact_number[name] = number
            print("Dictionary updated.")
        elif add == "no":
            quit = input("Do you want to quit?")
            if quit == "yes":
                break
            else:
                print("keep searching...")

        n = n + 1
"""