"""
FIT1056 Project: EmpowerU
Group: Monday G1

This file contains class definition of Forum class.

This file backs up data entered when registering and all the forum posts (in a csv file).
It also populates the database (sql) with prev values entered.

Written by: Tashvi Vig
"""

import pymysql as pm
import csv

class Backup():
    def backup_register(self, values):
        """
        Stores all the information being entered during registration in a csv file. It also deletes
        forum posts when they reach 30 posts.

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
        cr.execute("SELECT * FROM forumData")  # Ensure forumData table exists
        forum_data = cr.fetchall()

        try:
            with open("Forum_backup.csv", "w+", newline="") as f:
                writer = csv.writer(f)
                column_header = ["id", "username", "post"]  # Assuming these are the columns
                writer.writerow(column_header)
                for post in forum_data:
                    writer.writerow(post)
        except EOFError:
            conn.commit()
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

            # New forumData table creation with primary key
            cr.execute("""
                CREATE TABLE IF NOT EXISTS forumData (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(20),
                    post TEXT
                )
            """)
            print("Forum data table created or exists.")

            cr.execute("SELECT * FROM students")
            rows = cr.fetchall()
            print(f"Number of rows in 'students' table: {len(rows)}")

            if len(rows) == 0:
                try:
                    with open("Register_backup.csv", "r") as f:
                        reader = csv.reader(f)
                        next(reader)  # Skip header row if present
                        print("CSV file opened successfully.")

                        for row in reader:
                            if len(row) == 7:  # Ensure each row has exactly 7 fields
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
