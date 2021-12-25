
def compound_interest(principle, rate, time):
    amount = principle * (1+rate/100) ** time
    CI = amount - principle
    return CI

principle = int(input("Enter principle amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time: "))

total = compound_interest(principle, rate, time)
print("Compound Interest is", total)




def compound_interest(principle, rate, time):
    amount = principle * (1 + rate / 100) ** time 
    ci = amount - principle
    return ci

principle = int(input("Enter the amount: "))
rate = int(input("Enter the rate: "))
time = int(input("Enter the time: "))





def compound_interest(principle, rate, time):
    amount = principle * (1 + rate/100) ** time
    ci = amount - principle
    return ci

principle = int(input("Enter the principle amount: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the time: "))

total = compound_interest(principle, rate, time)
print("Compound Interest =", total)





def compound_interest(principle, rate, time):
    print("Principle Amount =", principle)
    print("Rate of interest =", rate)
    print("Time =", time)

    amount = principle * (1 + rate/100) ** time
    ci = amount - principle
    print("Compound Interest is", ci)

compound_interest(10000, 5, 4)