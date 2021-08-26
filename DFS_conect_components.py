import pygame,time,random
from data_struct.stack import stack
from graph.normal import graph,node_list,edge_dict
from graph.color import *

pygame.init()

forget = (1,0,0)

screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))


memory_color  = Red
current_color = Flame
visited_color = Yellow


def memorize(node,Time = 0.3,show=True):

    if Time == 0:
        Time = 0.1

    pygame.draw.circle(screen,memory_color,node_list[node] , 10)
    
    if show:
        pygame.display.update()
        time.sleep(Time)



def visit(node,Time,show=True):
    if Time == 0:
        Time = 0.1
    pygame.draw.circle(screen,current_color,node_list[node],12)

    if show:
        pygame.display.update()
        time.sleep(Time)



def visited(node,Time,show=True):
    if Time == 0:
        Time = 0.1

    pygame.draw.circle(screen,  (255,255,255), node_list[node] , 12)
    pygame.draw.circle(screen,visited_color,node_list[node],10)
    

    if show:
        pygame.display.update()
        time.sleep(Time)



def mark(node,color,radius):

    pygame.draw.circle(screen, color, node_list[node] , radius)



def found(node):
    mark(node, (255,255,255), 20)
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Found",True,(250,250,250))                        
    screen.blit(text,text.get_rect(center = (910,290)))

#print graph:
for node1,node2 in edge_dict:                                                   # draw edges
    pygame.draw.line(screen,(255,255,255), node1, node2, 2)

for node in node_list:                                                          # draw nodes
    pygame.draw.circle(screen,  (0,0,255), node, 5)

pygame.display.update()







def dfs_connected_components(screen, node_list,seen,graph,process_stack,speed = 0):
    if speed == 0:
        Time = 0
    else:Time = 1/speed
    # informative test:


    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("DFS",True,Dark_yellow)                        
    screen.blit(text,text.get_rect(center = (920,50)))
    font = pygame.font.Font('freesansbold.ttf',15)
    pygame.draw.circle(screen,memory_color, (850,200),10)
    text = font.render("memory stack",True,memory_color)
    screen.blit(text,text.get_rect(center = (915,200)))                             
    text = font.render("(pilha de processamento)",True,memory_color)
    screen.blit(text,text.get_rect(center = (910,220)))

    font = pygame.font.Font('freesansbold.ttf',15)


    pygame.draw.circle(screen,  (255,255,255), (850,150) , 10)
    pygame.draw.circle(screen,visited_color,(850,150),8)
    text = font.render("seen (visto)",True,visited_color)                               # informative node       
    screen.blit(text,text.get_rect(center = (925,150)))

    pygame.draw.circle(screen,current_color,(850,175),10)
    text = font.render("current (atual)",True,current_color)                            # informative node   
    screen.blit(text,text.get_rect(center = (925,175)))




    pause = True
    current = 0
    process_stack.insert(0)

    node = 0
    
    while True :

        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                quit()                          #exit() program


            
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_SPACE:     #press breakspace to pause or play
                    pause = not pause   
                    time.sleep(0.2)
        
        if pause:
            continue

        
        
        if node < len(graph): 

            if process_stack.not_empty():
                current = process_stack.pop()
            
            elif not seen[node]:
                current = node

            else:
                node += 1
 

            #  iteration of dfs:
            if not seen[current]:

                visit(current,Time)

                seen[current] = True
                

                for neighbour in graph[current]:

                    if seen[neighbour]:
                        continue
                    
                    else:
                        memorize(neighbour,Time)
                        process_stack.insert(neighbour)


                visited(current,Time)


            pygame.display.update()

        else: #node ==len(graph)
            pause = True




#main:
source = 0
seen = list(False for x in range(len(graph)))
process_stack = stack()


mark(source,(0,205,205),12)

dfs_connected_components(screen, node_list,seen,graph,process_stack,source)