# GÜRCİSTAN
# https://news.google.com/covid19/map?hl=tr&gl=TR&ceid=TR%3Atr&mid=%2Fm%2F06qd3

import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, train_test_split
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriseti = pd.read_csv("Covid-19_Veri_Seti.csv")
X = veriseti["Vaka Sayısı (x)"].values
Y = veriseti["Vefat Sayısı (y)"].values
uzunluk = len(X)
X = X.reshape((uzunluk, 1))

# Eğitim ve test veri setinin oluşturulması
x_train, x_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=0)

clf = LinearRegression()
clf.fit(x_train, y_train)
clf.predict(x_test)
clf.score(x_test, y_test)


# Test seti sonuçlarının grafiği çizilmesi
plt.scatter(veriseti['Vaka Sayısı (x)'], veriseti['Vefat Sayısı (y)'])
plt.plot(x_train, clf.predict(x_train), color='red')
plt.title("Linear Graph")
plt.xlabel('Vaka Sayısı (x)')
plt.ylabel('Vefat Sayısı (y)')
plt.show()

# Performans değerlendirmeleri


def eval_metrics(y_train, y_test):
    rmse = np.sqrt(mean_squared_error(y_train, y_test))
    mae = mean_absolute_error(y_train, y_test)
    r2 = r2_score(y_train, y_test)
    return rmse, mae, r2


predicted_qualities = clf.predict(x_test)
(rmse, mae, r2) = eval_metrics(y_test, predicted_qualities)
print("  RMSE: {}".format(rmse))
print("  MAE: {}" .format(mae))
print("  R2: {}".format(r2))
