import pymysql as pm
from classes.User import User

class Student(User):
    def __init__(self, first_name, last_name, DOB, email, contact_number, username, password):
        super().__init__(first_name, last_name, DOB, email,contact_number, username, password)
        self.completed_quizzes = 0
        self.total_quizzes = 9

    def increment_progress(self):
        if self.completed_quizzes < self.total_quizzes:
            self.completed_quizzes += 1
            self.save_progress()

    def get_progress(self):
        return self.completed_quizzes, self.total_quizzes

    def save_progress(self):
        conn = pm.connect(host='localhost', user='root', password='FIT1056', database='EmpowerU')
        cr = conn.cursor()
        # Insert or update progress in the database
        cr.execute("""
            INSERT INTO student_progress (username, completed_quizzes, total_quizzes)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE completed_quizzes=%s, total_quizzes=%s
        """, (self.username, self.completed_quizzes, self.total_quizzes, self.completed_quizzes, self.total_quizzes))
        conn.commit()
        conn.close()

    def load_progress(self):
        conn = pm.connect(host='localhost', user='root', password='FIT1056', database='EmpowerU')
        cr = conn.cursor()
        cr.execute("SELECT completed_quizzes, total_quizzes FROM student_progress WHERE username = %s", (self.username,))
        result = cr.fetchone()
        if result:
            self.completed_quizzes, self.total_quizzes = result
        conn.close()
