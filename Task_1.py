import pandas as pd

df = pd.read_csv("marketing_campaign.csv", sep='\t')  


print("Before Cleaning:\n")
print(df.info())
print("\nMissing values:\n", df.isnull().sum())

df['Income'] = df['Income'].fillna(df['Income'].median())

df = df.drop_duplicates()

df['Education'] = df['Education'].str.lower().str.strip()
df['Marital_Status'] = df['Marital_Status'].str.lower().str.strip()

df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y', errors='coerce')

df.columns = df.columns.str.lower().str.replace(" ", "_")

df['income'] = df['income'].astype(int)

df.to_csv("cleaned_dataset.csv", index=False)


print("\nAfter Cleaning:\n")
print(df.info())
print("Cleaned dataset saved as 'cleaned_dataset.csv'")
