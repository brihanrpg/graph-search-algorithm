from collections import deque
import random

def busca_custo_minimo(labirinto):
    inicio = (labirinto.rows, labirinto.cols)
    fila = deque()
    nosVisitados = set()
    fila.append(inicio)
    aStarPath = {}

    while fila:
        vertice = fila.popleft()
        nosVisitados.add(vertice)

        if vertice == labirinto._goal:
            print("Objetivo encontrado")
            break

        movimentos = ["E", "S", "N", "W"]
        random.shuffle(movimentos)

        for d in movimentos:
            if labirinto.maze_map[vertice][d]:
                if d == 'E':
                    vizinho = (vertice[0], vertice[1] + 1)
                if d == 'W':
                    vizinho = (vertice[0], vertice[1] - 1)
                if d == 'N':
                    vizinho = (vertice[0] - 1, vertice[1])
                if d == 'S':
                    vizinho = (vertice[0] + 1, vertice[1])

                if vizinho not in nosVisitados:
                    fila.append(vizinho)
                    aStarPath[vizinho] = vertice

    caminho_percorrido = []
    cell = labirinto._goal
    caminho_percorrido.append(cell)
    while cell != inicio:
        cell = aStarPath[cell]
        caminho_percorrido.append(cell)

    distancia_total = len(caminho_percorrido) - 1

    print("Distância total percorrida:", distancia_total)
    print("Caminho percorrido:")
    for cell in reversed(caminho_percorrido):
        print(cell)

# Exemplo de uso
# Supondo que você tenha uma instância da classe Labirinto chamada 'labirinto'
#busca_custo_minimo(labirinto)


# import random

# # Custo acumulado (distância percorrida desde o início)


# def custo(labirinto):
#     inicio = (labirinto.rows, labirinto.cols)
#     fronteira=[]
#     nosVisitados=[]
#     fronteira.append(inicio)
#     custoPath={}

#     def cost(cell):
#      return custoPath[cell]

#     while fronteira != []:
#         # Ordenar a fronteira pelo custo acumulado para garantir que o caminho mais promissor seja explorado primeiro
#         fronteira.sort(key=lambda x: x[1])
#         vertice, custo_atual = fronteira.pop(0)
#         nosVisitados.append(vertice)

#         if vertice == labirinto._goal:
#             print("Objetivo encontrado")
#             break

#         movimentos = ["E", "S", "N", "W"]
#         random.shuffle(movimentos)

#         for d in movimentos:
#             if labirinto.maze_map[vertice][d] == True:
#                 if d == 'E':
#                     vizinho = (vertice[0], vertice[1] + 1)
#                 if d == 'W':
#                     vizinho = (vertice[0], vertice[1] - 1)
#                 if d == 'N':
#                     vizinho = (vertice[0] - 1, vertice[1])
#                 if d == 'S':
#                     vizinho = (vertice[0] + 1, vertice[1])

#                 if vizinho not in nosVisitados:
#                     if vizinho not in [x[0] for x in fronteira]:
#                         fronteira.append((vizinho, custo_atual + 1))
#                         custoPath[vizinho] = custo_atual + 1

#     #Construção do caminho
#     caminhoTotal = []
#     cell = labirinto._goal
#     caminhoTotal.append(cell)
#     while cell != inicio:
#         cell = custoPath[cell]
#         caminhoTotal.append(cell)
    
#     print("Distancia percorrida:", len(caminhoTotal) - 1)

#     fwdPath = {}
#     cell = labirinto._goal
#     while cell != inicio:
#         fwdPath[custoPath[cell]] = cell
#         cell = custoPath[cell]
#     return fwdPath
