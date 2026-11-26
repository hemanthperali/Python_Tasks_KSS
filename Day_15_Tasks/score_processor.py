'''Scenario:
A teacher stores student names and marks in a list of tuples.
Task:
● Convert data into a dictionary
● Use a loop + condition to find students scoring above 50
● Use math module to calculate average
● Store results in a text file'''

import math

# List of tuples containing names and marks
students =  [
    ("Arun", 85),
    ("Bala", 45),
    ("Charan", 70),
    ("Divya", 90),
    ("Esha", 35)]

# Convert list of tuples into dictionary
dict1 = dict(students)
print(dict1)

# Find students greater than 50
res = []
for name, marks in dict1.items():
    if marks > 50:
        res.append((name, marks))

# Calculate average
total = sum(dict1.values())
avg = math.floor(total/len(dict1))
print("Average Score:",avg)

# Store data in text file
with open ('students.txt','w') as file:
    file.write("Students Results\n")

    for name, marks in dict1.items():
        file.write(name + " : " + str(marks) + "\n")

    file.write("Average Marks:" + str(avg))
