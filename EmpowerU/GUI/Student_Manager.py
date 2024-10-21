"""
FIT1056 Project: EmpowerU
Group: Monday G1

Written by: Tashvi Vig

"""
import tkinter as tk
from tkinter import messagebox
import pymysql as pm

class StudentManager:
    def __init__(self):
        self.conn = pm.connect(host='localhost', user='root', password='FIT1056', database='EmpowerU')

    def get_all_students(self):
        """
        Fetch all students and their progress from the database.
        """
        with self.conn.cursor() as cursor:
            cursor.execute("""
                SELECT s.first_name, s.last_name, s.username, COALESCE(sp.quizzes_completed, 0) AS quizzes_completed
                FROM students s
                LEFT JOIN student_progress sp ON s.username = sp.username
            """)
            return cursor.fetchall()
        
    def close_connection(self):
        """
        Closes the database connection.
        """
        self.conn.close()
