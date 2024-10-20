"""
FIT1056 Project: EmpowerU
Group: Monday G1

Written by: Tashvi Vig
"""

import tkinter as tk
from Initial_window_GUI import LoginScreen 
from backup import Backup
#from forum import Forum

def main():
    root = tk.Tk()
    root.title("EmpowerU")
    
    backup_instance = Backup()
    backup_instance.populate_table()

    # Create the LoginScreen
    login_screen = LoginScreen(root)
    login_screen.grid(sticky="nsew")

    root.mainloop() 

if __name__ == "__main__":
    main()