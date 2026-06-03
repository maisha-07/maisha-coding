import pandas as pd

# Create sample data with some MISSING values (NaN)
data = {
    "name": ["Maisha", "Tom", "Sara", "Ahmed", "Lily", "Jin"],
    "city": ["London", "Paris", "Berlin", "London", None, "Tokyo"],
    "age": [25, 30, None, 28, 19, 35],
    "salary": [40000, 50000, 35000, None, 30000, 60000]
}

df = pd.DataFrame(data)
print("Data with missing values (NaN):")
print(df)

print("\nHow many missing in each column?")
print(df.isnull().sum())

print("\nDrop column")
print(df.dropna())

print("\nFilling missing values")
df_filled = df.fillna({
    'age' : df['age'].mean(),
    'city' : 'unknown',
    'salary' : 0
})

print(df_filled)

print("\nOriginal df")
print(df)

df['salary_k']=df['salary'].apply(lambda x: f"{x/1000}k" if pd.notna(x) else "N/A")

print("\nSalary i k format")
print(df)

def age_group(age):
    if pd.isna(age):
        return "unknown"
    elif age < 25:
        return "young"
    elif age < 35:
        return "Middle"
    else:
        return "Senior"

df['age_group'] = df['age'].apply(age_group)

print("\nWith age group")
print(df)

sales = pd.read_csv("sales.csv")
print("\nSales data")
print(sales)

pivot = sales.pivot_table(
    index='city',
    columns='product',
    values='amount',
    aggfunc='sum'
)

print("\nPivot table sales by city X product:")
print(pivot)

pivot_count = sales.pivot_table(
    index='city',
    columns='product',
    values='amount',
    aggfunc='count'
)

print("\nCount of sales per city X product:")
print(pivot_count)

print("\nPivot with 0 for missing:")
print(pivot.fillna(0))