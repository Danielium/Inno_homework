import pandas as pd
df = pd.read_csv('2 intermediate attestation titanic.csv', sep='\t')
# Убираю строки с отрицательными значениями возраста
df = df[df['Age'] >= 0]

# Сортирую по фамилиям, по возрастанию
df = df.sort_values(by='Name')

print(df.head())