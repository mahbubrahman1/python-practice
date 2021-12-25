# from tkinter import *

# myRoot = Tk()
# myRoot.title("First Tkinter")
# myRoot.geometry("500x400")
# myRoot.minsize(300,150)
# myRoot.mainloop()


# from tkinter import *

# data = Tk()

# data.title("Mahbubur Rahman")
# data.geometry("500x400")
# data.minsize(300, 200)
# Department = Label(data, text="Computer Science and Technology", bg="red", fg="white")
# Department.pack()

# data.mainloop()


# from tkinter import *

# pych = Tk()

# #design
# pych.title("Pycharm Community Edition")
# pych.geometry("733x434")
# pych.minsize(300, 200)
# pyText = Label(pych, text="It is the best IDE for developer", bg="gray", fg="white")
# pyText.pack()

# pych.mainloop()



# from tkinter import *
# pych = Tk()

# #design
# pych.title("PyCharm")
# pych.geometry("500x400")
# pych.minsize(300, 200)
# pyText = Label(pych, text="The Python IDE for Professional Developers")
# pyText.pack()
# install = Button(pych, text="Download Now", bd=3)
# install.pack()

# pych.mainloop()

# from tkinter import *

# phone = Tk()

# #design
# phone.title("iPhone 7+")
# phone.geometry("400x200")
# phone.minsize(250, 200)
# add = Label(phone, text="Let's meet to new iPhone")
# add.pack()
# buy = Button(phone, text="Buy Now", bd=3, bg="green")
# buy.pack()
# phone.mainloop()



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


# from tkinter import *
# root = Tk()

# root.geometry("450x300")
# root.minsize(200, 100)
# root.title("We provide all language")

# python = Label(root, text="Python", width=7)
# java = Label(root, text="Java", width=7)
# c = Label(root, text="C", width=7)
# dart = Label(root, text="Dart", width=7)
# kotlin = Label(root, text="Kotlin", width=7)
# cpp = Label(root, text="C++", width=7)

# python.grid(row=0, column=0)
# java.grid(row=0, column=1)
# c.grid(row=1, column=0)
# dart.grid(row=1, column=1)
# kotlin.grid(row=2, column=0)
# cpp.grid(row=2, column=1)

# root.mainloop()



# from tkinter import *
# root = Tk()

# n = Label(root, text="Name")
# info = Entry(root)

# n.grid(row=0, column=0)
# info.grid(row=0, column=1)

# root.mainloop()



# from tkinter import *

# root = Tk()

# # shape
# root.geometry("400x200")
# root.minsize(200, 100)

# # title
# root.title("Laptop Brand")

# # text & button
# Brand1 = Label(root, text="Asus")
# Brand1.grid()
# Brand1 = Button(root, text="Visit Store", bd=3)
# Brand1.grid()

# Brand2 = Label(root, text="Apple")
# Brand2.grid(column=1, row=0)
# Brand2 = Button(root, text="Visit Store", bd=3)
# Brand2.grid(column=1, row=1)

# Brand3 = Label(root, text="Dell")
# Brand3.grid(column=2, row=0)
# Brand3 = Button(root, text="Visit Store", bd=3)
# Brand3.grid(column=2, row=1)

# Brand4 = Label(root, text="Lenovo")
# Brand4.grid(column=3, row=0)
# Brand4 = Button(root, text="Visit Store", bd=3)
# Brand4.grid(column=3, row=1)

# Brand5 = Label(root, text="Samsung")
# Brand5.grid(column=4, row=0)
# Brand5 = Button(root, text="Visit Store", bd=3)
# Brand5.grid(column=4, row=1)

# Brand6 = Label(root, text="HP")
# Brand6.grid(column=5, row=0)
# Brand6 = Button(root, text="Visit Store", bd=3)
# Brand6.grid(column=5, row=1)

# root.mainloop()


# from tkinter import *
# from PIL import ImageTk, Image

# myRoot = Tk()

# myImage = Image.open("Tkinter/img3.jpg")
# picture = ImageTk.PhotoImage(myImage)
# lal = Label(myRoot, image=picture)
# lal.pack()

# myRoot.mainloop()

# from tkinter import *
# from PIL import ImageTk, Image

# root = Tk()

# add_picture = Image.open("Tkinter/img2.jpg")
# my_picture = ImageTk.PhotoImage(add_picture)
# lbl = Label(root, image=my_picture)
# lbl.pack()

