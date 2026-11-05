#  Write a function to find the sum of elements in a list using a user-defined function.

def sum_of_elements(lst):
    total = sum(lst)
    return total

result = sum_of_elements([1, 2, 3, 4, 5])
print("Sum of elements:", result)