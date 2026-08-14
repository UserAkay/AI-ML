import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

del df['species']

#Calculate Correlation Matrix
correlation_matrix = df.corr()

#Plot Heatmap
sns.heatmap(correlation_matrix, annot = True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()