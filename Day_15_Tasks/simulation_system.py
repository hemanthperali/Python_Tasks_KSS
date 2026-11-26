'''Scenario:
Simulate exam results and generate reports.
Task:
● Generate random marks using random
● Store in NumPy array
● Convert to Pandas DataFrame
● Use OOP to represent Student
● Use conditions + loops to assign grades
● Save report to file
● Handle errors using try-except
● Use math module for statistics'''


import random
import numpy as np
import pandas as pd
import math

#  Create Student class 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    #  Assign grades using conditions
    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        elif self.marks >= 40:
            return "E"
        else:
            return "Fail"


try:
    #  Generate random marks
    names = ["Alice", "Bob", "Charlie", "David", "Emma"]

    marks = [random.randint(0, 100) for i in range(5)]

    #  Store marks in NumPy array
    marks_array = np.array(marks)

    #  Create Student objects
    students = []

    for i in range(len(names)):
        student = Student(names[i], int(marks_array[i]))
        students.append(student)

    #  Assign grades and create report
    report = []

    for student in students:
        grade = student.get_grade()

        if student.marks >= 40:
            result = "Pass"
        else:
            result = "Fail"

        report.append({
            "Name": student.name,
            "Marks": student.marks,
            "Grade": grade,
            "Result": result
        })

    #  Convert into Pandas DataFrame
    df = pd.DataFrame(report)

    print("EXAM RESULTS")
    print(df)

    #  Calculate statistics using math module
    total = math.fsum(marks)
    average = total / len(marks)

    highest = max(marks)
    lowest = min(marks)

    print("\nEXAM STATISTICS")
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)

    #  Save report to file
    df.to_csv("exam_report.txt", index=False)

    print("\nReport saved successfully!")

except (ValueError, TypeError, ZeroDivisionError) as e:
    print("Data processing error:", e)
