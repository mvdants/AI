from typing import List
from math import sqrt
from statistics import mode
import pandas as pd


df = pd.DataFrame({
        "nome" : pd.Series(["Manuel", "Alberto", "Paula", "Samuela", "Antonio", "Sandro", "Idra", "Gelson", "Amelia", "Umar"]),
        "idade": pd.Series([32, 40, 16, 34, 55, 40, 20, 15, 55, 15]),
        "sexo": pd.Series(["m", "m", "f", "f", "m", "m", "f", "m", "f", "m"]),
        "desporto": pd.Series(["football", "basquete", "volei", "volei", "basquete", "volei", "basquete", "volei", "football", "football"])
    })


class DataPessoa:
    def __init__(self, nome: str, idade: int, sexo: str, desporto: str = None) -> None:
        self.nome: str = nome
        self.idade: int = idade
        self.sexo: int = 1 if sexo == "m" else 0
        self.desporto: str = desporto


_data: List = []
for d in range(len(df)):
    _data.append(DataPessoa(*df.iloc[d]))


def knn(pessoa: DataPessoa, k: int) -> List:
    def calcular_distancia(idade1: int, idade2: int, s1: int, s2: int):

        # Calculo da distancia euclidiana, em linha reta entre os dois objetos
        ret = sqrt(pow(idade1 - idade2, 2) + pow(s1 - s2, 2))
        return ret

    distancias: List = []
    for p in _data:
        distancias.append(calcular_distancia(pessoa.idade, p.idade, pessoa.sexo, p.sexo))
    
    # Atualisando a tabela de dados
    df["distancias"] = distancias

    # Inserindo uma nova coluna aos dados
    df_sorted = df.sort_values("distancias")

    # print dos k vizinhos feitos
    print(vizinhos := df_sorted.iloc[:k])

    desporto = vizinhos["desporto"]

    return mode(desporto)


if __name__ == "__main__":
    angelina = DataPessoa(nome="Angelina", idade=5, sexo="f")
    result = knn(pessoa=angelina, k=3)
    print(f"O desporto adequado para {angelina.nome} é {result}")
