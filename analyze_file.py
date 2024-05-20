import pandas as pd

# df = pd.read_csv('chunked_data/chunk_100_with_info.csv')
df = pd.read_csv('processed_data/chunk_100_with_info.csv')

# remove rows where title is NaN
df = df.dropna(subset=['title'])

# Ensure no NaN values in poster_path and tagline
df['poster_path'] = df['poster_path'].fillna('')
df['tagline'] = df['tagline'].fillna('')

# print null values
print(df.isnull().sum())

# Save the processed data
df.to_csv('processed_data/chunk_100_with_info.csv', index=False)