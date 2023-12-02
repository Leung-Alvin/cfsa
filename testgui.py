import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
from tkinter.font import Font
import shutil
import prompt
import random
import model
from database import os, get_folders_in_directory, get_valid_input, add_print
import numpy as np
import grammar

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

  
def compare_with_database(root_window):
    frame1 = tk.Toplevel(root_window) 
    frame1.title("Compare With Database") 
    frame1.geometry('1600x1200') 
    # Function for getting Input 
    # from textbox and printing it  
    # at label widget 
    prompts = prompt.get_prompts()
    pmt = tk.Label(frame1, text=np.random.choice(prompts, replace=False))
    pmt.pack()
    def printInput():
        text = inputtxt.get("1.0", "end-1c")
        # print(text)
        if text == "":
            messagebox.showinfo("Error", "Please enter text in the box.")
            return 
        else:
            lmao = model.predicto(text,75)
            string_1 = "My top 3 predictions given the top 75 words are: " + "\n" + str(list(lmao.keys())[:3])
            deltas_1 = "Top 75 Deltas: " + "\n" + str(list(lmao.values())[:3])
            lmao2 = model.predicto(text,45)
            string_2 = "My top 3 predictions given the top 45 words are: " + "\n" + str(list(lmao2.keys())[:3])
            deltas_2 = "Top 45 Deltas: " + "\n" + str(list(lmao2.values())[:3])
            # lmao3 = grammar.grammar_analyis(text)
            # string_3 = "My top 3 predictions given the grammar analysis are: " + "\n" + str(lmao3)
            lbl.config(text = string_1 + "\n" + deltas_1 + "\n" + string_2 + "\n" + deltas_2)
    
    def skipPrompt():
        pmt.config(text=np.random.choice(prompts, replace=False))
        inputtxt.delete("1.0", "end-1c") 
    # TextBox Creation 
    inputtxt = tk.Text(frame1, 
                    height = 50, 
                    width = 150) 
    
    inputtxt.place(relx=.05, rely = .20, relheight = .4, relwidth =.9) 
    
    # Button Creation 
    printButton = tk.Button(frame1, 
                            text = "Predict",  
                            command = printInput) 
    printButton.place(relx = .375, rely = .7, relheight = .1, relwidth =.15)
    
    skipPromptButton = tk.Button(frame1, 
                            text = "Skip Prompt",  
                            command = skipPrompt) 
    skipPromptButton.place(relx = .375, rely = .825, relheight = .1, relwidth =.15)  
    
    # Label Creation 
    lbl = tk.Label(frame1, text = "") 
    lbl.pack() 
    frame1.mainloop()

