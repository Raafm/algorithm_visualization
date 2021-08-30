algorithm = 4# int(input("algoritmo: bfs(1), dfs(2): "))


#bfs
if algorithm == 1:

    from algorithms.bfs import bfs
    from graph.normal import graph,node_list
    source = 0

    bfs(graph,node_list,source)


#dfs
if algorithm == 2:

    from algorithms.dfs import dfs
    from graph.normal import graph,node_list
    source = 0

    dfs(graph, node_list,source)  


#dijkstra
if algorithm == 3:

    from algorithms.dijkstra import dijkstra
    from graph.normal import graph,node_list
    source = 0
    target = 10

    dijkstra(graph, node_list,source,target)


#dfs to count connected components
if algorithm == 4:
    from algorithms.DFS_connect_components import dfs_connected_components
    from graph.normal import graph,node_list
    source = 0
    dfs_connected_components(graph, node_list, source)