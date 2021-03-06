algorithm = 14


#bfs
if algorithm == 1:

    from algorithms.bfs import bfs
    from graph.bigGraph import graph,node_list
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
    from graph.heartCycle import graph,node_list

    kruskal(graph,node_list,steps_mode = False)

# cycle with two given nodes
if algorithm == 7:
    from algorithms.cyclewith2nodes import cycleWith2Nodes
    from graph.normal import graph,node_list
    s = 10
    t = 50

    cycleWith2Nodes(graph, node_list,s,t)

#Cycle with node s
if algorithm == 8:
    from algorithms.cyclewith1node import cycleWith1Node
    from graph.normal import graph,node_list

    source = 1

    cycleWith1Node(graph, node_list,source)

#shortes Cycle with node s
if algorithm == 9:
    from algorithms.cyclewith1nodeshortest import cycleWith1NodeShortest
    from graph.heartCycle import graph,node_list
    

    source = 13

    cycleWith1NodeShortest(graph, node_list,source,Time = 0.15,cycle_color = (255,0,0))



if algorithm == 10:
    from algorithms.kurskanimatedfs import kruskanimatedfs
    from graph.bigGraph import graph,node_list

    kruskanimatedfs(graph,node_list,steps_mode = False)

if algorithm == 11:
    from algorithms.kruskanimatedUF import kruskal
    from graph.bigGraph import graph,node_list

    kruskal(graph,node_list,steps_mode = False)

if algorithm == 12:
    from algorithms.BellmanFord import BellmanFord
    from graph.normal import graph,node_list

    BellmanFord(graph,node_list,steps_mode = False)

if algorithm == 13:
    from algorithms.BellmanFord_iterative import BellmanFord
    from graph.normal import graph,node_list

    BellmanFord(graph,node_list,steps_mode = False)

if algorithm == 14:
    from algorithms.Boruvka import boruvka
    from graph.normal import graph,node_list

    boruvka(graph,node_list,steps_mode = False)

if algorithm == 15:
    from algorithms.MultithreadBoruvka import boruvka
    from graph.normal import graph,node_list

    boruvka(graph,node_list,steps_mode = False)