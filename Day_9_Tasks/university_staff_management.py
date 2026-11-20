'''A university has different staff types such as Professor, LabAssistant, and
Administrator. All inherit from a base class Staff. Implement hierarchical inheritance
to manage and display their information.'''

class Staff:
    name = "Hemanth"
    Id = 578

    def display(self):
        print("Staff Name:",self.name)
        print("Id:",self.Id)

class Professor(Staff):
    subject = "Python"

    def show(self):
        print("Professor Details:")
        self.display()
        print("Subject:",self.subject)

class LabAssistant(Staff):
    Lab = "Python Lab"

    def lab(self):
        print("Lab Assistant Details:")
        self.display()
        print("Lab:",self.Lab)

class Administrator(Staff):
    department = "Office"

    def admin(self):
        print("Administrator Details:")
        self.display()
        print("Department:",self.department)

p = Professor()
l = LabAssistant()
a = Administrator()

p.show()
l.lab()
a.admin()
