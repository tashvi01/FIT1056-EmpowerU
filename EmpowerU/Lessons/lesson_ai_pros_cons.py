"""
FIT1056 Project: EmpowerU
Group: Monday G1

Lesson for AI Pros and Cons

Written by: Tin

"""
# Lesson 3.2 AI Pros and Cons
import tkinter as tk
# from Homepage import Homepage
class lesson_AI_pros_cons(tk.Frame):
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
        self.lesson_label = tk.Label(self.inner_frame, text="Lesson 3.2:\nPros and Cons of AI", font=("Arial Bold", 20))
        self.lesson_label.grid(row=1, column=0, sticky=tk.S, padx=10, pady=10)
        # Lesson text
        self.lesson_text = tk.Label(self.inner_frame, justify="left", text="""
      As Artificial Intelligence (AI) becomes increasingly integrated into various sectors, it is important to 
      understand its advantages and disadvantages. AI has the potential to transform industries by enhancing 
      productivity and improving decision-making. However, it also raises significant ethical concerns and 
      poses risks to employment. This guide outlines the key pros and cons of AI to help you understand 
      its impact on society and the workplace.

      1. Advantages of AI in the Workplace

      One of the primary advantages of AI in the workplace is the reduction in human error for repetitive tasks. 
      AI systems can perform consistent and precise operations, minimizing mistakes that typically arise from 
      human fatigue or distraction. By automating routine processes, organizations can enhance productivity and 
      focus their human resources on more complex tasks that require creativity and critical thinking.

      Other options, such as decreased employee training and the elimination of all manual labor jobs, do not 
      accurately reflect the broader benefits of AI.

      2. Potential Disadvantages of AI

      A significant disadvantage of AI is that it lacks creativity and emotional intelligence. While AI systems 
      can analyze data and perform tasks efficiently, they do not possess the ability to understand human emotions 
      or think outside the box. This limitation can hinder their effectiveness in roles that require empathy or 
      innovative problem-solving.

      Unlike the false notion that AI systems can adapt without data or that they reduce the need for datasets, 
      these factors are critical to the successful implementation of AI technologies.

      3. Risks Associated with AI

      One of the major risks associated with AI is the potential loss of jobs due to automation. As AI systems 
      become more capable of performing tasks traditionally done by humans, there is concern about the displacement 
      of workers in various industries. While AI can create new job opportunities, the transition may lead to 
      significant workforce challenges in the short term.

      The other options, like increased employment in manual jobs and increased human cognitive abilities, do not 
      accurately represent the risks associated with AI.

      4. Ethical Concerns in AI Development

      A key ethical concern when developing AI is that AI systems can perpetuate biases present in training data. 
      If the data used to train AI models is biased, the AI can produce discriminatory outcomes, leading to unfair 
      treatment in critical areas like hiring or lending.

      While AI systems can reduce operational costs and improve accuracy in specific tasks, these benefits do not 
      outweigh the ethical implications of biased algorithms.

      5. AI in Healthcare

      In the healthcare sector, a significant pro of AI is that it can assist doctors by providing faster and 
      more accurate diagnoses. AI technologies, such as machine learning algorithms, can analyze vast amounts 
      of medical data to identify patterns and support clinical decision-making.

      It is essential to note that AI cannot guarantee 100% accurate treatments or diagnose diseases with 
      complete autonomy; human oversight remains crucial in healthcare applications to ensure safety and efficacy.""", font=("Arial", 11))
        self.lesson_text.grid(row=2, column=0, sticky=tk.S, padx=10, pady=10)
    def on_inner_frame_configure(self, event):
    # Update scrollregion to include the whole inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    # Set the canvas width to match the inner frame
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw"), width=self.canvas.winfo_width())

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    quiz_page = lesson_AI_pros_cons(root)
    root.mainloop()

