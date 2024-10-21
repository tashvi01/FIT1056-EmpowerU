"""
FIT1056 Project: EmpowerU
Group: Monday G1

Lesson for Cyberattacks Types

Written by: Tin

"""
# Lesson 2.2 Cyberattack Types
import tkinter as tk
# from Homepage import Homepage
class lesson_cyberattacks_types(tk.Frame):
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
        self.lesson_label = tk.Label(self.inner_frame, text="Lesson 2.2:\nInfosecurity Cyberattack Types", font=("Arial Bold", 20))
        self.lesson_label.grid(row=1, column=0, sticky=tk.S, padx=10, pady=10)
        # Lesson text
        self.lesson_text = tk.Label(self.inner_frame, justify="left", text="""      Common Attack Types and How They Work
        In today's digital age, it's essential to understand the most common types of cyberattacks and how they work. 
        This guide will introduce key cybersecurity terms and explain different attack methods, allowing you to make 
        informed decisions when faced with potential threats.

        1. Phishing Attacks

        Phishing is a type of attack where the attacker pretends to be a legitimate entity, like a bank or company, to 
        trick individuals into revealing personal information. For example, you might receive an email that looks like 
        it’s from your bank, asking you to click a link and log in. In reality, the link leads to a fake website 
        designed to steal your login credentials.

        Phishing relies on deception to steal sensitive information, unlike attacks that target network 
        vulnerabilities, such as disabling firewalls or intercepting data between systems.

        2. Malware

        Malware is any software designed to harm or exploit your system. A common type of malware is a virus, which can 
        which can spread to other computers and cause damage by corrupting files, stealing information, or allowing
        remote control of your system. 

        Other security tools, such as VPNs or encrypted communication lines, are not malware. Instead, they help 
        protect your data by securing your internet connection and making it harder for attackers to intercept or steal 
        information.

        3. Ransomware Attacks

        Ransomware is a specific type of malware that locks your files by encrypting them and demands payment 
        (ransom) to unlock them. You cannot access your files unless you pay the ransom or find a way to decrypt them.

        Unlike other forms of attack, such as data theft or phishing, ransomware focuses on holding your data 
        hostage until a payment is made.

        4. Brute Force Attacks

        A brute force attack involves guessing a user’s password by trying many different combinations of usernames and 
        passwords until the correct one is found. Attackers often use automated tools to speed up the process, and this 
        method is particularly effective when passwords are weak or simple.

        This attack method is based on trial and error and is different from attacks that rely on injecting malicious 
        code into a system or exploiting known vulnerabilities.

        5. Social Engineering Attacks

        Social engineering is a method where attackers manipulate or deceive individuals into providing confidential 
        information. They might impersonate a trusted figure, such as IT support, to trick someone into revealing sensitive 
        information like passwords.

        Social engineering targets human behavior, unlike attacks that exploit technical flaws in software. It’s based on 
        psychological manipulation, not hacking systems directly.

        Understanding these different types of cyberattacks will help you recognize threats and take steps to protect
        yourself. Stay cautious with any unexpected communication and make sure your devices are secured with strong
        passwords, up-to-date antivirus software, and other protective measures.""", font=("Arial", 11))
        self.lesson_text.grid(row=2, column=0, sticky=tk.S, padx=10, pady=10)
    def on_inner_frame_configure(self, event):
    # Update scrollregion to include the whole inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    # Set the canvas width to match the inner frame
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw"), width=self.canvas.winfo_width())

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    quiz_page = lesson_cyberattacks_types(root)
    root.mainloop()

