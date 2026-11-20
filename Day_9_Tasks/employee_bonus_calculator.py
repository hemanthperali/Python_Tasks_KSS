'''A company wants to apply a bonus calculation automatically before displaying the
salary. Create an Employee class and use a decorator that modifies the salary by
adding a bonus before displaying it'''

def add_bonus(func):
    def wrapper(self):
        bonus = int(input("Enter the bonus amount:"))
        self.salary = self.salary + bonus
        return func(self)
    return wrapper


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 

    @add_bonus
    def display(self):
        print("Employee Name:", self.name)
        print("Salary after Bonus:", self.salary )


e1 = Employee("Rahul", 30000)

e1.display()