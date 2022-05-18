def BORUVKA(graph,position, N):
    from algorithms.data_struct.RodUnionFind import UnionFind,linked_list
    from math import inf,hypot


    def distance(a, b):
        return hypot(a, b)

    #Crie uma floresta F com cada nó do grafo
    N_trees = N
    
    F = UnionFind(N)
    
    patriarchs = F.patriarch_list(python_list = True)
    edges = []
    while N_trees > 1:
        
        for patriarch in patriarchs:
            component = F.child_list(patriarch,python_list = True)
            w = inf
            edge = (-1,-1)
            for node in component:    

            
                for neighbour in graph[node]:
                    if neighbour == -1: continue

                    patriarch1 = F.find(node)
                    patriarch2 = F.find(neighbour)

                    if patriarch1 == patriarch2:
                        continue

                    W = distance(position[node],position[neighbour])

                    if W < w: w = W;edge = (node,neighbour)

            edges.append(edge) # best edge of this component

        for edge in edges:
            node1,node2 = edge
            F.Union(node1,node2)

        

def boruvka(graph,node_position, steps_mode = False):

    from math import hypot,inf 
    from algorithms.data_struct.RodUnionFind import UnionFind,linked_list
    import pygame,time
    from threading import Thread, Lock,Condition, Barrier
    
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
    choose_edge_color = White
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
    font = pygame.font.Font('freesansbold.ttf',number_size-1)

  
    F = UnionFind(len(graph))
    edge_dict = {}
        
    edge_list = []
    set_color = list( list_colors[x%len(list_colors)] for x in range(len(graph)))

    N_threads = 3
    display_mutex = Lock()
    F_mutex = Lock()
    mutex_edges = Lock()
    barrier = Barrier(N_threads+1)

    #functions
    def distance(node1,node2):
        return int(hypot(node1[0]-node2[0], node1[1]-node2[1]))   
    def show_weight(weight,position,font,weight_color = weight_color ):
        text = font.render(str(weight),True,weight_color,10)
        screen.blit(text,position)
    def median_point(p1,p2):
        return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
    def edge_counter(N_edge_MST):
        pygame.draw.rect(screen,Black,(1000,400,200,200))
        font = pygame.font.Font('freesansbold.ttf',20)
        text = font.render("edges in MST: " + str(N_edge_MST),True,choose_edge_color)                        
        screen.blit(text,text.get_rect(center = (1085,450)))
    def choose_sign():
        pygame.draw.rect(screen,Black,(965,250,1100,270))
        font = pygame.font.Font('freesansbold.ttf',22)
        text = font.render("Choose the shortest edge",True,choose_edge_color)                        
        screen.blit(text,text.get_rect(center = (1100,270)))
        
        text = font.render("for each tree",True,choose_edge_color)                        
        screen.blit(text,text.get_rect(center = (1100,300)))

        font = pygame.font.Font('freesansbold.ttf',number_size-1)
    def add_sign():
        pygame.draw.rect(screen,Black,(965,250,1100,270))
        font = pygame.font.Font('freesansbold.ttf',25)
        text = font.render("Add the edges",True,choose_edge_color)                        
        screen.blit(text,text.get_rect(center = (1100,270)))
        
        text = font.render("to the forest",True,choose_edge_color)                        
        screen.blit(text,text.get_rect(center = (1100,300)))

        font = pygame.font.Font('freesansbold.ttf',number_size)
    def end_algorithm(N_edge_MST):        
        font = pygame.font.Font('freesansbold.ttf',number_size)

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
        display_mutex.acquire()
        pygame.display.update()
        display_mutex.release()
    def paint_component(component_list,color,show = False, Time = 0,animation = False):
        for node in component_list:
            
            for neighbour in graph[node]:
                #if F.Find(node) != F.Find(neighbour) : continue
                if (neighbour,node) in edge_dict or (node, neighbour) in edge_dict:
                    # paint also the edges
                    pygame.draw.line(screen,color, node_position[node], node_position[neighbour],5)
                    pos = node_position[neighbour]
                    pygame.draw.circle(screen,color,pos,8)
                    if animation: 
                        time.sleep(Time)
                        display_mutex.acquire()
                        pygame.display.update()
                        display_mutex.release()         
            
        
        for node in component_list:
            pygame.draw.circle(screen,color,node_position[node],8)
        if show: 
            display_mutex.acquire()
            pygame.display.update()
            display_mutex.release()          
        if Time: 
            time.sleep(Time)
            1+1

    def find_best_edge(component):
        paint_component(component,White)
        display_mutex.acquire()
        pygame.display.update()
        display_mutex.release()
        time.sleep(0.1)
        
        candidates = [] # edges that can be selected by this component
        for node in component:    

            for neighbour in graph[node]:

                # if they are in the same component we don't want the edge
                F_mutex.acquire()
                same_component = F.Find(node) == F.Find(neighbour)
                F_mutex.release()
                if not same_component: 

                    W = distance(node_position[node],node_position[neighbour])
                    candidates.append((W,node,neighbour))
                    pygame.draw.line(screen,cur_edge_color,node_position[node], node_position[neighbour],2)
                    display_mutex.acquire()
                    pygame.display.update()
                    display_mutex.release()
                    time.sleep(0.01)
        time.sleep(0.3)

        edge = min(candidates)
        
        edge = edge[1],edge[2]

        return edge,candidates

    
    N_edge_MST = 0
    pause = False
    N = len(graph)

    def find_best_edges(patriarchs):
        print("threads:",N_edge_MST)
        print("entrou")
        for patriarch in patriarchs:
            
            F_mutex.acquire()
            component = F.child_list(patriarch,python_list = True)
            F_mutex.release()

            edge,candidates = find_best_edge(component)
            
            mutex_edges.acquire()
            edges.append(edge)
            mutex_edges.release()

            if N_edge_MST > 0:
                paint_component(component,set_color[patriarch])
            else:
                pygame.draw.circle(screen,Blue,node_position[patriarch],8)
                

            pygame.draw.line(screen,choose_edge_color,node_position[edge[0]], node_position[edge[1]],2)
            
            display_mutex.acquire()
            pygame.display.update()
            display_mutex.release()
            
            time.sleep(0.2)

            for edge in candidates:
                _,u,v = edge
                
                if (u,v) not in edges and (v,u) not in edges:
                    
                    pygame.draw.line(screen,not_choosen_color,node_position[u], node_position[v],4)
                    pygame.draw.line(screen,Dark_grey, node_position[u], node_position[v],1)
                else:
                    pygame.draw.line(screen,choose_edge_color,node_position[u], node_position[v],2)
                    

            display_mutex.acquire()
            pygame.display.update()
            display_mutex.release()

        print("esperando barreira")
        
        barrier.wait()        
        print("passou barreira")


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
    
    display_mutex.acquire()
    pygame.display.update()
    display_mutex.release()

    time.sleep(1)

    #show information
    font = pygame.font.Font('freesansbold.ttf',40)
    text = font.render("Multithread Borůvka",True,choose_edge_color)                        
    screen.blit(text,text.get_rect(center = (1000,70)))


    display_mutex.acquire()
    pygame.display.update()
    display_mutex.release()

    time.sleep(1.5)

    
    pygame.draw.rect(screen,Black,(1020,220,200,70))

    display_mutex.acquire()
    pygame.display.update()
    display_mutex.release()


    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("edges in MST: 0",True,choose_edge_color)                        
    screen.blit(text,text.get_rect(center = (1085,450)))
    display_mutex.acquire()
    pygame.display.update()
    display_mutex.release()
    time.sleep(1.5)

    # animation loop
   


    font = pygame.font.Font('freesansbold.ttf',22)
    text = font.render("Choose the shortest edge",True,choose_edge_color)                        
    screen.blit(text,text.get_rect(center = (1100,270)))
    
    text = font.render("for each tree",True,choose_edge_color)                        
    screen.blit(text,text.get_rect(center = (1100,300)))
    display_mutex.acquire()
    pygame.display.update()
    display_mutex.release()
    time.sleep(1)


    while N_edge_MST < N-1:
                        
            # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                quit()                          #exit() program
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_SPACE:     #press breakspace to pause or play
                    pause = not pause; time.sleep(0.2)
        if pause:continue

        patriarchs = []
        for P in range(N):
            if F.Find(P) == P:
                patriarchs.append(P)

        edges = []
        choose_sign()
        time.sleep(0.5)

        t1 = Thread(target = find_best_edges,args = (patriarchs[:len(patriarchs)//3],))
        t2 = Thread(target = find_best_edges,args = (patriarchs[len(patriarchs)//3:2*len(patriarchs)//3],)) 
        t3 = Thread(target = find_best_edges,args = (patriarchs[2*len(patriarchs)//3:],)) 
        t1.start()
        t2.start()
        t3.start()
        #find_best_edges(patriarchs)
        barrier.wait()
        
        time.sleep(0.5)
        add_sign()
        time.sleep(1)
        
        for edge in edges:

            # pygame stuff:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()                   #exit pygame,
                    quit()                          #exit() program
            

            node1,node2 = edge
            
            print(node1,node2)
            F.Union(node1,node2)
            
            edge_dict[(edge)] = True
            
            if (node2,node1) in edge_dict:continue
            N_edge_MST += 1
            edge_counter(N_edge_MST)
            pygame.draw.line(screen,set_color[F.Find(node1)], node_position[node1], node_position[node2],5)
            pygame.display.update()
            time.sleep(0.05)

        for Patriarch in range(N):
            if Patriarch != F.Find(Patriarch): continue
            if F.reference[Patriarch] is None: print("not a patriarch:",Patriarch);continue
            
            while pause:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()                   #exit pygame,
                        quit()                          #exit() program
                    if event.type == pygame.KEYDOWN:        
                        if event.key == pygame.K_SPACE:     #press breakspace to pause or play
                            pause = not pause; time.sleep(0.2)
            print("patriarca:",Patriarch)
            print("set:",F.child_list(Patriarch,python_list = True))

            # paint all set:
            component_color = set_color[Patriarch]  
            paint_component(component_list = F.child_list(Patriarch, python_list = True),color = component_color,show=True,Time = 0.005, animation= False)
            time.sleep(0.1)
        
        time.sleep(1.5)
    
    time.sleep(1)
    end_algorithm(N_edge_MST)
    while True:
                    # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                quit()                          #exit() program
