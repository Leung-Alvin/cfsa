import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
import prompt
import random
import model
import numpy as np
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

  
def compare_with_database():
    frame = tk.Tk() 
    frame.title("Compare With Database") 
    frame.geometry('1600x1200') 
    # Function for getting Input 
    # from textbox and printing it  
    # at label widget 
    prompts = prompt.get_prompts()
    pmt = tk.Label(frame, text=random.choice(prompts))
    pmt.pack()
    def printInput():
        text = inputtxt.get("1.0", "end-1c")
        if text == "":
            messagebox.showinfo("Error", "Please enter text in the box.")
            return 
        lmao = model.predicto(text)
        lbl.config(text = lmao) 
    # TextBox Creation 
    inputtxt = tk.Text(frame, 
                    height = 50, 
                    width = 150) 
    
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


def compare_two_prints():
    result = False
    def submit():
        # model.clear_temp()
        value1 = entry1.get("1.0", "end-1c")  # Retrieve text from the first text box
        value2 = entry2.get("1.0", "end-1c")  # Retrieve text from the second text box
        
        length1 = len(value1)
        length2 = len(value2)
        
        if length1 == 0 or length2 == 0:
            messagebox.showinfo("Error", "Please enter text in both boxes.")
            return
        
        minimum_length = min(len(value1), len(value2))
        
        value1 = value1[:minimum_length]
        value2 = value2[:minimum_length]
        # with open('survey/temp_-_mundanely.txt', 'w') as f:
        #     f.write(str(value1))
        # prediction = model.predicto(value2)
        prediction_1 = model.predicto(value1)
        prediction_2 = model.predicto(value2)
        results_1 = prediction_1.split("\n")[1].replace("Candidates: ","").replace("[","").replace("]","").split(", ")[0].replace("'","")
        results_2 = prediction_2.split("\n")[1].replace("Candidates: ","").replace("[","").replace("]","").split(", ")[0].replace("'","")
        print(results_1, results_2)
        if results_1 == results_2:
            results = "The two prints are likely by the same author."
        else:
            results = "The two prints are likely by different authors."
        frame = tk.Tk() 
        frame.title("Two Print Results") 
        frame.geometry('400x300')
        label = tk.Label(frame, text=results)
        label.pack()

    # Create the main window
    root = tk.Tk()
    root.title("Compare Two Prints")

    prompts = prompt.get_prompts()
    text_1 = np.random.choice(prompts, replace = False)
    text_2 = np.random.choice(prompts, replace = False)
    # Create the first text box
    label1 = tk.Label(root, text=text_1)
    label1.grid(row=0, column=0, padx=100, pady=10, sticky="w")

    entry1 = tk.Text(root, height=20, width=100)
    entry1.grid(row=0, column=1, padx=10, pady=10)

    # Create the second text box
    label2 = tk.Label(root, text=text_2)
    label2.grid(row=1, column=0, padx=100, pady=10, sticky="w")

    entry2 = tk.Text(root, height=20, width=100)
    entry2.grid(row=1, column=1, padx=10, pady=10)

    # Create the submission button
    submit_button = tk.Button(root, text="Predict", command=submit)
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()  # Start the Tkinter event loop
# Start the Tkinter event loop
# root.mainloop()     
def main(): 
    # root.mainloop()
    frame = tk.Tk()
    frame.state('zoomed') 
    frame.title("CFSA Prototype")
    # frame.geometry('1600x1200')
    CyberFont = Font(
        family = "Verdana",
        size = 42,
        weight = "bold",
        slant = "roman",
    )    
    frame.configure(bg="lightblue")
    #CFSA Title Widget
    label = tk.Label(frame, text="CFSA Demo", font = CyberFont, bg="lightblue", pady=10)
    label.grid(row=1, column=0, padx=100, pady=10, sticky="w") 
    # Button Creation
     
    db_compare_button = tk.Button(frame, 
                            text = "Compare With Database",  
                            command = compare_with_database)
    db_compare_button.grid(row=1, column=1, columnspan=100, pady=10) 
    # db_compare_button.pack()
    
    compare_two_prints_button = tk.Button(frame, 
                            text = "Compare Two Prints",  
                            command = compare_two_prints)
    compare_two_prints_button.grid(row=2, column=1, columnspan=100, pady=10)  
    # compare_two_prints_button.pack()
    
    def quit():
        frame.destroy()
    
    quit_button = tk.Button(frame, 
                            text = "Quit Application",  
                            command = quit)
    quit_button.grid(row=3, column=1, columnspan=100, pady=10) 
    # quit_button.pack()    

    frame.mainloop()
    
if __name__ == '__main__':
    main()