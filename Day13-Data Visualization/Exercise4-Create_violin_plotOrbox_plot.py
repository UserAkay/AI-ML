import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)
data = pd.DataFrame({
    "region": ["Lagos"]*50 + ["Abuja"]*50 + ["Ibadan"]*50,
    "sales_amount": np.concatenate([
        np.random.normal(1000, 150, 50),
        np.random.normal(800, 100, 50),
        np.random.normal(600, 120, 50)
    ])
})

plt.figure(figsize=(8, 5))
sns.violinplot(x="region", y="sales_amount", data=data)
plt.title("Sales Distribution by Region (Violin Plot)")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x="region", y="sales_amount", data=data)
plt.title("Sales Distribution by Region (Box Plot)")
plt.show()