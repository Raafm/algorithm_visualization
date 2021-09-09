algorithm = 7


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
    from graph.graphDENSE import graph,node_list
    source = 250
    dfs_connected_components(graph, node_list, source,speed = 100)


#prim
if algorithm == 5:
    from algorithms.prim import prim
    from graph.normal import graph,node_list
    source = 0
    prim(graph, node_list,source)


#kruskal
if algorithm == 6:
    from algorithms.kruskal import kruskal
    from graph.normal import graph,node_list

    kruskal(graph,node_list,steps_mode = False)

# cycle with two given nodes
if algorithm == 7:
    from algorithms.cyclewith2nodes import cycleWith2Nodes
    from graph.normal import graph,node_list
    s = 10
    t = 50

    cycleWith2Nodes(graph, node_list,s,t)