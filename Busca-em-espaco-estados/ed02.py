from pyamaze import maze, agent
from random import randint
from bfs import bfs
from dfs import dfs
from aStar import a_star
from custo import busca_custo_minimo
from befirst import best_first

def execucaoMaze(tamanho=30, possibilidadeCaminhos=10, algoritmo="dfs"):
    
    goalX, goalY = randint(1, tamanho), 1
    
    m = maze(tamanho, tamanho)
    m.CreateMaze(goalX, goalY, loopPercent=possibilidadeCaminhos)
    
    # Inclusao do agente no ambiente
    a = agent(m, footprints=True, shape="arrow", color='red')
    b = agent(m, footprints=True, color='blue', filled=True)

    # m.run()

    if algoritmo == "bfs":
        print("Executando a busca em largura")
        path1 = bfs(m)
        path2 = bfs(m)
    elif algoritmo == "dfs":
        print("Executando a busca em profundidade")
        path1 = dfs(m)
        path2 = dfs(m)
    elif algoritmo == 'aStar':
        print("Executando a busca A*")
        path1 = a_star(m)
        path2 = a_star(m)
    elif algoritmo == 'custo':
        print("Executando a busca custo mínimo")
        path1 = busca_custo_minimo(m)
        path2 = busca_custo_minimo(m)
    elif algoritmo == 'befirst':
        print("Executando a busca Be-First")
        path1 = best_first(m)
        path2 = best_first(m)
    else:
        path1 = m.path
        path2 = m.path
  
    m.tracePath({a: path1, b: path2})
    m.run()


if __name__=='__main__':
    execucaoMaze(tamanho=30, algoritmo="dfs")
