# Given a tuple `(10, 20, 30, 40, 50)`, write a program to print the first, last, and middle elements.

tup = (10,20,30,40,50)

# Get the first element
first_element = tup[0]

# Get the second element
last_element = tup[-1]

# Accessing middle element using floor division
middle_index = len(tup)//2
middle_element = tup[middle_index]

# Print the output
print("First Element:",first_element)
print("Middle Element:",middle_element)
print("Last Element:", last_element)