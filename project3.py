import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/abhay956555/python_project/0492ebfc2bec6e0abbeec1d8583450c4ff0a3396/BlinkIT%20Grocery%20Data.xlsx"

df = pd.read_excel(url)
print(df.head())

total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

item_sales = df.groupby("Item Type")["Sales"].sum().sort_values(ascending=False).head(10)

print(item_sales)

item_sales.plot(kind="bar", figsize=(8,5))
plt.title("Top 10 Item Types by Sales")
plt.xlabel("Item Type")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

outlet_sales = df.groupby("Outlet Type")["Sales"].sum().sort_values(ascending=False)

print(outlet_sales)

outlet_sales.plot(kind="bar", figsize=(7,5))
plt.title("Sales by Outlet Type")
plt.xlabel("Outlet Type")
plt.ylabel("Sales")
plt.xticks(rotation=30)
plt.show()

location_sales = df.groupby("Outlet Location Type")["Sales"].sum()
print(location_sales)

location_sales.plot(kind="pie", autopct="%1.1f%%", figsize=(6,6))
plt.title("Sales by Outlet Location Type")
plt.ylabel("")
plt.show()

size_sales= df.groupby("Outlet Size")["Sales"].sum()

print(size_sales)
size_sales.plot(kind="pie" , autopct="%1.1f%%", figsize=(6,6))
plt.title("Sales by Outlet Size")
plt.ylabel("")
plt.show()

outlet_year = df["Outlet Establishment Year"].value_counts().sort_index()

print(outlet_year)

outlet_year.plot(kind="line", marker="o", figsize=(8,5))
plt.title("Outlet Expansion Over Years")
plt.xlabel("Year")
plt.ylabel("Numner of Outlets")
plt.grid(True)
plt.show()

df["Item Fat Content"] = df["Item Fat Content"].replace({
    "LF": "Low Fat",
    "low fat": "Low Fat",
    "Low fat": "Low Fat",
    "reg": "Regular",
    })

fat_sales = df.groupby("Item Fat Content")["Sales"].sum()

print(fat_sales)

fat_sales.plot(kind="bar", figsize=(6,5))
plt.title("Sales by Fat Content")
plt.xlabel("Fat Content")
plt.ylabel("Sales")
plt.show()

plt.figure(figsize=(7,5))
plt.scatter(df["Item Visibility"], df["Sales"])
plt.title("Item Visibility vs Sales")
plt.xlabel("Item visibility")
plt.ylabel("Sales")
plt.show()

rating = df.groupby("Item Type")["Rating"].mean().sort_values(ascending=False)

print(rating)
rating.plot(kind="barh", figsize=(8,6))
plt.title("Average Rating by Item Type")
plt.xlabel("Average Rating")
plt.show()
