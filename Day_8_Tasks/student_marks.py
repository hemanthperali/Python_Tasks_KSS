''' Write a Python program to:
● Read the file
● Display all student records
● Calculate and display the average marks of the class'''

# Open the file in read mode
with open("marks.txt", "r") as file:

    total = 0
    count = 0

    print("Student Records:")

    # Read each line from the file
    for line in file:
        name, marks = line.split()

        # Display student details
        print(name, marks)

        # Calculate total marks
        total = total + int(marks)
        count = count + 1

    # Calculate average marks
    average = total / count

    print("\nAverage Marks:", average)