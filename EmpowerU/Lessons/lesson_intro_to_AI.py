"""
FIT1056 Project: EmpowerU
Group: Monday G1

Lesson for Introduction of AI

Written by: Tin

"""
# Lesson 3.1 Introduction to AI
import tkinter as tk
# from Homepage import Homepage
class lesson_intro_to_AI(tk.Frame):
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
        self.lesson_label = tk.Label(self.inner_frame, text="Lesson 3.1:\nIntroduction to AI", font=("Arial Bold", 20))
        self.lesson_label.grid(row=1, column=0, sticky=tk.S, padx=10, pady=10)
        # Lesson text
        self.lesson_text = tk.Label(self.inner_frame, justify="left", text="""What is AI?
      Artificial Intelligence (AI) is a branch of computer science that aims to create machines capable 
      of performing tasks that typically require human intelligence. This includes understanding language, 
      recognizing patterns, solving problems, and making decisions. AI technologies are increasingly integrated 
      into our daily lives, from virtual assistants like Siri and Alexa to recommendation systems on streaming 
      services. 

      The development of AI has been driven by advancements in algorithms, computational power, and access 
      to vast amounts of data. By mimicking human cognitive functions, AI systems can learn from experiences, 
      adapt to new situations, and improve their performance over time. 

      1. Definition of Artificial Intelligence

      Artificial Intelligence is defined as the ability of machines to perform tasks that require human 
      intelligence. This includes tasks such as understanding natural language, recognizing patterns, and 
      making decisions. AI systems can learn from experience, adapt to new inputs, and perform tasks 
      autonomously.

      The other options, like ancient computing devices and specific programming languages, do not capture 
      the essence of AI.

      2. Narrow AI vs. General AI

      Narrow AI refers to systems designed to solve specific problems without possessing general intelligence. 
      These AI systems are effective at completing particular tasks, such as image recognition or language 
      translation, but they lack the ability to perform any intellectual task that a human can do.

      In contrast, Artificial General Intelligence aims for broader cognitive abilities, which is not the focus 
      of Narrow AI.

      3. Supervised Learning

      Supervised learning is a type of machine learning where an algorithm learns from labeled training data 
      to make predictions. An example is predicting house prices based on historical data, where the model 
      is trained on known prices to make future predictions.

      Other options, like clustering and trial-and-error learning, do not involve labeled data, which is 
      essential for supervised learning.

      4. Neural Networks

      Neural networks are a widely-used AI model inspired by the structure of the human brain. They consist of 
      interconnected layers of nodes (neurons) that process information and are particularly effective in 
      tasks such as image and speech recognition.

      Genetic algorithms and decision trees are different methods used in AI but do not replicate the 
      brain’s structure like neural networks do.

      5. Machine Learning

      Machine learning relies on using large datasets to learn patterns and make predictions. This approach 
      allows systems to improve their performance over time as they are exposed to more data. Machine learning 
      encompasses various techniques, including supervised and unsupervised learning.

      Symbolic AI and rule-based systems are traditional AI methods that do not learn from data in the same 
      way as machine learning.""", font=("Arial", 11))
        self.lesson_text.grid(row=2, column=0, sticky=tk.S, padx=10, pady=10)
    def on_inner_frame_configure(self, event):
    # Update scrollregion to include the whole inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    # Set the canvas width to match the inner frame
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw"), width=self.canvas.winfo_width())

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    quiz_page = lesson_intro_to_AI(root)
    root.mainloop()

