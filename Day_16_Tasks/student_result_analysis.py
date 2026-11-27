'''Scenario:
scores = np.array([40, 60, 80, 30, 90])
Task:
● Categorize into:
○ Pass (>50)
○ Fail (<=50)
● Count using NumPy/Pandas
● Plot pie chart for Pass vs Fail'''


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

scores = np.array([40, 60, 80, 30, 90])

# Categorize into Pass and Fail
pass_students = scores[scores > 50]
fail_students = scores[scores <= 50]

# Count students
res = np.where(scores>50,"Pass","Fail")
counts = pd.Series(res).value_counts()

print(counts)
plt.pie(counts, labels=counts.index, autopct='%1.1f%%',
        startangle=90)

plt.title("Result Analysis")
plt.show()
