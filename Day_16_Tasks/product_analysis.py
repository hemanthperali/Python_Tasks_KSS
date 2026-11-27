'''Scenario:
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → product vs sales
○ Pie chart → sales contribution
○ Histogram → profit distribution
○ Scatter plot → sales vs profit'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

# 1. Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit": profit
})

print("Product Sales DataFrame:")
print(df)

# 2. Line Graph - Sales Trend
plt.figure(figsize=(12, 5))
plt.subplot(2,3,1)
plt.plot(products, sales, marker='o', color='blue')
plt.title("Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.grid(True)


# 3. Bar Chart - Product vs Sales
plt.subplot(2,3,2)
plt.bar(products, sales, color='green')
plt.title("Product-wise Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")

# 4. Pie Chart - Sales Contribution
plt.subplot(2,3,3)
plt.pie(sales, labels=products, autopct='%1.1f%%',
        startangle=90)
plt.title("Sales Contribution by Product")


# 5. Histogram - Profit Distribution
plt.subplot(2,3,4)
plt.hist(profit, bins=5, color='orange',
         edgecolor='black')
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

# 6. Scatter Plot - Sales vs Profit
plt.subplot(2,3,5)
plt.scatter(sales, profit, color='red')
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)

plt.tight_layout()
plt.show()
