'''You are given monthly sales:
sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])
Task:
● Filter all sales values greater than the average sales
● Return the filtered array.'''

import numpy as np

sales = np.array([12000,18000,9000,22000,15000,3000])

avg_sales = np.mean(sales)

print("Average Sales:",avg_sales)

filter_sales = sales[sales > avg_sales]

print("Filtered Values:",filter_sales)