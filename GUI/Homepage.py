"""
The homepage of EmpowerU 

"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import tkinter as tk
import Utilities as util
from profile import Profile
import os
from Utilities import switch_frame
from Progress_Tracker import ProgressTracker
from classes import Student

class Homepage(tk.Frame):
    def __init__(self,master,student):
        super().__init__(master)
        self.master = master
        util.fullscreen(self,master)
        self.student = student
        
        self.mainframe = tk.Frame(self.master,bg="lightblue")
        self.mainframe.grid(row=0,column=0,sticky="nsew")
        
        #background colour learnt from https://www.geeksforgeeks.org/tkinter-colors/
        self.config(bg="lightblue")
        
        #BOTTOM HALF OF SCREEN
        

        # # Configure rows and columns for even distribution
        self.mainframe.grid_rowconfigure(0, weight=1)
        self.mainframe.grid_rowconfigure(1, weight=1)  
        self.mainframe.grid_rowconfigure(2, weight=1)
        self.mainframe.grid_rowconfigure(3, weight=1)
        self.mainframe.grid_rowconfigure(4, weight=1)
        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.grid_columnconfigure(1, weight=1)  
        self.mainframe.grid_columnconfigure(2, weight=1)
            
        
        logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images/logo.png")
        self.logo = tk.PhotoImage(file=logo_path)  
        self.logo_label = tk.Label(self.mainframe, image=self.logo, height = 310, width=310)  
        self.logo_label.image = self.logo 
        self.logo_label.grid(row = 2, column=2,sticky="se",padx=30, pady = 10) 

    

        #Python lesson button
        #image from https://www.epl.ca/blogs/post/code-in-the-cold/
        python_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images/python_logo.PNG")
        self.python_button_img = tk.PhotoImage(file=python_path)
        self.python_lesson_button = tk.Button(self.mainframe,image = self.python_button_img,height= 150, width = 350,bg="lightblue", command=self.open_python)
        self.python_lesson_button.grid(column= 0, row = 1,sticky = "s")

        #info security lesson button
        #image from https://dxc.com/au/en/offerings/security
        infosec_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images/infosecurity_logo.PNG")
        self.infosec_img = tk.PhotoImage(file=infosec_path)
        self.infosec_button = tk.Button(self.mainframe,image=self.infosec_img,height=150,width=350,bg = "lightblue", command = self.open_infosec)
        self.infosec_button.grid(column=1,row=1,sticky = "s")

        #Introduction to ai lesson button
        intro_ai_logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images/intro_ai_logo.PNG")
        self.intro_ai_img = tk.PhotoImage(file=intro_ai_logo_path)
        self.intro_ai_button = tk.Button(self.mainframe,image = self.intro_ai_img, height=150, width=350, bg="lightblue", command = self.open_ai)
        self.intro_ai_button.grid(column=2, row=1,sticky = "s")
    
        #FORUM PLACEHOLDER
        self.forum_button = tk.Button(self.mainframe, text= "FORUM",font="Impact 30",bg = "SlateBlue1", command = self.open_forum)
        self.forum_button.grid(row=2, column=0, sticky ="ew")       
        

        self.top_bar = tk.Frame(self.master, bg="steelblue")  # Specify the background color and height
        self.top_bar.grid(row=0, column=0, sticky="new")  # Place it in the first row and expand it east-west

        
        #TOP BAR
        #Home label
        # fotnsize https://www.geeksforgeeks.org/how-to-change-the-tkinter-label-font-size/
        self.home_button = tk.Button(self.top_bar, text="HOME", bg="steelblue",font = "Impact 20", command= self.open_home)
        self.home_button.grid(row=0,column=0,padx=20,pady=20)

        #Progress bar
        self.progress_button = tk.Button(self.top_bar, text="PROGRESS", font="Impact 20", bg="lightblue", command=self.open_progress)
        self.progress_button.grid(row=0,column=1,padx=20,pady=20)

        #profile button
        self.profile_button = tk.Button(self.top_bar,text="PROFILE",font = "Impact 20", bg="mediumspringgreen",command= self.open_profile)
        self.profile_button.grid(row=0,column=2,padx=2)

        #configures the columns for the top bar
        self.top_bar.grid_columnconfigure(0, weight=1)
        self.top_bar.grid_columnconfigure(1, weight=1)
        self.top_bar.grid_columnconfigure(2, weight=1)
        self.top_bar.grid_rowconfigure(0, weight=1)


        
        

    def open_profile(self):
        from profile import Profile
        switch_frame(self, lambda master: Profile(master, self.student))

    def open_forum(self):
        from forum import Forum
        switch_frame(self,lambda master: Forum(master, self.student))
        
    def open_home(self):
        from Homepage import Homepage
        switch_frame(self, lambda master: Homepage(master, self.student))

    def open_progress(self):
        """Open a new window to display the student's progress."""
        progress_window = tk.Toplevel(self.master)  
        progress_window.title("Student Progress")
        progress_tracker = ProgressTracker(progress_window, self.student)  
        progress_window.geometry("300x100") 
    
    def open_python(self):
        sys.path.append("../Lessons")
        from Lessons.Lesson_python_accesspage import lesson_python_accesspage
        switch_frame(self,lambda master: lesson_python_accesspage(master, self.student))

    def open_ai(self):
        sys.path.append("../Lessons")
        from Lessons.Lesson_ai_accesspage import lesson_AI_accesspage
        switch_frame(self,lambda master: lesson_AI_accesspage(master, self.student))
    
    def open_infosec(self):
        sys.path.append("../Lessons")
        from Lessons.Lesson_infosecurity_accesspage import lesson_cyberattack_accesspage
        switch_frame(self,lambda master: lesson_cyberattack_accesspage(master, self.student))

if __name__ == "__main__":
    root = tk.Tk()  
    student = Student("First", "Last", "DOB", "email@example.com", "1234567890", "username", "password", 1)  # Example student instance
    homepage = Homepage(root, student)
    homepage.grid(row=0, column=0, sticky="nsew")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    homepage.mainloop()

        


    
        



    

    






    

if __name__ == "__main__":
    root = tk.Tk()  
    
    #create homepage
    homepage = Homepage(root)
    homepage.grid(row = 0, column = 0, sticky="nsew")

    #allows rows and columns to expand and contract when window is resized
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    homepage.mainloop()
