import pandas as pd
import numpy as np

np.random.seed(42)
data = pd.DataFrame({
    "sales_amount": np.concatenate([np.random.normal(1000, 100, 95), [5000, 50, 4800, 100, 4900]])
})

# IQR method to identify anomalies
Q1 = data["sales_amount"].quantile(0.25)
Q3 = data["sales_amount"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

anomalies = data[(data["sales_amount"] < lower_bound) | (data["sales_amount"] > upper_bound)]

print(f"Lower bound: {lower_bound:.2f}, Upper bound: {upper_bound:.2f}")
print(f"Number of anomalies found: {len(anomalies)}")
print("\nAnomalies:")
print(anomalies)

print("\nInterpretation: values far outside the IQR range are likely outliers,")
print("possibly data entry errors or unusually large/small sales events.")