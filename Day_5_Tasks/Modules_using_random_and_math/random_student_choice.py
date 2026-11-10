'''Write a program that uses random.choice() to randomly select a student from a 
list and display: 
"The selected student for presentation is: <name>'''

import random

# List of student names
students = ["Henry","David","John","Vijay","Arjun"]

# Select a random student
random_student = random.choice(students)

# Display the student
print(f"The selected student for presentation is : {random_student}")