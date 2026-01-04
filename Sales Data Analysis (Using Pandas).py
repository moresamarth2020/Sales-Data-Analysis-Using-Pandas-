import pandas as pd

# Create sample sales data
data = {
    "Date": ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05"],
    "Product": ["Laptop", "Mobile", "Laptop", "Tablet", "Mobile"],
    "Quantity": [2, 5, 1, 3, 4],
    "Price": [50000, 20000, 50000, 15000, 20000]
}

df = pd.DataFrame(data)

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

print("----- SALES DATA -----")
display(df)

# Total revenue
total_revenue = df["Total_Sales"].sum()
print("💰 Total Revenue:", total_revenue)

# Best selling product
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()
print("🏆 Best Selling Product:", best_product)

# Average sales per day
avg_sales = df["Total_Sales"].mean()
print("📊 Average Daily Sales:", avg_sales)
