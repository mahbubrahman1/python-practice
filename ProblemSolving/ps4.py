

# - GCD in python


import math

x = math.gcd(60, 48)
print("The GCD of 60 & 48 is:", x)


u = math.gcd(3, 17)
print("The GCD of 3 & 17 is:", u)





def find_gcd(x, y):
    if y == 0:
        return x
    else:
        return find_gcd(y, x % y)

x = 60
y = 48

result = find_gcd(x, y)
print("GCD =", result)





def find_gcd(x, y):
   if y == 0:
       return x
   else:
       return find_gcd(y, x % y)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

result = find_gcd(x, y)
print("GCD =", result)





def find_hcf(e, f):
    if f == 0:
        return e
    else:
        return find_hcf(f, e % f)
    
e = 90
f = 47

result = find_hcf(e, f)
print("HCF is", result)



# more details:       https://www.youtube.com/watch?v=g3OEEztC1zQ&ab_channel=codeitup


