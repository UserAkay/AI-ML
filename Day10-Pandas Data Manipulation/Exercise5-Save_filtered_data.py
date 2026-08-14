import pandas as pd

# 1. Create a sample DataFrame
data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Vikram"],
    "Marks": [85, 92, 67, 88, 45],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 2. Filter the data (example: students who scored more than 80)
filtered_df = df[df["Marks"] > 80]

print("\nFiltered DataFrame (Marks > 80):")
print(filtered_df)

# 3. Save the filtered data to a new CSV file
filtered_df.to_csv("filtered_students.csv", index=False)

print("\nFiltered data has been saved to 'filtered_students.csv'")