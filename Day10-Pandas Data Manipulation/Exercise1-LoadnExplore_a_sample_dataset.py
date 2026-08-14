#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd

#Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

#Explore Structure
print("First 5 Rows: \n", df.head())
print("Last 5 rows: \n", df.tail())
print(df.info())
print(df.describe())