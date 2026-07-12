import pandas as pd
import matplotlib.pyplot as plt

url="https://raw.githubusercontent.com/abhay956555/python_project/refs/heads/main/healthcare_dataset.csv"
df = pd.read_csv(url)

print(df.head())

df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"])

df["Hospital Stay"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days

avg_bill = df.groupby("Medical Condition")["Billing Amount"].mean().sort_values(ascending=False)
print(avg_bill)

insurance = df.groupby("Insurance Provider")["Billing Amount"].sum().sort_values(ascending=False)
print(insurance)

stay = df.groupby("Admission Type")["Hospital Stay"].mean()
print(stay)

hospital = df["Hospital"].value_counts()
print(hospital)

bins = [0, 20, 40, 60, 100]
labels = ["0-20", "21-40", "41-60", "61+"]

df["Age Group"] = pd.cut(df["Age"], bins=bins, labels=labels, include_lowest=True)

age_bill = df.groupby("Age Group")["Billing Amount"].sum().sort_values(ascending=False)
print(age_bill)

doctor = df.groupby("Doctor")["Billing Amount"].sum().sort_values(ascending=False)
print(doctor)

result = df["Test Results"].value_counts(normalize=True) * 100
print(result)

condition_stay = df.groupby("Medical Condition")["Hospital Stay"].mean().sort_values(ascending=False)
print(condition_stay)

med = df.groupby(["Medical Condition", "Medication"]).size().reset_index(name="Count")
most_med = med.loc[med.groupby("Medical Condition")["Count"].idxmax()]
print(most_med)

top10 = df.nlargest(10, "Billing Amount")
print(top10[["Name", "Age", "Medical Condition", "Billing Amount",
             "Admission Type", "Insurance Provider"]])
