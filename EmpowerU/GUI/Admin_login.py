"""
FIT1056 Project: EmpowerU
Group: Monday G1

The admin login page of EmpowerU

Written by: Tashvi Vig
"""

import tkinter as tk
import os
from signin import SignIn
import pymysql as pm
from Utilities import switch_frame
from classes.Teacher import Admin

class AdminLogin(tk.Frame):
    def __init__(self, master):  
        """
        Constructor for the AdminLogin Class

        Parameter(s):
        Master : master widget of this widget instance

        Return(s):
        None    
        """
        super().__init__(master) 
        self.master = master
        #self.admin = admin
        self.mainframe = tk.Frame(self)
        self.mainframe.pack()
        self.create_widgets_admin()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_widgets_admin(self):
        """
        Creates widgets of admin login

        Parameter(s):
        None

        Return(s):
        None        

        Written by: Tashvi Vig
        """

        # Load logo image
        logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images/logo.png")
        self.logo = tk.PhotoImage(file=logo_path)  
        self.label = tk.Label(self.mainframe, image=self.logo, width=750, height=300)
        self.label.image = self.logo
        self.label.grid(row=0, column=0, columnspan=2, sticky=tk.S, pady=10)

        # Welcome heading
        self.welcome_label = tk.Label(self.mainframe, text="Welcome to EmpowerU", font=("Arial Bold", 20))
        self.welcome_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Create username label and entry
        self.id_label = tk.Label(self.mainframe, text="ID:")
        self.id_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)  
        self.id_var = tk.StringVar()
        self.id_entry = tk.Entry(self.mainframe, textvariable=self.id_var)
        self.id_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create password label and entry
        self.password_label = tk.Label(self.mainframe, text="Password:")
        self.password_label.grid(row=3, column=0, sticky="e", padx=5, pady=5) 
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(self.mainframe, textvariable=self.password_var, show="*")
        self.password_entry.grid(row=3, column=1, padx=5, pady=5)

        # Alert message label
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self.mainframe, textvariable=self.alert_var, fg="red")
        self.alert_label.grid(row=4, column=0, columnspan=2, pady=5) 

        # Create sign-in button
        self.signin_button = tk.Button(self.mainframe, text="Sign In", command= self.sign_in_admin)
        self.signin_button.grid(row=6, column=1, padx=10, pady=5)

        # Create sign-out button
        from Initial_window_GUI import LoginScreen
        self.signout_button = tk.Button(self.mainframe, text="Return", command=self.sign_out)
        self.signout_button.grid(row=6, column=0, padx=10, pady=5)


    def authenticate_admin(self, id_input, password_input):
        """
        Checks whether the id and password entered are correct 

        Parameter(s):
        id_input (str): the id the user enters
        password_input (str): the password the user enters

        Return(s):
        admin instance      

        Written by: Tashvi Vig
        """
        self.id_input = id_input
        self.password_input = password_input
        conn= pm.connect(host='localhost', user='root', password='FIT1056') 
        cr=conn.cursor() 
        cr.execute("USE EmpowerU")
        cr.execute("SELECT * from ADMIN where id=%s and password=%s",(self.id_input, self.password_input))
        result = cr.fetchone()
        self.alert_var.set("")
        if result is None:
            self.alert_var.set("Invalid ID or password. Please try again.")
        else:
            id = result[0]
            password = result[1]
            username = result[2]

            admin = Admin(id, password, username)
            print(result)

            from Admin_homepage import admin_Homepage
            switch_frame(self, lambda master: admin_Homepage(self.master, admin))

        self.id_var.set("")
        self.password_var.set("")

        conn.commit()
        conn.close()
        return admin

    def sign_in_admin(self):
        """
        Stores the Admin's id and password and calls the authenticate function

        Parameter(s):
        None
     
        Return(s): 
        admin instance from authenticate
        """
        self.id = self.id_var.get()
        self.password = self.password_var.get()
        return self.authenticate_admin(self.id, self.password)

    def sign_out(self):
        """
        Goes back to the initial screen.

        Parameter(s):
        None

        Return(s):
        None     

        Written by: Tashvi Vig   
        """
        from Initial_window_GUI import LoginScreen
        switch_frame(self,LoginScreen)
        

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminLogin(master=root)
    app.pack() 
    root.mainloop()
