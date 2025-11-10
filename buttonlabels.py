
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Three Buttons and Labels")
root.geometry("300x300")

# Create labels
label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
label3 = tk.Label(root, text="Label 3")

# Create buttons
button1 = tk.Button(root, text="Button 1", command=lambda: label1.config(text="Button 1 clicked by Lydia"))
button2 = tk.Button(root, text="Button 2", command=lambda: label2.config(text="Button 2 clicked by Lydia"))
button3 = tk.Button(root, text="Button 3", command=lambda: label3.config(text="Button 3 clicked by Lydia"))

# Place widgets in the window
label1.pack(pady=5)
button1.pack(pady=5)
label2.pack(pady=5)
button2.pack(pady=5)
label3.pack(pady=5)
button3.pack(pady=5)

# Run the application
root.mainloop()
