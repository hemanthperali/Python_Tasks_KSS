'''  Write a Python program using the random module to generate 10 random integers 
between 1 and 100 and store them in a list. Print the list.'''

import random

# Intialize an empty list
list1 = []

#  Loop 10 times to generate add new number
for i in range(10):
    n =  random.randint(1,100)
    list1.append(n)

print(list1)