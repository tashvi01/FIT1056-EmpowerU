from classes.User import User

class Student(User):
    def __init__(self, first_name, last_name, DOB, email, contact_number, username, password, student_id):
        super().__init__(first_name, last_name, contact_number, DOB, email, username, password)
        self.student_id= student_id