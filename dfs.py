import pygame,time
from graph.display_graph import show_weight, median_point, display_graph, modify_node,  modify_edge
from graph.grafo import nodes,  edge_dict,  graph
from data_struct.stack import stack

pygame.init()

number_color = (255, 0, 255)  
number_size = 10
screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))
font = pygame.font.Font('freesansbold.ttf',number_size)

display_graph(screen,graph,nodes,edge_dict,number_size, font)

process_stack = stack()
source = int(input("source: "))
process_stack.insert(source)

pause = False

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                   #exit pygame,
            quit()                          #exit() program

    while process_stack.not_empty(): 

        current = process_stack.pop()
        if nodes[current][0] == (0,255,0):
            continue

        modify_node(screen,  nodes, (0,255,0), current , (0,0,0), font,  12,  True)
        time.sleep(0.1)
        
        if current == 39 or current == 32:                                              # nodes com uma so edge 

            neighbour = graph[current]

            if nodes[neighbour][0] == (0,255,0): 
                continue

            process_stack.insert(neighbour)
            modify_node(screen,  nodes, (0,255,255), neighbour, number_color,font, 9,  True)
            time.sleep(0.1)
            continue


        for neighbour in graph[current]:

            if nodes[neighbour][0] == (0,255,0): 
                continue
            process_stack.insert(neighbour)
            modify_node(screen,   nodes, (0,255,255), neighbour, number_color,font, 9,True)
            time.sleep(0.1)
        
