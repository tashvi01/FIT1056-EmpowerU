def switch_frame(current_frame, FrameClass):
    """
    Clears the current frame and opens the specified frame.

    Parameter(s):
    current_frame: The frame that is currently displayed.
    FrameClass: The class of the frame to be opened.

    Return(s):
    None

    Written by: Tashvi Vig
    """
    # Clear the current frame
    for widget in current_frame.mainframe.winfo_children():
        widget.destroy()

    # Create a new frame instance and pack it
    new_frame = FrameClass(current_frame.master)
    new_frame.grid(row=0, column=0, sticky="nsew")


def fullscreen(self,master):

    """
    fullscreens the widget window

    Parameter(s):
    master: Parent window or widget

    return(s):
    None

    Written by: Tommy Nguyen
    """

    #fullscreen needs master parameter because of tk.Frame doesn't have geometry() method 
    # Fullscreen information learnt from geeksforgeeks.org 1/10/2024: https://www.geeksforgeeks.org/how-to-create-full-screen-window-in-tkinter/

    #obtaining width and height of screen
    width = self.winfo_screenwidth()
    height = self.winfo_screenheight()

    #makes window match screen geometry
    #geometry() method called with master (tk.Tk instance) instead of self which is the frame
    master.geometry(f"{width}x{height}")
