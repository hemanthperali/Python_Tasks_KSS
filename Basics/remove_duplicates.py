# Given a list `[1, 2, 3, 2, 4, 1, 5, 3]`, remove duplicate elements while preserving the original order. Do not use `set()`.

l = [1,2,3,2,4,1,5,3]

# Create an empty list to store unique numbers
list1 = []

# Looping through each element in the given list
for i in l:
    # Check if the current number is not in new list
    if i not in list1:
        # If the number is new , add it to new list
        list1.append(i)

# Print the output
print(list1)
