# Write a program to check if an element exists in a set.

s1  = set([2,5,8,12,23,65,33])

element = int(input("Enter an element to check:"))

if element in s1:
    print(f"The element {element} present in the set.")
else:
    print("The element does not exists in the set.")