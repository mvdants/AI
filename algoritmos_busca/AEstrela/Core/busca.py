from math import sqrt
from typing import Tuple, List
from cidades import Cidade, todas_cidades
from tipagem import Custos, CidadesPercorridas


def heuristica_distancia(cidade_alvo: Cidade) -> List[Cidade]:
    """
    # 1 : Pegar todas as cidades existentes dentro do arquivo .txt (OK!)
    # 2 : Calcular a distancia em linha reta para seus vizinhos, partindo da cidade alvo
    # 3 : Pular para a proxima cidade vizinha, calcular hipotenusa do triangulo, atualizar a 
    # hipotenusa como nova distancia entre cidades
    # 4 : Retornar a lista com os nomes e as distancias em linha reta

    Args:
        cidade_alvo (Cidade): Cidade alvo que deseja calcular as distancias em linha reta

    Returns:
        List[Cidade]: Retornar lista com os nomes e as distancias em linha reta
    """
    def hipotenusa(cateto_oposto: float, cateto_adjacente: float):
        return sqrt(pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))

    print(todas_cidades())
    distancias_reta_entre_cidades: List = []
    for cidade_vizinha in cidade_alvo.cidades_vizinhas:
        print(f"{cidade_vizinha.nome} : {cidade_vizinha.distancia_entre_vizinho}")
        if not cidade_vizinha in distancias_reta_entre_cidades:
            distancias_reta_entre_cidades.append(cidade_vizinha)


def busca_AEstrela(cidade_origem: Cidade, cidade_alvo: Cidade) -> Tuple[CidadesPercorridas, Custos]:
    """

    Args:
        cidade_origem (Cidade): Cidade inicial de partida
        cidade_alvo (Cidade): Cidade final (objetivo/alvo)

    Returns:
        Tuple[CidadesPercorridas, Custos]: Retorna as cidades percorridas ate chegar ao destino
        e o custo feito passando entre cada cidade
    """
    return 0


if __name__ == "__main__":
    heuristica_distancia(Cidade("arad"))