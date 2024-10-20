import sys
sys.path.append("../Lessons")
import tkinter as tk
from lesson_datatypes import lesson_DataTypes
from lesson_conditionals import lesson_Conditionals 
from lesson_loops import lesson_Loops
sys.path.append("../GUI")
from GUI.Utilities import switch_frame
from GUI.Progress_Tracker import ProgressTracker

class lesson_python_accesspage(tk.Frame):
    def __init__(self, master, student):
        super().__init__(master, bg="lightblue")
        self.master = master
        self.student = student
        self.mainframe = tk.Frame(master, padx=3, pady=12, bg="lightblue")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        label_font = ("Helvetica", 16, "bold")
        button_font = ("Helvetica", 12, "bold")

        self.python_lesson_access = tk.Label(self, text="Python Lesson Access", font=("Arial Bold", 20), bg="lightblue", fg="Black")
        self.python_lesson_access.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.python_lesson_1 = tk.Label(self, text="Lesson 1.1: Data Types", font=label_font, bg="lightblue", fg="black")
        self.python_lesson_1.grid(row=1, column=0, padx=10, pady=10)
        self.python_lesson_1.button = tk.Button(self, text="Open lesson", font=button_font, command=lambda: switch_frame(self, lesson_DataTypes), bg="lightblue")
        self.python_lesson_1.button.grid(row=1, column=1)

        self.python_lesson_2 = tk.Label(self, text="Lesson 1.2: Conditionals", font=label_font, bg="lightblue", fg="black")
        self.python_lesson_2.grid(row=2, column=0, padx=10, pady=10)
        self.python_lesson_2.button = tk.Button(self, text="Open lesson", font=button_font, command=lambda: switch_frame(self, lesson_Conditionals), bg="lightblue")
        self.python_lesson_2.button.grid(row=2, column=1)

        self.python_lesson_3 = tk.Label(self, text="Lesson 1.3: Loops", font=label_font, bg="lightblue", fg="black")
        self.python_lesson_3.grid(row=3, column=0, padx=10, pady=10)
        self.python_lesson_3.button = tk.Button(self, text="Open lesson", font=button_font, command=lambda: switch_frame(self, lesson_Loops), bg="lightblue")
        self.python_lesson_3.button.grid(row=3, column=1)

        sys.path.append("../Quiz")
        from Quiz.python_quiz_access_page import PythonQuizAccessPage
        self.python_quiz = tk.Button(self, text="Open quiz", font=button_font, command=lambda: switch_frame(self, lambda master: PythonQuizAccessPage(self.master, self.student)), bg="lightblue")
        self.python_quiz.grid(row=4, column=1)

        from GUI.Homepage import Homepage  
        self.return_button = tk.Button(self, text="Return to Homepage", font=button_font, command=self.return_to_homepage, bg="lightblue")
        self.return_button.grid(row=5, column=1)

        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def on_show(self):
        self.grid(sticky="nsew")  # Ensures the frame fills the window when shown
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

    def return_to_homepage(self):
        sys.path.append("../GUI")
        from GUI.Homepage import Homepage  
        switch_frame(self, lambda master: Homepage(master, self.student))

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    python_lesson_page = lesson_python_accesspage(root)
    python_lesson_page.grid(sticky='nsew')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()

