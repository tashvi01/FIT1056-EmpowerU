"""
FIT1056 Project: EmpowerU
Group: Monday G1

Lesson for Datatypes

Written by: Tin

"""
# Lesson 1.1 Data Types
import tkinter as tk
# from Homepage import Homepage
class lesson_DataTypes(tk.Frame):
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
        self.lesson_label = tk.Label(self.inner_frame, text="Lesson 1.1:\nValues and Data Types", font=("Arial Bold", 20))
        self.lesson_label.grid(row=1, column=0, sticky=tk.S, padx=10, pady=10)
        # Lesson text
        self.lesson_text = tk.Label(self.inner_frame, justify="left", text="""        A value is one of the fundamental things that a program manipulates (like a word or number). 
        Values can be 10 (as a result of 5*2 or 7+3) or 'Hello World!'. These values are classifed into 
        different data types, 10 is an integer and 'Hello World!' is a string because it contains a string 
        or sequence of letters! They can be identified as being enclosed in quotation marks.
                                    
        This means an integer could be a string depending on how you want it to be interpreted. We can specify 
        this in the programs we write! We can specify numbers as a literal by typing it in directly eg. 5 42 and 
        we specify words by enclosing the characters in quotation marks. During the execution of a program, 
        the Python interpreter creates an internal representation of the literals specified in the program
        and it can then manipulate them. These internal representations are called values or objects.
                                    
        We don't see these internal representations unless we tell Python to "print" it out for us by using a
        print function to see a printed representation in the output window. For literals, it would show 
        exactly the same, however, for strings, their printed representation omits the quotation marks.
        If you are not sure what class (data type) a value falls into, Python has a function called type which 
        can tell you. Numbers with a decimal point belong to a class called float, because these numbers are 
        represented in a format called floating-point.
                                    
        There are also other objects called lists and dictionaries which have their own special representations
        for specifying objects as a literal in a program, and for displaying an object when you print it. There
        are more complex objects that we will not cover as that is for more advanced Python learners.
        
        Sometimes it is necessary to convert values from one type to another. Python provides a few simple function 
        that will allow us to do that. The functions int, float and str will (attempt to) convert their arguments 
        into types int, float and str respectively. We call these type conversion functions.
                                    
        The int function can take a floating point number or a string, and turn it into an int. For floating point 
        numbers, it discards the decimal portion of the number — a process we call truncation towards zero on the 
        number line.
        
        The type converter float can turn an integer, a float, or a syntactically legal string into a float.
        
        The type converter str turns its argument into a string. Remember that when we print a string, 
        the quotes are removed in the output window.
                                    
        One of the most powerful features of a programming language is the ability to manipulate variables. 
        A variable is a name that refers to a value. Assignment statements create new variables and also give 
        them values to refer to.
                                    
        message = "What's up, Doc?"
        n = 17
        pi = 3.14159
                                    
        This example makes three assignments. The first assigns the string value "What's up, Doc?" to a new 
        variable named message. The second assigns the integer 17 to n, and the third assigns the floating-point 
        number 3.14159 to a variable called pi.
                                    
        The assignment token, =, should not be confused with equality (we will see later that equality uses the == token). 
        The assignment statement links a name, on the left hand side of the operator, with a value, on the right hand side. 
        This is why you will get an error if you enter: 17 = n
        
        When reading or writing code, say to yourself “n is assigned 17” or “n gets the value 17” or “n is a reference to 
        the object 17” or “n refers to the object 17”. Don’t say “n equals 17”.
        
        The tokens +, -, and *, and the use of parentheses for grouping, mean in Python what they mean in mathematics. 
        The asterisk (*) is the token for multiplication, and ** is the token for exponentiation. Addition, subtraction, 
        multiplication, and exponentiation all do what you expect.
                                    
        In Python 3, which we will be using, the division operator / produces a floating point result (even if the result 
        is an integer; 4/2 is 2.0). If you want truncated division, which ignores the remainder, you can use the // 
        operator (for example, 5//2 is 2).
        
        print(9 / 5)
        print(5 / 9)
        print(9 // 5)
        Pay particular attention to the examples above. Note that 9//5 truncates rather than rounding, so it produces 
        the value 1 rather than 2.

        The truncated division operator, //, also works on floating point numbers. It truncates to the nearest integer, 
        but still produces a floating point result. Thus 7.0 // 3.0 is 2.0.
        
        The modulus operator, sometimes also called the remainder operator or integer remainder operator works on 
        integers (and integer expressions) and yields the remainder when the first operand is divided by the second. 
        In Python, the modulus operator is a percent sign (%). The syntax is the same as for other operators.
        
        Incrementing and decrementing are such common operations that programming languages often include special syntax 
        for it. In Python += is used for incrementing, and -= for decrementing. In some other languages, there is even a 
        special syntax ++ and -- for incrementing or decrementing by 1. Python does not have such a special syntax. To 
        increment x by 1 you have to write x += 1 or x = x + 1.
        
        Some Python collection types are able to change and some are not. If a type is able to change, then it is said to 
        be mutable. If the type is not able to change then it is said to be immutable. This will be expanded below.
        
        Unlike strings, lists are mutable. This means we can change an item in a list by accessing it directly as part of 
        of the assignment statement. Using the indexing operator (square brackets) on the left side of an assignment, we
        can update one of the list items.
        
        fruit = ["banana", "apple", "cherry"]
        print(fruit)

        fruit[0] = "pear"
        fruit[-1] = "orange"
        print(fruit)
        An assignment to an element of a list is called item assignment. Item assignment does not work for strings. 
        Recall that strings are immutable.""", font=("Arial", 11))
        self.lesson_text.grid(row=2, column=0, sticky=tk.S, padx=10, pady=10)
    def on_inner_frame_configure(self, event):
    # Update scrollregion to include the whole inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    # Set the canvas width to match the inner frame
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw"), width=self.canvas.winfo_width())

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    quiz_page = lesson_DataTypes(root)
    root.mainloop()

