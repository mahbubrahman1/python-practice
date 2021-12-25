
def simple_interest(amount, rate, time):
    si = (amount * rate * time) / 100
    return si

amount = int(input("Enter the amount of interest: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time of interest: "))

total = simple_interest(amount, rate, time)
print("The simple interest is", total)




def simple_interest(amount, rate, time):
    print("Amount:", amount)
    print("Rate:", rate)
    print("Time:", time)

    si = (amount * rate * time) / 100
    return si

amount = 10000
rate = 5
time = 5

total = simple_interest(amount, rate, time)
print("Total Simple Interest", total)