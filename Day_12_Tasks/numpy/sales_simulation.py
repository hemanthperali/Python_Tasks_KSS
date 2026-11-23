'''Scenario:
A company wants to simulate 10 days of sales (range 100–500).
Task:
● Generate random integers using NumPy.
● Print the array.
● Find the average sales.'''

from numpy import random
import numpy as np

x = np.random.randint(100,501,size = 10)

print("10 Days Sales:",x)

average = np.mean(x)

print("Average:",average)

