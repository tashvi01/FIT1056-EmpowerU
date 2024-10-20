"""
The Admin homepage of EmpowerU 

"""

import tkinter as tk
import Utilities as util
from profile import Profile

class Admin_Homepage(tk.Frame):
    def __init__(self,master,admin_user):
        super().__init__(master)
        self.master = master
        self.admin_user = admin_user
        util.fullscreen(self,master)
        
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

        
        #LESSON PLACEHOLDER
        # self.lesson_label = tk.Label(self.mainframe,text="LESSON PLACEHOLDER", font=20, bg = "gray35",fg = "azure").grid(row = 0 , column=0, rowspan=2)
        #FORUM PLACEHOLDER
        self.forum_button = tk.Button(self.mainframe,text= "FORUM",font=20,bg = "gray35",fg = "black",command=self.open_forum)
        self.forum_button.grid(row=0,rowspan=2, column=0)

        
        self.student_counter_label = tk.Label(self.mainframe,text="NUMBER OF STUDENTS: ", font="Impact 20", bg = "gray35",fg = "azure")
        self.student_counter_label.grid(row = 1 , column=0, rowspan=2)
    
        self.student_counter_num = tk.Label(self.mainframe,text=self.count_students(), font="Impact 20", bg = "gray35",fg = "azure")
        self.student_counter_num.grid(row = 1 , column=1, rowspan=2)
        self.top_bar = tk.Frame(self.master, bg="gray23")  # Specify the background color and height
        self.top_bar.grid(row=0, column=0, sticky="new")  # Place it in the first row and expand it east-west

        
        #TOP BAR
        #Home label
        # fotnsize https://www.geeksforgeeks.org/how-to-change-the-tkinter-label-font-size/
        self.home_label = tk.Label(self.top_bar, text="HOME", bg="gray23",font = "Impact 20",fg = "azure")
        self.home_label.grid(row=0,column=0,padx=20,pady=20)

        #Admin homepage label
        self.admin_label = tk.Label(self.top_bar,text = "ADMIN HOMEPAGE",font = "Impact 20", bg="gray23",fg = "azure")
        self.admin_label.grid(row=0,column=1,padx=20,pady=20)

        #profile button
        # self.profile_button = tk.Button(self.top_bar,text="PROFILE",font = "Impact 20", bg="dodgerblue",command= self.open_profile,fg = "azure")
        # self.profile_button.grid(row=0,column=2,padx=2)

        
        #configures the columns for the top bar
        self.top_bar.grid_columnconfigure(0, weight=1)
        self.top_bar.grid_columnconfigure(1, weight=1)
        self.top_bar.grid_columnconfigure(2, weight=1)
        self.top_bar.grid_rowconfigure(0, weight=1)
        


    def count_students(self):
        import csv
        file_name = "Register_backup.csv"
        with open(file_name, 'r', encoding="utf-8-sig") as register:
            csvDictReader = csv.DictReader(register)
            student_list = []
            for line in csvDictReader:
                student_list.append(line)
        return (len(student_list))
        
    def open_forum(self):
        from forum import Forum
        util.switch_frame(self, Forum(self.master,self.admin_user))

    # def open_profile(self):
    #     self.master.destroy()

    #     root = tk.Tk()  
    
    #     #create profile instance
    #     profile = Profile(root)
    #     profile.grid(row = 0, column = 0, sticky="nsew")

    #     #allows rows and columns to expand and contract when window is resized
    #     root.grid_rowconfigure(0, weight=1)
    #     root.grid_columnconfigure(0, weight=1)
        
    #     profile.mainloop()
        


        


    
        



    

    






    def fullscreen(self,master):

        #fullscreen needs master parameter because of tk.Frame doesn't have geometry() method 
        # Fullscreen information learnt from geeksforgeeks.org 1/10/2024: https://www.geeksforgeeks.org/how-to-create-full-screen-window-in-tkinter/

        #obtaining width and height of screen
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        #makes window match screen geometry
        #geometry() method called with master (tk.Tk instance) instead of self which is the frame
        master.geometry(f"{width}x{height}")
        

if __name__ == "__main__":
    root = tk.Tk()  
    
    #create homepage
    homepage = Admin_Homepage(root,"admin_user")
    homepage.grid(row = 0, column = 0, sticky="nsew")

    #allows rows and columns to expand and contract when window is resized
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    homepage.mainloop()
