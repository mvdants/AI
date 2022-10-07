"""
As colunas do banco de dados de vinhos esta separada da seguinte forma :

1) Alcohol 
2) Malic acid 
3) Ash 
4) Alcalinity of ash 
5) Magnesium 
6) Total phenols 
7) Flavanoids 
8) Nonflavanoid phenols 
9) Proanthocyanins 
10)Color intensity 
11)Hue 
12)OD280/OD315 of diluted wines 
13)Proline 

Sabendo que teremos 14 colunas, onde a primeira sera a sua identificacao e as outras 13
serao as caracteristicas mostradas acima.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from asyncore import read
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# - Definindo o arquivo chave para o banco de dados wine
db_wine = r"db/wine.data"

headernames = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium',
 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity',
  'Hue', 'OD280/OD315', 'Proline']

# headernames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Lendo o bando de dados
data = pd.read_csv(db_wine, sep=",", names=headernames)

# Selecionando dentro do bando de dados 
preset_x = data.iloc[:, 1:-1].values
preset_y = data.iloc[:, 0].values
print(preset_x)
print("-------------")
print(preset_y)
# - Escolher dentro do banco de dados, as amostras que serao fixas para validacao e as
# que serao utilisadas como teste de classificacao
X_train, X_test, y_train, y_test = train_test_split(preset_x, preset_y, test_size = 0.75)

# - Criando uma nova tabela de dados, com os dados normalizados entre 0 e 1
scaler = StandardScaler()
scaler.fit(X_train)


X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# - Escolher o numero de K vizinhos  
classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(X_train, y_train)

# - Realizar o metodo de KNN
y_pred = classifier.predict(X_test)

# - Realizar uma matriz de confusao, 3x3 cada linha/coluna com sua classe respectiva
result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(result)

result1 = classification_report(y_test, y_pred)
print("Classification Report:",)
print (result1)

result2 = accuracy_score(y_test,y_pred)
print("Accuracy:",result2)

# - Realizar variacoes dos K-vizinhos e variacoes da quantidade de amostras para serem
# classificadas