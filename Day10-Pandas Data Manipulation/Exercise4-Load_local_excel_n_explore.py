import pandas as pd

# 1. Load the Excel file
df = pd.read_excel("your_file.xlsx")   # change the file name

# 2. See basic information
print("Shape of the data (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types of each column:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nSummary of the data:")
print(df.info())

print("\nStatistical summary (only numeric columns):")
print(df.describe())

print("\nNumber of missing values in each column:")
print(df.isnull().sum())