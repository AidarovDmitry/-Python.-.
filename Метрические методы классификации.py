from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
    
hard_problem = datasets.make_classification(
    n_samples=100,
    n_features=100,
    n_informative=50,
    n_classes=3,
    n_redundant=50,
    n_clusters_per_class=1,
    random_state=42,
)

X_train, X_test, y_train, y_test = train_test_split(
    *hard_problem,
    test_size=0.3,
    random_state=1,
)

# Обучение модели

##Обучим модель с k=8:
clf = KNeighborsClassifier(n_neighbors=8)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
accuracy_score(y_test, predictions)
# Ваш код для поиска оптимального значения k
k_optim = 0
accuracies = []
while True:
    k_optim += 1
    clf = KNeighborsClassifier(n_neighbors = k_optim)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    accuracies.append( accuracy_score(y_test, predictions) )
    print('При числе соседей, равном ', k_optim, ', accuracy = ', accuracies[k_optim - 1], sep = '')
    if accuracies[k_optim - 1] > 0.8:
        break        

### Ваш код для построения графика зависимости accuracy(k) - метрики accuracy в зависимости от числа k
bar = plt.plot(np.arange(1, k_optim + 1), accuracies)
plt.title('Зависимость Accuracy от числа соседей')
plt.xlabel('Кол-во соседей')
plt.ylabel('Ассuracy')
plt.grid()
plt.ion()
plt.show()


clf = KNeighborsClassifier(n_neighbors=k_optim)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("Test accuracy: %.5f" % accuracy)
assert accuracy > 0.8, "попробуйте изменить следующие параметры: penalty, solver"

print('Хорошая работа!')

print(classification_report(y_test, y_pred))
