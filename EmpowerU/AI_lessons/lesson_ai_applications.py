# Lesson 3.3 Applications of AI
import tkinter as tk
# from Homepage import Homepage
class lesson_AI_applications(tk.Frame):
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
        self.lesson_label = tk.Label(self.inner_frame, text="Lesson 3.3:\nApplications of AI", font=("Arial Bold", 20))
        self.lesson_label.grid(row=1, column=0, sticky=tk.S, padx=10, pady=10)
        # Lesson text
        self.lesson_text = tk.Label(self.inner_frame, justify="left", text="""
      Artificial Intelligence (AI) is revolutionizing various sectors by enhancing efficiency, improving 
      decision-making, and creating new opportunities for innovation. From healthcare to finance, AI technologies 
      are being implemented to solve complex problems and streamline processes. This guide explores some of the 
      most notable applications of AI in different industries, providing examples that illustrate its impact on 
      our daily lives.

      1. AI in Healthcare

      One of the most significant applications of AI in healthcare is the use of AI-powered systems assisting 
      in medical diagnoses through image analysis. These systems analyze medical images, such as X-rays and 
      MRIs, to help detect conditions like tumors or fractures, often with greater accuracy and speed than human 
      radiologists. 

      Other examples, like automated stock trading systems and AI generating movie recommendations, do not 
      directly pertain to healthcare.

      2. AI in Finance

      In the finance industry, AI is commonly used for fraud detection by analyzing transactional data. AI 
      algorithms can identify unusual patterns and flag potentially fraudulent activities, protecting both 
      consumers and financial institutions from losses.

      While face recognition technology and writing personalized customer emails are important applications, they 
      do not capture the critical role of AI in fraud prevention.

      3. AI in Automotive Industry

      AI is widely used in the automotive industry to develop self-driving cars using sensors and machine 
      learning algorithms. These technologies enable vehicles to interpret their surroundings, make decisions, 
      and navigate autonomously, paving the way for safer and more efficient transportation.

      Manufacturing car parts using robots is a different application of automation but does not reflect the 
      advanced capabilities of AI in self-driving technology.

      4. AI in E-Commerce

      A common application of AI in e-commerce is the use of personalized product recommendations based on 
      browsing history. AI analyzes user behavior to suggest items that align with individual preferences, 
      enhancing the shopping experience and increasing sales for businesses.

      Options like using AI for customer service training and AI-generated customer product reviews do not 
      exemplify the direct impact of AI in enhancing the shopping experience through personalization.

      5. AI in Agriculture

      In agriculture, AI is applied to monitor crop health and optimize irrigation through machine learning. 
      These technologies analyze data from various sources, such as soil moisture levels and weather patterns, 
      allowing farmers to make informed decisions that maximize yield and conserve resources.

      Forecasting global economic trends and automating financial record-keeping are important but unrelated 
      to AI's specific role in agricultural practices.""", font=("Arial", 11))
        self.lesson_text.grid(row=2, column=0, sticky=tk.S, padx=10, pady=10)
    def on_inner_frame_configure(self, event):
    # Update scrollregion to include the whole inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    # Set the canvas width to match the inner frame
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw"), width=self.canvas.winfo_width())

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    quiz_page = lesson_AI_applications(root)
    root.mainloop()

