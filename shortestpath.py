
import pygame,time,random
from data_struct.queue import queue
from graph.normal import graph,node_list,edge_dict

pygame.init()

forget = (1,0,0)

screen_height = 700
screen_width = 1000
screen = pygame.display.set_mode((screen_width,screen_height))

screen.fill((0,0,0))




def memorize(node,Time = 0.01,show=True):

    pygame.draw.circle(screen,(255,0,0),node_list[node] , 10)
    
    if show:
        pygame.display.update()
        time.sleep(Time)



def visit(node,Time = 0.01,show=True):

    pygame.draw.circle(screen,(0,255,0),node_list[node],12)

    if show:
        pygame.display.update()
        time.sleep(Time)



def visited(node,Time = 0.01,show=True):
    pygame.draw.circle(screen,  (255,255,255), node_list[node] , 12)
    pygame.draw.circle(screen,(0,255,255),node_list[node],10)
    

    if show:
        pygame.display.update()
        time.sleep(Time)



def mark(node,color,radius):

    pygame.draw.circle(screen, color, node_list[node] , radius)



def found(node):
    mark(node, (255,255,255), 15)
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("found",True,(250,250,250))                        
    screen.blit(text,text.get_rect(center = (920,250)))


#print graph:
for node1,node2 in edge_dict:                                                   # draw edges
    pygame.draw.line(screen,(255,255,255), node1, node2, 2)

for node in node_list:                                                          # draw nodes
    pygame.draw.circle(screen,  (0,0,255), node, 5)

pygame.display.update()







def bfs(screen, node_list,seen,graph,process_list,source,target_node):

    # informative test:

    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("shortest path",True,(0,205,205))                        
    screen.blit(text,text.get_rect(center = (920,50)))
    font = pygame.font.Font('freesansbold.ttf',15)
    pygame.draw.circle(screen,(255,0,0), (850,200),10)
    text = font.render("memory queue",True,(255,0,0))
    screen.blit(text,text.get_rect(center = (915,200)))                             
    text = font.render("(fila de processamento)",True,(255,0,0))
    screen.blit(text,text.get_rect(center = (910,220)))

    font = pygame.font.Font('freesansbold.ttf',15)


    pygame.draw.circle(screen,  (255,255,255), (850,150) , 10)
    pygame.draw.circle(screen,(0,255,255),(850,150),5)
    text = font.render("seen (visto)",True,(0,255,0))                               # informative node       
    screen.blit(text,text.get_rect(center = (925,150)))

    pygame.draw.circle(screen,(0,255,0),(850,175),10)
    text = font.render("current (atual)",True,(0,255,0))                            # informative node   
    screen.blit(text,text.get_rect(center = (925,175)))




    n_layer = 0   # number of nodes in cur layer
    missing = 1   # missing nodes in current node

    pause = True
    current = source
    process_list.insert(source)


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
        if process_list.not_empty(): 



            current = process_list.pop()

 

            if not seen[current]:

                visit(current)

                seen[current] = True
                

                for neighbour in graph[current]:

                    if neighbour == target_node:
                        found(neighbour)
                        pause = True
                        break

                    if seen[neighbour]:
                        continue
                    else:
                        n_layer += 1
                        
                        memorize(neighbour)
                        process_list.insert(neighbour)


                time.sleep(0.5)
                visited(current)


        pygame.display.update()




#main:
source = 0
target_node = 20
seen = list(False for x in range(len(graph)))
process_list = queue()


mark(target_node,(255,255,0),12)
mark(source,(0,205,205),12)

bfs(screen, node_list,seen,graph,process_list,source, target_node)