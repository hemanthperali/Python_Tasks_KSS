'''Scenario:
Manage employee data.
Task:
● Create a class Employee
● Store employees in a dictionary
● Save data to a file
● Use exception handling for invalid salary input
● Use loop to display all employees'''


#  Create Employee class
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)

#  Store employees in a dictionary
employees = {}

try:
    n = int(input("Enter number of employees: "))

    for i in range(n):
        print("\nEnter Employee Details")

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")

        try:
            salary = float(input("Enter Salary: "))

            if salary < 0:
                print("Invalid salary!")
                continue

            emp = Employee(emp_id, name, salary)
            employees[emp_id] = emp

        except ValueError:
            print("Invalid salary! Please enter a number.")
            continue

    #  Save employee data to a file
    with open("employees.txt", "w") as file:
        for emp in employees.values():
            file.write(
                f"{emp.emp_id}, {emp.name}, {emp.salary}\n"
            )

    print("\nEmployee details saved successfully!")

    #  Display all employees using loop
    print("\nEmployee Details:")

    for emp in employees.values():
        emp.display()

except ValueError:
    print("Invalid input! Enter a valid number.")


