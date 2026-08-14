import pandas as pd

# 1. Create a dictionary
data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Maths": [85, 92, 78, 88],
    "Science": [90, 85, 80, 95]
}

# 2. Create DataFrame from dictionary
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 3. Add a new calculated column (Total Marks)
df["Total"] = df["Maths"] + df["Science"]

# 4. Add another calculated column (Average)
df["Average"] = df["Total"] / 2

print("\nDataFrame after adding calculated columns:")
print(df)