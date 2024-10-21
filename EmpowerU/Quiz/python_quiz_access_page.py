"""
FIT1056 Project: EmpowerU
Group: Monday G1

Accesspage for Python quizzes

Written by: Ujjay

Edited by: Tashvi Vig
"""
import sys
import tkinter as tk
from GUI.Utilities import switch_frame


class PythonQuizAccessPage(tk.Frame):
    def __init__(self, master,student):
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

        self.python_quiz_name = tk.Label(self, text="Python Quiz Access", font=label_font, bg="lightblue", fg="black")
        self.python_quiz_name.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.python_quiz_name_1 = tk.Label(self, text="Data Type quiz", font=label_font, bg="lightblue", fg="black")
        self.python_quiz_name_1.grid(row=1, column=0, padx=10, pady=10)

        sys.path.append("../GUI")
        from GUI.Progress_Tracker import ProgressTracker
        sys.path.append("../Quiz")
        from Quiz.student_quiz_python_datatypes import PythonDataTypeQuizPage
        self.python_quiz_name_1_button = tk.Button(self, text="Start quiz", font=button_font, command=lambda: switch_frame(self, lambda master: PythonDataTypeQuizPage(master, ProgressTracker(self.master, self.student),self.student)), bg="lightblue")
        self.python_quiz_name_1_button.grid(row=1, column=1)

        from Quiz.student_quiz_python_loops import PythonLoopsQuizPage
        self.python_quiz_name_2 = tk.Label(self, text="Loops quiz", font=label_font, bg="lightblue", fg="black")
        self.python_quiz_name_2.grid(row=2, column=0, padx=10, pady=10)
        self.python_quiz_name_2_button = tk.Button(self, text="Start quiz", font=button_font, command=lambda: switch_frame(self, lambda master:PythonLoopsQuizPage(master, ProgressTracker(self.master, self.student), self.student)), bg="lightblue")
        self.python_quiz_name_2_button.grid(row=2, column=1)

        from Quiz.student_quiz_python_conditionals import PythonConditionalQuizPage
        self.python_quiz_name_3 = tk.Label(self, text="Conditional quiz", font=label_font, bg="lightblue", fg="black")
        self.python_quiz_name_3.grid(row=3, column=0, padx=10, pady=10)
        self.python_quiz_name_3_button = tk.Button(self, text="Start quiz", font=button_font, command=lambda: switch_frame(self, lambda master:PythonConditionalQuizPage(master, ProgressTracker(self.master, self.student),self.student)), bg="lightblue")
        self.python_quiz_name_3_button.grid(row=3, column=1)

        self.return_to_lesson_button = tk.Button(self, text="Return to Lesson", font=button_font, command=self.return_to_lesson, bg="lightblue")
        self.return_to_lesson_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def on_show(self):
        self.grid(sticky="nsew")  # Ensures the frame fills the window when shown
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
    
    def return_to_lesson(self):
        sys.path.append("../Lessons")
        from Lessons.Lesson_infosecurity_accesspage import lesson_cyberattack_accesspage
        switch_frame(self, lambda master: lesson_cyberattack_accesspage(self.master, self.student))


    
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    quiz_page = PythonQuizAccessPage(root)
    quiz_page.grid(sticky='nsew')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()

