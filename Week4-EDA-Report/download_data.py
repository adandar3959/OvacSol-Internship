import seaborn as sns
import pandas as pd

print("Loading Titanic dataset...")

df = sns.load_dataset('titanic')

df.to_csv('titanic.csv', index=False)

print(f"Dataset downloaded successfully!")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"\nSaved as: titanic.csv")
