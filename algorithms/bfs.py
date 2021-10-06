def bfs(graph, node_position, source = 0,steps_mode = False):
    
    from algorithms.data_struct.queue import queue
    import pygame,time
    from algorithms.colors import Springgreen,Cyan,Red,Green,Yellow,Lime,Black,White,deepskyblue
    process_list = queue()
    seen = list(False for x in range(len(graph)))                                   # haven't seen anyone yet

    screen_height = 700
    screen_width = 1300
    screen = pygame.display.set_mode((screen_width,screen_height))

    screen.fill((0,0,0))

    pygame.init()


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

    source_color = Green
    node_color = Blue
    current_color = Lime
    source_radius = 5    
    node_radius = 5


    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("BFS",True,(0,255,0))                   # informative node       
    screen.blit(text,text.get_rect(center = (1150,50)))
    
    font = pygame.font.Font('freesansbold.ttf',25)
    
    pygame.draw.circle(screen,(0,255,255), (1000,185),10)
    text = font.render("memory queue",True,(0,255,255))
    screen.blit(text,text.get_rect(center = (1110,183)))                             # informative node   
    text = font.render("(fila de processamento)",True,(0,255,255))
    screen.blit(text,text.get_rect(center = (1100,220)))

    pygame.draw.circle(screen,  Lime,(1000,250)  ,10 )
    pygame.draw.circle(screen,  Springgreen, (1000,250)  ,7 )
    text = font.render("seen",True,Springgreen,20)
    screen.blit(text,text.get_rect(center = (1060,250)))
    pygame.display.update()
    

    for node in range(len(graph)):
        for neighbour in graph[node]:
            node1 = node_position[node]
            node2 = node_position[neighbour]
            pygame.draw.line(screen,(255,255,255), node1, node2,2)
            
    
    #draw circles (nodes)
    for node_number in range(len(graph)):                                                          # draw nodes
        if node_number == source:
            pygame.draw.circle(screen,source_color,node_position[node_number],source_radius)

        else:
            pygame.draw.circle(screen, node_color, node_position[node_number], node_radius)
    
    pygame.display.update()




    n_layer = 0   # number of nodes in cur layer
    missing = 1   # missing nodes in current node

    pause = True
    current = source
    process_list.insert(source)
    while True :
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

        if process_list.not_empty(): 
            
            if missing == 0:
                time.sleep(1)    
                missing = n_layer
                n_layer = 0

                
            

            pygame.draw.circle(screen,  Lime, node_position[current] ,8 )
            pygame.draw.circle(screen,  Springgreen, node_position[current] ,6 )

            missing -= 1
            current = process_list.pop()
            seen[current] = True
            
            #pygame.draw.circle(screen, Lime , node_position[current] , 6)

            for neighbour in graph[current]:
                if seen[neighbour]:
                    continue
                else:
                    n_layer += 1
                    pygame.draw.circle(screen,  Cyan, node_position[neighbour] , 8)
                    process_list.insert(neighbour)



        pygame.display.update()
