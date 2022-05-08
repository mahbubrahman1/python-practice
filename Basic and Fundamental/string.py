# greating = "hello"
# print(len(greating))


# name = "Mahbub's"
# print(name)


# name = 'mahbub\'s'
# print(name)


# country = "Bangladesh"
# print(country[5])


# country = "Bangladesh"
# print(country[3])


# country = "Bangladesh"
# for i in country:
#     print(i)


"""
char = ['A', 'B', 'C', 'D']
char[0] = 'Z'
print(char)

country = "Bangladesh"
country[0] = 'x'
print(country)

ditiyotate error asbe. eta অনেকটা লিস্টের মতোই।
কিন্তু লিস্টের সঙ্গে একটি পার্থক্য হচ্ছে, আমরা চাইলে লিস্টের
কোনো উপাদান পরিবর্তন করতে পারি, স্ট্রিংয়ের ক্ষেত্রে সেটি সম্ভব নয়।
"""

# country = "Bangla" + "desh"
# print(country)


# country = "Bangladesh"
# country.find("Ban")
# print(country)


# text = " i am the boss"
# print(text.lstrip())


# text = "I am a programmer"
# words = text.split()
# print(words)


# text = "I am a programmer"
# for word in text:
#     print(word)


# start = "Developer"
# print(start.startswith("Dev"))


# start = "Programmer"
# print(start.startswith("mm"))


# end = "Developer"
# print(end.endswith("per"))


# name = "Mr. Jhon"
# if name.startswith("Mr."):
#     print("Good Morning Sir!")


# day = "Saturday"
# if day.startswith("Sat"):
#     print("Today is holyday")


str = "a quick brown for jumps over the lazy dog"
for c in "abcdefghijklmnopqrstuvwxyz":
    print(c, str.count(c))