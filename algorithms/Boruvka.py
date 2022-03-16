def BORUVKA(list_edges, N):
    from algorithms.data_struct.ChildUnionFind import UnionFind,linked_list
    from math import inf
    #Crie uma floresta F com cada nó do grafo
    N_trees = N
    
    F = UnionFind(N)
    
    while N_trees > 1:

        best_edges_index = list(-1  for _ in range(N))
        best_edges_W     = list(inf for _ in range(N))
        
        for index,e in enumerate(list_edges):

            patriarch1 = F.find(node1)
            patriarch2 = F.find(node2)

            if F.Find(node1) == F.Find(node2):
                continue

            node1, node2, W = e

            w1 = best_edges_W[patriarch1]
            w2 = best_edges_W[patriarch2]

            if W < w1: best_edges_W[patriarch1] = W; best_edges_index[node1] = index; 
            if W < w2: best_edges_W[patriarch2] = W; best_edges_index[node2] = index; F.Union(node1,node2)
            
            

def boruvka(graph,node_position, steps_mode = False):

    from math import hypot,inf 
    from algorithms.data_struct.ChildUnionFind import UnionFind,linked_list
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
    darkslategrey   =       (47,79,79)
    Dark_sienna     =       (60,20,20)
    Bulgarian_rose  =       ( 72,6,7)
    Midnight_green  =        (0,73,83)
    
    list_colors = [
        Purple 	        ,
        Some_grey       ,
        Carmesim	    ,
        Lime            ,
        royalblue       ,
        Navy            ,
        skyblue	        ,
        Dark_gray       ,
        Maroon 	        ,
        Olive  	        ,
        Green  	        ,  
        deepskyblue	    ,
        cadetblue	    ,
        Dark_sienna     ,
        Castanho	    ,        	
  	    Cyan 	        ,
        Springgreen	    ,
        Flame           ,
        Magenta	        , 	
        Gray	        ,  
        Yellow	        ,
        Orange	        ,
        Teal	        ,
        Midnight_green  , 
        Bulgarian_rose  ,
        darkslategrey	,  
        dodgerblue	    ,  
        cornflowerblue	,  
        steelblue	    ,  
        Dark_red        ,  
        mediumslateblue	,  
        Dark_yellow     ,
    ]
    SP = 0

    node_radius       = 5
    node_color        = Blue
    cur_edge_color    = Green
    choose_edge_color = White#lightsteelblue
    not_choosen_color = Black

    number_size = 12
    weight_color = Cyan
    memory_color = Red
    current_color = Lime
    visited_color = Cyan
    
    screen_height = 700
    screnn_width = 1250
    screen = pygame.display.set_mode((screnn_width,screen_height))
    screen.fill((0,0,0))

    pygame.init()

    F = UnionFind(len(graph))
    edge_list = []
    set_color = list( list_colors[x%len(list_colors)] for x in range(len(graph)))

    #functions
    def distance(node1,node2):
        return int(hypot(node1[0]-node2[0], node1[1]-node2[1]))   



    def show_weight(weight,position,font,weight_color = weight_color ):
        text = font.render(str(weight),True,weight_color,10)
        screen.blit(text,position)

    def median_point(p1,p2):
        return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

    #start =730
    start_list = 710        
    def show_weight_list(edge_list,first = 0):
        pygame.draw.rect(screen,Light_grey,(start_list,0,250,1000))
        
        font = pygame.font.Font('freesansbold.ttf',30)
        text = font.render("edges",True, Black)                        
        screen.blit(text,text.get_rect(center = (780,20)))

        height_id1 = 0
        height_id2 = 0
        height_id3 = 0
        font = pygame.font.Font('freesansbold.ttf',number_size-1)
        for edge_id in range(len(edge_list)-first):
            if 15*edge_id+20 < screen_height-80:
                show_weight(edge_list[edge_id+first],(start_list+20,15*edge_id+60),font)
                height_id1 = edge_id+1
            elif 15*(edge_id-height_id1)+20 < screen_height-80:
                show_weight(edge_list[edge_id+first],(start_list+95,15*(edge_id-height_id1)+60),font)
                height_id2 = edge_id+1
            elif 15*(edge_id-height_id2)+20 < screen_height-80:
                show_weight(edge_list[edge_id+first],(start_list+165,15*(edge_id-height_id2)+60),font)
                height_id3 = edge_id+1

        pygame.display.update()

    def edge_counter(N_edge_MST):
        pygame.draw.rect(screen,Black,(1000,400,200,200))
        font = pygame.font.Font('freesansbold.ttf',20)
        text = font.render("edges in MST: " + str(N_edge_MST),True,choose_edge_color)                        
        screen.blit(text,text.get_rect(center = (1085,450)))




    font = pygame.font.Font('freesansbold.ttf',number_size)

    # draw edges
    for node in range(len(graph)):
        for neighbour in graph[node]:
            node1 = node_position[node]
            node2 = node_position[neighbour]
            pygame.draw.line(screen,Dark_grey, node1, node2,1)
            show_weight(distance(node1,node2),median_point(node1,node2),font)
    
    #draw circles (nodes)
    for node_number in range(len(graph)):                                                          # draw nodes
            pygame.draw.circle(screen, node_color, node_position[node_number], node_radius)
    
    pygame.display.update()




    #show information
    font = pygame.font.Font('freesansbold.ttf',40)
    text = font.render("Borůvka",True,choose_edge_color)                        
    screen.blit(text,text.get_rect(center = (1100,70)))


    pygame.display.update()

    time.sleep(1)

    mst  = list(False for _ in range(len(graph)))
    edge_dict = {}

    #creating edge_list
    font = pygame.font.Font('freesansbold.ttf',number_size-1)
    for node1 in range(len(graph)):
        for node2 in graph[node1]:
            weight = distance(node_position[node1], node_position[node2])
            if (weight,node2,node1) in edge_list: continue
            edge_list.append((weight,node1, node2))
    
    show_weight_list(edge_list)
    time.sleep(1)


    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("edges",True, Black)                        
    screen.blit(text,text.get_rect(center = (780,20)))
   
    pygame.display.update()

    time.sleep(1)
    pygame.draw.rect(screen,Black,(1020,220,200,70))

    pygame.display.update()


    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("edges in MST: 0",True,choose_edge_color)                        
    screen.blit(text,text.get_rect(center = (1085,450)))
    pygame.display.update()
    time.sleep(1)

    # animation loop
   
    edge_id = 0
    N_edge_MST = 0

    N = len(graph)

    font = pygame.font.Font('freesansbold.ttf',22)
    text = font.render("Choose the shortest edge",True,choose_edge_color)                        
    screen.blit(text,text.get_rect(center = (1100,270)))
    
    text = font.render("for each tree",True,choose_edge_color)                        
    screen.blit(text,text.get_rect(center = (1100,300)))
    pygame.display.update()
    time.sleep(1)


    best_edges_index = list(-1  for _ in range(N))
    best_edges_W     = list(inf for _ in range(N))

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

        # if algorithm has finished (MST is complete)
        if N_edge_MST == len(graph)-1:
            time.sleep(1)
            pygame.draw.rect(screen,Black,(965,250,1100,270)) # erase notes
            pygame.draw.rect(screen,Black,(0,0,710,1000))
            for node1,node2 in edge_dict:
                pos1 = node_position[node1]
                pos2 = node_position[node2]
                pygame.draw.line(screen,White,pos1, pos2,2)
                show_weight(distance(pos1, pos2),median_point(pos1, pos2),font,Cyan)
            for node in range(len(graph)):
                pygame.draw.circle(screen,White,node_position[node],8)
            edge_counter(N_edge_MST)
            pygame.display.update()
            pause = True
            continue
        

        # take an edge from the list
        weight,node1,node2 = edge_list[edge_id]
    
  

        if pause:
            continue
        

        if steps_mode: # pause every step of the algorithm
            pause = True  # when this iteration ends,the animation is paused              
        
        

        if F.Find(node1) != F.Find(node2):
            
            pygame.draw.line(screen,cur_edge_color,node_position[node1], node_position[node2],2)
            
            font = pygame.font.Font('freesansbold.ttf',number_size-1)
            show_weight(edge_list[edge_id],(start_list+20,15*0 + 60),font,Green)

            pygame.display.update()    
            time.sleep(0.1)

            patriarch1 = F.Find(node1)
            patriarch2 = F.Find(node2)

            w1 = best_edges_W[patriarch1]
            w2 = best_edges_W[patriarch2]
            added = False
            if weight < w1:
                e_index = best_edges_index[patriarch1]
                # best_edges_index.count(e_index) > 1 ---> the edge were selected by more than one
                # so we shouldn't remove it, to avoid erasing an possible selected edge
                if e_index != -1  and best_edges_index.count(e_index) == 1:
                    W,u,v = edge_list[e_index]# edge antiga
                    
                    pygame.draw.line(screen,not_choosen_color,node_position[u], node_position[v],4)
                    pygame.draw.line(screen,Dark_grey, node_position[u], node_position[v],1)

                    r = 8 if N_edge_MST > 0 else 5

                    color = set_color[u] if N_edge_MST > 0 else Blue
                    pygame.draw.circle(screen,color,node_position[u],r)
                    color = set_color[v] if N_edge_MST > 0 else Blue
                    pygame.draw.circle(screen,color,node_position[v],r)

                best_edges_W[patriarch1] = weight; best_edges_index[patriarch1] = edge_id
                pygame.draw.line(screen,choose_edge_color,node_position[node1],node_position[node2],3)
                added = True

            if weight < w2:
                e_index = best_edges_index[patriarch2]
                if e_index != -1 and best_edges_index.count(e_index) == 1:
                    W,u,v = edge_list[e_index]# edge antiga
                    
                    pygame.draw.line(screen,not_choosen_color,node_position[u], node_position[v],4)
                    pygame.draw.line(screen,Dark_grey, node_position[u], node_position[v],1)

                    r = 8 if N_edge_MST > 0 else 5

                    color = set_color[u] if N_edge_MST > 0 else Blue
                    pygame.draw.circle(screen,color,node_position[u],r)
                    color = set_color[v] if N_edge_MST > 0 else Blue
                    pygame.draw.circle(screen,color,node_position[v],r)
       
                best_edges_W[patriarch2] = weight; best_edges_index[patriarch2] = edge_id
                pygame.draw.line(screen,choose_edge_color,node_position[node1],node_position[node2],3)
                added = True
            
            if not added:
                pygame.draw.line(screen,Dark_grey,node_position[node1], node_position[node2],2)
                pygame.display.update()
                time.sleep(0.1)
                        

        elif (node1,node2) not in edge_dict and (node2,node1) not in edge_dict:
            font = pygame.font.Font('freesansbold.ttf',number_size-1)
            pygame.draw.line(screen,not_choosen_color,node_position[node1], node_position[node2],4)
            show_weight(distance(node_position[node1],node_position[node2]),median_point(node_position[node1],node_position[node2]),font,Black)#erase weight
            pygame.draw.circle(screen,set_color[node1],node_position[node1],8)
            pygame.draw.circle(screen,set_color[node2],node_position[node2],8)
            pygame.display.update()
        
        r = 8 if N_edge_MST > 0 else 5

        color = set_color[node1] if N_edge_MST > 0 else Blue
        pygame.draw.circle(screen,color,node_position[node1],r)
        color = set_color[node2] if N_edge_MST > 0 else Blue
        pygame.draw.circle(screen,color,node_position[node2],r)
        show_weight_list(edge_list,first = edge_id+1)

        if not steps_mode:
            time.sleep(0.01)
            1+1
            

        edge_id += 1
        if edge_id == len(edge_list):
            time.sleep(0.3)
            pygame.draw.rect(screen,Black,(965,250,1100,270))
            font = pygame.font.Font('freesansbold.ttf',25)
            text = font.render("Add the edges",True,choose_edge_color)                        
            screen.blit(text,text.get_rect(center = (1100,270)))
            
            text = font.render("to the forest",True,choose_edge_color)                        
            screen.blit(text,text.get_rect(center = (1100,300)))

            font = pygame.font.Font('freesansbold.ttf',number_size-1)
            edge_id = 0
            for edge_index in best_edges_index:
                if edge_index == -1: continue

                weight,node1,node2 = edge_list[edge_index]

                # components already connected
                if F.Find(node1) == F.Find(node2): continue

                F.Union(node1, node2)
                N_edge_MST += 1

                edge_dict[(node1,node2)] = True

                edge_counter(N_edge_MST)
                
                Patriarch = F.Find(node1)
                node_ptr  = F.child_list(node1).head
                 
                pygame.draw.line(screen,set_color[Patriarch], node_position[node1], node_position[node2],5)
                pygame.display.update()
                time.sleep(0.1)


                while node_ptr is not None:
                    node = node_ptr.data
                    pos = node_position[node]
                    set_color[node] = set_color[Patriarch]
                    pygame.draw.circle(screen,set_color[Patriarch],pos,8)
                    
                    node_ptr = node_ptr.next
                    for neighbour in graph[node]:
                        if (node,neighbour) in edge_dict or (neighbour,node) in edge_dict:
                            pygame.draw.line(screen,set_color[Patriarch], node_position[node], node_position[neighbour],5)

            pygame.display.update()
            time.sleep(0.3)
            # creating new edge list (eliminating edges already in mst)
            new_edge_list = []
            for  weight, node1, node2 in edge_list:
                # if the node is not in mst
                if not (   (node1,node2) in edge_dict or (node2,node1) in edge_dict  ):
                    new_edge_list.append(( weight, node1, node2))
                    show_weight(distance(node_position[node1],node_position[node2]),median_point(node_position[node1],node_position[node2]),font,Cyan)
                edge_list = new_edge_list

            best_edges_index = list(-1  for _ in range(N))
            best_edges_W     = list(inf for _ in range(N))
            
            pygame.draw.rect(screen,Black,(965,250,1100,270))
            font = pygame.font.Font('freesansbold.ttf',22)
            text = font.render("Choose the shortest edge",True,choose_edge_color)                        
            screen.blit(text,text.get_rect(center = (1100,270)))
            
            text = font.render("for each tree",True,choose_edge_color)                        
            screen.blit(text,text.get_rect(center = (1100,300)))

            font = pygame.font.Font('freesansbold.ttf',number_size-1)
            time.sleep(0.5)

