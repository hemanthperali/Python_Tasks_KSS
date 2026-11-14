''' Write a Python program that:
● Reads employee data from the file
● Displays all employee details
● Finds the employee with the highest salary
● Appends a new employee record to the file'''

# Open and read the employee file
with open("employees.txt", "r") as file:
    data = file.readlines()

print("Employee Details:")

highest_salary = 0
highest_employee = ""

# Display employee details and find highest salary
for line in data:
    name, salary = line.split()
    salary = int(salary)

    print(name, salary)

    if salary > highest_salary:
        highest_salary = salary
        highest_employee = name

# Display employee with highest salary
print("\nEmployee with Highest Salary:")
print(highest_employee, highest_salary)

# Take new employee details
new_name = input("\nEnter new employee name: ")
new_salary = input("\nEnter new employee salary: ")

# Append new employee record to the file
with open("employees.txt", "a") as file:
    file.write(new_name + " " + new_salary + "\n")

print("New employee record added successfully!")