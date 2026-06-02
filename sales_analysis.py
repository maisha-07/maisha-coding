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

print("\nLondon sales over 700")
print(df[(df['city'] == 'London') & (df['amount']>700)] )

print("\nSales sorted by amount (high to low):")
print(df.sort_values('amount', ascending=False) )

df['discount_price'] = df['amount'] * 0.9
print("\nDiscounted column:")
print(df)

print("\nSales by city and product:")
print(df.groupby(['city' , 'product'])['amount'].sum())


print("\nUnique product:")
print(df['product'].nunique())


print("\nProduct count:")
print(df['product'].value_counts())


customer_data = {
    "city": ["London", "Paris", "Berlin", "Tokyo"],
    "country": ["UK", "France", "Germany", "Japan"],
    "vat_rate": [20, 20, 19, 10]
}

customers_df = pd.DataFrame(customer_data)

print("\nCustomer data:")
print(customers_df)

merged = df.merge(customers_df , on='city')
print("\nMerged data:")
print(merged)

print("\ntotal sales per country:")
print(merged.groupby('country')['amount'].sum())