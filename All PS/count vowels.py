
sentence = "i love you, do you love me?"
vowels = ["a", "e", "i", "o", "u"]
c = 0

for x in sentence:
    if x in vowels:
        c = c + 1  # c =+ 1
print(c)



sentence = "I Love You, Do You Love ME"
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] # capital and small latters use korlam arki jodi sentence a capital or small latter thake
c = 0

for i in sentence:
    if i in vowels:
        c += 1
print(c)





def count_vowels(sentence):
    c = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in sentence:
        if i in vowels:
            c += 1
    return c
    
sentence = input("Enter the sentence: ")
result = count_vowels(sentence)
print("Total vowels in this sentence", result)






















