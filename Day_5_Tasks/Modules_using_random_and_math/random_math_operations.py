'''
  Write a Python program that generates 20 random numbers between 1 and 200 using 
the random module and store them in a list. 
Then using the math module, compute and display: 
● Maximum value 
● Minimum value 
● Square root of the maximum number 
● Logarithm of the minimum number
'''


import random
import math

list1 = []

for i in range(20):
    num = random.randint(1,200)
    list1.append(num)

# Find the maximum number
max_number = max(list1)

#Find minimum number
min_number = min(list1)

# Square root of maximum number
max_sqrt = math.sqrt(max_number)

# Logarithm of minimum number
min_log = math.log(min_number)


# Display the result
print("Random Numbers:",list1)
print("Maximum Number:",max_number)
print("Minimum Number:",min_number)
print("Square root of maximum number:",max_sqrt)
print("Logarithm of minimum number:",min_log)




