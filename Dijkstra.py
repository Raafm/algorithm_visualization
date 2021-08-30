from data_struct.priority_queue import Heap
from graph.normal import graph,node_list
from graph.weight_graph import edge_dict
from graph.color import *
from math import hypot


INFINITY = 100000

def distance(node1,node2):
    return hypot(node1[0]-node2[0], node1[1]-node2[1])

def atribute_distance():
    for node1,node2 in edge_dict:
        edge_dict[(node1,node2)] = int(distance(node1,node2))   

    print("edge_dict =  ", edge_dict)

def show_weight(peso,position,font,peso_color = (0,255,255)):
    text = font.render(str(peso),True,peso_color,10)
    screen.blit(text,position)

def median_point(p1,p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)


def memorize(node,Time = 0.1,show=True ):
    pygame.draw.circle(screen,(255,0,0),node_list[node],10)

    if show:
        pygame.display.update()
        time.sleep(Time)


def visit(node,Time = 0.1,show=True):

    pygame.draw.circle(screen,(0,255,0),node_list[node],10)

    if show:
        pygame.display.update()
        time.sleep(Time)



def visited(node,Time = 0.1,show=True):
    pygame.draw.circle(screen,  White, node_list[node] , 10)
    pygame.draw.circle(screen,  Black,node_list[node] ,9)
    pygame.draw.circle(screen,(0,255,255),node_list[node],7)
    

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



###############prepare:

target_color = Yellow


mst  = list(False for _ in range(len(graph)))
dist = list(INFINITY for _ in range(len(graph)))
predecessor = list(-1 for _ in range(len(graph)))

PQ = Heap(comp = lambda node1,node2: node1[1] > node2[1])

source = 0
target = 55
####################

predecessor[source] = source
dist[source] = 0
PQ.insert( (source,dist[source]) )



import pygame,time


pygame.init()


screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))


number_size = 12
peso_color = Cyan
memory_color = Red
current_color = Lime
visited_color = Cyan

font = pygame.font.Font('freesansbold.ttf',number_size)

for node1,node2 in edge_dict: 
    peso = edge_dict[(node1,node2)]
                                                        # draw edges
    pygame.draw.line(screen,(255,255,255), node1, node2, 2)
    show_weight(peso,median_point(node1,node2),font)

for node in node_list:                                                          # draw nodes
    pygame.draw.circle(screen,  (0,0,255), node, 5)



mark(target,Dark_yellow,12)
mark(source,Dark_yellow,12)


font = pygame.font.Font('freesansbold.ttf',18)
text = font.render("Dijkstra",True,Dark_yellow)                        
screen.blit(text,text.get_rect(center = (900,70)))

font = pygame.font.Font('freesansbold.ttf',15)
pygame.draw.circle(screen,memory_color, (850,200),7)
text = font.render("priority queue",True,memory_color)
screen.blit(text,text.get_rect(center = (915,200)))                             
text = font.render("(fila de prioridade)",True,memory_color)
screen.blit(text,text.get_rect(center = (910,220)))


pygame.draw.circle(screen, White, (850,150) , 10)
pygame.draw.circle(screen,Black, (850,150) ,9)
pygame.draw.circle(screen,visited_color,(850,150),7)
text = font.render("seen (visto)",True,visited_color)                               # informative node       
screen.blit(text,text.get_rect(center = (925,150)))

pygame.draw.circle(screen,current_color,(850,175),7)
text = font.render("current (atual)",True,current_color)                            # informative node   
screen.blit(text,text.get_rect(center = (925,175)))

pygame.display.update()

current = 0
found = False
pause = True
while True:

    
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


    if not found:
        # pegar minimo da Heap
        current,peso = PQ.pop()



        if dist[current] < peso:
            continue
        if current == target:
            mark(current,White,10)
            mark(current,Black,9)
            mark(current,target_color,7)
            pygame.display.update()
            found = True
            time.sleep(2)
            continue
        
        if current != source: visit(current)
        # tentar atualizar os elementos

        for neighbour in graph[current]:

            if mst[neighbour]: continue

            total_distance = distance(node_list[current], node_list[neighbour]) + dist[current]
            if total_distance < dist[neighbour]:
                dist[neighbour] = total_distance
                PQ.insert((neighbour,dist[neighbour]))
                predecessor[neighbour] = current 
                memorize(neighbour)

        mst[current] = True

        if current != source:visited(current)



    else:  #if found, current == target

        pygame.draw.line(screen,Yellow,node_list[predecessor[current]],node_list[current],3)
        current = predecessor[current]
        pygame.display.update()
        time.sleep(0.3)
        if current == source:
            pause = True
