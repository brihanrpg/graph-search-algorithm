import heapq
import random

def busca_custo_minimo(labirinto):
    inicio = (labirinto.rows, labirinto.cols)
    fronteira = []
    nosVisitados = set()
    heapq.heappush(fronteira, (0, inicio))
    custoMinimoPath = {}

    while fronteira:
        custo, vertice = heapq.heappop(fronteira)
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
                    novo_custo = custo + 1
                    heapq.heappush(fronteira, (novo_custo, vizinho))
                    custoMinimoPath[vizinho] = vertice

    fwdPath = {}
    cell = labirinto._goal
    while cell != inicio:
        fwdPath[custoMinimoPath[cell]] = cell
        cell = custoMinimoPath[cell]

    return fwdPath
