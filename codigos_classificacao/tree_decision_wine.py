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

# Lendo o banco de dados
data = pd.read_csv(db_wine, sep=",", names=headernames)

# Colocando os valores que iremos utilisar como teste e treino
x_preset = data.iloc[:, 1:]
y_preset = data.iloc[:, 0]

# %%
# Inicialisando o metodo de classificacao (tree)
# - foi escolhido o metodo gini para realizar a homogeneidade entre os nós
# - foi visto que para maximizar custo_processamento/precisao, teriamos o melhor resultado apos 2 nós
model = tree.DecisionTreeClassifier(criterion="gini",max_depth=2)

# Realocando os dados como treino e teste
# - foi utilisado 67% para treino e 33% para teste, objetivo : evitar underfitting e overfitting : utilisando
# em media, 2x o numero de dados para treino, em relacao aos dados de teste.
# - random_state = 1, valor para estabilisar o split e aumentar a precisao do treino
x_train, x_test, y_train, y_test = train_test_split(x_preset, y_preset, test_size = 0.67, random_state=1)

# Treinando nosso modelo de classificacao
model.fit(x_train, y_train)

# Plotando nossa arvore de escolhas
tree.plot_tree(model, filled=True,class_names=['RUIM', 'BOM', 'OTIMO']);

# Utilisando o modelo criado, baseado nos dados de treinos, para predizer o resultado, baseado nos dados de teste
y_pred = model.predict(x_test)

# %%

# Print para verificar a precisao e coerencia do modelo criado
print(metrics.confusion_matrix(y_test, y_pred))
print(metrics.accuracy_score(y_test,y_pred))

"""
Results : 

  Confusion Matrix:
 [[41  0  0]
  [ 4 46  0]
  [ 0  1 28]]
  
  Accurancy : 0.9583333333333334
"""
