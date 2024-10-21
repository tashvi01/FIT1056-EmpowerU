"""
FIT1056 Project: EmpowerU
Group: Monday G1

Lesson for Cyberattacks

Written by: Tin

"""
# Lesson 2.1 Cyberattacks
import tkinter as tk
# from Homepage import Homepage
class lesson_cyberattacks(tk.Frame):
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
        self.lesson_label = tk.Label(self.inner_frame, text="Lesson 2.1:\nInfosecurity Cyberattacks", font=("Arial Bold", 20))
        self.lesson_label.grid(row=1, column=0, sticky=tk.S, padx=10, pady=10)
        # Lesson text
        self.lesson_text = tk.Label(self.inner_frame, justify="left", text="""      What to Do During a Cyberattack?
        In today's digital world, cyberattacks are a real and ever-present threat. Knowing how to act swiftly and 
        effectively can reduce the damage caused and even prevent further harm. This guide will help you understand 
        the basic steps to take if you ever find yourself facing a potential cyberattack or suspicious activity.

        1. Immediate Response to a Suspected Cyberattack
        If you suspect your system is under a cyberattack, the first and most critical action you can take is to 
        disconnect your device from the internet. This prevents further unauthorized access or data from being 
        stolen. Staying online could allow attackers to continue accessing your system. While it may be tempting to 
        restart the system to resolve issues, doing so may cause you to lose important evidence that could help 
        determine the source or extent of the attack.

        It's also important to avoid ignoring the situation, as cyberattacks rarely resolve themselves. In fact, 
        attackers could use the time you wait to cause more damage.

        2. Dealing with Suspicious Emails or Unusual Account Activity
        Cybercriminals often use phishing emails or strange account activity to trick you into taking actions that 
        could compromise your security. If you receive a suspicious email or notice unusual activity, the best action 
        is to report the incident to your IT or security team. They are equipped to handle these threats and 
        investigate further.

        Simply deleting the email may not address the larger issue, especially if it’s part of a broader attack. 
        Avoid forwarding suspicious emails to friends for their opinion, as this can spread malicious content or 
        links to others, potentially causing them harm.

        3. Handling Malware Infections
        Malware is software designed to harm or exploit any device it infects. If you suspect that malware has 
        compromised your device, the first step is to run a full malware scan using up-to-date antivirus software. 
        Antivirus tools are specifically designed to detect and remove malware. It's crucial that your antivirus 
        software is up-to-date because new malware variants are created regularly.

        Manually deleting files to try to remove malware is not effective, as malware can hide in various places and 
        often regenerates. Similarly, continuing to use your device without taking action can expose you to more 
        harm, such as data theft or further system damage.

        4. Responding to Compromised Passwords
        Passwords are the first line of defense for your accounts. If you suspect your passwords have been compromised,
         you should immediately change your passwords and enable multi-factor authentication (MFA). 

        Multi-factor authentication (MFA) adds an extra layer of protection by requiring something beyond just your 
        password, like a code sent to your phone or biometric verification (e.g., fingerprint). Even if someone has your 
        password, MFA ensures that they would still need the second form of verification to access your account. 

        Simply disabling your accounts temporarily may not fully protect you, as attackers could still try to exploit 
        them later. Also, continuing to use compromised passwords is risky, as attackers may already have access to them.

        5. Importance of Collecting Evidence
        In the event of a cyberattack, it’s critical to collect evidence. This might include logs, screenshots, 
        suspicious emails, or other records of what happened. Having this information is crucial for legal and 
        forensic investigations, which can help identify the attacker, improve your system's security, and potentially 
        recover lost data.

        Confronting the attacker personally is never advisable. Cyberattacks are usually carried out anonymously, 
        and confronting the wrong person could lead to more trouble. Additionally, while learning from the attack to 
        create better security protocols is useful, your first priority should be gathering evidence for investigators 
        who can act on the incident.

        By following these steps, you can minimize the damage from a cyberattack and protect your personal or 
        organizational data. Stay vigilant and always prioritize security by being proactive in your approach.
        """, font=("Arial", 11))
        self.lesson_text.grid(row=2, column=0, sticky=tk.S, padx=10, pady=10)
    def on_inner_frame_configure(self, event):
    # Update scrollregion to include the whole inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    # Set the canvas width to match the inner frame
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw"), width=self.canvas.winfo_width())

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    quiz_page = lesson_cyberattacks(root)
    root.mainloop()