# def view_prints(root_window):
    
    
def edit_database(root_window):
    base_directory = "databases"

    def get_folders_in_directory(directory_path):
        folders = [f for f in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, f))]
        return folders
    #def get_files_in_folder(folder_path):
        #files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        #return files
    
    def display_file_content():
        selected_folder = listbox.get(tk.ACTIVE)

        if not selected_folder:
            tk.messagebox.showinfo("Select File", "Please select a file.")
            db.lift()

        selected_file = contents_listbox.get(tk.ACTIVE)
        selected_file_path = os.path.join(base_directory, selected_folder, selected_file)
        
        edit_text_widget.delete(1.0, tk.END)

        #encodings_to_try = ['utf-8', 'latin-1', 'utf-16', 'cp1252']
        
        #for encoding in encodings_to_try:
        try:
            with open(selected_file_path, 'r', encoding= 'utf-8') as file:
                current_content = file.read()

            # Enable the edit_text_widget for editing
            edit_text_widget.config(state=tk.NORMAL)
            edit_text_widget.delete(1.0, tk.END)
            edit_text_widget.insert(tk.END, current_content)

            #break  # Break out of the loop if successful
        except UnicodeDecodeError:
            pass  # Try the next encoding if decoding fails
        except FileNotFoundError:
            edit_text_widget.insert(tk.END, "File not found.")
    def display_folder_contents():
        selected_item = listbox.get(tk.ACTIVE)

        if not selected_item:
            tk.messagebox.showinfo("Select Folder", "Please select a folder.")
            db.lift()
            listbox.get(tk.DISABLED)

        selected_directory = os.path.join(base_directory, selected_item)

        contents_listbox.delete(0, tk.END)

        try:
            contents = os.listdir(selected_directory)
            for item in contents:
                    contents_listbox.insert(tk.END, item)
        except FileNotFoundError:
            contents_listbox.insert(tk.END, "Contents not available.")

    def add_new_file():
        selected_folder = listbox.get(tk.ACTIVE)

        if not selected_folder:
            tk.messagebox.showinfo("Select Folder", "Please select a folder.")
            return

        selected_directory = os.path.join(base_directory, selected_folder)

        file_dialog_window = tk.Toplevel(db)
        file_dialog_window.transient(db)
        file_dialog_window.grab_set()

        # Ask the user to select a text file using the file explorer
        file_path = filedialog.askopenfilename(parent = file_dialog_window, title="Select a Text File", filetypes=[("Text files", "*.txt")])
        
        file_dialog_window.destroy()
        
        if file_path:
            # Extract the file name from the selected path
            new_file_name = os.path.basename(file_path)

            # Construct the new file path in the selected directory
            new_file_path = os.path.join(selected_directory, new_file_name)

            try:
                shutil.copy(file_path, new_file_path)

                # Update the contents_listbox to include the new file
                contents_listbox.insert(tk.END, new_file_name)

                # Update the folder_listbox to display the current folders
                contents_listbox.delete(0, tk.END)
                display_folders()
            except FileExistsError:
                tk.messagebox.showinfo("File Exists", "File with that name already exists in the selected directory.")

    def delete_selected_file():
        selected_file = contents_listbox.get(tk.ACTIVE)
        if not selected_file:
            tk.messagebox.showinfo("Select File", "Please select a file.")
            db.lift()
            return
        db.focus_force()

        confirmation = tk.messagebox.askyesno("Delete File", f"Do you want to delete the file '{selected_file}'?")
        if confirmation:
            selected_folder = listbox.get(tk.ACTIVE)
            file_path = os.path.join(base_directory, selected_folder, selected_file)
            try:
                # Check if it's a directory before attempting to remove
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    # Update the listbox and clear the text widget
                    display_folder_contents()
                    edit_text_widget.delete(1.0, tk.END)
            except OSError as e:
                tk.messagebox.showerror("Error", f"Error deleting file: {e}")

    def save_changes():
        selected_folder = listbox.get(tk.ACTIVE)
        selected_file = contents_listbox.get(tk.ACTIVE)
        selected_file_path = os.path.join(base_directory, selected_folder, selected_file)

        try:
            edited_content = edit_text_widget.get(1.0, tk.END)

            with open(selected_file_path, 'w', encoding = 'utf-8') as file:
                file.write(edited_content)

            # Disable the edit_text_widget after saving changes
            edit_text_widget.config(state=tk.DISABLED)
        except FileNotFoundError:
            edit_text_widget.insert(tk.END, "File not found.")

    def display_folders():

        folders = get_folders_in_directory(base_directory)
        
        listbox.delete(0, tk.END)  # Clear existing items

        for folder in folders:
            listbox.insert(tk.END, folder)

    def bind_display_file_contents(event):
        edit_text_widget.delete(1.0, tk.END)
    
    def bind_display_folder_contents(event):
        widget_under_cursor = event.widget.winfo_containing(event.x_root, event.y_root)
        if widget_under_cursor != contents_listbox:
            contents_listbox.delete(0, tk.END)
            
    db = tk.Toplevel(root_window)
    db.title("Database")
    db.geometry("900x800")

    listbox = tk.Listbox(db, width=30)
    listbox.grid(row = 1, column = 20, columnspan = 3, padx = 10, pady = 10)
    listbox.bind('<ButtonRelease-1>', bind_display_folder_contents)

    display_button = tk.Button(db, text="Display Folders", command=display_folders)
    display_button.grid(row=2, column = 20, columnspan= 2, pady=10)

    delete_folder_button = tk.Button(db, text="Delete Fingerprint", command = delete_selected_file)
    delete_folder_button.grid(row=2, column= 31, columnspan=2, pady=10)

    add_file_button = tk.Button(db, text="Add New File", command=add_new_file)
    add_file_button.grid(row=3, column= 20, columnspan=2, pady=10)

    contents_listbox = tk.Listbox(db, width=40)
    contents_listbox.grid(row=1, column=30, columnspan = 3, padx=10, pady=10)
    contents_listbox.bind('<ButtonRelease-1>', bind_display_file_contents)

    view_contents_button = tk.Button(db, text="View Contents", command=display_folder_contents)
    view_contents_button.grid(row=2, column = 30, columnspan= 2, pady=10)

    edit_text_widget = tk.Text(db, height=20, width=50, state=tk.DISABLED)
    edit_text_widget.grid(row=5, column=30, columnspan=4, pady=10)

    save_button = tk.Button(db, text="Save Changes", command=save_changes)
    save_button.grid(row=6, column=30, columnspan=2, pady=10)

    display_text_files_button = tk.Button(db, text="Display Prints", command=display_file_content)
    display_text_files_button.grid(row=3, column=30, columnspan=2, pady=10)

