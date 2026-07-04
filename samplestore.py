import pandas as pd

df = pd.read_csv("SampleSuperstore.csv")
print(df.columns)
print(df.head())

print(df.info())

print(df.describe)

print(df.isnull().sum())

df = df.drop_duplicates()
df = df.dropna()

print(df.isnull().sum())

df["Profit_Percentage"] = (df["Profit"] / df["Sales"]) * 100

print(df.head())

total_revenue = df["Sales"].sum()

print("Total REvenue =", total_revenue)

print("Total Profit =", df["Profit"].sum())

print("Total Order =", len(df))

print(df.groupby("Category")["Sales"].sum())

print(df.groupby("Region")["Profit"].sum())

print(df.groupby("Category")["Sales"].sum())
print(df.groupby("State")["Sales"].sum().sort_values(ascending=False).head())
print(df.groupby("City")["Sales"].sum().sort_values(ascending=False).head())
import matplotlib.pyplot as plt

df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sles")
plt.show()