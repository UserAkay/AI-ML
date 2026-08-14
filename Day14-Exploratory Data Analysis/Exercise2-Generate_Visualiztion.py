import  matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Load Datset
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")


#Bar Char: Survival rate by class
survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color="skyblue")
plt.title("Survival Rate By Class")
plt.ylabel("Survival Rate")
plt.show()

#Histogram: Age Distribution
sns.histplot(df["Age"], kde = True, bins=20, color = "purple")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("frequency")
plt.show()

#Scatter Plot: Age vs Fare
plt.scatter(df["Age"], df["Fare"], alpha = 0.5, color = "green")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()