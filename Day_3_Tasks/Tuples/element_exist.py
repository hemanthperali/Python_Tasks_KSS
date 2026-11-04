#  Write a program to check whether an element exists in a tuple.

tup = (3,5,2,7,8,5,0,9,)

element = int(input("Enter an element to check: "))

if element in tup:
    print(f"The element {element} exists in the tuple.")
else:
    print(f"The element {element} does not exist in the tuple.")