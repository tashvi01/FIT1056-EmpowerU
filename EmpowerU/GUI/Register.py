"""
FIT1056 Project: EmpowerU
Group: Monday G1

This file contains class definition of Register class

It creates a Register GUI and allows users to register.

Written by: Tashvi Vig
"""

import tkinter as tk
from tkinter import messagebox
import pymysql as pm
from backup import Backup
from Utilities import switch_frame

class Register(tk.Frame):
    def __init__(self, master=None):  
        """
        Constructor for the Register Class

        Parameter(s):
        Master : master widget of this widget instance

        Return(s):
        None    
        """
        super().__init__(master) 
        self.master = master
        self.mainframe = tk.Frame(master)
        self.create_widgets()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_widgets(self):
        """
        Creates widgets that are to be displayed in the Register window

        Parameters(s):
        none

        Return(s):
        none

        """
         
        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.dob_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.contact_number_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, fg="red")
        self.alert_label.pack(padx=10, pady=10)

        # First Name
        self.first_name_inp_label = tk.Label(self, text="Please enter your first name:")
        self.first_name_inp_label.pack(padx=10, pady=5)
        self.first_name_inp_entry = tk.Entry(self, textvariable=self.first_name_var)
        self.first_name_inp_entry.pack(padx=10, pady=5)

        # Last Name
        self.last_name_inp_label = tk.Label(self, text="Please enter your last name:")
        self.last_name_inp_label.pack(padx=10, pady=5)
        self.last_name_inp_entry = tk.Entry(self, textvariable=self.last_name_var)
        self.last_name_inp_entry.pack(padx=10, pady=5)

        # Date of Birth
        self.dob_inp_label = tk.Label(self, text="Please enter your Date of Birth:")
        self.dob_inp_label.pack(padx=10, pady=5)
        self.dob_inp_entry = tk.Entry(self, textvariable=self.dob_var)
        self.dob_inp_entry.pack(padx=10, pady=5)

        # Email
        self.email_inp_label = tk.Label(self, text="Please enter your email:")
        self.email_inp_label.pack(padx=10, pady=5)
        self.email_inp_entry = tk.Entry(self, textvariable=self.email_var)
        self.email_inp_entry.pack(padx=10, pady=5)

        # Contact Number
        self.contact_number_inp_label = tk.Label(self, text="Please enter your contact number:")
        self.contact_number_inp_label.pack(padx=10, pady=5)
        self.contact_number_inp_entry = tk.Entry(self, textvariable=self.contact_number_var)
        self.contact_number_inp_entry.pack(padx=10, pady=5)

        # Username
        self.username_inp_label = tk.Label(self, text="Please enter your desired username:")
        self.username_inp_label.pack(padx=10, pady=5)
        self.username_inp_entry = tk.Entry(self, textvariable=self.username_var)
        self.username_inp_entry.pack(padx=10, pady=5)

        # Password
        self.password_inp_label = tk.Label(self, text="Please enter your desired password:")
        self.password_inp_label.pack(padx=10, pady=5)
        self.password_inp_entry = tk.Entry(self, textvariable=self.password_var, show="*")
        self.password_inp_entry.pack(padx=10, pady=5)

        # ENTER 
        self.enter_button = tk.Button(self, text="ENTER", command=self.check)
        self.enter_button.pack(padx=10, pady=10)
        self.return_button = tk.Button(self, text="RETURN", command=self.reset_and_return)
        self.return_button.pack(padx=10, pady=10)

    def reset_and_return(self):
        """
        Resets all fields and switches to the login screen.
        
        Parameter(s):
        None

        Return(s):
        None
        """

        self.first_name_var.set("")
        self.last_name_var.set("")
        self.dob_var.set("")
        self.email_var.set("")
        self.contact_number_var.set("")
        self.username_var.set("")
        self.password_var.set("")
        self.alert_var.set("") 

        # Switch to the LoginScreen
        from Initial_window_GUI import LoginScreen
        switch_frame(self, LoginScreen)



    def check(self):
        """
        Checks whether the date and contact number entered is valid. If it is the calls data_to_sql()

        Parameter(s):
        none

        Return(s):
        Boolean
        
        """
        # Clear previous alerts
        self.alert_var.set("")

        is_valid = True

        # Validate date of birth
        if not self.is_valid_date_format(self.dob_var.get()):
            self.alert_var.set("Invalid date format. Please enter in DD/MM/YYYY.")
            self.dob_var.set("")  
            self.dob_inp_entry.focus_set() 
            is_valid = False

        # Validate contact number
        if not self.is_valid_contact_number(self.contact_number_var.get()):
            self.alert_var.set("Invalid contact number. It must be 10 digits.")
            # Reset the contact number field and set focus to it
            self.contact_number_var.set("")  # Clear the contact number field
            self.contact_number_inp_entry.focus_set()  # Set focus back to the contact number field
            is_valid = False

        if not is_valid:
            return False
        else:
            self.data_to_sql()

    def data_to_sql(self):
        """
        Forms a connection with sql and makes a database and a table with the new students login details

        Parameter(s):
        None

        Return(s): 
        None
        """

        first_name_value = self.first_name_var.get()
        last_name_value = self.last_name_var.get()
        dob_value = self.dob_var.get()
        email_value = self.email_var.get()
        contact_number_value = self.contact_number_var.get()
        username_value = self.username_var.get()
        password_value = self.password_var.get()

        conn= pm.connect(host='localhost', user='root', password='FIT1056') 
        cr=conn.cursor() 
        cr.execute("create database if not exists EmpowerU") 
        cr.execute("use EmpowerU") 
        cr.execute("create table if not exists students (first_name varchar(20), last_name varchar(20), DOB date, email varchar(20), contact_number varchar(20), username varchar(20), password varchar(20))") 
        dob_formatted = f"{dob_value[6:]}-{dob_value[3:5]}-{dob_value[:2]}"  # Converts to 'YYYY-MM-DD'
        values_tuple = (first_name_value, last_name_value, dob_formatted, email_value, int(contact_number_value), username_value, password_value)
        cr.execute("INSERT INTO students (first_name, last_name, DOB, email, contact_number, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s)", values_tuple)

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data has been stored successfully!")
        backup_instance = Backup
        backup_instance.backup_register(self,values_tuple)

        from Initial_window_GUI import LoginScreen
        switch_frame(self, LoginScreen)

    def is_valid_contact_number(self, contact_num):
        """
        Checks whether the contact number is entered is in the right format

        Parameters:
        contact_num (Str) : The contact number that has been provided as an input

        Output:
        Returns boolean
        
        """

        self.contact_num = contact_num

        if len(self.contact_num) == 10:
            if self.contact_num.isdigit():
                return True
            else:
                return False
        else:
            return False
        
    def is_leap_year(self, year):
        """
        This function checks if the year is a leap year.

        Parameters:
        - year: int

        Returns:
        bool - True if given year is a leap year, False otherwise
        """
    
        # Utilising Python smart evaluation
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    def is_date_valid(self, day, month, year):
        """
        This function checks whether the given date exists in the Gregorian calendar.

        Parameters:
        - day: int, (converted) integer value of the day
        - month: int, (converted) integer value of the month
        - year: int, (converted) integer value of the year in the Gregorian calendar

        Returns:
        bool - True if the given date exists in the Gregorian calendar, False otherwise
        """
        valid_days = None
        valid_months = range(1, 13)

        if month in [1, 3, 5, 7, 8, 10, 12]:
            valid_days = range(1, 32)
        elif month in [4, 6, 9, 11]:
            valid_days = range(1, 31)
        elif month == 2 and self.is_leap_year(year):
            valid_days = range(1, 30)
        elif month == 2 and not self.is_leap_year(year):
            valid_days = range(1, 29)
        else:
            return False

        return day in valid_days and month in valid_months and 0 <= year <= 2006
    
    def is_valid_date_format(self,input_date_value):
        """
        This function checks whether the string value input by the user is 
        a valid date (on or before 2006) *AND* presented in DD/MM/YYYY format

        Parameters:
        - input_date_value: str; the value provided by the user

        Returns:
        bool - True if input value is a valid date in DD/MM/YYYY format (on or before 2006), 
            False otherwise
        """

        numeric_chars = "0123456789"

        if len(input_date_value) == 10 and input_date_value[2] == "/" and input_date_value[5] == "/":
            day, month, year = input_date_value.split("/")

            if (all([char in numeric_chars for char in day]) 
                and all([char in numeric_chars for char in month]) 
                and all([char in numeric_chars for char in year])):

            # if day.isdigit() and month.isdigit() and year.isdigit():
                day = int(day)
                month = int(month)
                year = int(year)
                return self.is_date_valid(day, month, year)

        return False

