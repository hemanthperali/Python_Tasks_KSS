# Write a program to assign grades based on marks (for example: A, B, C, Fail).

marks = int(input("Enter the marks:"))

if marks > 90:
    grade = "A"
elif marks > 80:
    grade = "B"
elif marks > 70:
    grade = "C"
else:
    grade = "Fail"

print(f"Marks Obtained : {marks}")
print(f"Grade :{grade}")