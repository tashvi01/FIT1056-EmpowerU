"""
FIT1056 Project: EmpowerU
Group: Monday G1

The backup file which stores all data entered in sql in csvs and populates tables with data when opened on every laptop.

Written by: Tashvi Vig
"""


import pymysql as pm
import csv

class Backup():
    def backup_register(self, values):
        """
        Stores all the information being entered during registration in a csv file. 

        Parameter(s): 
        values: tuple of the values being entered in the table

        Return(s):
        None
        """
        conn = pm.connect(host='localhost', user='root', password='FIT1056')
        cr = conn.cursor()
        cr.execute("CREATE DATABASE IF NOT EXISTS EmpowerU")
        cr.execute("USE EmpowerU")
        cr.execute("SELECT * FROM students")
        students_data = cr.fetchall()

        try:
            with open("Register_backup.csv", "w+", newline="") as f:
                writer = csv.writer(f)
                column_header = ["first_name", "last_name", "DOB", "email", "contact_number", "username", "password"]
                writer.writerow(column_header)
                for student in students_data:
                    if student != values:
                        writer.writerow(student)
        except EOFError:
            conn.commit()
            conn.close()

    def backup_forum(self):
        """
        Backup all forum posts to a CSV file.

        Parameter(s):
        None

        Return(s): 
        None
        """
        conn = pm.connect(host='localhost', user='root', password='FIT1056')
        cr = conn.cursor()
        cr.execute("CREATE DATABASE IF NOT EXISTS EmpowerU")
        cr.execute("USE EmpowerU")
        
        try:
            cr.execute("SELECT * FROM forumData")  
            forum_data = cr.fetchall()

            with open("Forum_backup.csv", "w+", newline="") as f:
                writer = csv.writer(f)
                column_header = ["id", "username", "post"]  
                writer.writerow(column_header)
                for post in forum_data:
                    writer.writerow(post)

        except Exception as e:
            print(f"An error occurred: {e}") 
        finally:
            conn.close() 

    def backup_admin(self):
        """
        Backup all admin data to a CSV file.

        Parameter(s):
        None

        Return(s): 
        None
        """
        conn = pm.connect(host='localhost', user='root', password='FIT1056')
        cr = conn.cursor()
        cr.execute("CREATE DATABASE IF NOT EXISTS EmpowerU")
        cr.execute("USE EmpowerU")
        cr.execute("SELECT * FROM admin")  
        admin_data = cr.fetchall()

        try:
            with open("admin.csv", "w+", newline="") as f:
                writer = csv.writer(f)
                column_header = ["id", "password", "username"] 
                writer.writerow(column_header)
                for admin in admin_data:
                    writer.writerow(admin)
        except EOFError:
            conn.commit()
            conn.close()

    def backup_progress_tracker(self):
        """
        Backup student progress to a CSV file.

        Parameter(s):
        None

        Return(s): 
        None        
        """

        conn = pm.connect(host='localhost', user='root', password='FIT1056', database='EmpowerU')
        cr = conn.cursor()

        try:
            cr.execute("SELECT username, quizzes_completed, total_quizzes FROM student_progress")
            progress_data = cr.fetchall()

            with open("Progress_backup.csv", "w+", newline="") as f:
                writer = csv.writer(f)
                column_header = ["username", "quizzes_completed", "total_quizzes"]
                writer.writerow(column_header)
                for row in progress_data:
                    writer.writerow(row)

            print("Progress backup successful.")
        except Exception as e:
            print(f"Error during backup: {e}")
        finally:
            cr.close()
            conn.close()

    def populate_table(self):
        """
        Initializes the database and populates tables with data when opened on every laptop.

        Parameter(s):
        None

        Return(s):
        None
        """
        try:
            conn = pm.connect(host='localhost', user='root', password='FIT1056')
            cr = conn.cursor()
            print("Database connection successful.")

            cr.execute("CREATE DATABASE IF NOT EXISTS EmpowerU")
            cr.execute("USE EmpowerU")
            cr.execute(""" 
                CREATE TABLE IF NOT EXISTS students (
                    first_name VARCHAR(20),
                    last_name VARCHAR(20),
                    DOB DATE,
                    email VARCHAR(20),
                    contact_number VARCHAR(20),
                    username VARCHAR(20),
                    password VARCHAR(20)
                )
            """)
            print("Students table created or exists.")

            cr.execute("""
                CREATE TABLE IF NOT EXISTS forumData (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(20),
                    post TEXT
                )
            """)
            print("Forum data table created or exists.")

            cr.execute("""
                CREATE TABLE IF NOT EXISTS admin (
                    id varchar(20),
                    password VARCHAR(20),
                    username VARCHAR(20)
                )
            """)
            print("Admin table created or exists.")

            cr.execute("""
                CREATE TABLE IF NOT EXISTS student_progress (
                    username VARCHAR(100) PRIMARY KEY,
                    first_name VARCHAR(100),
                    last_name VARCHAR(100),
                    quizzes_completed INT DEFAULT 0,
                    total_quizzes INT DEFAULT 0
                )
            """)
            print("Progress tracker table created or exists.")

            # Populate students table from backup CSV
            cr.execute("SELECT * FROM students")
            rows = cr.fetchall()
            print(f"Number of rows in 'students' table: {len(rows)}")

            if len(rows) == 0:
                try:
                    with open("Register_backup.csv", "r") as f:
                        reader = csv.reader(f)
                        next(reader) 
                        print("CSV file opened successfully.")

                        for row in reader:
                            if len(row) == 7: 
                                values_tuple = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                                cr.execute("""
                                    INSERT INTO students (first_name, last_name, DOB, email, contact_number, username, password)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                                """, values_tuple)
                            else:
                                print(f"Skipping invalid row: {row}")
                except FileNotFoundError:
                    print("Error: The CSV file 'Register_backup.csv' was not found.")
                except Exception as e:
                    print(f"Error reading CSV: {e}")

            # Populate admin table from admin CSV
            cr.execute("SELECT * FROM admin")
            admin_rows = cr.fetchall()
            print(f"Number of rows in 'admin' table: {len(admin_rows)}")

            if len(admin_rows) == 0:
                try:
                    with open("admin.csv", "r") as f:
                        reader = csv.reader(f)
                        next(reader)  
                        print("Admin CSV file opened successfully.")

                        for row in reader:
                            if len(row) == 3:  
                                admin_values_tuple = (row[0], row[1], row[2])  
                                cr.execute("""
                                    INSERT INTO admin (id, password, username)
                                    VALUES (%s, %s, %s)
                                """, admin_values_tuple)
                            else:
                                print(f"Skipping invalid row: {row}")
                except FileNotFoundError:
                    print("Error: The CSV file 'admin.csv' was not found.")
                except Exception as e:
                    print(f"Error reading CSV: {e}")

            # Populate progress tracker table from progress CSV
            cr.execute("SELECT * FROM student_progress")
            progress_rows = cr.fetchall()
            print(f"Number of rows in 'student_progress' table: {len(progress_rows)}")

            if len(progress_rows) == 0:
                try:
                    with open("Progress_backup.csv", "r") as f:
                        reader = csv.reader(f)
                        next(reader)  
                        print("Progress CSV file opened successfully.")

                        for row in reader:
                            if len(row) == 5:  
                                progress_values_tuple = (row[0], row[1], row[2], row[3], row[4])  
                                cr.execute("""
                                    INSERT INTO student_progress (username, first_name, last_name, quizzes_completed, total_quizzes)
                                    VALUES (%s, %s, %s, %s, %s)
                                """, progress_values_tuple)
                            else:
                                print(f"Skipping invalid row: {row}")
                except FileNotFoundError:
                    print("Error: The CSV file 'Progress_backup.csv' was not found.")
                except Exception as e:
                    print(f"Error reading CSV: {e}")

            # Check forum data count and delete if more than 30
            cr.execute("SELECT COUNT(*) FROM forumData")
            count = cr.fetchone()[0]
            if count >= 30:
                cr.execute("DELETE FROM forumData")  # Clear all posts if count >= 30

            conn.commit()
            print("Data committed to the database.")

        except pm.MySQLError as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"General error: {e}")
        finally:
            if conn:
                cr.close()
                conn.close()
                print("Database connection closed.")
