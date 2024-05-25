from sklearn.datasets import fetch_openml
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

mnist = fetch_openml(data_id=554) # https://www.openml.org/d/554

data = np.array(mnist.data)
targets = np.array(mnist.target)

X_train, X_test, y_train, y_test = train_test_split(data[:10000,:],
                                                   targets[:10000].astype('int'), #targets str to int convert
                                                   test_size=1/7.0,
                                                   random_state=0)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
y_train, y_test = np.squeeze(y_train), np.squeeze(y_test)

logreg = LogisticRegression(random_state=16, max_iter = 1000, n_jobs=5, tol=0.01, penalty = 'l2', solver = 'saga')
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

accuracy = np.mean(y_pred == y_test)

print("Test accuracy: %.5f" % accuracy)
assert accuracy > 0.9, "попробуйте изменить следующие параметры: penalty, solver"

print('Хорошая работа!')

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

precision = precision_score(y_test, y_pred, average='weighted')
print("Precision:", precision)

recall = recall_score(y_test, y_pred, average='weighted')
print("Recall (Sensitivity):", recall)

f1 = f1_score(y_test, y_pred, average='weighted')
print("F1-Score:", f1)

print(classification_report(y_test, y_pred))

