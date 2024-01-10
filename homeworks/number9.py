import pandas as pd
data = pd.read_csv('2.3 clients_countries_.csv', sep=',', decimal='.')
grouped = data.groupby('countries').agg({'client_id': 'count', 'age': 'mean'})

print(grouped)
