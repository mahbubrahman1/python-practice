
# from tkinter import *
# from PIL import ImageTk, Image

# root = Tk()

# root.geometry("1200x720")
# oneImage = Image.open("Tkinter/img2.jpg")
# photo = ImageTk.PhotoImage(oneImage)

# lab = Label(root, image=photo)
# lab.pack()

# root.mainloop()



# from tkinter import *
# from PIL import ImageTk, Image

# root = Tk()

# add_Photo = Image.open("Tkinter/img4.jpg")
# my_Photo = ImageTk.PhotoImage(add_Photo)
# lbl = Label(root, image=my_Photo)
# lbl.pack()

# root.mainloop()




from tkinter import *
from PIL import ImageTk, Image

my_root = Tk()

# title
my_root.title("My Image")

# text
text = Label(my_root, text="Only My")
text.pack()

# add picture
my_picture = Image.open("Tkinter/img1.jpg")
add_picture = ImageTk.PhotoImage(my_picture)
lbl = Label(my_root, image=add_picture)
lbl.pack()

my_picture2 = Image.open("Tkinter/img2.jpg")
add_picture2 = ImageTk.PhotoImage(my_picture2)
lbl = Label(my_root, image=add_picture2)
lbl.pack()

my_root.mainloop()