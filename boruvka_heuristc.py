from algorithms.colors import *
import pygame
import time
from algorithms.data_struct.RodUnionFind import UnionFind,linked_list
from math import inf,hypot
from random import randint


screen_height = 700
screen_width = 1250
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill((0,0,0))

pygame.init()
font = pygame.font.Font('freesansbold.ttf',11)



N = 100
graph = [ list( range(0,node) ) + list( range(node+1,N)) for node in range(N) ]


node_position1 = list( (randint(100,screen_width//2-50), randint(50,screen_height//2-50))
                       for _ in range(N//4)
                   ) 
node_position2 = list( (randint(screen_width//2 + 50,screen_width-50), randint(screen_height//2 + 50,screen_height-50))
                        for _ in range(N//4)
                    )


node_position3 = list( (randint(screen_width//2 + 50,screen_width-50), randint(50,screen_height//2-50))
                        for _ in range(N//4)
                    )


node_position4 = list( (randint(100,screen_width//2-50), randint(screen_height//2 + 50,screen_height-50))
                        for _ in range(N//4)
                    )


node_position = node_position1 + node_position2 + node_position3 + node_position4
 

list_colors = [
    Purple 	        ,
    Some_grey       ,
    Carmesim	    ,
    Lime            ,
    royalblue       ,
    Navy            ,
    skyblue	        ,
    Dark_gray       ,
    Maroon 	        ,
    Olive  	        ,
    Green  	        ,  
    deepskyblue	    ,
    cadetblue	    ,
    Dark_sienna     ,
    Castanho	    ,        	
    Cyan 	        ,
    Springgreen	    ,
    Flame           ,
    Magenta	        , 	
    Gray	        ,  
    Yellow	        ,
    Orange	        ,
    Teal	        ,
    Midnight_green  , 
    Bulgarian_rose  ,
    darkslategrey	,  
    dodgerblue	    ,  
    cornflowerblue	,  
    steelblue	    ,  
    Dark_red        ,  
    mediumslateblue	,  
    Dark_yellow     ,
]

node_radius       = 5
node_color        = Blue
cur_edge_color    = Green
choose_edge_color = White
not_choosen_color = Black





F = UnionFind(len(graph))
edge_dict = {}

N_edge_MST = 0
pause = False


edge_list = []
set_color = list( list_colors[x%len(list_colors)] for x in range(len(graph)))

def distance(node1,node2):
 
   return int(hypot(node1[0]-node2[0], node1[1]-node2[1]))   

def show_weight(weight,position,font,weight_color = Cyan ):
    text = font.render(str(weight),True,weight_color,10)
    screen.blit(text,position)
def median_point(p1,p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
    

def paint_component(component_list,color,show = False, Time = 0,animation = False):
    for node in component_list:
        
        for neighbour in graph[node]:
            #if F.Find(node) != F.Find(neighbour) : continue
            if (neighbour,node) in edge_dict or (node, neighbour) in edge_dict:
                # paint also the edges
                pygame.draw.line(screen,color, node_position[node], node_position[neighbour],5)
                pos = node_position[neighbour]
                pygame.draw.circle(screen,color,pos,8)
                if animation: 
                    time.sleep(Time)
                    
                    pygame.display.update()
                    

def find_best_edge(component):
    paint_component(component,White)
    
    pygame.display.update()
    
    
    
    candidates = [] # edges that can be selected by this component
    for node in component:    

        for neighbour in graph[node]:

            # if they are in the same component we don't want the edge
            
            same_component = F.Find(node) == F.Find(neighbour)
            
            if not same_component: 

                W = distance(node_position[node],node_position[neighbour])
                candidates.append((W,node,neighbour))
                #pygame.draw.line(screen,cur_edge_color,node_position[node], node_position[neighbour],2)
                #pygame.display.update()
                
                #time.sleep(0.01)
    #time.sleep(0.05)

    edge = min(candidates)
    
    edge = edge[1],edge[2]

    return edge,candidates

def find_best_edges(patriarchs):
    
    for patriarch in patriarchs:
        
        component = F.child_list(patriarch,python_list = True)
        
        edge,candidates = find_best_edge(component)
        
        edges.append(edge)


        if N_edge_MST > 0:
            paint_component(component,set_color[patriarch])
        else:
            pygame.draw.circle(screen,Blue,node_position[patriarch],8)
            

        pygame.draw.line(screen,choose_edge_color,node_position[edge[0]], node_position[edge[1]],2)
        
        
        pygame.display.update()
        
        
        time.sleep(0.05)

        for edge in candidates:
            _,u,v = edge
            
            if (u,v) not in edges and (v,u) not in edges:
                1+1
                #pygame.draw.line(screen,not_choosen_color,node_position[u], node_position[v],4)
                #pygame.draw.line(screen,darkslategrey, node_position[u], node_position[v],1)
            else:
                pygame.draw.line(screen,choose_edge_color,node_position[u], node_position[v],2)
                

        pygame.display.update()


#draw circles (nodes)
for node_number in range(len(graph)):         # draw nodes
    pygame.draw.circle(screen, node_color, node_position[node_number], node_radius)

pygame.display.update()


while N_edge_MST < N//8:#N-1:
                        
        # pygame stuff:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                   #exit pygame,
            quit()                          #exit() program
        if event.type == pygame.KEYDOWN:        
            if event.key == pygame.K_SPACE:     #press breakspace to pause or play
                pause = not pause; time.sleep(0.2)
    if pause:continue

    patriarchs = []
    for P in range(N):
        if F.Find(P) == P:
            patriarchs.append(P)

    edges = []

    #achar arestas
    find_best_edges(patriarchs)
    

    for edge in edges:

        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                quit()                          #exit() program
        

        node1,node2 = edge
        
        print(node1,node2)
        F.Union(node1,node2)
        
        edge_dict[(edge)] = True
        
        if (node2,node1) in edge_dict:continue
        N_edge_MST += 1

        pygame.draw.line(screen,set_color[F.Find(node1)], node_position[node1], node_position[node2],5)
        pygame.display.update()
        time.sleep(0.01)

    for Patriarch in range(N):
        if Patriarch != F.Find(Patriarch): continue
        if F.reference[Patriarch] is None: print("not a patriarch:",Patriarch);continue
        
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()                   #exit pygame,
                    quit()                          #exit() program
                if event.type == pygame.KEYDOWN:        
                    if event.key == pygame.K_SPACE:     #press breakspace to pause or play
                        pause = not pause; time.sleep(0.2)
        

        # paint all set:
        component_color = set_color[Patriarch]  
        paint_component(component_list = F.child_list(Patriarch, python_list = True),color = component_color,show=True,Time = 0.005, animation= False)
        time.sleep(0.01)