# root.mainloop()


# from tkinter import *
# from PIL import ImageTk, Image

# my_root = Tk()

# #title
# my_root.title("My Image")

# #add picture
# my_picture = Image.open("Tkinter/img1.jpg")
# add_picture = ImageTk.PhotoImage(my_picture)
# lbl = Label(my_root, image=add_picture)
# lbl.pack()

# my_root.mainloop()



# from tkinter import *

# root = Tk()

# # size
# root.geometry("1280x720")
# root.minsize(300, 150)

# # title
# root.title("YouTube")

# # frame
# f1 = Frame(root, bg="grey", borderwidth=5, relief=SUNKEN)
# f1.pack(side=LEFT, fill=Y)

# f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
# f2.pack(side=TOP, fill=X)

# # text
# txt = Label(f1, text="youtube.com")
# txt.pack(pady=300)

# txt = Label(f2, text="Welcome to YouTube", font="Roboto", fg="red", pady=22)
# txt.pack()

# root.mainloop()


# from tkinter import *

# my_root = Tk()

# def Out():
#     print("Enroll Successfully")

# my_root.geometry("500x300")

# but = Button(text="Enroll Now", bd=3, command=Out)
# but.pack()

# my_root.mainloop()





# from tkinter import *

# root = Tk()

# # size
# root.geometry("600x300")

# # title
# root.title("Online Mobile Shop")

# # button result
# def n20u():
#     print("You bought Samsung Galaxy Note20 Ultra")

# def s21u():
#     print("You bought Samsung Galaxy S21 Ultra")

# def n10l():
#     print("You bought Samsung Galaxy Note10 Lite")

# def s20p():
#     print("You bought Samsung Galaxy S20 Plus")

# def s10():
#     print("You bought Samsung Galaxy S10")

# def s20fe():
#     print("You bought Samsung Galaxy S20 Fan Edition")

# # text & button
# p = Label(text="Galaxy Note20 Ultra")
# p.pack()
# p = Button(text="Buy Now", command=n20u)
# p.pack()

# p2 = Label(text="Galaxy S21 Ultra")
# p2.pack()
# p2 = Button(text="Buy Now", command=s21u)
# p2.pack()

# p3 = Label(text="Galaxy Note10 Lite")
# p3.pack()
# p3 = Button(text="Buy Now", command=n10l)
# p3.pack()

# p4 = Label(text="Galaxy S20 Plus")
# p4.pack()
# p4 = Button(text="Buy Now", command=s20p)
# p4.pack()

# p5 = Label(text="Galaxy S10")
# p5.pack()
# p5 = Button(text="Buy Now", command=s10)
# p5.pack()

# p6 = Label(text="Galaxy S20FE")
# p6.pack()
# p6 = Button(text="Buy Now", command=s20fe)
# p6.pack()

# root.mainloop()






# from tkinter import *

# root = Tk()

# # size
# root.geometry("600x600")

# # title
# root.title("Online Mobile Shop")

# # button result
# def n20u():
#     output["text"] = "You bought Samsung Galaxy Note20 Ultra"

# def s21u():
#     output2["text"] = "You bought Samsung Galaxy S21 Ultra"

# def n10l():
#     output3["text"] = "You bought Samsung Galaxy Note10 Lite"

# def s20p():
#     output4["text"] = "You bought Samsung Galaxy S20 Plus"

# def s10():
#     output5["text"] = "You bought Samsung Galaxy S10"

# def s20fe():
#     output6["text"] = "You bought Samsung Galaxy S20FE"

# # text & button
# p = Label(text="Galaxy Note20 Ultra")
# p.pack()
# p = Button(text="Buy Now", bd=3, command=n20u)
# p.pack()
# output = Label()
# output.pack()

# p2 = Label(text="Galaxy S21 Ultra")
# p2.pack()
# p2 = Button(text="Buy Now", bd=3, command=s21u)
# p2.pack()
# output2 = Label()
# output2.pack()

# p3 = Label(text="Galaxy Note10 Lite")
# p3.pack()
# p3 = Button(text="Buy Now",bd=3, command=n10l)
# p3.pack()
# output3 = Label()
# output3.pack()

# p4 = Label(text="Galaxy S20 Plus")
# p4.pack()
# p4 = Button(text="Buy Now",bd=3, command=s20p)
# p4.pack()
# output4 = Label()
# output4.pack()

