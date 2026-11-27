'''Scenario:
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → daily temperature trend
○ Bar chart → day-wise temperature
○ Pie chart → proportion of high (>30) vs low temps
○ Histogram → temperature frequency
○ Scatter plot → day index vs temperature'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df = pd.DataFrame({"Temperatures":temps,"Days":days})
print(df)

plt.figure(figsize=(12,5))

# Line Graph - Daily temperature trend
plt.subplot(2,3,1)
plt.plot(days,temps,marker = 'o' ,color = 'b')
plt.title("Daily Temperature")
plt.xlabel("Temperatures")
plt.ylabel("days")
plt.grid(True)

# Bar Graph - Day wise temperature
plt.subplot(2,3,2)
plt.bar(days,temps,color = 'g')
plt.title("Day-wise Temperature")
plt.xlabel("Days")
plt.ylabel("Temperatures")

# Pie chart - proportion of high vs low temps
high = np.sum(temps > 30)
low = np.sum(temps <= 30)

labels = ["High ", "Low"]
values = [high, low]

plt.subplot(2,3,3)
plt.pie(values,labels = labels,autopct='%1.1f%%',startangle=90)
plt.title("High vs Low Temperature")


# Histogram - Temperature frequency
plt.subplot(2,3,4)
plt.hist(temps, bins = 7,color='r',edgecolor = 'black')
plt.title("Temperature Frequency")
plt.xlabel("Temperature")
plt.ylabel("Frequency")

# Scatter plot- Day index vs temperature
index = np.arange(len(days))

plt.subplot(2,3,5)
plt.scatter(index, temps, color='red')
plt.title("Day Index vs Temperature")
plt.xlabel("Day Index")
plt.ylabel("Temperature (°C)")
plt.xticks(index, days)

plt.tight_layout()
plt.show()