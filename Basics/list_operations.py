''' Given a list of numbers `[10, 20, 30, 40, 50]`, write a program to:
 Add 60 to the list.
 Remove 30.
 Print the list.'''

# Given list
l = [10,20,30,40,50]

# Adding an element
add_element = l.append(60)
print("Updated List after adding an element:",l)

# Removing an element
remove_element = l.remove(30)
print("Updated List after removing an element:",l)