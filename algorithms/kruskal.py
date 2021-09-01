def kruskal(graph,node_position, steps_mode = False):

    from math import hypot
    from algorithms.data_struct.UnionFind import union_find
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
    screnn_width = 1000
    screen = pygame.display.set_mode((screnn_width,screen_height))
    screen.fill((0,0,0))

    pygame.init()

    disjoint_set = union_find()
    edge_list = []
    
    #functions
    def distance(node1,node2):
        return int(hypot(node1[0]-node2[0], node1[1]-node2[1]))   



    def show_weight(weight,position,font,weight_color = weight_color ):
        text = font.render(str(weight),True,weight_color,10)
        screen.blit(text,position)

    def median_point(p1,p2):
        return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

    



    

    font = pygame.font.Font('freesansbold.ttf',number_size)


    for node in range(len(graph)):
        for neighbour in graph[node]:
            node1 = node_position[node]
            node2 = node_position[neighbour]
            pygame.draw.line(screen,(255,255,255), node1, node2,1)
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
    text = font.render("in MST",True,Cyan)                               # informative node       
    screen.blit(text,text.get_rect(center = (925,150)))

    pygame.draw.circle(screen,current_color,(830,175),10)
    text = font.render("current (atual)",True,current_color)                            # informative node   
    screen.blit(text,text.get_rect(center = (925,175)))

    pygame.display.update()


    mst  = list(False for _ in range(len(graph)))
    edge_dict = {}

    for node1 in len(graph):
        for node2 in graph[node1]:
            weight = distance(node1, node2)
            edge_list.append((weight,node1, node2))
    
    edge_list.sort()




    # animation loop
    nodes_in_tree = 1
    sorting = True
    Unions = False
    edge_id = 0


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
              

        if sorting:
            weight,node1,node2 = edge_list[edge_id]
            edge_id += 1
            
            pygame.display.update()
            continue
        if Unions:
            continue