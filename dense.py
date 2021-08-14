import pygame,time
from graph.graphDENSE import node_list,edge_dict

node_dict ={}                                                                   # convert position to node's index

for index,node in enumerate(node_list):

    node_dict[node] = index


graph = []                                                                      # create graph
for x in range(len(node_list)):
    graph.append([])

for node1,node2 in edge_dict:                                               

    graph[node_dict[node1]].append(node_dict[node2])                            # fill graph
    graph[node_dict[node2]].append(node_dict[node1])



pygame.init()


screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))

for node1,node2 in edge_dict:                                                   # draw edges
    pygame.draw.line(screen,(255,255,255), node1, node2, 2)

for node in node_list:                                                          # draw nodes
    pygame.draw.circle(screen,  (0,150,255), node, 5)


font = pygame.font.Font('freesansbold.ttf',15)


pygame.draw.circle(screen,  (255,255,255), (850,150) , 10)
pygame.draw.circle(screen,(0,255,0),(850,150),5)
text = font.render("seen (visto)",True,(0,255,0))                               # informative node       
screen.blit(text,text.get_rect(center = (925,150)))

pygame.draw.circle(screen,(0,255,0),(850,175),10)
text = font.render("current (atual)",True,(0,255,0))                            # informative node   
screen.blit(text,text.get_rect(center = (925,175)))




pygame.display.update()                                                         # display graph before algorithm


seen = []                                                 # haven't seen anyone yet

from data_struct.stack import stack


process_stack = stack()
source = 0

componente=0

color = [
     
(255,100,0),    
(124,252,0),   #gramado verde
(184,134,11),
(205,92,92),
(34,139,34),
(235,155,0),    
(200,200,0),   
(102,102,102), 		      
(158,158,158), # 	cinzento		  
(128,0,0),     # 	Marrom		      
(128,128,0),   # 	Oliva		      
(0,128,0),      # 	Verde	
(0,255,0),      #    lima
(150,80,200)  ,
(255,80,100) 
]



font = pygame.font.Font('freesansbold.ttf',30)
text = font.render("DFS",True,(0,255,0))                   # informative node       
screen.blit(text,text.get_rect(center = (950,50)))

font = pygame.font.Font('freesansbold.ttf',15)
pygame.draw.circle(screen,(255,0,0), (850,200),10)
text = font.render("memory stack",True,(255,0,0))
screen.blit(text,text.get_rect(center = (915,200)))                             # informative node   
text = font.render("(pilha de processamento)",True,(255,0,0))
screen.blit(text,text.get_rect(center = (910,220)))

pause = True            # doesn't start until press play (breakspace)
process_stack.insert(source)
current =0
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                   #exit pygame,
            quit()                          #exit() program


        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
                time.sleep(0.2)
    
    if pause:
        continue

    
    if process_stack.not_empty(): 


        current = process_stack.pop()
        if current in seen :
            continue

       

        seen.append(current)
        
        pygame.draw.circle(screen,  (0,255,0), node_list[current] , 5)

        for neighbour in graph[current]:
            if neighbour in seen:
                continue
            else:
                pygame.draw.circle(screen,  (255,0,0), node_list[neighbour] , 5)
                process_stack.insert(neighbour)
        
        pygame.draw.circle(screen,  (255,255,255), node_list[current] , 5)
        pygame.draw.circle(screen,  color[componente], node_list[current] , 2)
         


    elif len(seen) < len(graph):
        componente +=1
        for x in range(len(graph)):
            if x in seen: continue
            process_stack.insert(x)
            break


    pygame.display.update()
    time.sleep(0.05)