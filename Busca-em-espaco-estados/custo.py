import heapq
import random
from befirst import calcular_vizinho

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
                vizinho = calcular_vizinho(vertice, d)
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
