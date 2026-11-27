'''Scenario:
A school records marks of students in one subject:
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]
Task:
● Convert to Pandas DataFrame
● Plot:
○ Line graph → trend of marks
○ Bar chart → student vs marks
○ Pie chart → Pass (>50) vs Fail
○ Histogram → distribution of marks
○ Scatter plot → index vs marks'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame({"Marks":marks,"Students":students})
print(df)

#  Line Graph - Trend of marks
plt.figure(figsize=(12, 5))
plt.subplot(2,3,1)
plt.plot(students, marks, marker='o', color='blue')
plt.title("Trend of Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)


#  Bar Chart - Student vs Marks
plt.subplot(2,3,2)
plt.bar(students, marks, color='green')
plt.title("Student vs Marks")
plt.xlabel("Students")
plt.ylabel("Marks")


#  Pie Chart - Pass vs Fail
passed = np.sum(marks > 50)
failed = np.sum(marks <= 50)

plt.subplot(2,3,3)
plt.pie(
    [passed, failed],
    labels=["Pass", "Fail"],
    autopct="%1.1f%%",
    colors=["green", "red"],
    startangle=90
)
plt.title("Student Result")


#  Histogram - Distribution of marks
plt.subplot(2,3,4)
plt.hist(marks, bins=5, color='orange', edgecolor='black')
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

#  Scatter Plot - Index vs Marks
plt.subplot(2,3,5)
plt.scatter(range(len(marks)), marks, color='purple')
plt.title("Index vs Marks")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.grid(True)

plt.tight_layout()
plt.show()

