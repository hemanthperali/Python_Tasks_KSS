'''A school stores classroom data:
classes = [["Math", [30, 35]], ["Science", [25, 28]]]
Scenario:
● Create a deep copy of this structure.
● Modify student count in original.
Task:
● Prove that copied data remains unchanged.
● Explain why deep copy is required here.'''

import copy

classes = [["Math", [30, 35]], ["Science", [25, 28]]]

# Create a deep copy
copied_classes = copy.deepcopy(classes)

# Modify student count in original list
classes[0][1][0] = 40

# Print both lists
print("Original List:", classes)
print("Copied List:", copied_classes)



'''
Explanation : We need deep copy here because it creates independent nested objects
                 preventing unwanted changes.
'''

