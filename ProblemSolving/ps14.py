

# - Gravitation Force



mess1 = float(input("Enter the first mess: "))
mess2 = float(input("Enter the second mess: "))
r =  float(input("Enter the distance between the centres of the messes: "))

g = 6.673 * 10 ** -11
force = g * mess1 * mess2 / r ** 2

print("Gravitation force is", force)



mess1 = float(input("Enter the first mess: "))
mess2 = float(input("Enter the second mess: "))
r = float(input("Enter the distance of object: "))

g = 6.673 * (10 ** -11)
force = (g * mess1 * mess2) / (r ** 2)

print("Gravitation Force is %f Newton" % force)