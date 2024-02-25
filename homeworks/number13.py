import pandas as pd
from sklearn.cluster import KMeans
df = pd.read_csv('3.4 dataset.csv')
# Добавление комбинации столбцов
df['Name_Age'] = df['Name'] + '_' + df['Age'].astype(str)

# Вычисляемый столбец (например, длина имени)
df['Name_Length'] = df['Name'].apply(len)

# Кластеризация по возрасту и длине имени
kmeans_data = df[['Age', 'Name_Length']]
kmeans = KMeans(n_clusters=3)
df['Age_Name_Cluster'] = kmeans.fit_predict(kmeans_data)

# Вывод результатов
print(df)
