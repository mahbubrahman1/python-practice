# open a file
# file = open("myfile.txt", "w")

# getting some informations
# print("File name: ", file.name)
# print("Is it closed? Answer:", file.closed)
# print("Which Mode? Answer:", file.mode)

# write something on file
# file.write("Python and Java is my favorite language. They are super powerful language.")
# file.close()

# appending text on file
# file = open("myfile.txt", "a")
# file.write("Python use in AI, Machine Learning etc")
# file.close()

# uses of r+ (reading and writing)
# file = open("myfile.txt", "r+")
# my_text = file.read()
# print(my_text)

# amar jodi specific jotota letter lage
# file = open("myfile.txt", "r+")
# my_text = file.read(10)
# print(my_text)
# file.close()

# uses of w+ (only read and write)
file = open("myfile.txt", "w")
file.write("lost all!!")
file.close()