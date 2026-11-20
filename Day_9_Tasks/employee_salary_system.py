'''A company has two types of employees: Employee and Manager. Create a base class
Employee containing name and salary. Create a derived class Manager that inherits
from Employee and displays the employee details.
'''

class Employee:
    name = "hemanth"
    salary = 30000

class Manager(Employee):
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

e1 = Employee()
m = Manager()

m.display()
