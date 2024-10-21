"""
FIT1056 Project: EmpowerU
Group: Monday G1

Quiz for Cyberattack prevention

Written by: Ujjay

Edited by: Tashvi Vig
"""
import sys
import tkinter as tk
from tkinter import messagebox
from GUI.Utilities import switch_frame
class InfoSecuityPreventingCyberAttacksQuizPage(tk.Frame):
    counter = 0 # class variable to keep track of the number of times the page is opened

    def __init__(self, master, progress_tracker,student):
        super().__init__(master)
        InfoSecuityPreventingCyberAttacksQuizPage.counter += 1 # increment the counter whenever the page is opened
        self.progress_tracker = progress_tracker
        self.student = student
        
        # Frame that contains canvas and scrollbar
        self.mainframe = tk.Frame(master, padx=3, pady=12,bg="lightblue")
        self.mainframe.grid(column=0, row=0, sticky="nsew")

        # Configure grid expansion
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.grid_rowconfigure(0, weight=1)

        # Canvas for scrolling content
        self.canvas = tk.Canvas(self.mainframe,bg="lightblue")
        self.canvas.grid(column=0, row=0, sticky="nsew")

        # Scrollbar for the canvas
        self.scrollbar = tk.Scrollbar(self.mainframe, command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Frame inside the canvas
        self.inner_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        self.inner_frame.bind("<Configure>", self.on_inner_frame_configure)

        # Make inner_frame expand to fill the canvas
        self.inner_frame.grid_columnconfigure(0, weight=1)

        # Content within the inner_frame
        self.logo = tk.PhotoImage(file="../images/logo.png")
        self.label = tk.Label(self.inner_frame, image=self.logo, width=750, height=300)
        self.label.image = self.logo
        self.label.grid(row=0, column=0, sticky=tk.NS, pady=10)

        # Example questions
        self.create_question(self.inner_frame, 1, "1. What is the primary purpose of a firewall in preventing cyber attacks?", ["Encrypting data for secure storage", "Blocking unauthorized access to or from a private network", "Storing passwords securely"], "Blocking unauthorized access to or from a private network")
        self.create_question(self.inner_frame, 2, "2. How does two-factor authentication (2FA) improve security?", ["It requires both a password and a secondary factor (such as a phone or fingerprint) for access", "It creates a backup of your data in the cloud", "It doubles the strength of your password"], "It requires both a password and a secondary factor (such as a phone or fingerprint) for access")
        self.create_question(self.inner_frame, 3, "3. Which of the following is a key method to prevent phishing attacks?", ["Using an ad-blocker on all browsers", "Educating users about recognizing suspicious emails and avoiding clicking on unknown links", "Setting up automated responses to all unknown email senders"], "Educating users about recognizing suspicious emails and avoiding clicking on unknown links")
        self.create_question(self.inner_frame, 4, "4. What is the role of antivirus software in preventing cyber attacks?", ["Encrypting sensitive files", "Detecting and removing malware such as viruses, Trojans, and worms", "Preventing unauthorized users from accessing the network"], "Detecting and removing malware such as viruses, Trojans, and worms")
        self.create_question(self.inner_frame, 5, "5. What is the benefit of implementing multi-factor authentication (MFA)?", ["It eliminates the need for passwords", "It automatically encrypts all communications between devices", "It ensures that attackers cannot gain access even if they have compromised a user's password"], "It ensures that attackers cannot gain access even if they have compromised a user's password")

        # Button to check answers
        self.check_button = tk.Button(self.inner_frame, text="Check answers", command=self.check_answers)
        self.check_button.grid(row=21, column=0, sticky=tk.W, pady=10)
        
        self.return_button = tk.Button(self.inner_frame, text="Return to Lesson", command=self.return_to_lesson)
        self.return_button.grid(row=21, column=1, sticky=tk.W, pady=10)

    def on_inner_frame_configure(self, event):
        # Update scrollregion to include the whole inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        # Set the canvas width to match the inner frame
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw"), width=self.canvas.winfo_width())

    def create_question(self, parent, num, question_text, options, correct_answer):
        question_var = tk.StringVar(value=question_text)
        answer_var = tk.StringVar()

        question_label = tk.Label(parent, textvariable=question_var)
        question_label.grid(row=num*4-3, column=0, sticky=tk.W, pady=10)

        for i, option in enumerate(options):
            answer_option = tk.Radiobutton(parent, text=option, variable=answer_var, value=option)
            answer_option.grid(row=num*4-2+i, column=0, sticky=tk.W)

        # Store references for checking
        setattr(self, f'answer{num}', answer_var)
        setattr(self, f'correct_answer{num}', correct_answer)

    def check_answers(self):
        correct = 0
        for i in range(1, 6):
            if getattr(self, f'answer{i}').get() == getattr(self, f'correct_answer{i}'):
                correct += 1

        if correct == 5:
            messagebox.showinfo("Quiz Result", "Congratulations, you scored 5/5!")
        else:
            messagebox.showinfo("Quiz Result", f"Sorry, you scored {correct}/5.")

        self.progress_tracker.increment_progress()
    
    def return_to_lesson(self):
        sys.path.append("../Lessons")
        from Lessons.Lesson_infosecurity_accesspage import lesson_cyberattack_accesspage
        switch_frame(self, lambda master: lesson_cyberattack_accesspage(self.master, self.student))

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    quiz_page = InfoSecuityPreventingCyberAttacksQuizPage(root)
    root.mainloop()

