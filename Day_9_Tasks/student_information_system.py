'''A school wants a program to store student details. Create a Student class with
attributes such as name, roll number, and marks. Create objects for at least three
students and display their details'''

class Student:
    name = "Hemanth"
    roll_number = 501
    marks = 93

    def display(self):
        print("Name:",self.name)
        print("Roll Number:",self.roll_number)
        print("Marks:",self.marks,"\n")

s1 = Student()
s1.display()

s2 = Student()
s2.name = "Durga"
s2.roll_number = 502
s2.marks = 90
s2.display()

s3 = Student()
s3.name = "Rajesh"
s3.roll_number = 503
s3.marks = 88
s3.display()