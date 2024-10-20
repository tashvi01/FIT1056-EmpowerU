from classes.User import User

class Teacher(User):
    def __init__(self, first_name, last_name, DOB, email, contact_number, username, password,TeacherID):
        super().__init__(first_name, last_name, DOB, email, contact_number, username, password)
        self.TeacherID = TeacherID