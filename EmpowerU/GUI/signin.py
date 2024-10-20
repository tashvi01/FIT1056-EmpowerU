import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import tkinter as tk
import pymysql as pm
import os
from Utilities import switch_frame
from classes.Student import Student

class SignIn(tk.Frame):
    def __init__(self, master):
        """
        Constructor for SignIn class. Initializes the frame and adds widgets to it.
        
        Parameter(s):
        master (tk.Tk): The root window of the application.
        
        Return(s):
        None
        """
        super().__init__(master)
        self.mainframe = tk.Frame(master, padx=10, pady=10)  # Increased padding for mainframe
        self.mainframe.grid(column=0, row=0, sticky="nsew")

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
        self.username_label = tk.Label(self.mainframe, text="Username:")
        self.username_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)  # Align label to the right
        self.username_var = tk.StringVar()
        self.username_entry = tk.Entry(self.mainframe, textvariable=self.username_var)
        self.username_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create password label and entry
        self.password_label = tk.Label(self.mainframe, text="Password:")
        self.password_label.grid(row=3, column=0, sticky="e", padx=5, pady=5)  # Align label to the right
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(self.mainframe, textvariable=self.password_var, show="*")
        self.password_entry.grid(row=3, column=1, padx=5, pady=5)

        # Alert message label
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self.mainframe, textvariable=self.alert_var, fg="red")
        self.alert_label.grid(row=4, column=0, columnspan=2, pady=5)  # Center alert message

        #Admin login
        self.var = tk.IntVar()
        self.admin_button = tk.Checkbutton(self.mainframe, text="Admin Login",variable=self.var, command = self.admin_login)
        self.admin_button.grid(row=5, column=0, columnspan=2, pady=5)

        # Create sign-in button
        self.signin_button = tk.Button(self.mainframe, text="Sign In", command= self.sign_in)
        self.signin_button.grid(row=6, column=1, padx=10, pady=5)

        # Create sign-out button
        self.signout_button = tk.Button(self.mainframe, text="Return", command=self.sign_out)
        self.signout_button.grid(row=6, column=0, padx=10, pady=5)

    def admin_login(self):
        from Admin_login import AdminLogin
        switch_frame(self, AdminLogin)

    def authenticate(self, username_input, password_input):
        """
        Checks whether the username and password entered are correct 

        Parameter(s):
        username_input (str): the username the user enters
        password_input (str): the password the user enters

        Return(s):
        None      

        Written by: Tashvi Vig
        """
        self.username_input = username_input
        self.password_input = password_input
        conn= pm.connect(host='localhost', user='root', password='FIT1056') 
        cr=conn.cursor() 
        cr.execute("USE EmpowerU")
        cr.execute("SELECT * from STUDENTS where username=%s and password=%s",(self.username_input, self.password_input))
        result = cr.fetchone()
        self.alert_var.set("")
        if result is None:
            self.alert_var.set("Invalid username or password. Please try again.")
        else:

            first_name = result[0]  # Adjust based on your table structure
            last_name = result[1]
            date_of_birth = result[2]
            email = result[3]
            contact_number = result[4]
            username = result[5]
            password = result[6]

            student = Student(first_name, last_name, date_of_birth, email, contact_number, username, password)
            print(result)

            from Homepage import Homepage  
            switch_frame(self, lambda master: Homepage(master, student))


        self.username_var.set("")
        self.password_var.set("")

        conn.commit()
        conn.close()
        return result

    def sign_in(self):
        """
        Stores the User's username and password and calls the authenticate function

        Parameter(s):
        None
     
        Return(s): 
        None
        """
        self.username = self.username_var.get()
        self.password = self.password_var.get()
        self.authenticate(self.username, self.password)
        
    def hide_signin_page(self):
        self.mainframe.grid_forget()

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
