
year = int(input("Enter the year: "))

if year % 400 == 0:
    print("It is leap year")
elif year % 100 == 0:
    print("It is not leap year")
elif year % 4 == 0:
    print("It is leap year")
else:
    print("It is not leap year")





year = int(input("Enter the year: "))

if year % 100 != 0 and year % 4 == 0:
    print("It is leap year")
elif year % 100 == 0 and year % 400 == 0:
    print("It is leap year")
else:
    print("It is not leap year")






def leap_year(year):
    
    if year % 400 == 0:
        print("It is leap year")

    elif year % 100 == 0:
        print("It is not leap year")

    elif year % 4 == 0:
        print("It is leap year")

    else:
        print("It is not leap year")

year = int(input("Enter the year: "))
leap_year(year)
