import pandas as pd

# Read the CSV file
df = pd.read_csv("sales.csv")

# See what's in it
print("All sales:")
print(df)

print("\nFirst 3 rows:")
print(df.head(3))

print("\nColumn names + types:")
print(df.info())

print("\nQuick stats:")
print(df.describe())

# Total sales per city
print("\nTotal sales per city:")
print(df.groupby('city')['amount'].sum())

# Total sales per product
print("\nTotal sales per product:")
print(df.groupby('product')['amount'].sum())

# Best customer of all products
print("\nTop product (most sales):")
print(df.groupby('product')['amount'].sum().sort_values(ascending=False))

# Average sale amount
print("\nAverage sale:")
print(df['amount'].mean())

