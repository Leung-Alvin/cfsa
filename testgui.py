import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
import prompt
import random
#function to be called when the button is clicked
#def on_button_click():
    #messagebox.showinfo("Hello World")
#create the main window

# root = tk.Tk()
# root.geometry("1600x1200")
# #Set the window Title
# root.title("CFSA Prototype")

# CyberFont = Font(
#     family = "Verdana",
#     size = 42,
#     weight = "bold",
#     slant = "roman",
# )
# #setting background color


# root.configure(bg="lightblue")
# #CFSA Title Widget
# label = tk.Label(root, text="CFSA Demo", font = CyberFont, bg="lightblue", pady=10)

# label.place(x = 800, y = 300)

# #button = tk.Button(root, text="Click Me, ", command = on_button_click)
# #button.pack()

  

   

def main(): 
 
    # root.mainloop()
    frame = tk.Tk() 
    frame.title("TextBox Input") 
    frame.geometry('1600x1200') 
    # Function for getting Input 
    # from textbox and printing it  
    # at label widget 
    prompts = prompt.get_prompts()
    pmt = tk.Label(frame, text=random.choice(prompts))
    pmt.pack()
    def printInput(): 
        inp = inputtxt.get(1.0, "end-1c") 
        lbl.config(text = "Provided Input: "+inp) 
    # TextBox Creation 
    inputtxt = tk.Text(frame, 
                    height = 50, 
                    width = 75) 
    
    inputtxt.pack() 
    
    # Button Creation 
    printButton = tk.Button(frame, 
                            text = "Predict",  
                            command = printInput) 
    printButton.pack() 
    
    # Label Creation 
    lbl = tk.Label(frame, text = "") 
    lbl.pack() 
    frame.mainloop()