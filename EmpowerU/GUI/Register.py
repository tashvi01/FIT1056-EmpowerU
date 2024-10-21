"""
FIT1056 Project: EmpowerU
Group: Monday G1

The register function

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
        Constructor class of Register
        
        Parameter(s):
        Master: master widget

        Return(s):
        None

        Written by: Tashvi Vig
        """ 
        super().__init__(master) 
        self.master = master
        self.mainframe = tk.Frame(master)
        self.create_widgets()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_widgets(self):
        """
        Creates register's widgets

        Parameter(s):
        None

        Return(s):
        None

        Written by: Tashvi Vig        
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
        Resets and returns to initial window

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

        from Initial_window_GUI import LoginScreen
        switch_frame(self, LoginScreen)

    def check(self):
        """
        Checks whether the DOB and contact number are valid. Also if email, username and contact nmber are unique.

        Parameter(s):
        None

        Return(s):
        None

        Written by: Tashvi Vig
        
        """
        self.alert_var.set("")
        is_valid = True
        error_messages = []

        # Validate date of birth
        if not self.is_valid_date_format(self.dob_var.get()):
            error_messages.append("Invalid date format. Please enter in DD/MM/YYYY.")
            self.dob_var.set("")  
            self.dob_inp_entry.focus_set() 
            is_valid = False

        # Validate contact number
        if not self.is_valid_contact_number(self.contact_number_var.get()):
            error_messages.append("Invalid contact number. It must be 10 digits and should be unique.")
            self.contact_number_var.set("")
            self.contact_number_inp_entry.focus_set()
            is_valid = False

        # Check for existing email
        if not self.is_unique_email(self.email_var.get()):
            error_messages.append("This email is already registered.")
            self.email_var.set("")  
            self.email_inp_entry.focus_set()
            is_valid = False

        # Check for existing username 
        if not self.is_unique_username(self.username_var.get()):
            error_messages.append("This username is already taken.")
            self.username_var.set("")  
            self.username_inp_entry.focus_set()
            is_valid = False

        if error_messages:
            self.alert_var.set("\n".join(error_messages))
        if not is_valid:
            return False
        else:
            self.data_to_sql()

    def data_to_sql(self):
        """
        Enters details in sql after checking if they are valid.

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

        conn = pm.connect(host='localhost', user='root', password='FIT1056') 
        cr = conn.cursor() 
        cr.execute("CREATE DATABASE IF NOT EXISTS EmpowerU") 
        cr.execute("USE EmpowerU") 
        cr.execute("CREATE TABLE IF NOT EXISTS students (first_name VARCHAR(20), last_name VARCHAR(20), DOB DATE, email VARCHAR(20) UNIQUE, contact_number VARCHAR(20), username VARCHAR(20) UNIQUE, password VARCHAR(20))") 
        dob_formatted = f"{dob_value[6:]}-{dob_value[3:5]}-{dob_value[:2]}"  # Converts to 'YYYY-MM-DD'
        values_tuple = (first_name_value, last_name_value, dob_formatted, email_value, int(contact_number_value), username_value, password_value)
        cr.execute("INSERT INTO students (first_name, last_name, DOB, email, contact_number, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s)", values_tuple)

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data has been stored successfully!")
        backup_instance = Backup()
        backup_instance.backup_register(values_tuple)

        from Initial_window_GUI import LoginScreen
        switch_frame(self, LoginScreen)

    def is_valid_contact_number(self, contact_num):
        """
        Checks if the contact number is valid and unique.

        Parameter(s):
        None

        Return(s):
        bool or exists/not exists
        """

        # contact number is valid (10 digits)
        if len(contact_num) != 10 or not contact_num.isdigit():
            return False

        # contact number is unique in the database
        conn = pm.connect(host='localhost', user='root', password='FIT1056')
        cr = conn.cursor()
        cr.execute("USE EmpowerU")
        cr.execute("SELECT COUNT(*) FROM students WHERE contact_number = %s", (contact_num,))
        exists = cr.fetchone()[0] > 0
        conn.close()

        return not exists

    def is_unique_email(self, email):
        """
        Checks whether email is unique
        
        """
        conn = pm.connect(host='localhost', user='root', password='FIT1056')
        cr = conn.cursor()
        cr.execute("USE empoweru")
        cr.execute("SELECT COUNT(*) FROM students WHERE email = %s", (email,))
        exists = cr.fetchone()[0] > 0
        conn.close()
        return not exists

    def is_unique_username(self, username):
        """
        Checks whether username is unique
        
        """
        conn = pm.connect(host='localhost', user='root', password='FIT1056')
        cr = conn.cursor()
        cr.execute("USE empoweru")
        cr.execute("SELECT COUNT(*) FROM students WHERE username = %s", (username,))
        exists = cr.fetchone()[0] > 0
        conn.close()
        return not exists

    def is_leap_year(self, year):
        """
        Checks if it is a leap year
        
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def is_date_valid(self, day, month, year):
        """
        Checks if date is valid
        
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

        return day in valid_days and month in valid_months and 1800 <= year <= 2006

    def is_valid_date_format(self, input_date_value):
        """
        Checks if date is entered in the right format
        """
        numeric_chars = "0123456789"

        if len(input_date_value) == 10 and input_date_value[2] == "/" and input_date_value[5] == "/":
            day, month, year = input_date_value.split("/")
            if (all([char in numeric_chars for char in day]) 
                and all([char in numeric_chars for char in month]) 
                and all([char in numeric_chars for char in year])):
                day = int(day)
                month = int(month)
                year = int(year)
                return self.is_date_valid(day, month, year)

        return False
