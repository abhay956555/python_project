import pandas as pd

df = pd.read_csv("Employee.csv")


print("Top 5 Rows")
print(df.head())

print("\n last 5 rows")
print(df.tail())

print("\n dataset shape")
print(df.shape)

print("\n column names")
print(df.columns)

print("\n data type")
print(df.dtypes)

print("\n dataset informaton ")
print(df.info())

print("\n===== Statistical Summary =====")
print(df.describe())

if "salary" in df.columns:

 print("\n salary statistics")
 print("maximum salary :", df["salary"].max())
 print("minumum salary: ", df["salary"].min())
 print("average salary :", df["salary"].mean())
 print("total salary:", df["salary"].sum())

if "department" in df.columns:
    print("\n department wise employee count")
    print(df["department"].value_counts())





print("\n missing values")
print(df.isnull().sum())


print("\n duplicate rows")
print(df.duplicated().sum())


df.to_excel("employee.xlsx", index=False)