'''A DataFrame:
data = pd.DataFrame({
"Name": ["A", "B", "C"],
"Math": [80, 70, 60],
"Science": [90, 60, 70]
})
Task:
● Add a new column Total = Math + Science
● Find the student with the highest total marks'''

import pandas as pd

data = pd.DataFrame({"Name":["A","B","C"],
                     "Math":[80,70,60],
                     "Science":[90,60,70]})

df = pd.DataFrame(data)


df['Total'] = df["Math"] + df["Science"]

print(df)

highest = df.loc[df["Total"].idxmax()]

print("Student with highest marks:\n",highest)