import pandas as pd

#Load Titanic dataset
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

#Inspect Data
print(df.info())
print(df.describe())

#Handle Missing Values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

#Remove duplicate
df = df.drop_duplicates()

#Filter data: Passenges in first class
first_class = df[df["Pclass"] == 1]
print("First Class Passengers \n", first_class.head())