
def BellmanFord(graph,node_position, source = 0, target = 70 ,steps_mode = False):
    
    from math import hypot
    from algorithms.data_struct.priority_queue import Heap
    import pygame,time
    
    Black	     =	    (0,0,0)
    White	     =	    (255,255,255)
    Red  	     =	    (255,0,0)
    Lime	     =	    (0,255,0)
    Blue	     =	    (0,0,200)
    Yellow	     =	    (255,255,0)
    Dark_yellow  =      (250,200,0)
    Cyan 	     =	    (0,255,255)
    Green  	     =	    (0,180,0)
    Springgreen	 =      (0,255,127)

    ###############prepare:
    INFINITY = 100000
    target_color = Springgreen
    source_color = Green
    target_radius = source_radius = node_radius = 10 
    node_color = Blue

    number_size = 12
    weight_color = Cyan
    memory_color = Red
    current_color = Lime
    visited_color = Cyan



    screen_height = 700
    screen_width = 1200
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill(Black)

    pygame.init()

    font = pygame.font.Font('freesansbold.ttf',number_size)


    #functions
    def distance(node1,node2):
        return int(hypot(node1[0]-node2[0], node1[1]-node2[1]))   



    def show_weight(peso,position,font,weight_color = weight_color ):
        text = font.render(str(peso),True,weight_color,10)
        screen.blit(text,position)

    def median_point(p1,p2):
        return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

    def w(node1,node2):
        return distance(node_position[node1],node_position[node2])


    def memorize(node,Time = 0.1,show=True ):
        pygame.draw.circle(screen,(255,0,0),node_position[node],10)

        if show:
            pygame.display.update()
            time.sleep(Time)


    def visit(node,Time = 0.1,show=True):

        pygame.draw.circle(screen,(0,255,0),node_position[node],10)

        if show:
            pygame.display.update()
            time.sleep(Time)



    def visited(node,Time = 0.1,show=True):
        pygame.draw.circle(screen,  White, node_position[node] , 10)
        pygame.draw.circle(screen,  Black,node_position[node] ,9)
        pygame.draw.circle(screen,(0,255,255),node_position[node],7)
        

        if show:
            pygame.display.update()
            time.sleep(Time)



    def mark(screen,node_center,colors,radius=8,show=True,Time = 0.05,text = None,text_color = (226, 88, 34)):

        if len(colors) == 2:
            pygame.draw.circle(screen, colors[0], node_center , radius = 8)
            pygame.draw.circle(screen, colors[1], node_center , radius=5)
        else:
            pygame.draw.circle(screen, colors, node_center , radius)

        
        if text is not None:
            font = pygame.font.Font('freesansbold.ttf',15)
            text = font.render(text,True,text_color)                        
            screen.blit(text,text.get_rect(center = node_center))
        if show:
            pygame.display.update()
            time.sleep(Time)



    def found(node):
        mark(screen, node, (255,255,255), 15)
        font = pygame.font.Font('freesansbold.ttf',20)
        text = font.render("found",True,(250,250,250))                        
        screen.blit(text,text.get_rect(center = (920,250)))






    for node in range(len(graph)):
        for neighbour in graph[node]:
            node1 = node_position[node]
            node2 = node_position[neighbour]
            pygame.draw.line(screen,(255,255,255), node1, node2,2)
            show_weight(distance(node1,node2),median_point(node1,node2),font)
    
    #draw circles (nodes)
    for node_number in range(len(graph)):                                                          # draw nodes
        if node_number == source:
            pygame.draw.circle(screen,source_color,node_position[node_number],source_radius)
        elif node_number == target:
            pygame.draw.circle(screen,target_color,node_position[node_number],target_radius)
        else:
            pygame.draw.circle(screen, node_color, node_position[node_number], node_radius)
    
    pygame.display.update()



    #show source and target
    mark(screen,node_position[ target],target_color,12)
    mark(screen,node_position[ source],source_color,12)

    #show information
    font = pygame.font.Font('freesansbold.ttf',25)
    text = font.render("Bellman-Ford",True,White)                        
    screen.blit(text,text.get_rect(center = (1000,70)))

    font = pygame.font.Font('freesansbold.ttf',15)
    pygame.draw.circle(screen,memory_color, (950,200),7)
    text = font.render("priority queue",True,memory_color)
    screen.blit(text,text.get_rect(center = (1015,200)))                             
    text = font.render("(fila de prioridade)",True,memory_color)
    screen.blit(text,text.get_rect(center = (1010,220)))


    pygame.draw.circle(screen, White, (950,150) , 10)
    pygame.draw.circle(screen,Black, (950,150) ,9)
    pygame.draw.circle(screen,visited_color,(950,150),7)
    text = font.render("seen (visto)",True,visited_color)                               # informative node       
    screen.blit(text,text.get_rect(center = (1025,150)))

    pygame.draw.circle(screen,current_color,(950,175),7)
    text = font.render("current (atual)",True,current_color)                            # informative node   
    screen.blit(text,text.get_rect(center = (1025,175)))

    pygame.display.update()

    N = len(graph)
    
    dist = list( INFINITY for _ in range(N)  )
    prev = list( -1 for _ in range(N) )
    dist[source] = 0


    edge_list = []
    for node in range(N):
        for neighbour in graph[node]:
            edge_list.append((node,neighbour,w(node,neighbour)))

    for k in range(N - 1): #O(EV)
        change = False
        for u, v, weight in edge_list:                         # O(E)
            
            mark(screen,node_position[u],Yellow,show=False)
            mark(screen,node_position[v],Yellow,Time=0.05)

            if dist[u] != INFINITY:
                
                if dist[u] + weight < dist[v]: 
                    change = True
                    dist[v] = dist[u] + weight
                    if prev[v] != -1:
                        pygame.draw.line(screen, White, node_position[prev[v]], node_position[v] ,2)
                    prev[v] = u

                    pygame.draw.line(screen, Green, node_position[u], node_position[v] ,2)
                    pygame.display.update()
                    time.sleep(0.05)
                
    

            mark(screen,node_position[u],Blue,show=False)
            mark(screen,node_position[v],Blue,Time=0.03)

        if not change:
            break


    cur = target
    while cur != source: 
        pygame.draw.line(screen, Dark_yellow, node_position[cur], node_position[prev[cur]] ,3)
        pygame.display.update()
        time.sleep(0.05)
        cur = prev[cur]
    

    

#animation loop
    current = 0
    
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
        
        if steps_mode: #pause every step of the algorithm
            pause = True  #when this iteration ends,the animation is paused






if __name__ == "__main__":
    
    from test_graph import graph,node_position
    from colors import *
    
    source = 0
    target = 55
    BellmanFord(graph,node_position,source,target,steps_mode = True)