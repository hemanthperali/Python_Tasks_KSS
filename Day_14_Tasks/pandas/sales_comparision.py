'''A shop tracks fruit sales:
S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"])
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])
Task:
● Add both series
● Find the total sales of all fruits combined'''

import pandas as pd

s1 = pd.Series([10,20,30], index = ["apple","banana","cherry"])
s2 = pd.Series([5,15,25], index = ["apple","banana","cherry"])

add_sales = s1.add(s2)
total_sales = add_sales.sum()

print(add_sales)
print("Total sales of all fruits:",total_sales)