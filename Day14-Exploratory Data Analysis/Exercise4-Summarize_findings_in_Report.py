import pandas as pd
import numpy as np

np.random.seed(42)
data = pd.DataFrame({
    "region": ["Lagos"]*50 + ["Abuja"]*50,
    "sales_amount": np.concatenate([np.random.normal(1000, 100, 50), np.random.normal(800, 90, 50)])
})

report_lines = []
report_lines.append("SALES DATA ANALYSIS REPORT")
report_lines.append("=" * 30)
report_lines.append(f"Total records: {len(data)}")
report_lines.append(f"Average sales: {data['sales_amount'].mean():.2f}")
report_lines.append(f"Median sales: {data['sales_amount'].median():.2f}")
report_lines.append(f"Standard deviation: {data['sales_amount'].std():.2f}")
report_lines.append(f"Min sales: {data['sales_amount'].min():.2f}")
report_lines.append(f"Max sales: {data['sales_amount'].max():.2f}")

report_lines.append("\nSales by region:")
for region, avg in data.groupby("region")["sales_amount"].mean().items():
    report_lines.append(f"  {region}: average = {avg:.2f}")

report = "\n".join(report_lines)
print(report)

with open("findings_report.txt", "w") as f:
    f.write(report)