algorithm = 3# int(input("algoritmo: bfs(1), dfs(2): "))



if algorithm == 1:

    from algorithms.bfs import bfs
    from graph.normal import graph,node_list
    source = 0

    bfs(graph,node_list,source)


if algorithm == 2:

    from algorithms.dfs import dfs
    from graph.normal import graph,node_list
    source = 0

    dfs(graph, node_list,source)  


if algorithm == 3:

    from algorithms.dijkstra import dijkstra
    from graph.normal import graph,node_list
    
    dijkstra(graph, node_list)