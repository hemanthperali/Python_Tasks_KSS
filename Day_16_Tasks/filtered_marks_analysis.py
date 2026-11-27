'''Scenario:
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]
Task:
● Convert to DataFrame
● Filter students with marks > 50
● Plot bar chart only for filtered students'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

marks = np.array([45,80,60,30,90])
names = ["A","B","C","D","E"]

df = pd.DataFrame({"Marks":marks,"Names":names})
print(df)

filter_students = df[df["Marks"]>50]

plt.bar(filter_students["Names"],filter_students["Marks"])

plt.title("Student Marks")

plt.show()