
# - Check palindrome sting



string = input("Enter string: ")

result = string[-1::-1]

if(string == result):
    print("It's Palindrome string")
else:
    print("It's not Palondrome string")



string = "mahbuburrahman"

def isitPalindrome(string):
    return string == string[-1::-1]
    
ans = isitPalindrome(string)

if ans:
    print("It's palindrome string")
else:
    print("It's not palindrome string")


# for more info please check this video: https://www.youtube.com/watch?v=iti83ge6ge4&t=237s&ab_channel=codeitup