'''A DataFrame:
df = pd.DataFrame({
"A": [10, 20, 30],
"B": [5, 15, 25]
}, index=["x", "y", "z"])
Task:
● Select row with index "y"
● Delete row "x"
● Print updated DataFrame'''

import pandas as pd

df = pd.DataFrame({"A":[10,20,30],
                   "B":[5,15,25]},index =["x","y","z"])

print("Selected row:\n",df.loc["y"],"\n")

print("Deleted row:\n",df.drop("x"),"\n")

print("Updated Dataframe:\n",df,"\n")