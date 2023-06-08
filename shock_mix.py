import pandas as pd
import random

data = '/home/neurophar/Documents/shock_mix/input.csv'
df = pd.read_csv(data, sep=',')

columns = df.columns[1:].tolist()

for i, row in df.iterrows():
    used_numbers = set(row[columns].dropna().tolist())
    available_numbers = set(range(1, 12)).difference(used_numbers)
    
    for col in columns[1:]:
        available_row_numbers = available_numbers.difference(df[col].dropna().tolist())
        value = random.choice(list(available_row_numbers))
        df.at[i, col] = int(value)
        used_numbers.add(value)


print(df)