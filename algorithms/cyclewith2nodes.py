
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


def memorize(screen,node_center,radius=10,Time = 0.1,show=True,sender_on = False):
    Springgreen	    =       (0,255,127)
    Flame           =       (226, 88, 34)
    pygame.draw.circle(screen,Springgreen,node_center,radius)
    
    if sender_on:
        font = pygame.font.Font('freesansbold.ttf',15)
        text = font.render("s",True,Flame)                        
        screen.blit(text,text.get_rect(center = node_center))
    else:
        font = pygame.font.Font('freesansbold.ttf',15)
        text = font.render("r",True,Flame)                        
        screen.blit(text,text.get_rect(center = node_center))
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



def mark(screen,node_center,color,radius=8,show=True,Time = 0.1,text = None,text_color = (226, 88, 34)):

    pygame.draw.circle(screen, color, node_center , radius)
    
    if text is not None:
        font = pygame.font.Font('freesansbold.ttf',15)
        text = font.render(text,True,text_color)                        
        screen.blit(text,text.get_rect(center = node_center))
    if show:
        pygame.display.update()
        time.sleep(Time)


def change(screen,node_center,show=True,Time = 0.1,):
        Flame = (226, 88, 34)
        Blue = (0,0,255)
        color = Blue

        pygame.draw.circle(screen, color, node_center , 12)
        pygame.draw.circle(screen, color, node_center , 10)

        font = pygame.font.Font('freesansbold.ttf',12)
        text = font.render("s",True,Flame)                        
        screen.blit(text,text.get_rect(center = node_center))

        if show:
            pygame.display.update()
            time.sleep(Time)
            pygame.display.update()



def display_graph(screen,graph,N,node_position,s,t,edges_animation = False,first_display = True):
    N2 = len(graph)

    White       = (255, 255, 255)
    Blue        = (0, 0, 200)
    Dark_yellow = (250, 200, 0)
    Flame       = (226, 88, 34)
    #print edges
    for node in range(N2):
        for neighbour in graph[node]:
            pygame.draw.line(screen,White,node_position[node%N],node_position[neighbour%N],1)
                   
            if edges_animation:
                if node != s and node != t:
                    node_center = node_position[node%N]
                    font = pygame.font.Font('freesansbold.ttf',15)
                    text = font.render("s",True,Flame)                        
                    screen.blit(text,text.get_rect(center = node_center))
                elif node == s:
                    node_center = node_position[node%N]
                    font = pygame.font.Font('freesansbold.ttf',15)
                    text = font.render("S",True,Dark_yellow)                        
                    screen.blit(text,text.get_rect(center = node_center))
                else:
                    node_center = node_position[node%N]
                    font = pygame.font.Font('freesansbold.ttf',15)
                    text = font.render("T",True,Dark_yellow)                        
                    screen.blit(text,text.get_rect(center = node_center))
                pygame.display.update()
                time.sleep(0.02)

    #print nodes
    for node in range(N):
        if first_display:
            mark(screen,node_position[node],Blue,12,False)
        else:
            mark(screen,node_position[node],Blue,12,False,text = "r")

    mark(screen,node_position[s],Dark_yellow,12,False,text = "S",text_color = Flame)
    mark(screen,node_position[t],Dark_yellow,12,False,text = "T",text_color = Flame)

    pygame.display.update()
    if edges_animation: time.sleep(1.5)

