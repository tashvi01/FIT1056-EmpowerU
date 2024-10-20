import tkinter as tk
from lesson_cyberattacks import lesson_cyberattacks
from lesson_cyberattack_types import lesson_cyberattacks_types 
from lesson_cyberattacks_defense import lesson_cyberattacks_defense
from Utilities import switch_frame

class lesson_cyberattack_accesspage(tk.Frame):
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

        self.infosecurity_lesson_access = tk.Label(self, text="Infosecurity Lesson Access", font=("Arial Bold", 20), bg="lightblue", fg="Black")
        self.infosecurity_lesson_access.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.infosecurity_lesson_1 = tk.Label(self, text="Lesson 2.1: Cyberattacks", font=label_font, bg="lightblue", fg="black")
        self.infosecurity_lesson_1.grid(row=1, column=0, padx=10, pady=10)
        self.infosecurity_lesson_1.button = tk.Button(self, text="Open lesson", font=button_font, command=lambda: switch_frame(self, lesson_cyberattacks), bg="lightblue")
        self.infosecurity_lesson_1.button.grid(row=1, column=1)

        self.infosecurity_lesson_2 = tk.Label(self, text="Lesson 2.2: Cyberattack Types", font=label_font, bg="lightblue", fg="black")
        self.infosecurity_lesson_2.grid(row=2, column=0, padx=10, pady=10)
        self.infosecurity_lesson_2.button = tk.Button(self, text="Open lesson", font=button_font, command=lambda: switch_frame(self, lesson_cyberattacks_types), bg="lightblue")
        self.infosecurity_lesson_2.button.grid(row=2, column=1)

        self.infosecurity_lesson_3 = tk.Label(self, text="Lesson 2.3: Cyberattack Prevention", font=label_font, bg="lightblue", fg="black")
        self.infosecurity_lesson_3.grid(row=3, column=0, padx=10, pady=10)
        self.infosecurity_lesson_3.button = tk.Button(self, text="Open lesson", font=button_font, command=lambda: switch_frame(self, lesson_cyberattacks_defense), bg="lightblue")
        self.infosecurity_lesson_3.button.grid(row=3, column=1)

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
    infosecurity_access_page = lesson_cyberattack_accesspage(root)
    infosecurity_access_page.grid(sticky='nsew')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()

