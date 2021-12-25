

def reverse_string(string):
    
    reverse = " "
    for char in string:
        reverse = char + reverse
    return reverse

string = input("Enter your string: ")
print(reverse_string(string))





def sumofelements(my_list):

    sum = 0
    for i in my_list:
        sum = sum + i
    return sum
my_list = [4, 5, 6, 3, 8, 9]

print(sumofelements(my_list))




# almost sum of elements er moto. 
# justs sum = sum + i er jaygay ami 
# reverse = i + reverse kore dichi cause eita toh ulta bhabe jug korte hobe



















