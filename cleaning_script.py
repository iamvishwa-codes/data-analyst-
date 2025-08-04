Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd

# Load the dataset
df = pd.read_csv('Mall_Customers.csv')

# Preview the data
print(df.head())
print(df.info())

# Remove duplicates
df = df.drop_duplicates()

# Rename columns for consistency
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Standardize gender column
df['gender'] = df['gender'].str.lower().str.strip()

# Check for missing values
print(df.isnull().sum())

# Fill or drop missing values if any
df = df.dropna()  # or df.fillna(...)

# Save cleaned dataset
df.to_csv('cleaned_mall_customers.csv', index=False)
