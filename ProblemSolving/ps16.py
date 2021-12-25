
# - Check all prime numbers


start = int(input("Start from here: "))
end = int(input("End: "))

for i in range(start, end + 1):
    if i > 1:

        for x in range(2, i):
            if i % x == 0:
                break
        else:
            print(i)

 




def all_prime(start, end):
    for i in range(start, end + 1):
        if i > 0:

            for x in range(2, i):
                if i % x == 0:
                    break
            else:
                print(i)

start = int(input("Start: "))
end = int(input("End: "))
all_prime(start, end)
