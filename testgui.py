import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

\
#function to be called when the button is clicked
#def on_button_click():
    #messagebox.showinfo("Hello World")
#create the main window
root = tk.Tk()
root.geometry("1600x1200")
#Set the window Title
root.title("CFSA Prototype")

CyberFont = Font(
    family = "Verdana",
    size = 42,
    weight = "bold",
    slant = "roman",
)
#setting background color


root.configure(bg="lightblue")
#CFSA Title Widget
label = tk.Label(root, text="CFSA Demo", font = CyberFont, bg="lightblue", pady=10)

label.place(x = 800, y = 300)

#button = tk.Button(root, text="Click Me, ", command = on_button_click)
#button.pack()

root.mainloop()