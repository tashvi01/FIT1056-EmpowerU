"""
FIT1056 Project: EmpowerU
Group: Monday G1

Lesson for Conditionals

Written by: Tin

"""
# Lesson 1.2 Conditionals
import tkinter as tk
# from Homepage import Homepage
class lesson_Conditionals(tk.Frame):
    counter = 0 # class variable to keep track of the number of times the page is opened

    def __init__(self, master):
        super().__init__(master)

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
        self.canvas.grid_columnconfigure(0, weight=1)
        self.canvas.grid_rowconfigure(0, weight=1)

        # Scrollbar for the canvas
        self.scrollbar = tk.Scrollbar(self.mainframe, command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Frame inside the canvas
        self.inner_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw", width=master.winfo_screenwidth(), height=master.winfo_screenheight())
        self.inner_frame.bind("<Configure>", self.on_inner_frame_configure)

        # Make inner_frame expand to fill the canvas
        self.inner_frame.grid_columnconfigure(0, weight=1)

        # Content within the inner_frame
        self.logo = tk.PhotoImage(file="../images/logo.png")
        self.label = tk.Label(self.inner_frame, image=self.logo, width=750, height=300)
        self.label.image = self.logo
        self.label.grid(row=0, column=0, sticky=tk.NS, pady=10)
        # Lesson label
        self.lesson_label = tk.Label(self.inner_frame, text="Lesson 1.2:\nConditionals", font=("Arial Bold", 20))
        self.lesson_label.grid(row=1, column=0, sticky=tk.S, padx=10, pady=10)
        # Lesson text
        self.lesson_text = tk.Label(self.inner_frame, justify="left", text="""        You will encounter more advanced functionalities and subtle changes in programs than the ones you 
        are likely capable of at the moment. For example, a messaging app might only set a message’s title bold 
        if it has not been read by the user. Or a video game needs to update the position of all the characters 
        that are not asleep. This is done with something called a conditional statement.
        
        The Python type for storing true and false values is called bool, named after the British mathematician, 
        George Boole. George Boole created Boolean Algebra, which is the basis of all modern computer arithmetic.

        There are only two Boolean values. They are True and False. Capitalization is important, since true and 
        false are not boolean values (remember Python is case sensitive).
        A Boolean expression is an expression that evaluates to a Boolean value. The equality operator, ==, 
        compares two values and produces a Boolean value related to whether the two values are equal to one another.
                                    
        print(5 == 5)
        print(5 == 6)
        
        In the first statement, the two operands are equal, so the expression evaluates to True. In the second 
        statement, 5 is not equal to 6, so we get False.
                    
        Although these operations are probably familiar to you, the Python symbols are different from the 
        mathematical symbols. A common error is to use a single equal sign (=) instead of a double equal sign (==). 
        Remember that = is an assignment operator and == is a comparison operator. Also, there is no such thing 
        as =< or =>. Note too that an equality test is symmetric, but assignment is not. For example, if a == 7 
        then 7 == a. But in Python, the statement a = 7 is legal and 7 = a is not.
        
        There are three logical operators: and, or, and not. All three operators take Boolean operands and produce 
        Boolean values. The semantics (meaning) of these operators is similar to their meaning in English:

        x and y 
        is True if both x and y are True. Otherwise, and produces False.

        x or y 
        yields True if x or y or both are True. Only if both operands are False does or yield False.

        not x 
        yields False if x is True, and vice versa.
                                    
        x = 5
        print(x > 0 and x < 10)
        The expression x > 0 and x < 10 is True only if x is greater than 0 and at the same time, x is less than 10. In 
        other words, this expression is True if x is between 0 and 10, not including the endpoints.
                                    
        In order to write useful programs, we almost always need the ability to check conditions and change the behavior 
        of the program accordingly. Selection statements, sometimes also referred to as conditional statements, give us 
        this ability. The simplest form of selection is the if statement. This is sometimes referred to as binary 
        selection since there are two possible paths of execution.
        
        The syntax for an if/elif/else statement looks like this:

        if BOOLEAN EXPRESSION:
            STATEMENTS_1 # executed if condition evaluates to True
        elif BOOLEAN EXPRESSION:                                                       
            STATEMENTS_2 # executed if condition evaluates to True when the condition before it is false
        else:
            STATEMENTS_3 # executed if condition before it evaluates to False (and is reached)
                                    
        The boolean expression after the if statement is called the condition. If it is true, then the indented 
        statements get executed. If not, then the condition of elif is checked. It it is true then the indented
        statements get executed. If not, finally the statements indented under the else clause get executed.
        (elif is a combination of else and if, get it?)
                                    
        The if statement consists of a header line and a body. The header line begins with the keyword if followed by a 
        boolean expression and ends with a colon (:).

        The indented statements that follow are called a block. The first unindented statement marks the end of the block.

        Each of the statements inside the first block of statements is executed in order if the boolean expression 
        evaluates to True. The entire first block of statements is skipped if the boolean expression evaluates to False, 
        and instead all the statements under the else clause are executed.

        There is no limit on the number of statements that can appear under the two clauses of an if statement, but 
        there has to be at least one statement in each block.
        
        Another form of the if statement is one in which all other clauses are omitted entirely. This creates what is 
        sometimes called unary selection. In this case, when the condition evaluates to True, the statements are 
        executed. Otherwise the flow of execution continues to the statement after the body of the if.""", font=("Arial", 11))
        self.lesson_text.grid(row=2, column=0, sticky=tk.S, padx=10, pady=10)
    def on_inner_frame_configure(self, event):
    # Update scrollregion to include the whole inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    # Set the canvas width to match the inner frame
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw"), width=self.canvas.winfo_width())

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    quiz_page = lesson_Conditionals(root)
    root.mainloop()

