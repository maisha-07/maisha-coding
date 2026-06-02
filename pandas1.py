import pandas as pd

# Create a DataFrame (table) just like customers in SQL
data = {
    "name": ["Maisha", "Tom", "Sara", "Ahmed", "Lily"],
    "city": ["London", "Paris", "Berlin", "London", "Paris"],
    "age": [25, 30, 22, 28, 19]
}

df = pd.DataFrame(data)

print(df)

print("\nfirst 3 rows:")
print(df.head(3))

print("\n:Names:")
print(df['name'])

print("\nAverage age:")
print(df['age'].mean())

print("\nLondon customers:")
print(df[df['city'] == 'London'])

print("\nCount per city:")
print(df.groupby('city').size())

print("\nAverage age per city:")
print(df.groupby('city')['age'].mean())

print("\nMin, Max per city:")
print(df.groupby('city')['age'].agg(['min', 'max', 'mean']))

