def kruskal(graph,node_position, steps_mode = False):

    from math import hypot
    from algorithms.data_struct.ChildUnionFind import UnionFind,linked_list
    import pygame,time
    
    Black	     =	    (0,0,0)
    White	     =	    (255,255,255)
    Red  	     =	    (255,0,0)
    Dark_red     =     	(150,0,0)
    Lime	     =	    (0,255,0)
    Blue	     =	    (0,0,200)
    Yellow	     =	    (255,255,0)
    Dark_yellow  =      (250,200,0)
    Flame        =      (226,88,34)
    Cyan 	     =	    (0,255,255)
    Magenta	     =	    (255,0,255)
    Gray	     =	    (128,128,128)
    Dark_gray    =      (50, 50, 50)
    Maroon 	     =	    (128,0,0)
    Olive  	     =	    (128,128,0)
    Green  	     =	    (0,180,0)
    Purple 	     =	    (128,0,128)
    Teal	     =	    (0,128,128)
    Navy	     =	    (0,0,128)
    Castanho	 =	    (165,42,42)
    Light_sky    = 		(135,206,250)
    Carmesim	 =	    (220,20,60)
    Cream        =	    (245,255,250)
    Some_grey    =  	(112,128,144)
    Light_grey   =  	(119,136,153)
    Melada	     =      (240,255,240)
    Orange	     =      (255,165,0)
    Springgreen	 =      (0,255,127)
    Dark_grey    =      (41,41,41)

    
    list_colors = [
        Purple 	    ,
        Cyan 	    ,
        Carmesim	,
        Lime        ,
        Orange	    ,
        Springgreen	,
        Melada	    ,
        Light_sky   ,
        Dark_gray   ,
        Maroon 	    ,
        Olive  	    ,
        Green  	    ,
        Cream       ,
        Teal	    ,
        Dark_red    ,
        Castanho	,	
        Some_grey   ,  	
        Light_grey  , 
        Navy	    ,
        Magenta	    , 	
        Gray	    ,  
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
    screnn_width = 1000
    screen = pygame.display.set_mode((screnn_width,screen_height))
    screen.fill((0,0,0))

    pygame.init()

    disjoint_set = UnionFind(len(graph))
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

    
    def show_weight_list(edge_list,first = 0):
        pygame.draw.rect(screen,Light_grey,(730,0,70,1000))
        font = pygame.font.Font('freesansbold.ttf',number_size-1)
        for edge_id in range(len(edge_list)-first): 
            show_weight(edge_list[edge_id+first],(730,15*edge_id+20),font)
        pygame.display.update()



    font = pygame.font.Font('freesansbold.ttf',number_size)


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
    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("Kruskal",True,Cyan)                        
    screen.blit(text,text.get_rect(center = (900,70)))


    pygame.draw.circle(screen,Cyan,(830,150),10)
    text = font.render("in MST",True,Cyan)                         
    screen.blit(text,text.get_rect(center = (925,150)))

    pygame.draw.circle(screen,current_color,(830,175),10)
    text = font.render("current",True,current_color)                  
    screen.blit(text,text.get_rect(center = (925,175)))
    text = font.render("(atual)",True,current_color)                  
    screen.blit(text,text.get_rect(center = (925,205)))

    pygame.display.update()

    time.sleep(1)

    mst  = list(False for _ in range(len(graph)))
    edge_dict = {}


    font = pygame.font.Font('freesansbold.ttf',number_size-1)
    for node1 in range(len(graph)):
        for node2 in graph[node1]:
            weight = distance(node_position[node1], node_position[node2])
            if (weight,node2,node1) in edge_list: continue
            edge_list.append((weight,node1, node2))
    
    show_weight_list(edge_list)

    time.sleep(1)
    edge_list.sort()
    pygame.draw.rect(screen,Light_grey,(730,0,70,1000))
    pygame.display.update()

    time.sleep(2)

    for edge_id in range(len(edge_list)): 
        show_weight(edge_list[edge_id],(730,15*edge_id+20),font)
        pygame.display.update()
        time.sleep(0.001)
  

    pygame.display.update()

    # animation loop
    nodes_in_tree = 1
    sorting = True
    Unions = False
    edge_id = 0


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


        if edge_id == len(edge_list): continue
        weight,node1,node2 = edge_list[edge_id]
        pygame.draw.line(screen,cur_edge_color,node_position[node1], node_position[node2],2)
        pygame.display.update()        


        if pause:
            continue
        

        if steps_mode: #pause every step of the algorithm
            pause = True  #when this iteration ends,the animation is paused              
        

        

        if not steps_mode:
            time.sleep(0.5)
        
        pygame.draw.line(screen,Black,node_position[node1], node_position[node2],2)
        

        if disjoint_set.Find(node1) != disjoint_set.Find(node2):

            pygame.draw.line(screen,choose_edge_color,node_position[node1], node_position[node2],5)
            pygame.draw.circle(screen,choose_edge_color,node_position[node1],8)
            pygame.draw.circle(screen,choose_edge_color,node_position[node2],8)
            pygame.display.update()
            if not steps_mode: time.sleep(0.1)

            disjoint_set.Union(node1,node2)
        
        elif (node1,node2) not in edge_dict and (node2,node1) not in edge_dict:
            pygame.draw.line(screen,not_choosen_color,node_position[node1], node_position[node2],2)
            show_weight(distance(node_position[node1],node_position[node2]),median_point(node_position[node1],node_position[node2]),font,Black)#erase weight
            pygame.draw.circle(screen,choose_edge_color,node_position[node1],8)
            pygame.draw.circle(screen,choose_edge_color,node_position[node2],8)
            pygame.display.update()
            if not steps_mode: time.sleep(0.1)

        edge_dict[(node1,node2)] = True
        show_weight_list(edge_list,first=edge_id+1)
        if not steps_mode:
            time.sleep(0.5)
     
        edge_id += 1
        if edge_id == len(edge_list):
            pause = True