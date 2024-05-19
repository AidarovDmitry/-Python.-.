import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
Y = 4 + 3 * X + np.random.randn(100, 1)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = LinearRegression()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)


plt.scatter(X_train, Y_train, label = 'Обучающие  данные')
plt.scatter(X_test, Y_pred, label = 'Предсказанные данные')
#plt.title()
plt.xlabel('Признак')
plt.ylabel('Целевая переменная')
plt.legend()
plt.grid()
plt.show()

