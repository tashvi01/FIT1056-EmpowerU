# Lesson 2.3 Cyberattacks Defense
import tkinter as tk
# from Homepage import Homepage
class lesson_cyberattacks_defense(tk.Frame):
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
        self.lesson_label = tk.Label(self.inner_frame, text="Lesson 2.3:\nInfosecurity Cyberattack Prevention", font=("Arial Bold", 20))
        self.lesson_label.grid(row=1, column=0, sticky=tk.S, padx=10, pady=10)
        # Lesson text
        self.lesson_text = tk.Label(self.inner_frame, justify="left", text="""Key Tools and Methods
      In the field of cybersecurity, various tools and practices are employed to defend against attacks 
      and protect sensitive information. This guide introduces important concepts and methods that enhance 
      security, helping you understand how to protect your systems and data effectively.

      1. Firewalls

      A firewall is a security system that monitors and controls incoming and outgoing network traffic. 
      Its primary purpose is to block unauthorized access to or from a private network, acting as a barrier 
      between your internal network and external threats from the internet. By setting rules for what traffic 
      is allowed or denied, firewalls help prevent attackers from accessing your systems.

      Firewalls do not store passwords or encrypt data; instead, they focus on controlling access to the 
      network to prevent unauthorized intrusion.

      2. Two-Factor Authentication (2FA)

      Two-factor authentication (2FA) is a method of enhancing security by requiring two forms of verification 
      before granting access to an account. Typically, this includes something the user knows (like a password) 
      and something they have (such as a phone or fingerprint). Even if an attacker has stolen your password, 
      they cannot access your account without the second factor, making 2FA a powerful tool for protecting 
      sensitive information.

      2FA does not double the strength of your password or back up your data; its role is to add an extra 
      layer of protection during the login process.

      3. Preventing Phishing Attacks

      Phishing attacks involve tricking individuals into giving away sensitive information, often through 
      deceptive emails. One of the most effective ways to prevent phishing is educating users to recognize 
      suspicious emails and avoid clicking on unknown links. Training employees to spot phishing attempts 
      is a critical line of defense against these attacks.

      While tools like ad-blockers can enhance security, they do not specifically prevent phishing, which 
      targets user behavior.

      4. Antivirus Software

      Antivirus software is a crucial tool for detecting and removing malware such as viruses, trojans, and 
      worms. It scans your system for known malicious programs and helps eliminate them before they can cause 
      damage. Antivirus solutions are regularly updated to recognize new threats as they emerge.

      Antivirus software focuses on detecting malware and does not encrypt files or prevent unauthorized 
      users from accessing a network directly.

      5. Multi-Factor Authentication (MFA)

      Multi-factor authentication (MFA) goes beyond just two factors, sometimes requiring multiple forms of 
      verification before granting access. The benefit of MFA is that even if an attacker manages to steal a 
      user’s password, they will still need to pass additional security checks, such as a code sent to a phone, 
      before gaining access.

      MFA does not eliminate the need for passwords or encrypt communications, but it significantly strengthens 
      account security by requiring multiple forms of verification.""", font=("Arial", 11))
        self.lesson_text.grid(row=2, column=0, sticky=tk.S, padx=10, pady=10)
    def on_inner_frame_configure(self, event):
    # Update scrollregion to include the whole inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    # Set the canvas width to match the inner frame
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw"), width=self.canvas.winfo_width())

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    quiz_page = lesson_cyberattacks_defense(root)
    root.mainloop()

