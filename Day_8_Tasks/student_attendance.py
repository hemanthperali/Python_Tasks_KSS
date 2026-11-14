'''A teacher wants to store student attendance in a file named attendance.txt. Write a
Python program that takes a student name as input and appends it to the file. Then
display the contents of the file.'''

# Take the student name as input
name = input("Enter student name: ")

# Append the name to attendance.txt
file =  open("attendance.txt", "a") 
file.write(name + "\n")
file.close()

# Display the contents of the file
print("\nStudent Attendance:")

file = open("attendance.txt","r")
print(file.read())
file.close()

