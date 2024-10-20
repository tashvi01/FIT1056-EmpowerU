import tkinter as tk 
import Utilities as util
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from classes.Student import Student
from Utilities import switch_frame

class Profile(tk.Frame):
    def __init__(self,master,student):
        super().__init__(master)
        self.master = master
        self.student = student
        util.fullscreen(self,master)
       
        
        self.mainframe = tk.Frame(self.master, bg = "lightblue")
        self.mainframe.grid(row = 0, column=0, sticky="nsew")

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
        self.student_first_name = tk.Label(self.mainframe, text = self.student.first_name, bg = "lightblue",fg="black",font=fonts)
        self.student_first_name.grid(row = 1, column = 1, sticky = "nsew")

        self.student_last_name_la = tk.Label(self.mainframe, text = "Last Name", bg = "lightblue",fg="black",font=fonts)
        self.student_last_name_la.grid(row = 2, column = 0, sticky = "nsew")
        self.student_last_name = tk.Label(self.mainframe, text = self.student.last_name, bg = "lightblue",fg="black",font=fonts)
        self.student_last_name.grid(row = 2, column = 1, sticky = "nsew")


        self.student_dob_la = tk.Label(self.mainframe, text = "Date of Birth", bg = "lightblue",fg="black",font=fonts)
        self.student_dob_la.grid(row = 3, column = 0, sticky = "nsew")
        self.student_dob = tk.Label(self.mainframe, text = self.student.DOB, bg = "lightblue",fg="black",font=fonts)
        self.student_dob.grid(row = 3, column = 1, sticky = "nsew")

        self.student_email_la = tk.Label(self.mainframe, text = "Email", bg = "lightblue",fg="black",font=fonts)
        self.student_email_la.grid(row = 4, column = 0, sticky = "nsew")
        self.student_email = tk.Label(self.mainframe, text = self.student.email, bg = "lightblue",fg="black",font=fonts)   
        self.student_email.grid(row = 4, column = 1, sticky = "nsew")

        self.return_button = tk.Button(self.mainframe, text= "RETURN", command = self.return_to_home, bg = "lightblue",fg="black")
        self.return_button.grid(row=5, column=0,columnspan=2, sticky = "nsew")

        logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images/logo.png")
        self.logo = tk.PhotoImage(file=logo_path)  
        self.label = tk.Label(self.mainframe, image=self.logo, width=310, height=310, bg = "lightblue")
        self.label.image = self.logo
        self.label.grid(row=0, column=0,columnspan=2, sticky="nsew", padx=30,pady=10)

    def return_to_home(self):
        from Homepage import Homepage  
        switch_frame(self, lambda master: Homepage(master, self.student))

    

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