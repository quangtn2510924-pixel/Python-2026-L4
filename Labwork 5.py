import openpyxl 
import pandas as pd

df = pd.read_csv("students.csv")
print(df.head())
print(df[["name", "GPA"]])
high_gpa_students = df[df["GPA"] >= 3.5]
print(high_gpa_students)
print(f"Số hàng: {df.shape[0]}, Số cột: {df.shape[1]}")
sorted_students = df.sort_values(by="GPA", ascending=False)
print(sorted_students)
avg_gpa_by_major = df.groupby("major")["GPA"].mean()
print(avg_gpa_by_major)