
import tkinter as tk
import sqlite3
from  tkinter import messagebox
conn = sqlite3.connect("form_data.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")
conn.commit()

# Submit data
def submit_data():
    name = name_entry.get()
    age = age_entry.get()
    if name and age.isdigit():
        cursor.execute("INSERT INTO user_data (name, age) VALUES (?, ?)", (name, int(age)))
        conn.commit()
        messagebox.showinfo("Success", "Data submitted successfully!")
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter valid name and age.")

# Read and print data with 77 appended
def read_data():
    cursor.execute("SELECT name, age FROM user_data")
    rows = cursor.fetchall()
    for name, age in rows:
        print(f"{name}77", f"{age + 77}")

# GUI setup
root = tk.Tk()
root.title("Form to Database")
root.geometry("300x200")

tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Age:").pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

tk.Button(root, text="Submit", command=submit_data).pack(pady=10)
tk.Button(root, text="Read and Print", command=read_data).pack(pady=5)

root.mainloop()
conn.close()

