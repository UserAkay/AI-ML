import pandas as pd

sales = pd.DataFrame({
    "region": ["Lagos", "Abuja", "Lagos", "Ibadan", "Abuja", "Lagos", "Ibadan"],
    "product_category": ["Electronics", "Clothing", "Clothing", "Electronics",
                          "Electronics", "Furniture", "Furniture"],
    "sales_amount": [1200, 450, 600, 900, 1100, 300, 250],
    "year": [2024, 2024, 2025, 2024, 2025, 2025, 2024]
})

def custom_variance(series):
    mean = series.mean()
    return ((series - mean) ** 2).mean()

print(sales.groupby("region")["sales_amount"].agg(custom_variance))
print(sales.groupby("region")["sales_amount"].var())