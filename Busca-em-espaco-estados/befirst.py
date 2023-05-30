import random

def best_first(labirinto):
    inicio = (labirinto.rows, labirinto.cols)
    fronteira = []
    nosVisitados = []
    fronteira.append(inicio)
    bestFirstPath = {}

    while fronteira:
        vertice = fronteira.pop(0)
        nosVisitados.append(vertice)

        if vertice == labirinto._goal:
            print("Objetivo encontrado")
            break

        movimentos = ["E", "S", "N", "W"]
        random.shuffle(movimentos)
        movimentos.sort(key=lambda d: heuristica(labirinto, vertice, d))

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

                if vizinho not in nosVisitados and vizinho not in fronteira:
                    fronteira.append(vizinho)
                    bestFirstPath[vizinho] = vertice

    fwdPath = {}
    cell = labirinto._goal
    while cell != inicio:
        fwdPath[bestFirstPath[cell]] = cell
        cell = bestFirstPath[cell]

    return fwdPath


def heuristica(labirinto, vertice, direcao):
    if direcao == 'E':
        vizinho = (vertice[0], vertice[1] + 1)
    if direcao == 'W':
        vizinho = (vertice[0], vertice[1] - 1)
    if direcao == 'N':
        vizinho = (vertice[0] - 1, vertice[1])
    if direcao == 'S':
        vizinho = (vertice[0] + 1, vertice[1])

    objetivo = labirinto._goal
    return distancia_euclidiana(vizinho, objetivo)


def distancia_euclidiana(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
