# Statistical Analysis of Real-World Data: 
# 1. Perform Exploratory Data Analysis
# 2. Conduct Hypothesis Tests
# 3. Apply Linear Regression

# Extend the project by exploring additional relationships(e.g, day of the week vs tip amount)
# Perform multiple linear regression with additional varibales (e.g, include smoking status)
# Use another real-world dataset(e.g, healthcare or sales data to apply similar techniques)

# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from sklearn.linear_model import LinearRegression

# Load Dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
contingency_table = pd.crosstab(df['smoker'], df['time'])

# Inspect Data
print(df.info())
print(df.describe())

del df["sex"]
del df["smoker"]
del df["day"]
del df["time"]

# Visualize Distributions
sns.histplot(df["total_bill"], kde=True)
plt.title("Distribution Heatmap")
plt.show()

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Perform Chi-Square Test
chi2, p, dot, expected = chi2_contingency(contingency_table)
print("Chi-Square Statistic: ", chi2)
print("P-Value: ", p)

# Interpret Result
alpha = 0.05
if p <= alpha:
    print("Reject the null hypothesis: varibales are dependent")
else:
    print("Fail Reject the null hypothesis: varibales are independent")    

# Define variables
x = df['total_bill'].values.reshape(-1, 1)
y = df['tip'].values

# Fit Linear Regression
model = LinearRegression()
model.fit(x, y)

# Output Coefficients
print("Slope: ", model.coef_[0])
print("Interpret: ", model.intercept_)
print("R-Squared; ", model.score(x, y))

# PLot Regression
sns.scatterplot(x = df['total_bill'], y = df['tip'], color='blue')
plt.plot(df['total_bill'], model.predict(x), color="red", label="Regression Lines")
plt.title("Total Bill vs Tip")
plt.legend()
plt.show()