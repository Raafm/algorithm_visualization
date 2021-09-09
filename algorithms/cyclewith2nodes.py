from data_struct.queue import queue
from data_struct.stack import stack
import math
import pygame,time
from colors import *



def arrow(screen, start, end, lcolor = (255,255, 255), tricolor = (255,255,255),  trirad= 8, thickness=5):
    pygame.draw.line(screen, lcolor, start, end, thickness)
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi/2
    rad = 180/math.pi
    pygame.draw.polygon(screen, tricolor, (
            (end[0] + trirad * math.sin(      rotation    ), end[1] + trirad * math.cos(     rotation     )),                    
            (end[0] + trirad * math.sin(rotation - 120*rad), end[1] + trirad * math.cos(rotation - 120*rad)),
            (end[0] + trirad * math.sin(rotation + 120*rad), end[1] + trirad * math.cos(rotation + 120*rad))
        )
    )
    pygame.display.update()


def memorize(screen,node_center,radius=10,Time = 0.1,show=True):
    pygame.draw.circle(screen,(255,0,0),node_center,radius)

    if show:
        pygame.display.update()
        time.sleep(Time)


def visit(screen,node_center,visit_color = (0,255,0),radius = 10,show=True,Time = 0.1):

    pygame.draw.circle(screen,visit_color,node_center,radius)

    if show:
        pygame.display.update()
        time.sleep(Time)



def visited(screen,node_center,radius = 10,show=True,Time = 0.1):
    Cyan 	     =	    (0,255,255)
    pygame.draw.circle(screen, Cyan , node_center , radius)

    

    if show:
        pygame.display.update()
        time.sleep(Time)



def mark(screen,node_center,color,radius,show=True,Time = 0.1):

    pygame.draw.circle(screen, color, node_center , radius)
    if show:
        pygame.display.update()
        time.sleep(Time)


pygame.init()

forget = (1,0,0)

screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))

Q = queue()
S = stack()

s=0
t=1
cur = 0
graph = [[]]
visited  = list( False for _ in range(len(graph)))
parent   = list(  -1   for _ in range(len(graph)))
flow_to1 = list(  -1   for _ in range(len(graph)))
flow_to2 = list(  -1   for _ in range(len(graph)))

node_position= []

visited[s] = True

bfs1 = True
bfs2 = True
update_path1 = False
update_path2 = False
drawing = False
pause = False
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

    if bfs1:
        if Q.not_empty():
            cur = Q.pop()
            visit(screen,node_position[cur],Time = 0.01)
        else:
            bfs1 = False
            update_path1 = True

        if cur == t:
            while Q.not_empty():Q.pop()
            continue

        for neighbour in  len(graph):
            if (not visited[neighbour]) and (graph[cur][neighbour] > 0):
                visited[neighbour] = True
                parent[neighbour]  = cur
                Q.insert(neighbour)
                memorize(screen,node_position[neighbour],Time = 0.01)
                
            

    elif update_path1:
        if not drawing:
            cur = t
            while s != cur:
                pred = parent[cur]
                S.insert((pred,cur)) 
                cur = pred
            drawing = True      
        else:
            if S.not_empty():
                node1,node2 = S.pop()
                arrow(screen,node_position[node1],node_position[node2],Cyan,Cyan)
            else:
                drawing = False
                bfs2 = True
                update_path1 = False
                visited = list(False for _ in range(len(graph)))
                visited[s] = True
                Q.insert(s)
    


    elif bfs2:
        if Q.not_empty():
            cur = Q.pop()
            visit(screen,node_position[cur],Time = 0.01)
        else:
            bfs2 = False
            update_path2 = True


        if cur ==  t:
            while Q.not_empty():Q.pop()
            continue  

        if flow_to1[cur] > 0:
            pred = flow_to1[cur]
            if not visited[pred]:
                Q.insert(pred)
                visited[pred] = True
                parent[pred]  = cur
                memorize(screen,node_position[cur],Time = 0.01)

        for neighbour in  len(graph):
            if (not visited[neighbour]) and (graph[cur][neighbour] > 0):
                visited[neighbour] = True
                parent[neighbour]  = cur
                Q.insert(neighbour)
                memorize(screen,node_position[neighbour],Time = 0.01)



    elif update_path2:
        if not drawing:
            cur = t
            while s != cur:
                pred = parent[cur]
                if flow_to1[pred] != cur:
                    flow_to2[cur] = pred
                    S.insert((pred,cur))
                cur = pred 

            drawing = True      
        else:
            if S.not_empty():
                node1,node2 = S.pop()
                arrow(screen,node_position[node1],node_position[node2],Cyan,Cyan)
            else:
                drawing = False
                visited = list(False for _ in range(len(graph)))
                visited[s] = True
                Q.insert(s)
                update_path2 = False



    
    else:
        cur = t
        while s != cur:
            pred = flow_to1[cur]
            S.insert((pred,cur))
            cur = pred

        while S.not_empty():
            node1,node2 = S.pop()
            arrow(screen,node_position[node1],node_position[node2],Flame,Dark_red,10,7)
            time.sleep(0.01)

        cur = t
        while cur != s:
            pred = flow_to2[cur]
            arrow(screen,node_position[pred],node_position[cur],Flame,Dark_red,10,7)
            time.sleep(0.01)
            cur = pred