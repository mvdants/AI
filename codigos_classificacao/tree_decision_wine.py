# %%
import pandas as pd
from sklearn import tree
from sklearn import metrics
from sklearn.model_selection import train_test_split

# - Definindo o arquivo chave para o banco de dados wine
db_wine = r"db/wine.data"

headernames = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium',
 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity',
  'Hue', 'OD280/OD315', 'Proline']

# headernames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Lendo o bando de dados
data = pd.read_csv(db_wine, sep=",", names=headernames)

x_preset = data.iloc[:, 1:]
y_preset = data.iloc[:, 0]

model = tree.DecisionTreeClassifier(criterion="gini")

x_train, x_test, y_train, y_test = train_test_split(x_preset, y_preset, test_size = 0.5)

model.fit(x_train, y_train)
tree.plot_tree(model, filled=True,class_names=['RUIM', 'BOM', 'OTIMO']);

y_pred = model.predict(x_test)

print(metrics.confusion_matrix(y_test, y_pred))
print(metrics.accuracy_score(y_test,y_pred))

# %%
