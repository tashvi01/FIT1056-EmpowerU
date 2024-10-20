"""
FIT1056 Project: EmpowerU
Group: Monday G1

This file contains class definition of Forum class

It creates a forum GUI and displays posts, delete posts and let's user's create posts

Written by: Tashvi Vig
"""

import tkinter as tk
from tkinter import messagebox
import pymysql as pm
from Utilities import switch_frame
from signin import SignIn
from backup import Backup

class Forum(tk.Frame):
    def __init__(self, master, student=None, admin=None ):
        """
        Constructor of Forum class
        """  
        super().__init__(master) 
        self.master = master
        self.mainframe = tk.Frame(self)  
        self.student  = student
        self.admin = admin
        if student!=None:
            self.username = self.student.username
        elif admin != None:
            self.username = self.admin.username
        self.mainframe.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
        self.show_posts() 

    def create_widgets(self):
        """
        Creates widgets of the Forum class.

        Parameter(s):
        None

        Return(s):
        None        
        """
        self.forum_label = tk.Label(self, text="FORUM", font=("Arial Bold", 20))
        self.forum_label.pack(padx=10, pady=10)

        self.post_label = tk.Label(self, text="Type anything!")
        self.post_label.pack(padx=10, pady=10)

        self.post_text = tk.Text(self, wrap=tk.WORD, height=3, width=40)
        self.post_text.pack(padx=10, pady=10)

        self.post_button = tk.Button(self, text="Post", command=self.post_in_forum)
        self.post_button.pack(padx=10, pady=10)

        self.posts_frame = tk.Frame(self)
        self.posts_frame.pack(padx=10, pady=10)

        self.return_button = tk.Button(self, text="Return", command=self.return_home)
        self.return_button.pack(padx=20, pady=20)

    def post_in_forum(self):
        """
        The posts that are posted.

        Parameter(s):
        None

        Return(s):
        None        
        """
        post_content = self.post_text.get("1.0", tk.END).strip()
        if not post_content:
            messagebox.showwarning("Warning", "You must type something to post.")
            return

        conn = pm.connect(host='localhost', user='root', password='FIT1056')
        cr = conn.cursor()

        cr.execute("CREATE DATABASE IF NOT EXISTS EmpowerU")
        cr.execute("USE EmpowerU")

        cr.execute("""
            CREATE TABLE IF NOT EXISTS forumData (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(20),
                post TEXT
            )
        """)

        # Insert the new post into the database
        cr.execute("INSERT INTO forumData (username, post) VALUES (%s, %s)", (self.username, post_content))
        conn.commit()

        # Check and clear posts if they exceed 15
        self.delete_posts(cr)

        conn.commit()
        conn.close()

        self.post_text.delete("1.0", tk.END)  # Clear the text box after posting
        self.show_posts()  # Refresh the displayed posts

    def delete_posts(self, cr):
        """
        Deletes posts if they are more than 15.

        Parameter(s):
        cr: cursor
        
        Return(s):
        None
        """
        # Select the total number of posts
        cr.execute("SELECT COUNT(*) FROM forumData")
        count = cr.fetchone()[0]

        # If there are more than 15 posts, delete all
        if count > 15:
            cr.execute("DELETE FROM forumData")
            print("All posts cleared. Exceeded 15 posts.")

    def show_posts(self):
        """
        Displays posts in forum.

        Parameter(s):
        None

        Return(s):
        None        
        """
        # Clear previous posts
        for widget in self.posts_frame.winfo_children():
            widget.destroy()

        # Connect to the database to retrieve posts
        conn = pm.connect(host='localhost', user='root', password='FIT1056')
        cr = conn.cursor()
        cr.execute("CREATE DATABASE IF NOT EXISTS EmpowerU")
        cr.execute("USE EmpowerU")

        # Create the forumData table if it doesn't exist
        cr.execute("""
            CREATE TABLE IF NOT EXISTS forumData (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(20),
                post TEXT
            )
        """)

        # Fetch posts from the database
        cr.execute("SELECT username, post FROM forumData ORDER BY id DESC")
        posts = cr.fetchall()

        # Display each post
        for username, post in posts:
            post_label = tk.Label(self.posts_frame, text=f"{username}: {post}", wraplength=400, anchor="w")
            post_label.pack(anchor="w", padx=5, pady=5)

        backup_instance = Backup
        backup_instance.backup_forum(self)    
        conn.commit()
        conn.close()

    def return_home(self):
        """
        Returns to the appropriate homepage based on whether a student or admin is logged in.

        Parameter(s):
        None

        Return(s):
        None
        """
        from Homepage import Homepage  
        from Admin_homepage import admin_Homepage  

        if self.student is not None:
            # If a student is signed in, return to the student homepage
            switch_frame(self, lambda master: Homepage(master, self.student))
        elif self.admin is not None:
            # If an admin is signed in, return to the admin homepage
            switch_frame(self, lambda master: admin_Homepage(master, self.admin))
        else:
            # Handle the case where neither is logged in (optional)
            messagebox.showwarning("Warning", "No user is signed in.")
