'''A weather station records temperatures:
[28, 31, 35, 27, 40, 22]
Scenario:
The system needs temperatures above 30°C.
Task:
● Filter the values greater than 30 using NumPy boolean filtering.'''

import numpy as np

arr = np.array([28,31,35,27,40,22])

x = [False,True,True,False,True,False]

new_arr = arr[x]

print("Temperatures above 30:",new_arr)