'''Generate random numbers:
nums = np.random.randint(1, 100, 10)
Task:
● Filter values that are divisible by 5
● Return sorted result'''

import numpy as np

nums = np.random.randint(1,100,10)

filter_nums = nums[nums%5==0]

sort_nums = np.sort(filter_nums)

print("Filtered values:",filter_nums)
print("Sorted result:",sort_nums)