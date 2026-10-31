#  Write a program that searches for a number in a list and breaks the loop when found. 

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Enter a number to search : "))

for i in lst:
    if i == n:
        print(f"Number {n} found in the list.")
        break
else:
    print(f"Number {n} not found in the list.")