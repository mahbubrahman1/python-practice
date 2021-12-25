

lower_num = int(input("Enter lower range limit:"))
upper_num = int(input("Enter upper range limit:"))

for i in range(lower_num, upper_num+1):
   if i % 3 == 0 and i % 5==0:
      print(i)





start = int(input("start: "))
end = int(input("End: "))

for i in range(start, end+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)






num = int(input("Enter a number: "))
result = []

for i in range(num):
    if i % 3 == 0 and i % 5 == 0:
        result.append(i)
print(result)






def divisible(num):
    empty = []
    for i in range(num):
        if i % 3 == 0 and i % 5 == 0:
            empty.append(i)
    return empty

num = int(input("Enter you number: "))
result = divisible(num)
print(result, "this number are divisibel by 3 and 5")



def divisible(num):
    result = []
    for i in range(num):
        if i % 3 == 0 and i % 5 == 0:
            result.append(i)
    return result

num = int(input("How many numbers will end before that - "))
print(divisible(num))



num = int(input("Enter a number: "))
result = []

for i in range(num):
    if i % 3 == 0 and i % 5 == 0:
        result.append(i)
print(result)




def divisible(num):
    empty = []
    for i in range(num):
        if i % 3 == 0 and i % 5 == 0:
            empty.append(i)
    return empty
    
num = int(input("Enter your last number: "))
result = divisible(num)
print(result, "this number are divisibel by 3 and 5")





