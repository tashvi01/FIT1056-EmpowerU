import tkinter as tk
from student_quiz_infosecurity_info_on_cyberattacks import InfoSecuityInfoOnCyberattacksQuizPage
from student_quiz_infosecurity_preventing_cyber_attacks import InfoSecuityPreventingCyberAttacksQuizPage 
from student_quiz_infosecurity_help_during_cyber_attacks import InfoSecuityHelpDuringCyberAttacksQuizPage
from Utilities import switch_frame

class AIQuizAccessPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="lightblue")
        self.master = master
        self.mainframe = tk.Frame(master, padx=3, pady=12, bg="lightblue")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        label_font = ("Helvetica", 16, "bold")
        button_font = ("Helvetica", 12, "bold")

        self.python_quiz_name = tk.Label(self, text="Info Security Quiz Access", font=label_font, bg="lightblue", fg="black")
        self.python_quiz_name.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.python_quiz_name_1 = tk.Label(self, text="Info on cyber attacks quiz", font=label_font, bg="lightblue", fg="black")
        self.python_quiz_name_1.grid(row=1, column=0, padx=10, pady=10)
        self.python_quiz_name_1.button = tk.Button(self, text="Start quiz", font=button_font, command=lambda: switch_frame(self, InfoSecuityInfoOnCyberattacksQuizPage), bg="lightblue")
        self.python_quiz_name_1.button.grid(row=1, column=1)

        self.python_quiz_name_2 = tk.Label(self, text="Preventing cyber attacks quiz", font=label_font, bg="lightblue", fg="black")
        self.python_quiz_name_2.grid(row=2, column=0, padx=10, pady=10)
        self.python_quiz_name_2.button = tk.Button(self, text="Start quiz", font=button_font, command=lambda: switch_frame(self, InfoSecuityPreventingCyberAttacksQuizPage), bg="lightblue")
        self.python_quiz_name_2.button.grid(row=2, column=1)

        self.python_quiz_name_3 = tk.Label(self, text="Help during cyber attacks quiz", font=label_font, bg="lightblue", fg="black")
        self.python_quiz_name_3.grid(row=3, column=0, padx=10, pady=10)
        self.python_quiz_name_3.button = tk.Button(self, text="Start quiz", font=button_font, command=lambda: switch_frame(self, InfoSecuityHelpDuringCyberAttacksQuizPage), bg="lightblue")
        self.python_quiz_name_3.button.grid(row=3, column=1)

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
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    quiz_page = AIQuizAccessPage(root)
    quiz_page.grid(sticky='nsew')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()

