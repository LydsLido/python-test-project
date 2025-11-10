
import tkinter as tk
from tkinter import messagebox
import re  # Regular expressions for validation

# Function to validate email format
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Function to handle form submission
def submit_form():
    data = [entry.get() for entry in entries]
    email = data[1]  # Assuming Email is the second field

    if not is_valid_email(email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    messagebox.showinfo("Form Submitted", f"Entered Data:\n" + "\n".join(data))

# Create main window
root = tk.Tk()
root.title("Form with Email Validation")
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
