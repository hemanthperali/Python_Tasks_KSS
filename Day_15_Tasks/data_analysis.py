'''Scenario:
Analyze student marks.
Task:
● Generate marks using NumPy
● Convert into Pandas DataFrame
● Use conditions to filter passing students
● Calculate mean using math/NumPy
● Use loop to print result'''

import numpy as np
import pandas as pd

#  Generate student marks using NumPy
marks = np.random.randint(0, 101, size=6)

# Student names
students = ['A', 'B', 'C', 'D', 'E',
            'F']

#  Convert into Pandas DataFrame
df = pd.DataFrame({
    'Student': students,
    'Marks': marks
})

print("Student Marks:")
print(df)

#  Filter passing students (marks >= 40)
passed = df[df['Marks'] >= 40]

print("\nPassing Students:")
print(passed)

#  Calculate mean using NumPy and math
average = np.mean(marks)

print("\nAverage Marks :", average)

#  Use loop to print results
print("\nStudent Results:")

for i in range(len(df)):
    student = df.iloc[i]['Student']
    mark = df.iloc[i]['Marks']

    if mark >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print(student, "-", mark, "-", result)