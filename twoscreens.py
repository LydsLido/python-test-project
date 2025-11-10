
import tkinter as tk

# Function to switch to the second screen
def go_to_next_screen():
    screen1.pack_forget()  # Hide first screen
    screen2.pack(fill='both', expand=True)  # Show second screen

##Lyds: go_to_next_screen() is called when the user clicks the "Go to Screen 2" button.
##Lyds:pack_forget() hides screen1.
##Lyds:pack(fill='both', expand=True) displays screen2, making it fill the window.

# Function to go back to the first screen
def go_back():
    screen2.pack_forget()
    screen1.pack(fill='both', expand=True)
##Lyds: go_back() is called when the user clicks the "Back to Screen 1" button.
##Lyds: It hides screen2 and shows screen1 again.

# Create main window
root = tk.Tk()
root.title("Screen Navigation Example")
root.geometry("400x200")
##Lyds: tk.Tk() initializes the main application window.
##Lyds: title() sets the window title.
##Lyds: geometry() sets the window size to 400x200 pixels.

# First screen
screen1 = tk.Frame(root)
label1 = tk.Label(screen1, text="Welcome to Screen 1", font=("Arial", 14))
next_button = tk.Button(screen1, text="Go to Screen 2", command=go_to_next_screen)
##Lyds: screen1 is a Frame widget that acts as the first screen.
##Lyds: label1 is a label displayed on screen1.
##Lyds: next_button is a button that triggers go_to_next_screen() when clicked.

label1.pack(pady=20)
next_button.pack()
screen1.pack(fill='both', expand=True)
##Lyds: pack() places the label and button vertically.
##Lyds: pady=20 adds vertical spacing.
##Lyds: screen1.pack() makes the first screen visible initially.

# Second screen
screen2 = tk.Frame(root)
label2 = tk.Label(screen2, text="This is Screen 2", font=("Arial", 14))
back_button = tk.Button(screen2, text="Back to Screen 1", command=go_back)
##Lyds: screen2 is another Frame widget for the second screen.
##Lyds: label2 and back_button are placed on this screen.
##Lyds: back_button calls go_back() when clicked.

label2.pack(pady=20)
back_button.pack()
##Lyds: These widgets are packed but not shown initially because screen2.pack() is not called until navigation happens.

# Run the application
root.mainloop()
##Lyds: This starts the Tkinter event loop, keeping the window open and responsive.