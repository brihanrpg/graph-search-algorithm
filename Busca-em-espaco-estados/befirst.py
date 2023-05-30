from collections import deque

def befirst(labirinto):
    inicio = (labirinto.rows, labirinto.cols)
    fila = deque()        # Fila para armazenar os vértices a serem explorados
    nosVisitados = set()  # Conjunto para armazenar os vértices já visitados
    fila.append(inicio)
    bestFirstPath = {}    # Dicionário para armazenar o caminho percorrido

    while fila:
        vertice = fila.popleft()  # Retira o vértice na frente da fila

        nosVisitados.add(vertice)

        if vertice == labirinto._goal:
            print("Objetivo encontrado")
            break

        movimentos = ["E", "S", "N", "W"]
        movimentos.sort(key=lambda d: heuristica(labirinto, vertice, d))  # Ordena os movimentos com base na heurística

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
                    nosVisitados.add(vizinho)
                    bestFirstPath[vizinho] = vertice

    caminho_percorrido = []
    cell = labirinto._goal
    caminho_percorrido.append(cell)
    while cell != inicio:
        cell = bestFirstPath[cell]
        caminho_percorrido.append(cell)

    distancia_total = len(caminho_percorrido) - 1

    print("Distância total percorrida:", distancia_total)
    print("Caminho percorrido:")
    for cell in reversed(caminho_percorrido):
        print(cell)

    return bestFirstPath


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

