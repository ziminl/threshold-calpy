import csv

threshold = 50

with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        value = float(row['value_column'])
        if value > threshold:
            print(f"Row {row} exceeds the threshold of {threshold}.")


#or

import pandas as pd

threshold = 50

df = pd.read_csv('data.csv')
exceeds_threshold = df[df['value_column'] > threshold]
print(exceeds_threshold)
