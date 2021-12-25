
# from tkinter import *

# root = Tk()

# root.geometry("750x500")

# root.title("Notepad")

# root.iconbitmap("Tkinter/notes.ico")

# # file menu
# mainmenu = Menu(root)
# me1 = Menu(mainmenu, tearoff=0)
# me1.add_command(label="New")
# me1.add_command(label="New Window")
# me1.add_command(label="Open...")
# me1.add_command(label="Save")
# me1.add_command(label="Save As...")
# me1.add_separator()
# me1.add_command(label="Page Setup...")
# me1.add_command(label="Print...")
# me1.add_separator()
# me1.add_command(label="Exit")
# root.config(menu=mainmenu)
# mainmenu.add_cascade(label="File", menu=me1)

# # edit menu
# me2 = Menu(mainmenu, tearoff=0)
# me2.add_command(label="Undo")
# me2.add_command(label="Redo")
# me2.add_separator()
# me2.add_command(label="Cut")
# me2.add_command(label="Copy")
# me2.add_command(label="Paste")
# me2.add_command(label="Delete")
# me2.add_separator()
# me2.add_command(label="Find...")
# me2.add_command(label="Replace...")
# me2.add_command(label="Go To...")
# root.config(menu=mainmenu)
# mainmenu.add_cascade(label="Edit", menu=me2)

# # format menu
# me3 = Menu(mainmenu, tearoff=0)
# me3.add_command(label="Word Warp")
# me3.add_command(label="Font...")
# root.config(menu=mainmenu)
# mainmenu.add_cascade(label="Format", menu=me3)

# # view menu
# me4 = Menu(mainmenu, tearoff=0)
# me4.add_command(label="Zoom")
# me4.add_command(label="Status Bar")
# root.config(menu=mainmenu)
# mainmenu.add_cascade(label="View", menu=me4)

# # help menu
# me5 = Menu(mainmenu, tearoff=0)
# me5.add_command(label="View Help")
# me5.add_command(label="Send Feedback")
# me2.add_separator()
# me5.add_command(label="About Notepad")
# root.config(menu=mainmenu)
# mainmenu.add_cascade(label="Help", menu=me5)

# root.mainloop()

from tkinter import *
 
def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand =YES, fill =BOTH)
    return storeObj
 
def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand = YES, fill=BOTH)
    return storeObj
 
class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand = YES, fill =BOTH)
        self.master.title('Calculator')
 
        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,
          justify='right'
          , bd=30, bg="powder blue").pack(side=TOP,
                                          expand=YES, fill=BOTH)
 
        for clearButton in (["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda
                    storeObj=display, q=ichar: storeObj.set(''))
 
        for numButton in ("789/", "456*", "123-", "0.+"):
         FunctionNum = iCalc(self, TOP)
         for iEquals in numButton:
            button(FunctionNum, LEFT, iEquals, lambda
                storeObj=display, q=iEquals: storeObj
                   .set(storeObj.get() + q))
 
        EqualButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self,
                                storeObj=display: s.calc(storeObj), '+')
 
 
            else:
                btniEquals = button(EqualButton, LEFT, iEquals,
                                    lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                                    (storeObj.get() + s))
 
    def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")
 
 
if __name__=='__main__':
 app().mainloop()