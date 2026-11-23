'''A company stores employee data:
employees = [[101, "A"], [102, "B"], [103, "C"]]
Scenario:
● Create a shallow copy of the list.
● Modify one nested list (e.g., change "A" to "Z").
● Observe changes in both lists.
Task:
● Explain why the change reflects in both.
● Fix it using deep copy.'''

import copy

employees = [[101, "A"], [102, "B"], [103, "C"]]

# Create a shallow copy
shallow_copy = copy.copy(employees)

# Modify a nested list in shallow copy
shallow_copy[0][1] = "Z"

print("After Shallow Copy:")
print("Original List:", employees)
print("Shallow Copy:", shallow_copy)

# Create a deep copy
deep_copy = copy.deepcopy(employees)

# Modify a nested list in deep copy
deep_copy[0][1] = "A"

print("\nAfter Deep Copy:")
print("Original List:", employees)
print("Deep Copy:", deep_copy)


