import pygame,time,random
from data_struct.stack import stack
from graph.graphDENSE import graph,node_list,edge_dict
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

    pygame.draw.circle(screen,memory_color,node_list[node] , 7)
    
    if show:
        pygame.display.update()
        time.sleep(Time)



def visit(node,Time,show=True):
    if Time == 0:
        Time = 0.1
    pygame.draw.circle(screen,current_color,node_list[node],7)

    if show:
        pygame.display.update()
        time.sleep(Time)



def visited(node,Time,show=True):
    if Time == 0:
        Time = 0.1

    pygame.draw.circle(screen,  (255,255,255), node_list[node] , 7)
    pygame.draw.circle(screen,visited_color,node_list[node],5)
    

    if show:
        pygame.display.update()
        time.sleep(Time)



def mark(node,color,radius):

    pygame.draw.circle(screen, color, node_list[node] , radius)


def print_component(component_dict,component_color,SP):

    for node in component_dict:
        mark(node,Black,6)
        mark(node,component_color[SP],5)
    pygame.display.update()
   



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

    N_islands = -1
    
    component_color = [
        Purple 	    ,
        Cyan 	    ,
        Carmesim	,	
        Melada	    ,
        Light_sky   ,
        Dark_gray   ,
        Maroon 	    ,
        Olive  	    ,
        Green  	    ,
        Cream       ,
        Teal	    ,
        Dark_red    ,
        Castanho	,	
        Some_grey   ,  	
        Light_grey  , 
        Navy	    ,
        Magenta	    , 	
        Gray	    ,  
    ]
    SP = 0


    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("count",True,Dark_yellow)                        
    screen.blit(text,text.get_rect(center = (920,50)))
    
    font = pygame.font.Font('freesansbold.ttf',15)
    text = font.render("conected components",True,Dark_yellow)                        
    screen.blit(text,text.get_rect(center = (910,70)))

    font = pygame.font.Font('freesansbold.ttf',15)
    pygame.draw.circle(screen,memory_color, (850,200),7)
    text = font.render("memory stack",True,memory_color)
    screen.blit(text,text.get_rect(center = (915,200)))                             
    text = font.render("(pilha de processamento)",True,memory_color)
    screen.blit(text,text.get_rect(center = (910,220)))

    font = pygame.font.Font('freesansbold.ttf',15)


    pygame.draw.circle(screen,  (255,255,255), (850,150) , 7)
    pygame.draw.circle(screen,visited_color,(850,150),5)
    text = font.render("seen (visto)",True,visited_color)                               # informative node       
    screen.blit(text,text.get_rect(center = (925,150)))

    pygame.draw.circle(screen,current_color,(850,175),7)
    text = font.render("current (atual)",True,current_color)                            # informative node   
    screen.blit(text,text.get_rect(center = (925,175)))




    pause = True
    current = 0
   
    component_dict = {}

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

        
        # if we still have  nodes to see
        if node < len(graph): 


            # still in the same component
            if process_stack.not_empty():
                
                if not displayed:
                    font = pygame.font.Font('freesansbold.ttf',20)
                    pygame.draw.rect(screen, component_color[SP], (862,327 , 70, 25))
                    text = font.render("DFS",True,Dark_yellow)                        
                    screen.blit(text,text.get_rect(center = (895,340)))
                    displayed = True

                current = process_stack.pop()
                component_dict[current] = True
            

            # new connected components
            elif not seen[node]:
            
                
                print(component_dict)

                print_component(component_dict,component_color,SP)
                SP = SP+1 if SP < len(component_color)-1 else 0 

                component_dict.clear()


                N_islands += 1
             
                displayed = False
                font = pygame.font.Font('freesansbold.ttf',20)
             
                pygame.draw.rect(screen, Black, (800,350 ,300, 100))
                pygame.draw.rect(screen, Black, (862,327 , 70, 25))
                text = font.render("N° components = " + str(N_islands) ,True,  component_color[SP])                   # informative node       
                screen.blit(text,text.get_rect(center = (895,400)))
                pygame.display.update()

                current = node
                component_dict[current] = True
                time.sleep(1)
                

            # searching next component
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
            N_islands += 1
            font = pygame.font.Font('freesansbold.ttf',20)
            
            pygame.draw.rect(screen, Black, (800,350 ,300, 100))
            text = font.render("N° components = " + str(N_islands) ,True,  component_color[SP])                   # informative node       
            screen.blit(text,text.get_rect(center = (895,400)))
            print_component(component_dict,component_color,SP)
            pygame.display.update()
            pause = True





#main:
source = 0
seen = list(False for x in range(len(graph)))
process_stack = stack()


mark(source,(0,205,205),12)

dfs_connected_components(screen, node_list,seen,graph,process_stack,speed = 100)