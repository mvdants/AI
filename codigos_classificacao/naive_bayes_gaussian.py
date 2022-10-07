import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report


# - Definindo o arquivo chave para o banco de dados wine
db_wine = r"db/wine.data"

headernames = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium',
 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity',
  'Hue', 'OD280/OD315', 'Proline']

# headernames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Lendo o bando de dados
data = pd.read_csv(db_wine, sep=",", names=headernames)

preset_x = data.iloc[:, 1:-1].values
preset_y = data.iloc[:, 0].values

x_train, x_test, y_train, y_test = train_test_split(preset_x, preset_y, test_size = 0.5, random_state=int(time.time()))

gaussian_NB = GaussianNB()
gaussian_NB.fit(x_train, y_train)

y_pred = gaussian_NB.predict(x_test)

print(classification_report(y_test, y_pred))

print(accuracy_score(y_test, y_pred))
