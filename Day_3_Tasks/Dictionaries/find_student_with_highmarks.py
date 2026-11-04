# Write a program to find the student with the highest marks from a dictionary.
students = {
    "Student1": 85,
    "Student2": 92,
    "Student3": 78,
    "Student4": 95,
    "Student5": 88
}

highest_marks_student = max(students, key=students.get)
print(highest_marks_student,":", students[highest_marks_student])