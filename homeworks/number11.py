import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# Генерация случайных точек в двумерном пространстве
np.random.seed(0)
n_samples = 1000
X = np.random.randn(n_samples, 2)

# Добавление выбросов
outliers = np.random.uniform(low=-4, high=4, size=(100, 2))
X = np.vstack([X, outliers])

# Создание и обучение модели DBSCAN
epsilon = 0.5  # радиус окрестности
min_samples = 5  # минимальное количество точек в окрестности для формирования кластера
dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
dbscan.fit(X)

# Извлечение меток кластеров и меток выбросов (-1)
clusters = dbscan.labels_

# Визуализация результатов
plt.figure(figsize=(10, 6))

# Визуализация точек
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis', s=10)
plt.title('DBSCAN Clustering')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()