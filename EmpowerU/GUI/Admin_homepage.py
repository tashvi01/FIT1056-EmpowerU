"""
FIT1056 Project: EmpowerU
Group: Monday G1

The admin homepage of EmpowerU

Written by: Tommy Nguyen and Tashvi Vig
"""

import tkinter as tk
from Utilities import switch_frame
from tkinter import messagebox
from Student_Manager import StudentManager
from Utilities import fullscreen

class admin_Homepage(tk.Frame):
    def __init__(self,master,admin):
        """
        Constructor for the admin_Homepage Class

        Parameter(s):
        Master : master widget of this widget instance
        admin: instance of the admin logged in

        Return(s):
        None    
        """
        super().__init__(master)
        self.master = master
        self.admin = admin
        fullscreen(self,master)
        self.student_manager = StudentManager()
        self.mainframe = tk.Frame(self.master,bg="gray35")
        self.mainframe.grid(row=0,column=0,sticky="nsew")
        
        #background colour learnt from https://www.geeksforgeeks.org/tkinter-colors/
        self.config(bg="lightblue")

        #BOTTOM HALF OF SCREEN     
        # # Configure rows and columns for even distribution
        self.mainframe.grid_rowconfigure(0, weight=1)
        self.mainframe.grid_rowconfigure(1, weight=1)  
        self.mainframe.grid_rowconfigure(2, weight=1)

        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.grid_columnconfigure(1, weight=1)  
        self.mainframe.grid_columnconfigure(2, weight=1)            

        self.logo = tk.PhotoImage(file="../images/logo.png")
        self.logo_label = tk.Label(self.mainframe,image=self.logo)
        self.logo_label.grid(row = 1, column=2,sticky="e",padx=30, pady = 10)
        
        #FORUM 
        self.forum_button = tk.Button(self.mainframe,text= "FORUM",font=20,bg = "gray35",fg = "black",command=self.open_forum)
        self.forum_button.grid(row=0,rowspan=2, column=0)

        #View Students button
        self.view_students_button = tk.Button(self.mainframe, text="View All Students", command=self.display_students,font="Impact 20", bg = "gray35",fg = "azure")
        self.view_students_button.grid(row = 1 , column=0, rowspan=2)

        self.student_list_frame = tk.Frame(self.mainframe)
        self.student_list_frame.grid(row = 1 , column=1, rowspan=2)

        #Top Bar
        self.top_bar = tk.Frame(self.master, bg="gray23")  # Specify the background color and height
        self.top_bar.grid(row=0, column=0, sticky="new")  # Place it in the first row and expand it east-west

        #Home label
        # fotnsize https://www.geeksforgeeks.org/how-to-change-the-tkinter-label-font-size/
        self.home_label = tk.Label(self.top_bar, text="HOME", bg="gray23",font = "Impact 20",fg = "azure")
        self.home_label.grid(row=0,column=0,padx=20,pady=20)

        #Admin homepage label
        self.admin_label = tk.Label(self.top_bar,text = "ADMIN HOMEPAGE",font = "Impact 20", bg="gray23",fg = "azure")
        self.admin_label.grid(row=0,column=1,padx=20,pady=20)

        #shut_down button
        self.shutdown_button = tk.Button(self.top_bar,text="SHUT DOWN and LOG OUT",font = "Impact 20", bg="dodgerblue",command= self.master.destroy,fg = "azure")
        self.shutdown_button.grid(row=0,column=2,padx=2)

        
        #configures the columns for the top bar
        self.top_bar.grid_columnconfigure(0, weight=1)
        self.top_bar.grid_columnconfigure(1, weight=1)
        self.top_bar.grid_columnconfigure(2, weight=1)
        self.top_bar.grid_rowconfigure(0, weight=1)
        
    def display_students(self):
        """
        Display all students in a new full-screen window.
        
        Parametr(s):
        None

        Return(s): 
        None

        Written By: Tashvi Vig
        """
        new_window = tk.Toplevel(self.master)
        new_window.title("All Students")

        fullscreen(self, new_window)

        heading_label = tk.Label(new_window, text="All Students", font=("Arial", 24), bg="lightblue")
        heading_label.pack(pady=20)

        for widget in new_window.winfo_children():
            if widget != heading_label:
                widget.destroy()

        students = self.student_manager.get_all_students()

        if not students:
            messagebox.showinfo("Info", "No students found.")
            new_window.destroy()
            return

        total_quizzes = 9  # Fixed total number of quizzes

        for idx, (first_name, last_name, username, quizzes_completed) in enumerate(students):
            progress_text = f"Quizzes Completed: {quizzes_completed}, Total: {total_quizzes}"
            student_label = tk.Label(new_window, text=f"{first_name} {last_name} (Username: {username}) - {progress_text}", bg="lightblue")
            student_label.pack(anchor="w", padx=5, pady=5)

        return_button = tk.Button(new_window, text="Return to Admin Homepage", command=new_window.destroy)
        return_button.pack(pady=10)
        
    def open_forum(self):
        """
        Opens forum

        Parameter(s):
        None

        Return(s):
        None   

        Written By: Tashvi Vig     
        """

        from forum import Forum
        switch_frame(self,lambda master: Forum(master, None, self.admin))
           

if __name__ == "__main__":
    root = tk.Tk()  
    
    #create homepage
    homepage = admin_Homepage(root,"admin")
    homepage.grid(row = 0, column = 0, sticky="nsew")

    #allows rows and columns to expand and contract when window is resized
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    homepage.mainloop()