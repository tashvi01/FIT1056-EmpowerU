import tkinter as tk
from tkinter import messagebox
# from Homepage import Homepage
class PythonConditionalQuizPage(tk.Frame):
    counter = 0 # class variable to keep track of the number of times the page is opened

    def __init__(self, master):
        super().__init__(master)
        PythonConditionalQuizPage.counter += 1 # increment the counter whenever the page is opened
        
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
        self.create_question(self.inner_frame, 1, "", "1. What is the primary purpose of the `if` statement in Python?", ["To execute a block of code based on a condition", "To repeat a block of code", "To perform mathematical operations"], "To execute a block of code based on a condition")
        self.create_question(self.inner_frame, 2, "", "2. How can you execute multiple statements under a single `if` block in Python?", ["Separate statements with a semicolon", "Use the `elif` keyword", "Indent the statements to the same level"], "Indent the statements to the same level")
        self.create_question(self.inner_frame, 3, "x = 2\ny = 3\nif x > y:\n     print(x + y)", "3. What prints if the code snippet above ran?", ["5", "Nothing", "Error"], "Nothing")
        self.create_question(self.inner_frame, 4, "", "4. What is the purpose of the `elif` statement in Python?", ["To exit a loop", "To check if the previous condition is false", "To check if a condition is neither true nor false"], "To check if the previous condition is false")
        self.create_question(self.inner_frame, 5, "x = 5\nif x < 3:\n     print('X is less than 3')\nelif x == 3:\n     print('X is equal to 3')\nelse:\n     print('X is greater than 3')", "5. What would print if the code snippet above ran?", ["x is equal to 3", "x is less than 3", "x is greater than 3"], "x is greater than 3")
    

        # Button to check answers
        self.check_button = tk.Button(self.inner_frame, text="Check answers", command=self.check_answers)
        self.check_button.grid(row=25, column=0, sticky=tk.W, pady=10)
        
        # self.return_button = tk.Button(self.inner_frame, text="Return to Homepage", command=self.return_to_homepage)
        # self.return_button.grid(row=22, column=0, sticky=tk.W, pady=10)
    def on_inner_frame_configure(self, event):
        # Update scrollregion to include the whole inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        # Set the canvas width to match the inner frame
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw"), width=self.canvas.winfo_width())
    def create_question(self, parent, num, code_snippet, question_text, options, correct_answer):
        # Display code snippet in a Label widget with formatting for code
        if code_snippet:  # Only create the code label if there is a code snippet
            code_label = tk.Label(parent, text=code_snippet, bg="lightgray", fg="black", font=("Courier", 10), justify="left", anchor="w", width=40, height=8)  # Set width and height
            code_label.grid(row=num*5-5, column=0, sticky=tk.W, pady=10)  # Add extra padding to the bottom (20)
        
        # Display the question as a label
        question_var = tk.StringVar(value=question_text)
        question_label = tk.Label(parent, textvariable=question_var)
        question_label.grid(row=num*5-4, column=0, sticky=tk.W, pady=10)

        # Create the answer options as radio buttons
        answer_var = tk.StringVar()

        for i, option in enumerate(options):
            answer_option = tk.Radiobutton(parent, text=option, variable=answer_var, value=option)
            answer_option.grid(row=num*5-3+i, column=0, sticky=tk.W, padx=20)  # Add padding to separate options from the edge

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
    quiz_page = PythonConditionalQuizPage(root)
    root.mainloop()

