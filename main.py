from graph.tree import graph,node_list,edge_dict


import pygame,time


pygame.init()


screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))

for node1,node2 in edge_dict:                                                   # draw edges
    pygame.draw.line(screen,(255,255,255), node1, node2, 2)

for node in node_list:                                                          # draw nodes
    pygame.draw.circle(screen,  (0,0,255), node, 5)


font = pygame.font.Font('freesansbold.ttf',15)


pygame.draw.circle(screen,  (255,255,255), (850,150) , 10)
pygame.draw.circle(screen,(0,255,0),(850,150),5)
text = font.render("seen (visto)",True,(0,255,0))                               # informative node       
screen.blit(text,text.get_rect(center = (925,150)))

pygame.draw.circle(screen,(0,255,0),(850,175),10)
text = font.render("current (atual)",True,(0,255,0))                            # informative node   
screen.blit(text,text.get_rect(center = (925,175)))




pygame.display.update()                                                         # display graph before algorithm


seen = list(False for x in range(len(graph)))                                   # haven't seen anyone yet


algoritmo = 1# int(input("algoritmo: bfs(1), dfs(2): "))



if algoritmo == 1:
    
    from data_struct.queue import queue
    from algorithms.bfs import bfs

    process_list = queue()
    source = 0

    bfs(screen, node_list,seen,graph,process_list,source)


if algoritmo == 2:

    from data_struct.stack import stack
    from algorithms.dfs import dfs

    process_stack = stack()
    source = 0

    dfs(screen, node_list,seen,graph,process_stack,source)  
    