import pandas as pd
import numpy as np


data = {
    "Name": ["Amit", "Priya", "Rahul", "Neha", "Karan"],
    "Department": ["HR", "IT", "Finance", "HR", "IT"],
    "Salary": [55000, 75000, 48000, 62000, 90000],
    "Emp_id": [103, 408, 738, 683, 850],
    "Age":    [26, 45, 27, 34, 22]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nFirst 3 Rows:")
print(df.head(3))

print("\nLast 2 rows:")
print(df.tail(2))

print("\nshape:")
print(df.shape)

