import pandas as pd

customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "customer_name": ["Amaka", "Bola", "Chidi", "Deji"],
    "city": ["Lagos", "Abuja", "Lagos", "Ibadan"]
})

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105],
    "customer_id": [1, 2, 1, 3, 4],
    "product_id": [201, 202, 203, 201, 202],
    "quantity": [2, 1, 5, 3, 2]
})

products = pd.DataFrame({
    "product_id": [201, 202, 203],
    "product_name": ["Laptop", "Phone", "Headset"],
    "price": [1500, 800, 100]
})

customer_orders = pd.merge(customers, orders, on="customer_id", how="inner")
full_data = pd.merge(customer_orders, products, on="product_id", how="inner")
print(full_data)

full_data["total_price"] = full_data["quantity"] * full_data["price"]
print(full_data)

print(full_data.groupby("customer_name")["total_price"].sum())
print(full_data.groupby("product_name")["quantity"].sum().sort_values(ascending=False))
print(full_data[["quantity", "price", "total_price"]].corr())