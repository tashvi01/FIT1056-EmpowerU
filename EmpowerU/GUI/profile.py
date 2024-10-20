import tkinter as tk 
import Utilities as util
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from classes.Student import Student
class Profile(tk.Frame):
    def __init__(self,master,student_user):
        super().__init__(master)
        self.master = master
        self.student_user = student_user
        util.fullscreen(self,master)
       
        
        self.mainframe = tk.Frame(self.master, bg = "lightblue")
        self.mainframe.grid(row = 0, column=0, sticky="nsew")
        self.logo = tk.PhotoImage(file="logo.png")
        self.logo_label = tk.Label(self.mainframe,image=self.logo,width = 310, height = 310)
        self.logo_label.grid(row = 0,column=0,sticky="ne",padx=30,pady=10)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.columnconfigure(1, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=1)
        self.mainframe.rowconfigure(3,weight=1)
        self.mainframe.rowconfigure(4,weight=1)
        
        self.create_widgets()
    def create_widgets(self):
        fonts = 'Times 20 bold'
        self.student_first_name_la = tk.Label(self.mainframe, text = "First Name", bg = "lightblue", fg = "black",font=fonts)
        self.student_first_name_la.grid(row = 1, column = 0, sticky = "nsew")
        self.student_first_name = tk.Label(self.mainframe, text = self.student_user.first_name, bg = "lightblue",fg="black",font=fonts)
        self.student_first_name.grid(row = 1, column = 1, sticky = "nsew")

        self.student_last_name_la = tk.Label(self.mainframe, text = "Last Name", bg = "lightblue",fg="black",font=fonts)
        self.student_last_name_la.grid(row = 2, column = 0, sticky = "nsew")
        self.student_last_name = tk.Label(self.mainframe, text = self.student_user.last_name, bg = "lightblue",fg="black",font=fonts)
        self.student_last_name.grid(row = 2, column = 1, sticky = "nsew")


        self.student_dob_la = tk.Label(self.mainframe, text = "Date of Birth", bg = "lightblue",fg="black",font=fonts)
        self.student_dob_la.grid(row = 3, column = 0, sticky = "nsew")
        self.student_dob = tk.Label(self.mainframe, text = self.student_user.DOB, bg = "lightblue",fg="black",font=fonts)
        self.student_dob.grid(row = 3, column = 1, sticky = "nsew")

        self.student_email_la = tk.Label(self.mainframe, text = "Email", bg = "lightblue",fg="black",font=fonts)
        self.student_email_la.grid(row = 4, column = 0, sticky = "nsew")
        self.student_email = tk.Label(self.mainframe, text = self.student_user.email, bg = "lightblue",fg="black",font=fonts)   
        self.student_email.grid(row = 4, column = 1, sticky = "nsew")

        self.logo = tk.PhotoImage(file="logo.png")
        self.logo_label = tk.Label(self.mainframe,image=self.logo,width = 310, height = 310)
        self.logo_label.grid(row = 0,column=0,sticky="ne",padx=30,pady=10)



    

if __name__ == "__main__":
    root = tk.Tk()  
    Student1 = Student("first_name", 'last_name', 'DOB', 'email', 'contact_number', 'username', 'password')
    #create homepage
    profile = Profile(root,Student1)
    profile.grid(row = 0, column = 0, sticky="nsew")

    #allows rows and columns to expand and contract when window is resized
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    profile.mainloop()
