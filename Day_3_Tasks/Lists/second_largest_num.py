# Write a program to find the second largest number in a list. 

numbers = [23,43,33,26,74,12,56,89,90]
largest = max(numbers)

second_largest= []

for x in numbers:
    if x!=largest:
        second_largest.append(x)

second_largest_num = max(second_largest)
print("The second largest number is:", second_largest_num)

