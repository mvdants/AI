from numpy import ndarray, array, append
from typing import List
from collections import OrderedDict
from itertools import chain


file_cidades = "./Core/core_files/cidades_estrada.txt"


class Cidade:

    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.cidades_vizinhas: List[Cidade.Vizinha] = Cidade.vizinha(nome)
        self.distancia_cidade_alvo: float = 0.0
        self.pesos_heuristics_alvo: ndarray = array([])


    class Vizinha:

            def __init__(self, nome: str, distancia_entre_vizinho: float,
            pesos_entre_cidade: ndarray  = array([])) -> None:
                self.nome: str = nome
                self.distancia_entre_vizinho: float = distancia_entre_vizinho
                self.pesos_entre_cidade: ndarray = pesos_entre_cidade


    def get_cidades_vizinhas(self) -> List[List]:
        """
        Adquirir as informacoes das cidades vizinhas.

        Returns:
            List[List]: Uma lista contendo multiplas listas. 
            Das listas interiores,
            index 0 : nome da cidade vizinha,
            index 1 : distancia ate cidade vizinha
        """
        list_cidades_vizinhas: List = []
        for cidade in self.cidades_vizinhas:
            list_cidades_vizinhas.append([cidade.nome, cidade.distancia_entre_vizinho])
        
        return list_cidades_vizinhas

    @staticmethod
    def vizinha(nome: str) -> List[Vizinha]:
        """
        Conseguindo todas as informacoes da cidade indicada

        Args:
            nome (str): nome da cidade que deseja adquirir as informacoes

        Returns:
            List[CidadeVizinha]: Uma lista de todas as cidades vizinhas, ou seja,
            que realizam conexoes
        """
        # Trabalho inicial com o arquivo .txt
        cidades_tratadas = Cidade.tratamento_file_cidades()

        # Encontrando cidades que fazem conexoes com a cidade desejada
        cidades_vizinhas = Cidade.encontrar_conexoes(nome, cidades_tratadas)

        return cidades_vizinhas

    @staticmethod
    def tratamento_file_cidades() -> List:
        """
        Primeiro tratamento do arquivo : Remocao dos \n e transformar as linhas em lista,
        separando pela virgula

        Returns:
            List: Lista de todas as cidades (em ordem alfabetica)
        """
        # Abrindo o arquivo cidades
        with open(file_cidades, "r") as file:
            all_info_cidades: List = file.readlines()
            file.close()
        
        # Substituindo o "\n" pelo ""
        all_info_cidades = [_.replace("\n", "") for _ in all_info_cidades]

        # Primeira ordem alfabetica realizada (opcional)
        all_info_cidades.sort()

        # Separando os atributos pelas virgulas
        cidades_tratadas = [value.split(",") for value in all_info_cidades]

        return cidades_tratadas

    @staticmethod
    def encontrar_conexoes(nome: str, lista_cidades: List) -> List[Vizinha]:
        """
        Encontrar conexoes entre as cidades. Dentro do arquivo .txt, as cidades podem estar na 1 ou
        2 posicao. Logo, necessqrio verificar as duas.
        Args:
            nome (str): nome da cidade que desejamos obter as informacoes
            lista_cidades (List): lista de todas as cidades. Lista apos o primeiro tratamento do arq

        Returns:
            List[CidadeVizinha] : Lista das cidades que fazem conexoes com a cidade desejada
        """
        conexoes = [infos for infos in lista_cidades if (infos[0] == nome or infos[1] == nome)]
        lst_cidades_vizinha: List = []
        for cidades in conexoes:
            if cidades[0] == nome:
                lst_cidades_vizinha.append(Cidade.Vizinha(cidades[1], cidades[2]))
            else:
                lst_cidades_vizinha.append(Cidade.Vizinha(cidades[0], cidades[2]))

        return lst_cidades_vizinha


def todas_cidades():
    # Lista contendo todas cidades e distancias entre vizinhos
    _l = Cidade.tratamento_file_cidades()

    # Removendo os numeros da lista
    _l = list(filter(str.isalpha, list(chain(*_l))))
    # Removendo valores repetidos
    res = list(OrderedDict.fromkeys(_l))
    
    return res

if __name__ == "__main__":
    arad = Cidade("bucharest")
    cidades_vizinhas_arad = arad.get_cidades_vizinhas()
    print(cidades_vizinhas_arad)
    print("Compilacao completa !")
