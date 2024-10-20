import sys
sys.path.append("../Lessons")
import tkinter as tk
from lesson_intro_to_AI import lesson_intro_to_AI
from lesson_ai_pros_cons import lesson_AI_pros_cons 
from lesson_ai_applications import lesson_AI_applications
sys.path.append("../GUI")
from GUI.Utilities import switch_frame

class lesson_AI_accesspage(tk.Frame):
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

        self.AI_lesson_access = tk.Label(self, text="AI Lesson Access", font=("Arial Bold", 20), bg="lightblue", fg="Black")
        self.AI_lesson_access.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.AI_lesson_1 = tk.Label(self, text="Lesson 3.1: Introduction to AI", font=label_font, bg="lightblue", fg="black")
        self.AI_lesson_1.grid(row=1, column=0, padx=10, pady=10)
        self.AI_lesson_1_button = tk.Button(self, text="Open lesson", font=button_font, command=lambda: switch_frame(self, lesson_intro_to_AI), bg="lightblue")
        self.AI_lesson_1_button.grid(row=1, column=1)

        self.AI_lesson_2 = tk.Label(self, text="Lesson 3.2: Pros and Cons of AI", font=label_font, bg="lightblue", fg="black")
        self.AI_lesson_2.grid(row=2, column=0, padx=10, pady=10)
        self.AI_lesson_2_button = tk.Button(self, text="Open lesson", font=button_font, command=lambda: switch_frame(self, lesson_AI_pros_cons), bg="lightblue")
        self.AI_lesson_2_button.grid(row=2, column=1)

        self.AI_lesson_3 = tk.Label(self, text="Lesson 3.3: Applications of AI", font=label_font, bg="lightblue", fg="black")
        self.AI_lesson_3.grid(row=3, column=0, padx=10, pady=10)
        self.AI_lesson_3_button = tk.Button(self, text="Open lesson", font=button_font, command=lambda: switch_frame(self, lesson_AI_applications), bg="lightblue")
        self.AI_lesson_3_button.grid(row=3, column=1)

        sys.path.append("../Quiz")
        from Quiz.AI_quiz_access_page import AIQuizAccessPage
        self.infosecurtiy_quiz = tk.Button(self, text="Open quiz", font=button_font, command=lambda: switch_frame(self, lambda master: AIQuizAccessPage(self.master, self.student)), bg="lightblue")
        self.infosecurtiy_quiz.grid(row=4, column=1)

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
        self.grid

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
    AI_lesson_page = lesson_AI_accesspage(root)
    AI_lesson_page.grid(sticky='nsew')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()

