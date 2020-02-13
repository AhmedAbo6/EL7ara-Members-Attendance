import sqlite3
from tkinter import *
# import tkinter

root = Tk()
root.title("El7ara Members Attendance")

conn = sqlite3.connect("el7ara_members.db")

c = conn.cursor() 

c.execute("""CREATE TABLE IF NOT EXISTS members (
		name text,
		phone_number integer,
			)

	""")


entering_frame = LabelFrame(root,text="Entering", padx=20, pady=20)
entering_frame.pack(padx=30, pady=30)

l1 = Label(entering_frame, text="Name or Number: ")
e1 = Entry(entering_frame)
b1 = Button(entering_frame, text="Enter", command=None)

l1.grid(column=0, row=0)
e1.grid(column=1, row=0)
b1.grid(column=1, row=1)


view_frame = LabelFrame(root,text="existent", padx=20, pady=20)
view_frame.pack(padx=30, pady=30)
l2 = Label(view_frame, text=e1.get())
b2 = Button(view_frame, text="Leaving", command=None)
b2.grid(column=1, row=0)

l2.grid(column=0, row=0)


conn.close()
root.mainloop()