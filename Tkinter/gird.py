
# from tkinter import *
# myDesign = Tk()

# myDesign.title("About Phone")
# myDesign.geometry("500x300")

# brand = Label(myDesign, text="Brand")
# model = Label(myDesign, text="Model")
# brand.grid()
# model.grid(row=1)

# myDesign.mainloop()



# from tkinter import *

# root = Tk()
# root.title("Courses")

# Python = Button(root, text="Python", width=8)
# Cpp = Button(root, text="C++", width=8)
# Java = Button(root, text="Java", width=8)
# JavaScript = Button(root, text="JavaScript", width=8)

# Python.grid(row=0, column=0)
# Cpp.grid(row=0, column=1)
# Java.grid(row=1, column=0)
# JavaScript.grid(row=1, column=1)

# root.mainloop()



from tkinter import *
root = Tk()

root.geometry("450x300")
root.minsize(200, 100)
root.title("We provide all language")

python = Label(root, text="Python", width=7)
java = Label(root, text="Java", width=7)
c = Label(root, text="C", width=7)
dart = Label(root, text="Dart", width=7)
kotlin = Label(root, text="Kotlin", width=7)
cpp = Label(root, text="C++", width=7)

python.grid(row=0, column=0)
java.grid(row=0, column=1)
c.grid(row=1, column=0)
dart.grid(row=1, column=1)
kotlin.grid(row=2, column=0)
cpp.grid(row=2, column=1)

root.mainloop()
