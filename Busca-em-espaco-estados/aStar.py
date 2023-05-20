import random

def a_star(labirinto):
    inicio = (labirinto.rows, labirinto.cols)
    fronteira=[]
    nosVisitados=[]
    fronteira.append(inicio)
    aStarPath={}

    # Função heurística (distância em linha reta até o objetivo)
    def heuristic(cell):
        goal = labirinto._goal
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

    # Custo acumulado (distância percorrida desde o início)
    def cost(cell):
        return len(aStarPath) + heuristic(cell)

    while fronteira != []:
        # Ordenar a fronteira pelo custo acumulado para garantir que o caminho mais promissor seja explorado primeiro
        fronteira.sort(key=lambda x: cost(x))
        vertice = fronteira.pop(0)
        nosVisitados.append(vertice)

        if vertice == labirinto._goal:
            print("Objetivo encontrado")
            break

        movimentos = ["E", "S", "N", "W"]
        random.shuffle(movimentos)

        for d in movimentos:
            if labirinto.maze_map[vertice][d] == True:
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
                    aStarPath[vizinho] = vertice

    fwdPath = {}
    cell = labirinto._goal
    while cell != inicio:
        fwdPath[aStarPath[cell]] = cell
        cell = aStarPath[cell]
    return fwdPath
