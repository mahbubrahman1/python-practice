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