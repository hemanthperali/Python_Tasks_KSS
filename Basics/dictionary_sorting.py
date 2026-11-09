'''
Given a dictionary:
 
    ```python
    students = {
        "Rahul": 85,
        "Amit": 92,
        "Priya": 78,
        "Sneha": 95
    }
    ```
 
    Sort the dictionary based on marks in descending order and print the top two students.
'''

students = {"Rahul": 85, "Amit": 92, "Priya": 78, "Sneha": 95}

# Sort the dictionary based on marks in descending order
sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)

# Get the top two students
top_two_students = sorted_students[:2]

print("Top two students based on marks:")
for student, marks in top_two_students:
    print(f"{student}: {marks}")
    