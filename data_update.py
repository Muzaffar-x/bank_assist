import os
import pandas as pd

csv = 'main.csv'
output_path = 'data/snips/slot_label.txt'
column_name = 'iob'
df = pd.read_csv(csv)

if column_name not in df.columns:
    raise ValueError(f"Column '{column_name}' not found in the CSV file.")

unique_values = set()
for value in df[column_name].dropna():
    values = value.split()
    unique_values.update(values)

with open(output_path, 'w') as f:
    for item in sorted(unique_values):
        f.write(f"{item}\n")

print(f"Unique values have been written to '{output_path}'.")
