import random

def dfs(labirinto):
    inicio = (labirinto.rows, labirinto.cols)
    fronteira=[]
    nosVisitados=[]
    fronteira.append(inicio)
    dfsPath={}

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
                if d=='E':
                    vizinho=(vertice[0],vertice[1]+1)
                if d=='W':
                    vizinho=(vertice[0],vertice[1]-1)
                if d=='N':
                    vizinho=(vertice[0]-1,vertice[1])
                if d=='S':
                    vizinho=(vertice[0]+1,vertice[1])
                
                if vizinho not in nosVisitados and vizinho not in fronteira:
                    fronteira.append(vizinho)
                    dfsPath[vizinho]=vertice
                

    fwdPath={}
    cell=labirinto._goal
    while cell != inicio:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return fwdPath
