"""
The homepage of EmpowerU 

"""

import tkinter as tk
import Utilities as util
from profile import Profile

class Homepage(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        util.fullscreen(self,master)
        
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
            

        self.logo = tk.PhotoImage(file="logo.png")
        self.logo_label = tk.Label(self.mainframe,image=self.logo,width = 310, height = 310)
        self.logo_label.grid(row = 2,column=2,sticky="se",padx=30,pady=10)

    

        #Python lesson button
        #image from https://www.epl.ca/blogs/post/code-in-the-cold/
        self.python_button_img = tk.PhotoImage(file="python_logo.PNG")
        #TODO add command to buttons
        self.python_lesson_button = tk.Button(self.mainframe,image = self.python_button_img,height= 150, width = 350,bg="lightblue")
        self.python_lesson_button.grid(column= 0, row = 1,sticky = "s")

        #info security lesson button
        #image from https://dxc.com/au/en/offerings/security
        self.infosec_img = tk.PhotoImage(file="infosecurity_logo.PNG")
        self.infosec_button = tk.Button(self.mainframe,image=self.infosec_img,height=150,width=350,bg = "lightblue")
        self.infosec_button.grid(column=1,row=1,sticky = "s")

        #Introduction to ai lesson button
        self.intro_ai_img = tk.PhotoImage(file="intro_ai_logo.PNG")
        self.intro_ai_button = tk.Button(self.mainframe,image = self.intro_ai_img, height=150, width=350, bg="lightblue")
        self.intro_ai_button.grid(column=2, row=1,sticky = "s")
    
        #FORUM PLACEHOLDER
        self.forum_label = tk.Label(self.mainframe,text= "FORUM PLACEHOLD",font=20,bg = "lightblue")
        self.forum_label.grid(row=2,rowspan=2, column=0)

        
        

        self.top_bar = tk.Frame(self.master, bg="steelblue")  # Specify the background color and height
        self.top_bar.grid(row=0, column=0, sticky="new")  # Place it in the first row and expand it east-west

        
        #TOP BAR
        #Home label
        # fotnsize https://www.geeksforgeeks.org/how-to-change-the-tkinter-label-font-size/
        self.home_label = tk.Label(self.top_bar, text="HOME", bg="steelblue",font = "Impact 20")
        self.home_label.grid(row=0,column=0,padx=20,pady=20)

        #Progress bar
        #TODO: progress bar
        self.progressbar_filler = tk.Label(self.top_bar,text = "PROGRESS BAR PLACEHOLDER",font = "Impact 20", bg="steelblue")
        self.progressbar_filler.grid(row=0,column=1,padx=20,pady=20)

        #profile button
        self.profile_button = tk.Button(self.top_bar,text="PROFILE",font = "Impact 20", bg="mediumspringgreen",command= self.open_profile)
        self.profile_button.grid(row=0,column=2,padx=2)

        #configures the columns for the top bar
        self.top_bar.grid_columnconfigure(0, weight=1)
        self.top_bar.grid_columnconfigure(1, weight=1)
        self.top_bar.grid_columnconfigure(2, weight=1)
        self.top_bar.grid_rowconfigure(0, weight=1)


        
        

    def open_profile(self):
        self.master.destroy()

        root = tk.Tk()  
    
        #create profile instance
        profile = Profile(root)
        profile.grid(row = 0, column = 0, sticky="nsew")

        #allows rows and columns to expand and contract when window is resized
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        
        profile.mainloop()

        
        


        


    
        



    

    






    

if __name__ == "__main__":
    root = tk.Tk()  
    
    #create homepage
    homepage = Homepage(root)
    homepage.grid(row = 0, column = 0, sticky="nsew")

    #allows rows and columns to expand and contract when window is resized
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    homepage.mainloop()
