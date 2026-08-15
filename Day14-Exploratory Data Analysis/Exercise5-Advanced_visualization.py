import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)
data = pd.DataFrame({
    "sales_amount": np.random.normal(1000, 150, 100),
    "quantity": np.random.randint(1, 20, 100),
    "price": np.random.normal(50, 10, 100),
    "region": np.random.choice(["Lagos", "Abuja", "Ibadan"], 100)
})

# Pairplot to see relationships between numeric variables
sns.pairplot(data, hue="region")
plt.suptitle("Pairplot of Sales Data", y=1.02)
plt.show()

# Boxplot for distribution across a category
plt.figure(figsize=(8, 5))
sns.boxplot(x="region", y="price", data=data)
plt.title("Price Distribution by Region")
plt.show()