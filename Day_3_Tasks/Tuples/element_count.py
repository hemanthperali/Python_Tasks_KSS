# Write a program to count how many times an element appears in a tuple.

t = (3,5,2,7,8,5,0,9,)
element = int(input("Enter an element to count: "))

count = t.count(element)
print(f"The element {element} appears {count} times.")