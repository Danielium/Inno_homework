import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv('attestation_3_dataset.csv', sep=',')
X = df[['x_1', 'x_2']]
y = df['y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)
# Построение графика предсказанных значений
plt.scatter(y_test, y_pred)
plt.xlabel("Фактическое значение y")
plt.ylabel("Предсказанное значение y")
plt.title("Фактическое значение y vs Предсказанное значение y")
plt.show()