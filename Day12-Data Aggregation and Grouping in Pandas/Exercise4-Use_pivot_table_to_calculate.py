import pandas as pd

sales = pd.DataFrame({
    "region": ["Lagos", "Abuja", "Lagos", "Ibadan", "Abuja", "Lagos", "Ibadan"],
    "product_category": ["Electronics", "Clothing", "Clothing", "Electronics",
                          "Electronics", "Furniture", "Furniture"],
    "sales_amount": [1200, 450, 600, 900, 1100, 300, 250],
    "year": [2024, 2024, 2025, 2024, 2025, 2025, 2024]
})

print(pd.pivot_table(sales, values="sales_amount", index="region", aggfunc="sum"))
print(pd.pivot_table(sales, values="sales_amount", index="year", aggfunc="sum"))
print(pd.pivot_table(sales, values="sales_amount", index="region", columns="year", aggfunc="sum", fill_value=0))