import pandas as pd

# Load REAL ONS data
df = pd.read_csv("ons_rental.csv", skiprows=6, encoding='latin1')

# See what's in it
print("Shape (rows, columns):", df.shape)
print("\nFirst 10 rows:")
print(df.head(10))

print("\nColumn names:")
print(df.columns.tolist())

print("\nColumn types + nulls:")
df.info()
