

# - Grade Point



english = int(input("Enter marks of English: "))
mathematics = int(input("Enter marks ofMathematics: "))
phycics = int(input("Enter marks of Physics: "))
biology = int(input("Enter marks of Biology: "))
history = int(input("Enter marks of History: "))
islam = int(input("Enter marks of Islam: "))
bangla = int(input("Enter marks of Bangla: "))

average = (english + mathematics + phycics + biology + history + islam + bangla) / 7

if average >= 90:
    print("Grade A+")
elif average >= 80:
    print("Grade A")
elif average >= 70:
    print("Grade A-")
elif average >= 60:
    print("Grade B")
elif average >= 50:
    print("Grade C")
elif average >= 40:
    print("Grade D")
else:
    print("Fail")





english = int(input("Enter the marks of English: "))
bangla = int(input("Enter the marks of Bangla: "))
history = int(input("Enter the marks of History: "))
chemistry = int(input("Enter the marks of Chemictry: "))
physics = int(input("Enter the marks of Physics: "))
math = int(input("Enter the marks of Math: "))

average = (english + bangla + history + chemistry + physics + math) / 6

if average >= 80 and average <= 100:  # ekhane average er man jodi 80 er cheye soman/boro hoy ebong average er man jodi 100 er cheye soman/choto hoy tahole A+ print korbe
    print("A+")
elif average >= 70 and average <= 79: # thik same vabe average er man jodi 70 er soman/boro hoy ebong average er man jodi 79 er soman/choto hoy tahole A print korbe
    print("A")
elif average >= 60 and average <= 69:
    print("A-")
elif average >= 50 and average <= 59:
    print("B")
elif average >= 40 and average <= 49:
    print("C")
elif average >= 33 and average <= 39:
    print("D")
else:
    print("Oh! You are fail.")




# markOne = int(input("Enter marks1: "))
# markTwo = int(input("Enter marks2: "))
# markThree = int(input("Enter marks3: "))
# markFour = int(input("Enter marks4: "))
# markFive = int(input("Enter marks6: "))
#
# tot = markOne + markTwo + markThree + markFour + markFive
# avg = tot / 5
#
# if avg>=91 and avg<=100:
#     print("Your Grade is A1")
# elif avg>=81 and avg<91:
#     print("Your Grade is A2")
# elif avg>=71 and avg<81:
#     print("Your Grade is B1")
# elif avg>=61 and avg<71:
#     print("Your Grade is B2")
# elif avg>=51 and avg<61:
#     print("Your Grade is C1")
# elif avg>=41 and avg<51:
#     print("Your Grade is C2")
# elif avg>=33 and avg<41:
#     print("Your Grade is D")
# elif avg>=21 and avg<33:
#     print("Your Grade is E1")
# elif avg>=0 and avg<21:
#     print("Your Grade is E2")
# else:
#     print("Invalid Input!")





