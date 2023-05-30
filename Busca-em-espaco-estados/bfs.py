import random
from befirst import calcular_vizinho

def bfs(labirinto):
    inicio = (labirinto.rows, labirinto.cols)
    fronteira=[]
    nosVisitados=[]
    fronteira.append(inicio)
    bfsPath={}

    distancia_total = 0

    while fronteira !=[]:
        vertice=fronteira.pop(0)
        nosVisitados.append(vertice)

        if vertice == labirinto._goal:
            print("objetivo encontrado")
            break

        movimentos=["E", "S", "N", "W"]
        random.shuffle(movimentos)

        for d in movimentos:
            if labirinto.maze_map[vertice][d]==True:
                vizinho = calcular_vizinho(vertice, d)
                
                if vizinho not in nosVisitados and vizinho not in fronteira:
                    fronteira.append(vizinho)
                    bfsPath[vizinho]=vertice
                    distancia_total += 1
    
    print("Caminho percorrido: ", distancia_total)
    fwdPath={}
    cell=labirinto._goal
    while cell != inicio:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath