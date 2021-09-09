
def prim(graph,node_position, source = 0, steps_mode = False):
    
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
    Flame        =      (226,88,34)
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




    ####################

    
    
    
    screen_height = 700
    screnn_width = 1000
    screen = pygame.display.set_mode((screnn_width,screen_height))
    screen.fill((0,0,0))

    pygame.init()

    font = pygame.font.Font('freesansbold.ttf',number_size)


    #functions
    def distance(node1,node2):
        return int(hypot(node1[0]-node2[0], node1[1]-node2[1]))   



    def show_weight(weight,position,font,weight_color = weight_color ):
        text = font.render(str(weight),True,weight_color,10)
        screen.blit(text,position)

    def median_point(p1,p2):
        return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)


    def memorize(node,Time = 0.1,show=True ):
        pygame.draw.circle(screen,(255,0,0),node_position[node],10)

        if show:
            pygame.display.update()
            time.sleep(Time)


    def visit(node,Time = 0.1,show=True):

        pygame.draw.circle(screen,Dark_yellow,node_position[node],10)

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



    def mark(node,color,radius):

        pygame.draw.circle(screen, color, node_position[node] , radius)



    def finished(node):
        mark(node, (255,255,255), 15)
        font = pygame.font.Font('freesansbold.ttf',20)
        text = font.render("finished",True,(250,250,250))                        
        screen.blit(text,text.get_rect(center = (920,250)))










    for node in range(len(graph)):
        for neighbour in graph[node]:
            node1 = node_position[node]
            node2 = node_position[neighbour]
            pygame.draw.line(screen,(255,255,255), node1, node2,1)
            show_weight(distance(node1,node2),median_point(node1,node2),font)
    
    #draw circles (nodes)
    for node_number in range(len(graph)):                                                          # draw nodes
        if node_number == source:
            pygame.draw.circle(screen,source_color,node_position[node_number],source_radius)
        else:
            pygame.draw.circle(screen, node_color, node_position[node_number], node_radius)
    
    pygame.display.update()



    #show source and target
    mark(source,source_color,12)

    #show information
    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("prim",True,Dark_yellow)                        
    screen.blit(text,text.get_rect(center = (900,70)))

    font = pygame.font.Font('freesansbold.ttf',20)
    pygame.draw.circle(screen,memory_color, (830,200),10)
    text = font.render("priority queue",True,memory_color)
    screen.blit(text,text.get_rect(center = (915,200)))                             
    text = font.render("(fila de prioridade)",True,memory_color)
    screen.blit(text,text.get_rect(center = (910,220)))


    
    pygame.draw.circle(screen,Dark_yellow,(830,150),10)
    text = font.render("in MST",True,Dark_yellow)                               # informative node       
    screen.blit(text,text.get_rect(center = (925,150)))


    pygame.display.update()

    dist = list(INFINITY for _ in range(len(graph)))
    mst  = list(False for _ in range(len(graph)))
    PQ   = Heap(comp = lambda node1,node2: node1[1] > node2[1])
    edge_dict = {}
    dist[source] = 0

    # put neighbours of source
    for neighbour in graph[source]:
        dist[neighbour] = distance(node_position[source], node_position[neighbour])
        PQ.insert(   (neighbour, dist[neighbour], source)   )



    # animation loop
    current = 0
    nodes_in_tree = 1


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
              

        if nodes_in_tree < len(graph):
            # pegar minimo da Heap
            if PQ.not_empty():
                current,weight,predecessor = PQ.pop()

            else:continue

            if mst[current]:
                continue
            if dist[current] < weight:
                continue

            edge_dict[(current,predecessor)] = True
            pygame.draw.line(screen,Dark_yellow,node_position[current],node_position[predecessor],3)
            mark(current,Flame,node_radius)
            pygame.display.update()

            

            
            if current != source: visit(current)
            # tentar atualizar os elementos

            nodes_in_tree += 1

            for neighbour in graph[current]:

                if mst[neighbour]: continue

                weight = distance(node_position[current], node_position[neighbour])
                if weight < dist[neighbour]:
                    dist[neighbour] = weight
                    PQ.insert(     ( neighbour ,dist[neighbour], current )  )
                     
                    memorize(neighbour)

            mst[current] = True

            
            time.sleep(0.1)


        else:  #finished
            pygame.draw.rect  (screen,    Black    ,  (0,0 ,800, 700))
            for node1,node2 in edge_dict:
                
                pygame.draw.line  (screen, Dark_yellow , node_position[node1] , node_position[node2],3)
                pygame.draw.circle(screen, Dark_yellow , node_position[node1] , node_radius//2)
                pygame.draw.circle(screen, Dark_yellow , node_position[node2] , node_radius//2)
                
            pygame.display.update()
            pause = True




if __name__ == "__main__":
    
    from test_graph import graph,node_position
    from colors import *
    
    source = 0

    prim(graph, node_position, source = 0, steps_mode = True)