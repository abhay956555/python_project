import pandas as pd
import matplotlib.pyplot as plt

# Read Dataset
df = pd.read_csv("healthcare_dataset.csv")

print(df.head())

# Convert date columns
df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"])

# Hospital Stay
df["Hospital Stay"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days

# 1. Average Billing by Medical Condition
avg_bill = df.groupby("Medical Condition")["Billing Amount"].mean().sort_values(ascending=False)
print(avg_bill)

# 2. Total Billing by Insurance Provider
insurance = df.groupby("Insurance Provider")["Billing Amount"].sum().sort_values(ascending=False)
print(insurance)

# 3. Average Hospital Stay by Admission Type
stay = df.groupby("Admission Type")["Hospital Stay"].mean()
print(stay)

# 4. Hospital with Highest Number of Patients
hospital = df["Hospital"].value_counts()
print(hospital)

# 5. Age Group with Highest Billing
bins = [0, 20, 40, 60, 100]
labels = ["0-20", "21-40", "41-60", "61+"]

df["Age Group"] = pd.cut(df["Age"], bins=bins, labels=labels, include_lowest=True)

age_bill = df.groupby("Age Group")["Billing Amount"].sum().sort_values(ascending=False)
print(age_bill)

# 6. Doctor with Highest Revenue
doctor = df.groupby("Doctor")["Billing Amount"].sum().sort_values(ascending=False)
print(doctor)

# 7. Percentage of Test Results
result = df["Test Results"].value_counts(normalize=True) * 100
print(result)

# 8. Medical Condition with Longest Average Hospital Stay
condition_stay = df.groupby("Medical Condition")["Hospital Stay"].mean().sort_values(ascending=False)
print(condition_stay)

# 9. Most Frequent Medication for Each Medical Condition
med = df.groupby(["Medical Condition", "Medication"]).size().reset_index(name="Count")
most_med = med.loc[med.groupby("Medical Condition")["Count"].idxmax()]
print(most_med)

# 10. Top 10 Patients with Highest Billing
top10 = df.nlargest(10, "Billing Amount")
print(top10[["Name", "Age", "Medical Condition", "Billing Amount",
             "Admission Type", "Insurance Provider"]])