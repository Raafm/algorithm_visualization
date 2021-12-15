def kruskanimatedfs(graph,node_position, steps_mode = False):

    from math import hypot
    from algorithms.data_struct.UnionFind import UnionFind
    from algorithms.data_struct.queue import queue
    import pygame,time
    
    Black	        =	    (0,0,0)
    White	        =	    (255,255,255)
    Red  	        =	    (255,0,0)
    Dark_red        =     	(150,0,0)
    Lime	        =	    (0,255,0)
    Blue	        =	    (0,0,200)
    Yellow	        =	    (255,255,0)
    Dark_yellow     =       (250,200,0)
    Flame           =       (226,88,34)
    Cyan 	        =	    (0,255,255)
    Magenta	        =	    (255,0,255)
    Gray	        =	    (128,128,128)
    Dark_gray       =       (50, 50, 50)
    Maroon 	        =	    (128,0,0)
    Olive  	        =	    (128,128,0)
    Green  	        =	    (0,180,0)
    Purple 	        =	    (128,0,128)
    Teal	        =	    (0,128,128)
    Navy	        =	    (0,0,128)
    Light_sky       = 		(135,206,250)
    Castanho	    =	    (165,42,42)
    Carmesim	    =	    (220,20,60)
    Cream           =	    (245,255,250)
    Some_grey       =       (112,128,144)
    Light_grey      =       (119,136,153)
    Melada	        =       (240,255,240)
    Orange	        =       (255,165,0)
    Springgreen	    =       (0,255,127)
    Dark_grey       =       (41,41,41)
    skyblue	        =       (135,206,235)
    deepskyblue	    =       (0,191,255)
    lightsteelblue	=       (176,196,222)
    dodgerblue	    =       (30,144,255)
    cornflowerblue	=       (100,149,237)
    steelblue	    =       (70,130,180)
    cadetblue	    =       (95,158,160)
    mediumslateblue	=       (123,104,238)
    royalblue   	=       (65,105,225)

    
    list_colors = [
        Purple 	        ,
        Some_grey       ,
        Carmesim	    ,
        Lime            ,
        royalblue       ,
        Light_grey      , 
        skyblue	        ,
        Dark_gray       ,
        Maroon 	        ,
        Olive  	        ,
        Green  	        ,  
        deepskyblue	    ,
        Dark_red        ,
        Light_sky       ,
        Castanho	    ,        	
  	    Cyan 	        ,
        Springgreen	    ,
        Flame           ,
        Magenta	        , 	
        Gray	        ,  
        Yellow	        ,
        Orange	        ,
        Teal	        ,
        Melada	        , 
        Cream           ,
        lightsteelblue	,  
        dodgerblue	    ,  
        cornflowerblue	,  
        steelblue	    ,  
        cadetblue	    ,  
        mediumslateblue	,  
        Dark_yellow     ,
    ]
    SP = 0

    node_radius       = 5
    node_color        = Blue
    cur_edge_color    = Green
    choose_edge_color = Cyan
    not_choosen_color = Black

    number_size = 12
    weight_color = Cyan
    memory_color = Red
    current_color = Lime
    visited_color = Cyan
    
    screen_height = 700
    screen_width = 1200
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill((0,0,0))

    pygame.init()

    disjoint_set = UnionFind(len(graph))
    edge_list = []
    set_color = list( list_colors[x%len(list_colors)] for x in range(len(graph)))
    
    #functions
    def distance(node1,node2):
        return int(hypot(node1[0]-node2[0], node1[1]-node2[1]))   




    font = pygame.font.Font('freesansbold.ttf',number_size)


    for node in range(len(graph)):
        for neighbour in graph[node]:
            node1 = node_position[node]
            node2 = node_position[neighbour]
            pygame.draw.line(screen,Dark_grey, node1, node2,1)
    
    #draw circles (nodes)
    for node_number in range(len(graph)):                                                          # draw nodes
            pygame.draw.circle(screen, node_color, node_position[node_number], node_radius)
    
    pygame.display.update()




    #show information
    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("Kruskal ",True,Cyan)                        
    screen.blit(text,text.get_rect(center = (1050,70)))
    text = font.render("animated",True,Cyan)                        
    screen.blit(text,text.get_rect(center = (1050,100)))
    text = font.render("with BFS",True,Cyan)                        
    screen.blit(text,text.get_rect(center = (1050,140)))


    pygame.display.update()

    time.sleep(1)

    edge_dict = {}


    font = pygame.font.Font('freesansbold.ttf',number_size-1)
    for node1 in range(len(graph)):
        for node2 in graph[node1]:
            weight = distance(node_position[node1], node_position[node2])
            if (weight,node2,node1) in edge_list: continue
            edge_list.append((weight,node1, node2))
    


    time.sleep(1)

    font = pygame.font.Font('freesansbold.ttf',25)
    text = font.render("Sort edges",True,Cyan)                        
    screen.blit(text,text.get_rect(center = (1100,250)))
    pygame.display.update()

    time.sleep(1)

    pygame.draw.rect(screen,Black,(1000,230,200,100))
    edge_list.sort()


    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("edges",True, Black)                        
    screen.blit(text,text.get_rect(center = (780,20)))

    # animation loop
   
    edge_id = 0
    N_edge_MST = 0

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

        if N_edge_MST == len(graph)-1:
            if  edge_id == len(edge_list):
                continue
            _,node1,node2 = edge_list.pop(edge_id)
            edge_id+1
            
                   
            pygame.draw.line(screen,Black,node_position[node1], node_position[node2],2)
            pygame.display.update()
            time.sleep(0.003)
            continue



        weight,node1,node2 = edge_list[edge_id]
        pygame.draw.line(screen,cur_edge_color,node_position[node1], node_position[node2],2)

        pygame.display.update()        
        if not pause: time.sleep(0.1) 

        if disjoint_set.Find(node1) != disjoint_set.Find(node2):
            pygame.draw.line(screen,choose_edge_color,node_position[node1], node_position[node2],5)            

            
            Patriarch1 = disjoint_set.Find(node1)
            Patriarch2 = disjoint_set.Find(node2)
            Q = queue()
            seen = list(False for _ in range(len(graph)))
            Q.insert(node1)
            
            seen[node1]=True
            
            while Q.not_empty():
                node = Q.pop()
                pos = node_position[node]
                set_color[node] = set_color[Patriarch2]
                pygame.draw.circle(screen,set_color[Patriarch2],pos,8)
                for neighbour in graph[node]:
                    if not seen[neighbour] and( disjoint_set.Find(neighbour) == Patriarch1 ):
                        Q.insert(neighbour)
                        seen[neighbour] = True     
                    pygame.display.update()
                    time.sleep(0.003)
            pygame.draw.circle(screen,set_color[node2],pos,8)

            disjoint_set.Union(node1,node2)
            pygame.draw.circle(screen,set_color[Patriarch2],node_position[node2],8)
            pygame.display.update()

            N_edge_MST += 1

           


        
        elif (node1,node2) not in edge_dict and (node2,node1) not in edge_dict:
            pygame.draw.line(screen,not_choosen_color,node_position[node1], node_position[node2],2)
            pygame.draw.circle(screen,set_color[node1],node_position[node1],8)
            pygame.draw.circle(screen,set_color[node2],node_position[node2],8)
            pygame.display.update()
            

        edge_dict[(node1,node2)] = True


     
        edge_id += 1
        if edge_id == len(edge_list) or  N_edge_MST == len(graph)-1:
            pause = True

