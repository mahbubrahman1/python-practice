
string = "geek" # user input dileo hobe
result = string[-1::-1]

if string == result:
    print("It is palindrome string")
else:
    print("It is not palindrome string")




def palindrome(string):
    return string == string[-1::-1]

string = "madam"
ans = palindrome(string)

if ans:
    print("It is palindrome string")
else:
    print("It is not palindrome string")


    