def compare_two_prints(root_window):
    result = False
    def submit():
        # model.clear_temp()
        value1 = entry1.get("1.0", "end-1c")  # Retrieve text from the first text box
        value2 = entry2.get("1.0", "end-1c")  # Retrieve text from the second text box
        print(value1)
        print(value2)
        length1 = len(value1)
        length2 = len(value2)
        
        if length1 == 0 or length2 == 0:
            messagebox.showinfo("Error", "Please enter text in both boxes.")
            return
        
        # minimum_length = min(len(value1), len(value2))
        
        # value1 = value1[:minimum_length]
        # value2 = value2[:minimum_length]
        # with open('survey/temp_-_mundanely.txt', 'w') as f:
        #     f.write(str(value1))
        # prediction = model.predicto(value2)
        #str(list(lmao2.keys())[:3])
        prediction_1 = model.predicto(value1, 45)
        prediction_2 = model.predicto(value2, 45)
        results_1 = list(prediction_1.keys())[:3]
        results_2 = list(prediction_2.keys())[:3]
        deltas_1 = str(list(prediction_1.values())[:3])
        deltas_2 = str(list(prediction_2.values())[:3])
        if results_1[0] == results_2[0]:
            results = "The two prints are likely by the same author." + "\n\n" + "Author_1 Candidates: " + str(results_1) + "\n" + "Author_1 Deltas: " + deltas_1 + "\n\n" + "Author_2 Candidates: " + str(results_2) + "\n" + "Author_2 Deltas: " + deltas_2
        elif results_1[0] == results_2[1] or results_1[1] == results_2[0]:
            results = "The two prints are probably by the same author." + "\n\n" + "Author_1 Candidates: " + str(results_1) + "\n" + "Author_1 Deltas: " + deltas_1 + "\n\n" + "Author_2 Candidates: " + str(results_2) + "\n" + "Author_2 Deltas: " + deltas_2
        elif results_1[1] == results_2[2] or results_1[2] == results_2[1]:
            results = "The two prints are possibly or possibly not by the same author." + "\n\n" + "Author_1 Candidates: " + str(results_1) + "\n" + "Author_1 Deltas: " + deltas_1 + "\n\n" + "Author_2 Candidates: " + str(results_2) + "\n" + "Author_2 Deltas: " + deltas_2
        elif results_1[2] == results_2[2]:
            results = "The two prints are probably not by the same author" + "\n\n" + "Author_1 Candidates: " + str(results_1) + "\n" + "Author_1 Deltas: " + deltas_1 + "\n\n" + "Author_2 Candidates: " + str(results_2) + "\n" + "Author_2 Deltas: " + deltas_2
        else:
            results = "The two prints are unlikely to be by the same author" + "\n\n" + "Author_1 Candidates: " + str(results_1) + "\n" + "Author_1 Deltas: " + deltas_1 + "\n\n" + "Author_2 Candidates: " + str(results_2) + "\n" + "Author_2 Deltas: " + deltas_2
        frame = tk.Tk() 
        frame.title("Two Print Results") 
        frame.geometry('600x300')
        label = tk.Label(frame, text=results)
        label.pack()

    # Create the sub window

    cmp = tk.Toplevel(root_window)

    cmp.title("Compare Two Prints")
    prompts = prompt.get_prompts()
    text_1 = np.random.choice(prompts, replace = False)
    text_2 = np.random.choice(prompts, replace = False)
    # Create the first text box
    label1 = tk.Label(cmp, text=text_1)
    label1.grid(row=0, column=0, padx=1, pady=10, sticky="w")

    entry1 = tk.Text(cmp, height=20, width=100)
    entry1.grid(row=0, column=1, padx=10, pady=10)

    # Create the second text box
    label2 = tk.Label(cmp, text=text_2)
    label2.grid(row=1, column=0, padx=100, pady=10, sticky="w")

    entry2 = tk.Text(cmp, height=20, width=100)
    entry2.grid(row=1, column=1, padx=10, pady=10)

    # Create the submission button
    submit_button = tk.Button(cmp, text="Predict", command=submit)
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    cmp.mainloop()  # Start the Tkinter event loop
# Start the Tkinter event loop
# root.mainloop()
# 

