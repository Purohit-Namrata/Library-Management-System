from tkinter import *
from tkinter import messagebox
import re

def addbook():
    info1=e1.get()
    info2=e2.get()
    info3=e3.get()
    if not re.match(r"^[0-9]{100}$",info1):
          messagebox.showinfo("Error","Please enter valid Book id")
          return
    if not re.match(r"^[A-Za-z\s]+$",info2):
          messagebox.showinfo("Error", "Please enter a valid book name")
          return
    if not re.match(r"^[A-Za-z\s]+$",info3):
          messagebox.showinfo("Error", "Please enter a valid author name")
          return
          
    messagebox.showinfo("Success","Book added successfully")

def searchbook():
    info1=e4.get()
    messagebox.showinfo("Info","Enter Book id to search")
    if not re.match(r"^[0-9]{100}$",info1):
          messagebox.showinfo("Error","Please enter valid Book id")
          return

def viewbook():
    pass

def clear():
    b4.config(e1.delete(0,END))
    b4.config(e2.delete(0,END))
    b4.config(e3.delete(0,END))
    b4.config(e4.delete(0,END))

root=Tk()
root.title("Library Management System")
root.minsize(width=400, height=400)
root.geometry('500x400')

lbl1=Label(root,text="Library Management System", bg="Light Blue",fg='Black', padx=20,pady=20,font=("Arial", 16, "bold"))
lbl1.pack()

Label(root, text="Book Id:").pack()
e1 = Entry(root)
e1.pack()

Label(root, text="Book Title:").pack()
e2 = Entry(root)
e2.pack()

Label(root, text="Book Author:").pack()
e3 = Entry(root)
e3.pack()

Label(root, text="Search Book(With id):").pack()
e4 = Entry(root)
e4.pack()

b1=Button(root,text="Add book",command=addbook)
b1.pack()
b2=Button(root,text="Search book",command=searchbook)
b2.pack()
b3=Button(root,text="View book",command=viewbook)
b3.pack()
b4=Button(root,text="Clear",command=clear)
b4.pack()
b5=Button(root,text="Exit",command=root.destroy)
b5.pack()

root.mainloop()
