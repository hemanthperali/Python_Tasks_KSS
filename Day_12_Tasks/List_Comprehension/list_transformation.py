'''A dataset contains:
data = [[1, 2, 3], [4, 5], [6]]
Task:
● Flatten the list using list comprehension.
● Then create a new list containing squares of only even numbers.'''

data = [[1,2,3],[4,5],[6]]

# Flatten the list
flat_list = [num for i in data for num in i]

# Print the flattened list
print("Flattened list:",flat_list)

# Find squares of even numbers
even_num = [num**2 for num in flat_list if num%2==0]

# Print the squares
print("Squares of even numbers:",even_num)