def cycleWith2Nodes(graph,node_position,s = 0,t = 1,steps_mode = False):
    from algorithms.colors import Dark_red,Flame,Cyan,White,Blue,royalblue,Black,Springgreen,Green,Lime,Cream,Dark_yellow,Yellow
    from algorithms.data_struct.queue import queue
    from algorithms.data_struct.stack import stack

    pygame.init()

    screen_height = 700
    screnn_width = 1300
    screen = pygame.display.set_mode((screnn_width,screen_height))

    screen.fill((0,0,0))    

    N = len(graph) #number of nodes in the graph
    display_graph(screen,graph,N,node_position,s,t)

    for _ in range(N):
        graph.append([])
    
    for node in range(N):
        if node != s and node != t:
            for neighbour in graph[node]:
                graph[node+N].append(neighbour)
                graph[node] = [node+N]
    
    temp_list = graph[t]
    graph[t] = []
    for neighbour in temp_list:
        graph[t].append(neighbour+N)



    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Find smallest cycle",True,Dark_yellow)                        
    screen.blit(text,text.get_rect(center = (950,70)))
    
    text = font.render("with the 2 yellow nodes",True,Dark_yellow)                        
    screen.blit(text,text.get_rect(center = (950,90)))
    
    pygame.display.update()
    time.sleep(2)



    # ALGORITHM STARTS HERE
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Split each not yellow node",True,White) 
    screen.blit(text,text.get_rect(center = (950,150)))
    pygame.display.update()
    time.sleep(2)
    text = font.render("in sender and receiver nodes",True,White)                        
    screen.blit(text,text.get_rect(center = (950,170)))
    pygame.display.update()
    time.sleep(2)

    pygame.draw.rect(screen,Black,(0,0,800,2000))
    display_graph(screen,graph,N,node_position,s,t,edges_animation=True,first_display=False)
    pygame.draw.rect(screen,Black,(800,130,500,200))
    time.sleep(1)

    predecessor = list( -1 for _ in range(2*N))
    predecessor[s] = s
    flow_to = list( -1 for _ in range(2*N))
    Q = queue()
    
    start = True
    bfs = True
    path = False
    cycle = False
    first_iteration = True

    pause = False
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
        
        if steps_mode: #pause every step of the algorithm
            pause = True  #when this iteration ends,the animation is paused


        if bfs:
            
            if start:

                font = pygame.font.Font('freesansbold.ttf',20)
                text = font.render("First BFS",True,Cyan) 
                screen.blit(text,text.get_rect(center = (950,150)))
                text = font.render("Searching augmenting path",True,royalblue)                        
                screen.blit(text,text.get_rect(center = (950,170)))
                pygame.display.update()
                time.sleep(2)
                for neighbour in graph[s]:
                    Q.insert(neighbour)
                    predecessor[neighbour] = s
                    memorize(screen,node_position[neighbour],Time = 0.1,sender_on= False)
                start = False
                
            
            cur = Q.pop()
            visit(screen,node_position[cur%N],radius = 14,Time = 0.3)
            for neighbour in graph[cur]:
                if predecessor[neighbour] < 0: # has not seen the node
                    Q.insert(neighbour)
                    predecessor[neighbour] = cur
                    memorize(screen,node_position[neighbour%N],Time = 0.1,sender_on = (neighbour >= N) )
                
                    if neighbour == t:
                        bfs = False
                        path = True
                        time.sleep(1.5)
                        break
            
            mark(screen,node_position[cur%N],Black,radius = 14,show = False)
            visited(screen,node_position[cur%N],radius = 12,Time = 0.1)    
            if cur < N:        
                change(screen,node_position[cur%N],Time = 0.1)
            
            time.sleep(0.2)


            



        elif path:
            cur = t
            S = stack()
            
            path_edge_dict = {}

            while cur != s:
                pred = predecessor[cur]
                S.insert((pred,cur)) # insert to make a good animation latter
                path_edge_dict[(pred,cur)] = True

                #reverse edge
                graph[cur].append(pred) 
                graph[pred].remove(cur)
                
                if flow_to[pred] == cur:  #counter flux
                    S.pop()
                    S.insert((-pred,-cur))
                else:
                    flow_to[cur] = pred
                
                cur = pred
            
           
            while S.not_empty(): # animation showing path
                node1,node2 = S.pop()
                if node1 < 0 or node2 < 0:
                    node1,node2 = -node1,-node2
                    pygame.draw.line(screen,Black,node_position[node1%N], node_position[node2%N],5)
                    pygame.draw.line(screen,White,node_position[node1%N], node_position[node2%N],1)
                    mark(screen,node_position[node1%N],Blue,radius = 14)
                    mark(screen,node_position[node2%N],Blue,radius = 14)
                    pygame.display.update()
                else:
                    arrow(screen,node_position[node1%N],node_position[node2%N],royalblue,White,5,5)
                    mark(screen,node_position[node1%N],Blue,radius = 14)
                time.sleep(0.3)

            if first_iteration == True:
                
                pygame.draw.rect(screen,Black,(0,0,2000,2000))
                #print edges
                for node in range(2*N):
                    for neighbour in graph[node]:
                        if ( (neighbour,node) not in path_edge_dict ) and ( (node,neighbour) not in path_edge_dict ):  
                            pygame.draw.line(screen,White,node_position[node%N],node_position[neighbour%N],1)
                        

                path_edge_dict = {}
                
                cur = t
                while cur != s:
                    pred = predecessor[cur]
                    pygame.draw.line(screen,royalblue,node_position[cur%N],node_position[pred%N],5)
                    cur = pred

                #print nodes
                for node in range(N):
                    mark(screen,node_position[node%N],Blue,12,False)

                pygame.display.update()

                first_flow_to_t = flow_to[t]
                flow_to[t] = -1
                predecessor = list(-1 for _ in range(2*N))
                predecessor[s] = s
                Q = queue()
                Q.insert(s)

                first_iteration = False
                path = False
                bfs = True
                time.sleep(1.5)


            else:
                cycle = True
                path = False
                mark(screen,node_position[t],Dark_yellow,12)
                mark(screen,node_position[s],Dark_yellow,12)
                time.sleep(1.5)
        


        elif cycle:
            
#            cur = t
#            S = stack()
#            while cur != s:
#                pred = flow_to[cur]
#                S.insert((pred,cur))
#                cur = pred
#           
#            while S.not_empty():
#                node1,node2 = S.pop()
#                arrow(screen,node_position[node1%N],node_position[node2%N],Lime,Green,6,4)
#                time.sleep(0.3)
#            
#            cur = first_flow_to_t
#            arrow(screen,node_position[t],node_position[cur%N])
#            while cur != s:
#                node2,node1 = flow_to[cur],cur
#                arrow(screen,node_position[node1%N],node_position[node2%N],Lime,Green,6,4)
#                cur = flow_to[cur]
#                time.sleep(0.3)
            
            cycle = False
            pause = True
            

            
            
                