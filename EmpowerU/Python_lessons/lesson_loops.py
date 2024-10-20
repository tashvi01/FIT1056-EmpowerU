# Lesson 1.3 Loops
import tkinter as tk
# from Homepage import Homepage
class lesson_Loops(tk.Frame):
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
        self.lesson_label = tk.Label(self.inner_frame, text="Lesson 1.3:\nLoops", font=("Arial Bold", 20))
        self.lesson_label.grid(row=1, column=0, sticky=tk.S, padx=10, pady=10)
        # Lesson text
        self.lesson_text = tk.Label(self.inner_frame, justify="left", text="""        Computers are often used to automate repetitive tasks. Repeating identical or similar tasks without 
        making errors is something that computers do well and people do poorly.

        Repeated execution of a sequence of statements is called iteration. Because iteration is 
        so common, Python provides several language features to make it easier. In this section we 
        are going to look at the while statement.
        
        The while statement provides a general mechanism for iterating. Similar to the if statement, 
        it uses a boolean expression to control the flow of execution. The body of while will be repeated 
        as long as the controlling boolean expression evaluates to True.
        
        We can use the while loop to create any type of iteration we wish based on a condition. For example, 
        the program in the video above could be written using while.  We will create a variable called a_number 
        and initialize it to 1, the first number in the summation. Every iteration will add a_number to the 
        running total until all the values have been used. In order to control the iteration, we must create a 
        boolean expression that evaluates to True as long as we want to keep adding values to our running total. 
        In this case, as long as a_number is less than or equal to the value n, we should keep going.
        
        # Return the sum of 1+2+3 ... n 
        total  = 0
        n = 10
        a_number = 1
        while a_number <= n:
            total = total + a_number
            a_number = a_number + 1
            print(total)
        
        You can almost read the while statement as if it were in natural language. It means, while a_number is less 
        than or equal to n, continue executing the body of the loop. Within the body, each time, update total 
        during each iteration and increment a_number. After the body of the loop, we go back up to the condition of 
        the while and reevaluate it. When a_number becomes greater than n, the condition fails and flow of control 
        continues to the return statement.
        
        As a programmer you often want to execute a certain block of code over and over again or go through sequences 
        of data one by one performing some set of operations each time. This practice is known as iteration, and 
        iterators are one of the most powerful fundamental tools available to programmers.

        Iterables are objects that can be iterated upon, meaning they contain a set of countable values that can be
        traversed in order. Lists, strings, tuples and dictionaries are all examples of iterable Python objects.

        We can traverse through iterators using the first type of loop we'll be covering, the for loop.

        A for loop allows you to iterate through an iterable, such as:

        Iterating through each element of a list or tuple

        Iterating through each character of a string

        Iterating through each key and its associated value in a dictionary

        This allows us to go through a set of items one by one and perform operations on them. As you can 
        imagine, this is a crucial processing pattern in almost all software around the world.

        In Python, the for statement allows us to write programs that implement iteration. As a simple example, 
        let’s say we have some friends, and we’d like to send them each an email inviting them to our party. 
        We don’t quite know how to send email yet, so for the moment we’ll just print a message for each friend.
        
        for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
            print("Hi", name, "Please come to my party on Saturday!")
        Here’s how it works:

            name in this for statement is called the loop variable or, alternatively, the iterator variable.

            The list of names in the square brackets is the sequence over which we will iterate.

            Line 2 is the loop body. The loop body is always indented. The indentation determines exactly what 
            statements are “in the loop”. The loop body is performed one time for each name in the list.

            On each iteration or pass of the loop, first a check is done to see if there are still more items to 
            be processed. If there are none left (this is called the terminating condition of the loop), the loop 
            has finished. Program execution continues at the next statement after the loop body.

            If there are items still to be processed, the loop variable is updated to refer to the next item in 
            the list. This means, in this case, that the loop body is executed here 7 times, and each time name 
            will refer to a different friend.

            At the end of each execution of the body of the loop, Python returns to the for statement, to see if 
            there are more items to be handled.

            The overall syntax is for <loop_var_name> in <sequence>:

            Between the words for and in, there must be a variable name for the loop variable. You can’t put a 
            whole expression there.

            A colon is required at the end of the line

            After the word in and before the colon is an expression that must evaluate to a sequence 
            (e.g, a string or a list or a tuple). It could be a literal, or a variable name, or a more complex 
            expression.""", font=("Arial", 11))
        self.lesson_text.grid(row=2, column=0, sticky=tk.S, padx=10, pady=10)
    def on_inner_frame_configure(self, event):
    # Update scrollregion to include the whole inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    # Set the canvas width to match the inner frame
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw"), width=self.canvas.winfo_width())

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    quiz_page = lesson_Loops(root)
    root.mainloop()

