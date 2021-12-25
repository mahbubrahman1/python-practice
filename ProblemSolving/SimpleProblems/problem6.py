

def cvowels(sentence):
    count = 0
    vowels = ["a","k","j","e","i","p"]
    for char in sentence:
        if char in vowels:
            count = count + 1
    return count
print(cvowels("Hello World"))
