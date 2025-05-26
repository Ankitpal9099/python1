# import tkinter
# form tkinter import tkinter
# from tkinter import messagebox
from tkinter import Tk
from tkinter import messagebox
from tkinter import filedialog
m = tkinter.Tk()  
m.withdraw()  # Hide the root window
def show_message(title, message):
    messagebox.showinfo(title, message)
    
m.mainloop()
def get_file_path():
    file_path = filedialog.askopenfilename()
    if file_path:
        return file_path
    else:
        show_message("Error", "No file selected.")
        return None