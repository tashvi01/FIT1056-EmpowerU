import pymysql as pm

class User():
  def __init__(self, first_name, last_name, DOB, email, contact_number, username, password):
      self.first_name = first_name
      self.last_name = last_name
      self.DOB = DOB
      self.email = email
      self.contact_number = contact_number
      self.username = username
      self.password = password