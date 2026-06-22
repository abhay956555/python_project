import pandas as pd


data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Abhay", "Anmol", "Aditya", "Hariom"],
    "Department": ["HR", "IT", "Finance", "HR", "IT"],
    "Salary": [45000, 60000, 55000, 70000, 50000]
}

df = pd.DataFrame(data)

print("Employee Dataset:")
print(df)


print("\nEmployees earning above ₹50,000:")
print(df[df["Salary"] > 50000])


print("\nHR Employees:")
print(df[df["Department"] == "HR"])

print("\nHighest Salary Employee:")
print(df[df["Salary"] == df["Salary"].max()])