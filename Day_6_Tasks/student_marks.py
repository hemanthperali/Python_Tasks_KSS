''' Develop a Python program to manage student marks for three subjects. Store the subject
names in a tuple, maintain unique student names in a set, and store each student’s marks
in a list inside a dictionary where the key is the student name. Create user-defined
functions to add a student with marks, display all student records, and calculate the average
marks of a student. Implement a recursive function to calculate the total marks from the list of
marks. The program should interact with the user through a simple menu. Also include
exception handling to handle ValueError (non-numeric marks input), ZeroDivisionError
(average calculation issues), TypeError (incorrect data type in marks), and NameError (when a
student name entered does not exist in the dictionary).'''


# Student Marks Management System

# Tuple to store subject names
subjects = ("Python", "Java", "C Programming")

# Set to maintain unique student names
student_names = set()

# Dictionary to store student names and their marks
student_records = {}


# Function to add a student and their marks
def add_student():
    try:
        name = input("Enter student name: ").strip()

        if not name:
            print("Student name cannot be empty!")
            return

        if name in student_names:
            print("Student already exists!")
            return

        marks = []

        for subject in subjects:
            mark = float(input(f"Enter marks in {subject}: "))

            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100!")
                return

            marks.append(mark)

        student_names.add(name)
        student_records[name] = marks

        print("Student added successfully!")

    except ValueError:
        print("Error: Please enter numeric marks only!")

    except TypeError:
        print("Error: Invalid data type in marks!")


# Recursive function to calculate total marks
def calculate_total(marks):

    if len(marks) == 0:
        return 0

    return marks[0] + calculate_total(marks[1:])


# Function to display all student records
def display_records():
    if not student_records:
        print("No student records available!")
        return

    print("\n------ STUDENT RECORDS ------")

    for name, marks in student_records.items():
        print("\nStudent Name:", name)

        for i in range(len(subjects)):
            print(subjects[i], ":", marks[i])

        print("Total Marks:", calculate_total(marks))


# Function to calculate average marks
def calculate_average():
    try:
        name = input("Enter student name: ").strip()

        if name not in student_records:
            raise NameError("Student name does not exist!")

        marks = student_records[name]

        total = calculate_total(marks)

        average = total / len(marks)

        print("\nStudent Name:", name)
        print("Total Marks:", total)
        print("Average Marks:", average)

    except NameError as e:
        print("Error:", e)

    except ZeroDivisionError:
        print("Error: Cannot calculate average with zero marks!")

    except TypeError as e:
        print("Error:", e)


# Main menu-driven program
while True:

    print("\n===== STUDENT MARKS MANAGEMENT =====")
    print("1. Add Student")
    print("2. Display All Student Records")
    print("3. Calculate Average Marks")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            display_records()

        elif choice == 3:
            calculate_average()

        elif choice == 4:
            print("Thank You!")
            break

        else:
            print("Invalid choice! Please select 1 to 4.")

    except ValueError:
        print("Error: Please enter a valid menu number!")
