import pygame,time,random
from data_struct.queue import queue
from graph.normal import graph,node_list,edge_dict
from graph.color import *


pygame.init()

forget = (1,0,0)

screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))


memory_color  =  Teal
current_color =  Lime  
visited_color =  Cyan


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







def bfs(screen, seen , graph , process_queue , source , speed = 0):

    if speed == 0:
        Time = 0
    else:Time = 1/speed
    # informative test:

    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("BFS",True,(0,205,205))                        
    screen.blit(text,text.get_rect(center = (900,50)))
    font = pygame.font.Font('freesansbold.ttf',15)
    pygame.draw.circle(screen,memory_color, (830,200),10)
    text = font.render("memory queue",True, memory_color)
    screen.blit(text,text.get_rect(center = (895,200)))                             
    text = font.render("(fila de processamento)",True,memory_color)
    screen.blit(text,text.get_rect(center = (890,220)))

    font = pygame.font.Font('freesansbold.ttf',15)


    pygame.draw.circle(screen,  (255,255,255), (830,150) , 10)
    pygame.draw.circle(screen,  visited_color, (830,150) , 8)
    text = font.render("seen (visto)",True,visited_color)                               # informative node       
    screen.blit(text,text.get_rect(center = (905,150)))

    pygame.draw.circle(screen,current_color,(830,175),10)
    text = font.render("current (atual)",True,current_color)                            # informative node   
    screen.blit(text,text.get_rect(center = (905,175)))



    pause = True
    current = source
    process_queue.insert(source)


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


        #  iteration of bfs:
        if process_queue.not_empty(): 



            current = process_queue.pop()

 

            if not seen[current]:

                visit(current,Time)

                seen[current] = True
                

                for neighbour in graph[current]:

                    if seen[neighbour]:
                        continue
                    
                    else:
                        memorize(neighbour,Time)
                        process_queue.insert(neighbour)


                visited(current,Time)


        pygame.display.update()




#main:
source = 0
seen = list(False for x in range(len(graph)))
process_queue = queue()


mark(source,(0,205,205),12)

bfs(screen, seen,graph,process_queue,source)