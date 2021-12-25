
p = int(input("Enter the principle amount: "))
r = float(input("Enter the rate: "))
t = float(input("Enter the time: "))

amount = (p*(1+r/100)**t)
ci = amount - p
print("Compound Interest = %0.2f" % ci)





def compound_interest(principle, rate, time):

    print("Principle amount:", principle)
    print("Rate of interest:", rate)
    print("Time the money is invested:", time)

    amount = (principle*(1+rate/100)**time)
    ci = amount - principle
    return ci

principle = 600000
rate = 6
time = 3
total = compound_interest(principle, rate, time)
print("Compound Interest = %0.2f" % total)
