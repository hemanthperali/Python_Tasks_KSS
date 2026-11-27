'''Scenario:
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
Task:
● Convert into DataFrame
● Plot:
○ Line graph → salary trend
○ Bar chart → department-wise salary comparison
○ Pie chart → department distribution
○ Histogram → salary distribution
○ Scatter plot → index vs salary'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

df = pd.DataFrame({"Salaries":salaries,"Departments":departments})
print(df)

plt.figure(figsize=(10,5))

# Line Graph - Salary Trend
plt.subplot(2,3,1)
plt.plot(salaries,departments,marker = 'o',color = 'g')
plt.title("Salary Trend")
plt.xlabel("Departments")
plt.ylabel("Salaries")
plt.grid(True)

# Bar Graph - department -wise salary comparision
department_salary = df.groupby("Departments")["Salaries"].mean()

plt.subplot(2,3,2)
plt.bar(department_salary.index,department_salary.values,color = 'b')
plt.title("Salary Comparision")
plt.xlabel("Departments")
plt.ylabel("salaries")

# Pie Chart - Department Distribution
department_count = df["Departments"].value_counts()
plt.subplot(2,3,3)
plt.pie(department_count,labels=department_count.index,autopct='%1.1f%%',startangle=90)
plt.title("Department Distribution")

# Histogram - Salary Distribution
plt.subplot(2,3,4)
plt.hist(salaries,bins=6,color='r',edgecolor = 'black')
plt.title("Salary Distribution")
plt.xlabel("salaries")
plt.ylabel("Frequency")

# Scatter plot - index vs salary
index1 = np.arange(len(salaries))
plt.subplot(2,3,5)
plt.scatter(index1,salaries,color = 'b')
plt.title("Employee Index vs Salary")
plt.xlabel("Employee Index")
plt.ylabel("Salaries")

plt.tight_layout()
plt.show()

