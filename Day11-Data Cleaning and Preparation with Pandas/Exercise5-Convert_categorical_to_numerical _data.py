import pandas as pd

data = pd.DataFrame({
    "customer_id": [1, 2, 3, 4, 5],
    "city": ["Lagos", "Abuja", "Lagos", "Ibadan", "Abuja"],
    "membership": ["Gold", "Silver", "Gold", "Bronze", "Silver"]
})

data_encoded = pd.get_dummies(data, columns=["city", "membership"])
dummy_cols = data_encoded.columns.difference(["customer_id"])
data_encoded[dummy_cols] = data_encoded[dummy_cols].astype(int)
print(data_encoded)