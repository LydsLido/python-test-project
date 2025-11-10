import tkinter as tk

root = tk.Tk()
root.title("Tkinter in VS Code")

label = tk.Label(root, text="Hello Lydia!")
label.pack()

button = tk.Button(root, text="Click Me", command=lambda: print("Button clicked"))
button.pack()

root.mainloop()
