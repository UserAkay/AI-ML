# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

from scipy.stats import skew, kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Analyze sepal_length
feature = df["sepal_length"]
print("skewness; ", skew(feature))
print("kurtosis: ", kurtosis(feature))

# Visualize Distribution
sns.histplot(feature, kde=True)
plt.title("Distribution of Sepal Length")
plt.show()
