import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

url = "https://github.com/abhay956555/python_project/blob/17ea389551868dfae81479294d2063479a653d28/cricket_score.csv"

df = pd.read_csv(url)

print("===Head==")
print(df.head())

print("\n===Tail===")
print(df.tail())

print("\n====info===")
print(df.info())

print("\n describe")
print(df.describe(include="all"))

print("\n missing values")
print(df.isnull().sum())

print("\n duplicates")
print(df.duplicated().sum())

print("\n unique name")
print(df["name"].unique())

print("\n name count")
print(df["name"].value_counts())


plt.figure(figsize=(6,6))
plt.hist(df["matches"], bins=10)
plt.title("Histogram Of matches")
plt.xlabel("mattches")
plt.ylabel("frequency")
plt.show()

plt.figure(figsize=(12, 5))
sns.countplot(x="odi", data=df)
plt.title("count Plot Of Odi")
plt.show()

plt.figure(figsize=(6,6))
plt.scatter(df["matches"],df["test"])
plt.title("matches vs test")
plt.xlabel("matches")
plt.ylabel("test")
plt.show()

plt.figure(figsize=(6, 6))
sns.boxplot(y=df["matches"])
plt.title("box Plot Of matches")
plt.show()

plt.figure(figsize=(6,6))
numeric_df= df.select_dtypes(include=["number"])
sns.heatmap(df[["odi", "test",  "matches"]].corr(),
             annot=True,
             cmap="coolwarm"

)

plt.title("correlation Heatmap")
plt.show()