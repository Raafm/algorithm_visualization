from graph.normal import graph
from data_struct.queue import queue
import random

seen = list(False for x in range(len(graph)))  # se estiver completa com True, significa que viu todo mundo

source = random.randint(0,len(graph)-1)

Q = queue()

n_layer = 0
missing = 0
####################


def BFS(current):


    Q.insert(current)

    while Q.not_empty():




        # visito o current
        seen[current] = True
        
        # empilha os vizinhos do current
        for neighbour in graph[current]:

            if not seen[neighbour]:
                Q.insert(neighbour)
                
                # tiro um node e RECURSAO 
        
        current = Q.pop()


######### modifique umas linhas para fazer a bfs


BFS(source)



#modifque uma