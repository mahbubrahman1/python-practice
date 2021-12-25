
# from tkinter import *

# pych = Tk()

# pych.title("PyCharm")
# pych.geometry("500x400")
# pych.minsize(300, 200)

# pyText = Label(pych, text="The Python IDE for Professional Developers")
# pyText.pack()
# download = Button(pych, text="Download Now")
# download.pack()

# pych.mainloop()




from tkinter import *

pych = Tk()

pych.title("PyCharm")
pych.geometry("500x400")
pych.minsize(300, 200)

pyText = Label(pych, text="The Python IDE for Professional Developers")
pyText.pack()
download = Button(pych, text="Download Now", bd=3, bg="red", fg="white") # bd means buttons size
download.pack()

pych.mainloop()