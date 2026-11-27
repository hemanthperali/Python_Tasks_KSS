'''Scenario:
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → month-wise comparison
○ Pie chart → contribution of each month
○ Histogram → frequency of sales values
○ Scatter plot → month index vs sales'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

df = pd.DataFrame({"Months":months,"Sales":sales})
print(df)

plt.figure(figsize=(12,5))

plt.subplot(2,3,1)
plt.plot(months, sales, marker='o', color='blue')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)


# Bar Chart - Month-wise Comparison
plt.subplot(2,3,2)
plt.bar(months, sales, color='green')
plt.title("Month-wise Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")


#  Pie Chart - Monthly Contribution
plt.subplot(2,3,3)
plt.pie(sales, labels=months, autopct='%1.1f%%',
        startangle=90)
plt.title("Monthly Sales Contribution")


# Histogram - Frequency of Sales Values
plt.subplot(2,3,4)
plt.hist(sales, bins=5, color='orange',
         edgecolor='black')
plt.title("Frequency Distribution of Sales")
plt.xlabel("Sales Values")
plt.ylabel("Frequency")


#  Scatter Plot - Month Index vs Sales
month_index = np.arange(len(months))

plt.subplot(2,3,5)
plt.scatter(month_index, sales, color='red')
plt.title("Month Index vs Sales")
plt.xlabel("Month Index")
plt.ylabel("Sales")
plt.xticks(month_index, months)


plt.tight_layout()
plt.show()
