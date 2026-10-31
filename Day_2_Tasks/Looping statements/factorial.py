# Write a program to calculate the factorial of a number using a loop.

n = int(input("Enter a number:"))
factorial = 1

while n > 0:
    factorial *= n
    n -= 1
print("Factorial :", factorial)