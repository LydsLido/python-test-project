
import tkinter as tk

# Function to switch to the second screen
def go_to_next_screen():
    # Append "lyds" to each entry field
    for entry in entries:
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current_text + "lyds")
    
    screen1.pack_forget()
    screen2.pack(fill='both', expand=True)

# Function to go back to the first screen
def go_back():
    screen2.pack_forget()
    screen1.pack(fill='both', expand=True)

# Create main window
root = tk.Tk()
root.title("Screen Navigation with Data Update")
root.geometry("400x300")

# First screen with form
screen1 = tk.Frame(root)
labels_text = ["Field 1", "Field 2", "Field 3"]
entries = []

for i, text in enumerate(labels_text):
    label = tk.Label(screen1, text=text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    
    entry = tk.Entry(screen1, width=30)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

next_button = tk.Button(screen1, text="Go to Screen 2", command=go_to_next_screen)
next_button.grid(row=len(labels_text), column=0, columnspan=2, pady=20)

screen1.pack(fill='both', expand=True)

# Second screen
screen2 = tk.Frame(root)
label2 = tk.Label(screen2, text="This is Screen 2", font=("Arial", 14))
back_button = tk.Button(screen2, text="Back to Screen 1", command=go_back)

label2.pack(pady=20)
back_button.pack()

# Run the application
root.mainloop()
