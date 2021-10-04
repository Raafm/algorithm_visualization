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

    mark(screen,node_position[s],White,10,False)

    pygame.display.update()


def show_cycle(screen,parent,node_position,node,source):
    White =	    (255,255,255)
    cur = node
    while cur != source:
        mark(screen,node_position[cur],White)
        cur = parent[cur]
    

def cycleWith1Node(graph,node_position,source = 0):
    from algorithms.colors import Dark_red,Flame,Cyan,White,Blue,Red,Black,Springgreen,Green,Lime,Cream,Dark_yellow,Yellow,skyblue
    from algorithms.data_struct.stack import stack

    pygame.init()

    screen_height = 700
    screen_width = 1300
    screen = pygame.display.set_mode((screen_width,screen_height))

    screen.fill((0,0,0))    

    N = len(graph) #number of nodes in the graph
    display_graph(screen,graph,node_position,source)

    NOT_SEEN = 0
    IN_STACK = 1
    SEEN    = 2
    NEIGHBOUR = 3
    status = list( NOT_SEEN for _ in range(N) )
    status[source] = SEEN
    
    parent = list( -1 for _ in range(N) )

    S = stack()
    
    for node in graph[source]:
        status[node] = NEIGHBOUR 
        parent[node] = source 
        mark(screen,node_position[node],Flame)
        S.insert(node)
    
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
       
        if S.not_empty():
            cur = S.pop()
            if status[cur] == IN_STACK:
                mark(screen,node_position[cur],Green)

            for neighbour in graph[cur]:
                if status[neighbour] == NOT_SEEN:
                    status[neighbour] = IN_STACK
                    parent[neighbour] = cur
                    S.insert(neighbour)
                    mark(screen,node_position[neighbour],Red)
                elif status[neighbour] == NEIGHBOUR and parent[cur] != neighbour:
                    parent[neighbour] = cur
                    show_cycle(screen,parent,node_position,neighbour,source)
                    pause = True
                    break

            if pause:continue
            
            if status[cur] == IN_STACK:
                status[cur] = SEEN
                mark(screen,node_position[cur],Dark_yellow)

            