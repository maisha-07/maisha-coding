import pandas as pd
df = pd.read_csv("london_rentals.csv")

print("First 5 rows:")
print(df.head())

print("\nColumns + types")
df.info()

print("\nQuick stats:")
print(df.describe())

print("\nUnique boroughs:")
print(df['borough'].unique())

print("\nUnique years:")
print(df['year'].unique())

# INSIGHT 1 - Highest 2-bed rent in 2026
print("\nINSIGHT 1: Top 5 most expensive 2-bed boroughs in 2026")
top_expensive = df[(df['year'] == 2026) & (df['property_type'] == '2bed')]
print(top_expensive.sort_values('median_rent_pcm', ascending=False).head())


# INSIGHT 2 - Rent growth 2022 to 2026 in Hackney (2bed)
print("\nINSIGHT 2: Hackney 2-bed rent growth")
hackney = df[(df['borough'] == 'Hackney') & (df['property_type'] == '2bed')]
print(hackney[['year', 'median_rent_pcm']])

# Calculate growth %
rent_2022 = hackney[hackney['year'] == 2022]['median_rent_pcm'].values[0]
rent_2026 = hackney[hackney['year'] == 2026]['median_rent_pcm'].values[0]
growth = ((rent_2026 - rent_2022) / rent_2022) * 100
print(f"Growth: {growth:.1f}%")


# INSIGHT 3 - Average rent by zone (2026)
print("\nINSIGHT 3: Average rent by zone in 2026")
zone_avg = df[df['year'] == 2026].groupby('zone')['median_rent_pcm'].mean()
print(zone_avg)
