import tkinter as tk 
import Utilities as util

class Profile(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        util.fullscreen(self,master)

        self.mainframe = tk.Frame(self.master, bg = "lightblue")
        self.mainframe.grid(row = 0, column=0, sticky="nsew")
        



    

if __name__ == "__main__":
    root = tk.Tk()  
    
    #create homepage
    profile = Profile(root)
    profile.grid(row = 0, column = 0, sticky="nsew")

    #allows rows and columns to expand and contract when window is resized
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    profile.mainloop()
