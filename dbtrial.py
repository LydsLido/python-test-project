
import tkinter as tk
import sqlite3
from tkinter import messagebox

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("form_data.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    age INTEGER
)
""")
conn.commit()

# Function to submit form data to the database
def submit_form():
    data = [entry.get() for entry in entries]
    
    # Insert data into the database
    cursor.execute("INSERT INTO users (name, email, phone, address, age) VALUES (?, ?, ?, ?, ?)", data)
    conn.commit()
    
    messagebox.showinfo("Success", "Data submitted successfully!")
    
    # Clear the form
    for entry in entries:
        entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("User Form")
root.geometry("400x300")

# Labels and Entry fields
labels_text = ["Name", "Email", "Phone", "Address", "Age"]
entries = []

for i, text in enumerate(labels_text):
    label = tk.Label(root, text=text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    
    entry = tk.Entry(root, width=30)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.grid(row=len(labels_text), column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()

# Close the database connection when done (optional, if you want to handle it later)
# conn.close()
