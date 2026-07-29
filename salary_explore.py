import pandas as pd

df = pd.read_csv("salaries.csv")

print("Shape (rows, columns):", df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nColumn info:")
df.info()

print("\nStats summary:")
print(df.describe())

# INSIGHT 1 - Top 10 highest-paying job titles
print("\nINSIGHT 1: Top 10 highest-paying job titles")
top_jobs = df.groupby('Job Title')['Salary'].mean().sort_values(ascending=False).head(10)
print(top_jobs)

# INSIGHT 2 - Data Analyst salary by country
print("\nINSIGHT 2: Data Analyst salary by country")
data_analysts = df[df['Job Title'] == 'Data Analyst']
print(f"Total Data Analysts in dataset: {len(data_analysts)}")
country_salary = data_analysts.groupby('Country')['Salary'].mean().sort_values(ascending=False)
print(country_salary)

# INSIGHT 3 - Salary growth with experience (for Data Analysts)
print("\nINSIGHT 3: Data Analyst salary by years of experience")
da_experience = data_analysts.groupby('Years of Experience')['Salary'].mean().sort_index()
print(da_experience)
