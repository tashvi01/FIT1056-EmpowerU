"""
FIT1056 Project: EmpowerU
Group: Monday G1

The Progress Tracker for each student.

Written by: Tashvi Vig
"""

import tkinter as tk
import pymysql as pm
from backup import Backup

class ProgressTracker:
    def __init__(self, master, student):
        """
        Constructor class for Progress Tracker.

        Parameter(s):
        master : the master window
        student: instance of the student logged in        
        """

        self.master = master
        self.student = student
        
        # Initialize the database connection and create the progress table
        self.conn = pm.connect(host='localhost', user='root', password='FIT1056', database='EmpowerU')
        self.initialize_progress_table()

        # Total quizzes
        self.total = 9  

        # Fetch initial progress
        self.completed, _ = self.get_student_progress()  # Fetch only completed quizzes

        # Initialize the progress label
        self.progress_label = tk.Label(master, text=self.get_progress_text(), bg="lightblue", font=("Arial", 14))
        self.progress_label.grid(row=0, column=0, padx=10, pady=10)

    def initialize_progress_table(self):
        """
        Create the progress table if it doesn't exist.
        
        Parameter(s):
        None

        Return(s):
        None

        Written by: Tashvi Vig
        
        """
        with self.conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS student_progress (
                    username VARCHAR(100) PRIMARY KEY,
                    first_name VARCHAR(100),
                    last_name VARCHAR(100),
                    quizzes_completed INT DEFAULT 0,
                    total_quizzes INT DEFAULT 0
                )
            """)
        self.conn.commit()

    def get_student_progress(self):
        """
        Fetch the student's progress from the database.
        
        Parameter(s):
        None

        Return(s):
        total

        Written by: Tashvi Vig      
        
        """
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT quizzes_completed, total_quizzes FROM student_progress WHERE username = %s", (self.student.username,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                # If no record exists, initialize it
                self.initialize_student_progress()
                return 0, self.total  # Default values

    def initialize_student_progress(self):
        """
        Insert a new record for the student in the progress table.
        
        Parameter(s):
        None

        Return(s):
        None

        Written by: Tashvi Vig        
        """
        with self.conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO student_progress (username, first_name, last_name)
                VALUES (%s, %s, %s)
            """, (self.student.username, self.student.first_name, self.student.last_name))
        self.conn.commit()

    def increment_progress(self):
        """
        Increment the student's progress and update the display.

        Parameter(s):
        None

        Return(s):
        None

        Written by: Tashvi Vig        
        """
        self.completed += 1
        self.total += 1 
        self.update_student_progress()  # Update the database
        self.update_label()
        self.backup_progress_tracker()  # Call to backup progress after updating


    def update_student_progress(self):
        """
        Update the student's progress in the database.
        
        Parameter(s):
        None

        Return(s):
        None

        Written by: Tashvi Vig        
        """
        with self.conn.cursor() as cursor:
            cursor.execute("""
                UPDATE student_progress
                SET quizzes_completed = %s, total_quizzes = %s
                WHERE username = %s
            """, (self.completed, self.total, self.student.username))
        self.conn.commit()

    def update_label(self):
        """
        Update the progress label with the current progress.

        Parameter(s):
        None

        Return(s):
        None

        Written by: Tashvi Vig        
        """
        self.progress_label.config(text=self.get_progress_text())

    def get_progress_text(self):
        """
        Return the text to be displayed for the current progress.
        
        Parameter(s):
        None

        Return(s):
        None

        Written by: Tashvi Vig
        """
        return f"Quizzes Completed: {self.completed}/{self.total}"

    def close_connection(self):
        """
        Close the database connection.

        Parameter(s):
        None

        Return(s):
        None

        Written by: Tashvi Vig        
        """
        self.conn.close()