# p5 = Label(text="Galaxy S10")
# p5.pack()
# p5 = Button(text="Buy Now",bd=3, command=s10)
# p5.pack()
# output5 = Label()
# output5.pack()

# p6 = Label(text="Galaxy S20FE")
# p6.pack()
# p6 = Button(text="Buy Now",bd=3, command=s20fe)
# p6.pack()
# output6 = Label()
# output6.pack()

# root.mainloop()



# import builtins
# from tkinter import *

# root = Tk()

# root.geometry("600x400")

# f = Frame(root, borderwidth=5, bg="yellow", relief=SUNKEN)
# f.pack(side=LEFT, anchor=NW)

# b1 = Button(f, fg="green", text="enroll now")
# b1.pack(side=LEFT, padx=23)

# root.mainloop()



# from tkinter import *

# root = Tk()

# root.geometry("500x300")

# user = Label(text="Username:", font=("helvetica 10"))
# password = Label(text="Password:", font=("helvetica 10"))
# user.grid()
# password.grid(row=1)

# name_data = StringVar()
# pass_data = StringVar()
# name_enter = Entry(root, textvariable=name_data)
# pass_enter = Entry(root, textvariable=pass_data)
# name_enter.grid(row=0, column=1)
# pass_enter.grid(row=1, column=1)

# root.mainloop()




# from tkinter import *

# myRoot = Tk()

# myRoot.geometry("500x200")
# myRoot.minsize(200, 100)

# myRoot.title("My Information")

# def output():

#     print(f"Your Name: {name_info.get()}")
#     print(f"Your Roll: {roll_info.get()}")
#     print(f"Your Department: {department_info.get()}")

# name = Label(text="Name:", font=("helvetica 11"))
# roll = Label(text="Roll:", font=("helvetica 11"))
# department = Label(text="Department:", font=("helvetica 11"))
# name.grid(row=0)
# roll.grid(row=1)
# department.grid(row=2)

# name_info = StringVar()
# roll_info = StringVar()
# department_info = StringVar()
# name_enter = Entry(myRoot, textvariable=name_info)
# roll_enter = Entry(myRoot, textvariable=roll_info)
# department_enter = Entry(myRoot, textvariable=department_info)
# name_enter.grid(row=0, column=1)
# roll_enter.grid(row=1, column=1)
# department_enter.grid(row=2, column=1)

# Button(text="Submit", bd=2, command=output).grid()
# myRoot.mainloop()





# from tkinter import *

# root = Tk()

# root.geometry("500x300")

# design = Label(root, text="I am a Software Engineer at Google", font=("Helvetica 11"))
# design.grid(row=0, column=1)

# root.mainloop()


from tkinter import *

my_root = Tk()

my_root.geometry("260x280")

my_root.title("Student Information")

def submit():
    print("Your information submitted")

# heading
Label(my_root, text="M P I", font=("Roboto", 11, "bold"), pady=15).grid(row=0, column=4)

# text for our form
name = Label(my_root, text="Name")
roll = Label(my_root, text="Roll")
registration = Label(my_root, text="Registration")
department = Label(my_root, text="Department")
shift = Label(my_root, text="Shift")
session = Label(my_root, text="Session")

# pack text for our form
name.grid(row=2, column=1)
roll.grid(row=3, column=1)
registration.grid(row=4, column=1)
department.grid(row=5, column=1)
shift.grid(row=6, column=1)
session.grid(row=7, column=1)

# text from user
name_data = StringVar()
roll_data = StringVar()
registration_data = StringVar()
department_data = StringVar()
shift_data = StringVar()
session_data = StringVar()

# entries for our form
name_entry = Entry(my_root, textvariable=name_data)
roll_entry = Entry(my_root, textvariable=roll_data)
registration_entry = Entry(my_root, textvariable=registration_data)
department_entry = Entry(my_root, textvariable=department_data)
shift_entry = Entry(my_root, textvariable=shift_data)
session_entry = Entry(my_root, textvariable=session_data)

# pack text for our form
name_entry.grid(row=2, column=4)
roll_entry.grid(row=3, column=4)
registration_entry.grid(row=4, column=4)
department_entry.grid(row=5, column=4)
shift_entry.grid(row=6, column=4)
session_entry.grid(row=7, column=4)

# check button & pack
check_robo = Checkbutton(text="I am not robot!")
check_robo.grid(row=8, column=4)

Button(text="Submit", command=submit).grid(row=9, column=4)

my_root.mainloop()