def on_enter(button):
    button.config(bg = '#9d9dff')

def on_leave(button):
    button.config(bg = 'SystemButtonFace')

def main(): 
    # root.mainloop()

    frame = tk.Tk()
    frame.state('zoomed') 
    frame.title("CFSA Prototype")
    frame.minsize(width=900, height=660)
    # frame.geometry('1600x1200')
    
    CyberFont = Font(
        family = "Verdana",
        size = 37,
        weight = "bold",
        slant = "roman",
    )    

    CyberFontSub = Font(
        family = "helvetica",
        size = 30,
        weight = "bold",
        slant = "roman",
    )   

    CyberFontButton = Font(
        family = "Verdana",
        weight = "bold",
        slant = "roman",
    )
    frame.configure(bg="lightblue")

    #CFSA Title Widget
    label = tk.Label(frame, text="CFSA CyberSecurity Suite", font = CyberFont, bg="#D3D3D3", bd = 0, highlightthickness=5,  highlightbackground="grey", fg = "#000080")
    label.place(relx = .5, rely = .1, relheight=.2, relwidth=.8, anchor = "center")
    #label.pack(padx= 100, pady= 100) 
    #label = tk.Label(frame, text="CFSA Demo", font = ('Starzoom-Shavian', 25), bg="lightblue", pady=10)
    
    #Subtitle Widget
    label = tk.Label(frame, text="Demo Version", font = CyberFontSub, bg="lightblue", pady=10)
    label.place(relx = .5, rely = .27, relheight=.2, relwidth=.8, anchor = "center") 
    # Button Creation
     
    db_compare_button = tk.Button(frame, 
                            text = "Compare With Database",  
                            command = lambda: compare_with_database(frame), font = CyberFontButton, width = 35, height = 5)
    db_compare_button.place(relx = .65, rely= .4, relheight=.1, relwidth=.25, anchor = "center") 
    # db_compare_button.pack()
    
    #button light up
    db_compare_button.bind('<Enter>', lambda event, btn = db_compare_button: on_enter(btn))
    db_compare_button.bind('<Leave>', lambda event, btn = db_compare_button: on_leave(btn))

    compare_two_prints_button = tk.Button(frame, 
                            text = "Compare Two Prints",  
                            command = lambda: compare_two_prints(frame), font = CyberFontButton, width = 35, height = 5)
    compare_two_prints_button.place(relx = .35, rely = .4, relheight=.1, relwidth=.25, anchor = "center")  
    # compare_two_prints_button.pack()
    
    compare_two_prints_button.bind('<Enter>', lambda event, btn = compare_two_prints_button: on_enter(btn))
    compare_two_prints_button.bind('<Leave>', lambda event, btn = compare_two_prints_button: on_leave(btn))

    view_prints_button = tk.Button(frame, 
                            text = "Placeholder",  
                            command = lambda: compare_two_prints(frame), font = CyberFontButton, width = 35, height = 5)
    view_prints_button.place(relx = .65, rely = .6,  relheight=.1, relwidth=.25, anchor = "center")  
    # compare_two_prints_button.pack()
    
    view_prints_button.bind('<Enter>', lambda event, btn = view_prints_button: on_enter(btn))
    view_prints_button.bind('<Leave>', lambda event, btn = view_prints_button: on_leave(btn))

    placeholder_button = tk.Button(frame, 
                            text = "View Fingerprints",  
                            command = lambda: edit_database(frame), font = CyberFontButton, width = 35, height = 5)
    placeholder_button.place(relx = .35, rely = .6,  relheight=.1, relwidth=.25, anchor = "center")  
    # compare_two_prints_button.pack()
    
    placeholder_button.bind('<Enter>', lambda event, btn = placeholder_button: on_enter(btn))
    placeholder_button.bind('<Leave>', lambda event, btn = placeholder_button: on_leave(btn))

    def quit():
        frame.destroy()
    
    quit_button = tk.Button(frame, 
                            text = "Quit Application",  
                            command = quit, width = 30, font = CyberFontButton, height = 5, anchor = "center")
    quit_button.place(relx = .5, rely = .9,  relheight=.1, relwidth=.2, anchor = "center") 

    quit_button.bind('<Enter>', lambda event, btn = quit_button: on_enter(btn))
    quit_button.bind('<Leave>', lambda event, btn = quit_button: on_leave(btn))

    
    
    # quit_button.pack()    

    frame.mainloop()
    
if __name__ == '__main__':
    main()