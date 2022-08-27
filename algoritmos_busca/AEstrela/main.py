"""
1) Pegar todas as cidades existentes no arquivo, retirando as cidades que forem se repetir,
e deixando em ordem alfabetica.
OBS.: Trabalhar com csv, melhor de compreender e fazer alteracoes futuras

2) Fazer uma heuristica para calcular em a distancia em linha reta das cidades existentes
ate a cidade objetivo
OBS.: Permitir usuario adicionar pesos entre cada cidade, assim aumentando a gama de 
variaveis possiveis de escolha

3) Fazer a busca de AEstrela
OBS. : Funcao tera um parametro que permite adicionar heuristics. Dssa forma, usuario
poderia escolher "filtros" a serem usados para calcular distancia.

/!\ Passo futuro : Fazer um site/API/interface para deixar usuario escolher parametros para
desejar que o algoritmo busque a melhor opcao, usuario criará seu arquivo CSV para deixar 
o algoritmo calcular (se baseando nos pesos), a melhor escolha possivel a ser realizada.
"""

from Core.busca import busca_AEstrela
from Core.cidades import Cidade

busca_AEstrela(Cidade("arad"), Cidade("bucharest"))
