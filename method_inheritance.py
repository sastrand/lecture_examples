class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def print_contact(self):
        print("Name: {}\nEmail: {}".format(self.name, self.email))

class Student(Person):
    def __init__(self, name, email, stu_id):
        self.name = name
        self.email = email
        self.stu_id = stu_id
    def print_id(self):
        print("ID: {}".format(self.stu_id))

max = Student("Max", "max@pdx.edu", "11235")

max.print_contact()
max.print_id()
