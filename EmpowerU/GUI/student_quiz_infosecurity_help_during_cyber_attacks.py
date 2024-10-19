import tkinter as tk
from tkinter import messagebox
# from Homepage import Homepage
class InfoSecuityHelpDuringCyberAttacksQuizPage(tk.Frame):
    counter = 0 # class variable to keep track of the number of times the page is opened

    def __init__(self, master):
        super().__init__(master)
        InfoSecuityHelpDuringCyberAttacksQuizPage.counter += 1 # increment the counter whenever the page is opened
        
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
        self.create_question(self.inner_frame, 1, "1. What is the first step you should take if you suspect a cyber attack on your system?", ["Ignore it and hope it resolves itself", "Restart the system to refresh all processes", "Disconnect from the internet to prevent further unauthorized access"], "Disconnect from the internet to prevent further unauthorized access")
        self.create_question(self.inner_frame, 2, "2. If you receive a suspicious email or notice unusual account activity, which of the following is the most appropriate action?", ["Delete the email immediately and forget about it", "Report the incident to your IT or security team", "Forward the email to friends for their opinions"], "Report the incident to your IT or security team")
        self.create_question(self.inner_frame, 3, "3. What should you do if you suspect malware has infected your device?", ["Delete all files manually to remove the malware", "Run a full malware scan using up-to-date antivirus software", "Close all applications and continue using the device"], "Run a full malware scan using up-to-date antivirus software")
        self.create_question(self.inner_frame, 4, "4. Which of the following actions should you take if you suspect that your passwords have been compromised in a cyber attack?", ["Change your passwords immediately and enable multi-factor authentication (MFA)", "Disable your accounts temporarily", "Continue using the same passwords to avoid confusion"], "Change your passwords immediately and enable multi-factor authentication (MFA)")
        self.create_question(self.inner_frame, 5, "5. In the event of a cyber attack, why is it important to collect evidence?", ["To find and confront the attacker personally", "To create a new set of security protocols based on the attacker's method", "To improve the chances of prosecution and recovery in legal and forensic investigations"], "To improve the chances of prosecution and recovery in legal and forensic investigations")

        # Button to check answers
        self.check_button = tk.Button(self.inner_frame, text="Check answers", command=self.check_answers)
        self.check_button.grid(row=21, column=0, sticky=tk.W, pady=10)
        
        # self.return_button = tk.Button(self.inner_frame, text="Return to Homepage", command=self.return_to_homepage)
        # self.return_button.grid(row=22, column=0, sticky=tk.W, pady=10)
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
    # Uncomment when Tom remakes the homepage
    # def return_to_homepage(self):
    #     student_homepage = Homepage(self.master)
    #     self.destroy()
    #     student_homepage.fullscreen(self.master)
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    quiz_page = InfoSecuityHelpDuringCyberAttacksQuizPage(root)
    root.mainloop()

