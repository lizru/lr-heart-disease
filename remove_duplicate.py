import pandas as pd

# Load data
df = pd.read_csv('heart.csv')

# Drop duplicates inplace
df.drop_duplicates(inplace=True)

# Save back to CSV, overwriting original
df.to_csv('heart.csv', index=False)

print(f"Duplicates dropped. New row count: {len(df)}")
