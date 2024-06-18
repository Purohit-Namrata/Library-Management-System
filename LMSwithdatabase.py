import tkinter as tk
from tkinter import messagebox
import csv
import os
import re
 
def add_book():
    book_id = book_id_entry.get()
    book_title = book_title_entry.get()
    book_author = book_author_entry.get()

    if not re.match(r"^[0-9]$",book_id):
          messagebox.showinfo("Error","Please enter valid Book id")
          return
    if not re.match(r"^[A-Za-z\s]+$",book_title):
          messagebox.showinfo("Error", "Please enter a valid book name")
          return
    if not re.match(r"^[A-Za-z\s]+$",book_author):
          messagebox.showinfo("Error", "Please enter a valid author name")
          return

    if book_id == "" or book_title == "" or book_author == "":
        messagebox.showerror("Error", "Please fill all the fields!")
    else:
        with open("library.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([book_id, book_title, book_author])
        messagebox.showinfo("Success", "Book added successfully!")
        clear_textboxes()
 
def view_books():
    if os.path.exists("library.csv"):
        with open("library.csv", "r") as file:
            reader = csv.reader(file)
            books = [row for row in reader]
            if books:
                books_info = "\n".join(["ID: {}, Title: {}, Author: {}".format(*book) for book in books])
                messagebox.showinfo("Books List", books_info)
            else:
                messagebox.showinfo("Books List", "No books found.")
    else:
        messagebox.showinfo("Books List", "The library is empty.")
 
def search_book():
    search_value = search_entry.get()

    messagebox.showinfo("Info","Enter Book id to search")
    if not re.match(r"^[0-9]{100}$",search_value):
          messagebox.showinfo("Error","Please enter valid Book id")
          return
 
    if os.path.exists("library.csv"):
        with open("library.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if search_value in row:
                    messagebox.showinfo("Book Details", f"Book ID: {row[0]}\nTitle: {row[1]}\nAuthor: {row[2]}")
                    clear_searchbox()
                    return
            messagebox.showerror("Error", "Book not found!")
            clear_searchbox()
    else:
        messagebox.showinfo("Books List", "The library is empty.")
 
def clear_textboxes():
    book_id_entry.delete(0, tk.END)
    book_title_entry.delete(0, tk.END)
    book_author_entry.delete(0, tk.END)
 
def clear_searchbox():
    search_entry.delete(0, tk.END)
 
# Create the main window
window = tk.Tk()
window.title("Library Management System")
window.geometry("600x400")
 
# Create labels and entry boxes
title_label = tk.Label(window, text="Library Management System", font=("Arial", 18))
title_label.grid(row=0, column=1, padx=10, pady=10)
 
book_id_label = tk.Label(window, text="Book ID")
book_id_label.grid(row=1, column=0, padx=10, pady=10)
 
book_id_entry = tk.Entry(window)
book_id_entry.grid(row=1, column=1, padx=10, pady=10)
 
book_title_label = tk.Label(window, text="Book Title")
book_title_label.grid(row=2, column=0, padx=10, pady=10)
 
book_title_entry = tk.Entry(window)
book_title_entry.grid(row=2, column=1, padx=10, pady=10)
 
book_author_label = tk.Label(window, text="Author")
book_author_label.grid(row=3, column=0, padx=10, pady=10)
 
book_author_entry = tk.Entry(window)
book_author_entry.grid(row=3, column=1, padx=10, pady=10)
 
search_label = tk.Label(window, text="Search Book")
search_label.grid(row=4, column=0, padx=10, pady=10)
 
search_entry = tk.Entry(window)
search_entry.grid(row=4, column=1, padx=10, pady=10)
 
# Create buttons
add_button = tk.Button(window, text="Add Book", command=add_book)
add_button.grid(row=5, column=0, padx=10, pady=10)
 
view_button = tk.Button(window, text="View Books", command=view_books)
view_button.grid(row=5, column=1, padx=10, pady=10)
 
search_button = tk.Button(window, text="Search Book", command=search_book)
search_button.grid(row=5, column=2, padx=10, pady=10)
 
clear_button = tk.Button(window, text="Clear", command=clear_textboxes)
clear_button.grid(row=5, column=3, padx=10, pady=10)
 
# Run the main loop
window.mainloop()
 