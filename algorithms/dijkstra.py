
def dijkstra(graph,node_position, source = 0, target = 1 ,steps_mode = False):
    
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

    mst  = list(False for _ in range(len(graph)))
    dist = list(INFINITY for _ in range(len(graph)))
    predecessor = list(-1 for _ in range(len(graph)))

    PQ = Heap(comp = lambda node1,node2: node1[1] > node2[1])


    ####################

    predecessor[source] = source
    dist[source] = 0
    PQ.insert( (source,dist[source]) )
    screen_height = 700
    screnn_width = 1000
    screen = pygame.display.set_mode((screnn_width,screen_height))
    screen.fill((0,0,0))

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



    def mark(node,color,radius):

        pygame.draw.circle(screen, color, node_position[node] , radius)



    def found(node):
        mark(node, (255,255,255), 15)
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
    mark(target,target_color,12)
    mark(source,source_color,12)

    #show information
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





#animation loop
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
        
        if steps_mode: #pause every step of the algorithm
            pause = True  #when this iteration ends,the animation is paused
              

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

                total_distance = distance(node_position[current], node_position[neighbour]) + dist[current]
                if total_distance < dist[neighbour]:
                    dist[neighbour] = total_distance
                    PQ.insert((neighbour,dist[neighbour]))
                    predecessor[neighbour] = current 
                    memorize(neighbour)

            mst[current] = True

            if current != source:visited(current)



        else:  #if found, current == target

            pygame.draw.line(screen,Yellow,node_position[predecessor[current]],node_position[current],3)
            current = predecessor[current]
            pygame.display.update()
            time.sleep(0.3)
            if current == source:
                pause = True




if __name__ == "__main__":
    
    from test_graph import graph,node_position
    from colors import *
    
    source = 0
    target = 55
    dijkstra(graph,node_position,source,target,steps_mode = True)