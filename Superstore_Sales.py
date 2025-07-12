import pandas as pd

# Read CSV with correct encoding
df = pd.read_csv("Superstore_Sales.csv", encoding="cp1252", parse_dates=["Order Date"])

# Convert Order Date to Month-Year
df["Month-Year"] = df["Order Date"].dt.to_period("M").dt.to_timestamp()

# Drop rows with missing Region, Category, or Sales
df = df.dropna(subset=["Region", "Category", "Sales"])

# Save cleaned file
df.to_csv("Superstore_Clean.csv", index=False)

print("✅ Data cleaned and saved as Superstore_Clean.csv")
print(df.head())
