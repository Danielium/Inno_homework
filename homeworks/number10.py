import pandas as pd
sales_df = pd.read_csv('2.4 sales.csv', sep=',', decimal='.')
weather_df = pd.read_csv('2.4 weather.csv', sep=',', decimal='.')
merged_data = pd.merge(sales_df, weather_df, on='date')
print(merged_data) # или в Jupiter Notebook можно посторить график merged_data.plot()

