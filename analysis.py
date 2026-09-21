from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_excel(BASE_DIR / "Online Retail.xlsx")

print(df.head())

print(df.shape)

print(df.columns)

print(df.info())

print(df.isnull().sum())
print(df.duplicated().sum())
print((df["Quantity"] < 0).sum())
print((df["UnitPrice"] <= 0).sum())
print(df[df["UnitPrice"] <= 0].head(10))
print(df[df["UnitPrice"] <= 0]["UnitPrice"].value_counts())
df = df.drop_duplicates()

print(df.shape)
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

print(df.shape)
df = df[df["UnitPrice"] > 0]

print(df.shape)
df["Sales"] = df["Quantity"] * df["UnitPrice"]

print(df.head())
print(df.shape)
# =========================
# SALES ANALYSIS
# =========================

# 1. Total Sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# 2. Total Quantity Sold
total_quantity = df["Quantity"].sum()
print("Total Quantity Sold:", total_quantity)

# 3. Total Orders
total_orders = df["InvoiceNo"].nunique()
print("Total Orders:", total_orders)

# 4. Top 10 Products by Sales
top_products = (
    df.groupby("Description")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products:")
print(top_products)

# 5. Sales by Country
country_sales = (
    df.groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Countries:")
print(country_sales)

# 6. Monthly Sales
df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)

print("\nMonthly Sales:")
print(monthly_sales)

# 7. Top 10 Customers
top_customers = (
    df.groupby("CustomerID")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Customers:")
print(top_customers)
# =========================
# ADDITIONAL ANALYSIS
# =========================

# 8. Average Order Value (AOV)
aov = total_sales / total_orders
print("\nAverage Order Value:", round(aov, 2))


# 9. Monthly Order Count
monthly_orders = df.groupby("Month")["InvoiceNo"].nunique()

print("\nMonthly Orders:")
print(monthly_orders)


# =========================
# VISUALIZATION
# =========================

# =========================
# VISUALIZATION
# =========================

import matplotlib.pyplot as plt

# Create a folder for charts
CHART_DIR = BASE_DIR / "charts"
CHART_DIR.mkdir(exist_ok=True)


# 1. Monthly Sales Trend
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(CHART_DIR / "monthly_sales.png", dpi=300)
plt.show()
plt.close()


# 2. Top 10 Products
plt.figure(figsize=(10, 6))
top_products.sort_values().plot(kind="barh")
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")
plt.tight_layout()

plt.savefig(CHART_DIR / "top_products.png", dpi=300)
plt.show()
plt.close()


# 3. Top 10 Countries
plt.figure(figsize=(10, 6))
country_sales.sort_values().plot(kind="barh")
plt.title("Top 10 Countries by Sales")
plt.xlabel("Sales")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig(CHART_DIR / "top_countries.png", dpi=300)
plt.show()
plt.close()


# 4. Top 10 Customers
plt.figure(figsize=(10, 6))
top_customers.sort_values().plot(kind="barh")
plt.title("Top 10 Customers by Sales")
plt.xlabel("Sales")
plt.ylabel("Customer ID")
plt.tight_layout()

plt.savefig(CHART_DIR / "top_customers.png", dpi=300)
plt.show()
plt.close()


print("\nAll charts saved successfully!")