"""
FIT1056 Project: EmpowerU
Group: Monday G1

This file contains class definition of Login Screen class

It creates a Login Screen GUI and allows users to sign in and register or shut down.

Written by: Tashvi Vig
"""

import tkinter as tk
from Register import Register
from signin import SignIn
from forum import Forum
import os
from Utilities import switch_frame

class LoginScreen(tk.Frame):
    def __init__(self, master):
        """
        Constructor for the LoginScreen Class

        Parameter(s):
        Master : master widget of this widget instance

        Return(s):
        None    
        """
        super().__init__(master)
        self.mainframe = tk.Frame(master, padx=3, pady=12)
        self.mainframe.grid(column=0, row=0, sticky="nsew") 
        self.create_widgets()

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

    def create_widgets(self):
        """
        Creates widgets that are to be displayed in the Initial window

        Parameters(s):
        none

        Return(s):
        none

        """
        # Load logo image
        logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images/logo.png")
        self.logo = tk.PhotoImage(file=logo_path)  
        self.label = tk.Label(self.mainframe, image=self.logo, width=750, height=300)  
        self.label.image = self.logo 
        self.label.grid(row=0, column=0, sticky=tk.S, padx=10, pady=10) 

        # Welcome heading
        self.welcome_label = tk.Label(self.mainframe, text="Welcome to EmpowerU", font=("Arial Bold", 20))
        self.welcome_label.grid(row=1, column=0, pady=10)

        # Create buttons below the welcome label
        self.register_button = tk.Button(self.mainframe, text="Register", command= self.open_register)
        self.register_button.grid(row=2, column=0, padx=10, pady=5)

        self.signin_button = tk.Button(self.mainframe, text="Sign In", command= self.open_sign_in)
        self.signin_button.grid(row=3, column=0, padx=10, pady=5)

        # Button to shut down
        self.shutdown_button = tk.Button(self.mainframe, text="Shut down", command=self.master.destroy)
        self.shutdown_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10)


    def open_register(self):
        """
        opens register window

        Parameter(s):
        none

        Return(s):
        none
        
        """

        switch_frame(self,Register)

    def open_sign_in(self):
        """
        opens sign in window

        Parameter(s):
        none

        Return(s):
        none

        """        
        switch_frame(self,SignIn)
    