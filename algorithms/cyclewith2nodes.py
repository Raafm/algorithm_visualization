
import math
import pygame,time



def arrow(screen, start, end, lcolor = (255,255, 255), tricolor = (255,255,255),  trirad= 4, thickness=3):
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
    pygame.draw.circle(screen,(0,0,255),node_center,radius)

    if show:
        pygame.display.update()
        time.sleep(Time)


def visit(screen,node_center,visit_color = (0,255,0),radius = 10,show=True,Time = 0.1):

    pygame.draw.circle(screen,visit_color,node_center,radius)

    if show:
        pygame.display.update()
        time.sleep(Time)



def visited(screen,node_center,radius = 10,show=True,Time = 0.1):
    Cyan = (0,255,255)
    pygame.draw.circle(screen, Cyan , node_center , radius)

    

    if show:
        pygame.display.update()
        time.sleep(Time)



def mark(screen,node_center,color,radius=8,show=True,Time = 0.1):

    pygame.draw.circle(screen, color, node_center , radius)
    if show:
        pygame.display.update()
        time.sleep(Time)

def cycleWith2Nodes(graph,node_position,s = 0,t = 1):
    from algorithms.colors import Dark_red,Flame,Cyan,White,Blue,royalblue,Black,Springgreen,Green
    from algorithms.data_struct.queue import queue
    from algorithms.data_struct.stack import stack

    pygame.init()

    screen_height = 700
    screnn_width = 1300
    screen = pygame.display.set_mode((screnn_width,screen_height))

    screen.fill((0,0,0))    


    N = len(graph)
    #tranforming adj list in a matrix graph
    matrix_graph = list(list(False for _ in range(N)) for _ in range(N))
    input_graph = graph


    for node in range(N):
        for neighbour in graph[node]:
            pygame.draw.line(screen,White,node_position[node],node_position[neighbour],2)
            matrix_graph[neighbour][node] = matrix_graph[node][neighbour] = True 


    for node in range(N):
        pygame.draw.circle(screen,Blue,node_position[node],8)

    pygame.display.update()



    graph = matrix_graph



    Q = queue()
    S = stack()


    cur = s
    seen  = list( False for _ in range(N))
    parent   = list(  -1   for _ in range(N))
    flow_to1 = list(  -1   for _ in range(N))
    flow_to2 = list(  -1   for _ in range(N))


    seen[s] = True
    Q.insert(s)

    bfs1 = True
    bfs2 = False
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

            for neighbour in  range(N):
                if (not seen[neighbour]) and (graph[cur][neighbour]):
                    seen[neighbour] = True
                    parent[neighbour]  = cur
                    Q.insert(neighbour)
                    memorize(screen,node_position[neighbour],Time = 0.01)
            
            visited(screen,node_position[cur])
                    
                

        elif update_path1:
            if not drawing:
                pygame.draw.rect(screen,Black,(0,0,1000,1000))
                for node in range(N):
                    for neighbour in input_graph[node]:
                        pygame.draw.line(screen,White,node_position[node],node_position[neighbour],2)

                for node in range(N):
                    pygame.draw.circle(screen,Blue,node_position[node],8)


                cur = t
                while s != cur:
                    pred = parent[cur]
                    S.insert((pred,cur)) 
                    graph[pred][cur] = False
                    flow_to1[cur] = pred
                    cur = pred
                drawing = True      
            else:
                if S.not_empty():
                    node1,node2 = S.pop()
                    
                    arrow(screen,node_position[node1], node_position[node2],Springgreen,Green	)
                    time.sleep(0.3)

                else:
                    drawing = False
                    bfs2 = True
                    update_path1 = False
                    seen = list(False for _ in range(N))
                    seen[s] = True
                    Q.insert(s)
                    time.sleep(1)
        


        elif bfs2:
            
            if Q.not_empty():
                cur = Q.pop()
                visit(screen,node_position[cur],Time = 0.01)
            else:
                bfs2 = False
                update_path2 = True
                time.sleep(1)


            if cur ==  t:
                while Q.not_empty():Q.pop()
                continue  

            if flow_to1[cur] > 0:
                pred = flow_to1[cur]
                if not seen[pred]:
                    Q.insert(pred)
                    seen[pred] = True
                    parent[pred]  = cur
                    memorize(screen,node_position[cur],Time = 0.01)

            for neighbour in  range(N):
                if (not seen[neighbour]) and (graph[cur][neighbour] > 0):
                    seen[neighbour] = True
                    parent[neighbour]  = cur
                    Q.insert(neighbour)
                    memorize(screen,node_position[neighbour],Time = 0.01)

            visited(screen,node_position[cur])

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
                    arrow(screen,node_position[node1], node_position[node2],royalblue,royalblue)
                    time.sleep(0.3)

                else:
                    drawing = False
                    seen = list(False for _ in range(N))
                    seen[s] = True
                    Q.insert(s)
                    update_path2 = False



        
        else:
            time.sleep(1)
            cur = t
            while cur != s:
                pred = flow_to1[cur]
                S.insert((pred,cur))
                cur = pred

            while S.not_empty():
                node1,node2 = S.pop()
                arrow(screen,node_position[node1],node_position[node2],Flame,Dark_red,10,7)
                time.sleep(0.3)

            cur = t
            while cur != s:
                pred = flow_to2[cur]
                arrow(screen,node_position[cur],node_position[pred],Flame,Dark_red,10,7)
                time.sleep(0.3)
                cur = pred

            pause = True
            continue