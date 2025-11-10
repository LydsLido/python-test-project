
import tkinter as tk
from tkinter import messagebox

#### Lydias comments for understanding: tkinter is Python’s standard GUI library.
#### Lydias comments for understanding: messagebox is a submodule used to show popup dialogs (like alerts or info boxes).

# Function to handle form submission
def submit_form():
    data = [entry.get() for entry in entries]
    messagebox.showinfo("Form Submitted", f"Entered Data:\n" + "\n".join(data))
#### Lydias comments for understanding:submit_form() is called when the user clicks the Submit button.
#### Lydias comments for understanding:entry.get() retrieves the text from each input field.
#### Lydias comments for understanding:messagebox.showinfo() displays the collected data in a popup window.


# Create main window
root = tk.Tk()
root.title("Simple Form")
root.geometry("400x300")
#### Lydias comments for understanding: tk.Tk() initializes the main window.
#### Lydias comments for understanding: title() sets the window title.
#### Lydias comments for understanding: geometry() sets the window size to 400 pixels wide and 300 pixels tall.

# Labels and Entry fields
labels_text = ["Name", "Email", "Phone", "Address", "Age"]
entries = []

#### Lydias comments for understanding: labels_text is a list of field names.
#### Lydias comments for understanding: entries will store the Entry widgets (text fields) for later access.

for i, text in enumerate(labels_text):
    label = tk.Label(root, text=text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    
    entry = tk.Entry(root, width=30)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

#### Lydias comments for understanding:enumerate() gives both index i and label text text.
#### Lydias comments for understanding:tk.Label() creates a label widget.
#### Lydias comments for understanding:grid() places the label in row i, column 0, with padding.

#### Lydias comments for understanding:sticky="e" aligns the label to the right (east).

#### Lydias comments for understanding:tk.Entry() creates a text input field.
#### Lydias comments for understanding:grid() places the entry next to the label in column 1.
#### Lydias comments for understanding:Each entry is stored in the entries list for later use.
    
# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.grid(row=len(labels_text), column=0, columnspan=2, pady=20)


#### Lydias comments for understanding: tk.Button() creates a button labeled "Submit".
#### Lydias comments for understanding: command=submit_form links the button to the function.
#### Lydias comments for understanding: grid() places the button below all fields.
#### Lydias comments for understanding: row=len(labels_text) ensures it’s in the next row.
#### Lydias comments for understanding: columnspan=2 makes the button span across both columns.

# Run the application
root.mainloop()
#### Lydias comments for understanding: This keeps the window open and responsive to user actions.