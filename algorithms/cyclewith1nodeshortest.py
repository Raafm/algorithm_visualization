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


def mark(screen,node_center,color,radius=8,show=True,Time = 0.1,text = None,text_color = (0, 0, 0),text_size = 15):

    pygame.draw.circle(screen, color, node_center , radius)
    
    if text is not None:
        font = pygame.font.Font('freesansbold.ttf',text_size)
        text = font.render(text,True,text_color)                        
        screen.blit(text,text.get_rect(center = node_center))
    if show:
        pygame.display.update()
        time.sleep(Time)


def change(screen,node_center,show=True,Time = 0.1,):
        Flame = (226, 88, 34)
        skyblue	        =       (135,206,235)
        color = skyblue

        pygame.draw.circle(screen, color, node_center , 12)
        

        font = pygame.font.Font('freesansbold.ttf',13)
        text = font.render("s",True,Flame)                        
        screen.blit(text,text.get_rect(center = node_center))

        if show:
            pygame.display.update()
            time.sleep(Time)
            pygame.display.update()



def display_graph(screen,graph,node_position,s):
    N = len(graph)

    White       = (255, 255, 255)
    Blue        = (0, 0, 200)
    Dark_yellow = (250, 200, 0)
    Flame       = (226, 88, 34)
    Yellow	        =	    (255,255,0)
    Cyan 	        =	    (0,255,255)

    
    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("Find the shortest cycle",True,White)                        
    screen.blit(text,text.get_rect(center = (930,70)))
    text = font.render("with the node s: ",True,White)                        
    screen.blit(text,text.get_rect(center = (930,100)))
    mark(screen,(1100,100),White,15,text = "s",text_color = (0,0,0), text_size = 22)
    pygame.display.update()
    time.sleep(1.5)

    font = pygame.font.Font('freesansbold.ttf',25)
    pygame.draw.circle(screen,Cyan, (840,200),12)
    text = font.render("memory queue",True,Cyan)
    screen.blit(text,text.get_rect(center = (970,200)))                             # informative node   
    text = font.render("(fila de processamento)",True,Cyan)
    screen.blit(text,text.get_rect(center = (970,220)))
    pygame.display.update()
    
    

    #print edges
    for node in range(N):
        for neighbour in graph[node]:
            pygame.draw.line(screen,White,node_position[node],node_position[neighbour],1)
                   
           

    #print nodes
    for node in range(len(node_position)):
        if node == s:
            mark(screen,node_position[node],Blue,8,False)
        else:
            mark(screen,node_position[node],Blue,8,False)

    mark(screen,node_position[s],White,10,False,text = "s")

    pygame.display.update()
    time.sleep(1.5)


def show_cycle(screen,parent,node_position,node2,node1,source):

    White =	    (255,255,255)

    cur1 = node1
    cur2 = node2

    while cur1 != source and cur2 != source:

        mark(screen,node_position[cur1],White)
        mark(screen,node_position[cur2],White)
        arrow(screen,node_position[cur1],node_position[parent[cur1]],White,(0,0,0))
        arrow(screen,node_position[cur2],node_position[parent[cur2]],White,(0,0,0))
        node1 = parent[cur1]
        cur1 = parent[cur1]
        node2 = parent[cur2]
        cur2 = parent[cur2]
        time.sleep(0.3)

    arrow(screen,node_position[node1],node_position[source],White,(0,0,0))
    mark(screen,node_position[source],White,10,text = "s")

    while cur1 != source:

        mark(screen,node_position[cur1],White)
        arrow(screen,node_position[cur1],node_position[parent[cur1]],White,(0,0,0))
        node1 = parent[cur1]
        cur1 = parent[cur1]
        time.sleep(0.3)

    while cur1 != source:

        mark(screen,node_position[cur2],White)
        arrow(screen,node_position[cur2],node_position[parent[cur2]],White,(0,0,0))
        node1 = parent[cur2]
        cur1 = parent[cur2]
        time.sleep(0.3)

    if node2 != source:
        arrow(screen,node_position[node2],node_position[source],White,(0,0,0))
        mark(screen,node_position[source],White,10,text = "s")
        mark(screen,node_position[node2],White,10)

    if node1 != source:
        arrow(screen,node_position[node1],node_position[source],White,(0,0,0))
        mark(screen,node_position[source],White,10,text = "s")
        mark(screen,node_position[node1],White,10)


def cycleWith1NodeShortest(graph,node_position,source = 0):
    from algorithms.colors import Dark_red,Flame,Cyan,White,Blue,Red,Black,Springgreen,Green,Lime,Cream,Dark_yellow,Yellow,lightsteelblue,Teal
    from algorithms.data_struct.queue import queue

    pygame.init()

    screen_height = 700
    screen_width = 1300
    screen = pygame.display.set_mode((screen_width,screen_height))

    screen.fill((0,0,0))    

    N = len(graph) #number of nodes in the graph
    display_graph(screen,graph,node_position,source)

    
    color = list( Blue for _ in range(N) )
    color[source] = White
    
    parent = list( -1 for _ in range(N) )

    Q = queue()

    color_list = [Springgreen,Teal,Red,Dark_yellow]
    i = 0

    for node in graph[source]:
        color[node] = color_list[i]
        i+=1

        parent[node] = source 
        mark(screen,node_position[node],color[node])
        Q.insert(node)
    
    pause = False
    running =  True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_SPACE:     #press breakspace to pause or play
                    pause = not pause   
                    time.sleep(0.2)
    
        if pause:
            continue
       
        if Q.not_empty():
            cur = Q.pop()
            
            mark(screen,node_position[cur],color[cur],Time = 0.15)

            for neighbour in graph[cur]:

                if color[neighbour] == Blue:

                    color[neighbour] = color[cur]
                    parent[neighbour] = cur
                    Q.insert(neighbour)
                    mark(screen,node_position[neighbour],Cyan)

                elif neighbour != source and color[neighbour] != color[cur]:
                    
                    font = pygame.font.Font('freesansbold.ttf',30)
                    text = font.render("Found!",True,White)                        
                    screen.blit(text,text.get_rect(center = (930,400)))
                    mark(screen,node_position[neighbour],White)

                    time.sleep(2)
                    arrow(screen,node_position[cur],node_position[neighbour],White,Black)
                    show_cycle(screen,parent,node_position,neighbour,cur,source)
                    Q = queue() #empty queue
                    pause = True
                    break


            