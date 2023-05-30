import random
from befirst import calcular_vizinho

def dfs(labirinto):
    inicio = (labirinto.rows, labirinto.cols)
    fronteira=[]
    nosVisitados=[]
    fronteira.append(inicio)
    dfsPath={}

    distancia_total = 0
    
    while fronteira !=[]:
        vertice=fronteira.pop()  # Alteração: Usamos pop() em vez de pop(0) para retirar o último elemento da lista
        nosVisitados.append(vertice)

        if vertice == labirinto._goal:
            print("Objetivo encontrado")
            break

        movimentos=["E", "S", "N", "W"]
        random.shuffle(movimentos)

        for d in movimentos:
            if labirinto.maze_map[vertice][d]==True:
                vizinho = calcular_vizinho(vertice, d)
                
                if vizinho not in nosVisitados and vizinho not in fronteira:
                    fronteira.append(vizinho)
                    dfsPath[vizinho]=vertice
                    distancia_total += 1

    print("Caminho percorrido: ", distancia_total)

    fwdPath={}
    cell=labirinto._goal
    while cell != inicio:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return fwdPath
