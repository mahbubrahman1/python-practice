# def myFunction():
#
#     def output():
#         print("Hello! World.")
#
#     return output
#
# show = myFunction()
# show()


# def myWrapper(myFunction):
#     def testFunction():
#         print("Computer Engineering")
#         print("Architectural Engineering")
#         print("Mechanical Engineering")

#         myFunction()
#
#     return testFunction
#
# def hard():
#     print("it's so hard!")
#
# hard = myWrapper(hard)
# hard()


"""
def helloDecorator(func):
    def inner1():
        print("Hello, this is before function execution")

        func()

        print("This is after function execution")

    return inner1

def functionToBeUsed():
    print("This is inside the function!!")

functionToBeUsed = helloDecorator(functionToBeUsed)

functionToBeUsed()
"""


"""
# decorator
def myWrapper(myFunction):
    def testFunction():
        print("Computer Engineering")
        print("Architectural Engineering")
        
        myFunction()
        
        print("Mechanical Engineering")

    return testFunction

@myWrapper
def hard():
    print("it's so hard!")  

hard()
"""


def helloDecorator(func):
    def inner1():
        print("Hello, this is before function execution")
        print("This is after function execution")

        func()

    return inner1

@helloDecorator
def functionToBeUsed():
    print("This is inside the function!!")

functionToBeUsed()