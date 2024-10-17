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