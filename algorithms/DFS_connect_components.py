
def dfs_connected_components( graph, node_position, source=0, speed = 0):
    import pygame,time,random
    from algorithms.data_struct.stack import stack

   
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

    pygame.init()

    forget = (1,0,0)

    screen_height = 700
    screnn_width = 1000
    screen = pygame.display.set_mode((screnn_width,screen_height))

    screen.fill((0,0,0))


    memory_color  = Red
    current_color = Flame
    visited_color = Yellow
    node_color = Blue
    source_color = Blue
    node_radius = source_radius = 5




    def memorize(node,Time = 0.3,show=True):

        if Time == 0:
            Time = 0.1

        pygame.draw.circle(screen,memory_color,node_position[node] , 7)

        if show:
            pygame.display.update()
            time.sleep(Time)



    def visit(node,Time,show=True):
        if Time == 0:
            Time = 0.1
        pygame.draw.circle(screen,current_color,node_position[node],7)

        if show:
            pygame.display.update()
            time.sleep(Time)



    def visited(node,Time,show=True):
        if Time == 0:
            Time = 0.1

        pygame.draw.circle(screen,  (255,255,255), node_position[node] , 7)
        pygame.draw.circle(screen,visited_color,node_position[node],5)


        if show:
            pygame.display.update()
            time.sleep(Time)



    def mark(node,color,radius):

        pygame.draw.circle(screen, color, node_position[node] , radius)


    def print_component(component_dict,component_color,SP):

        for node in component_dict:
            mark(node,Black,6)
            mark(node,component_color[SP],5)
        pygame.display.update()



    mark(source,(0,205,205),12)


    if speed == 0:
        Time = 0
    else:Time = 1/speed
    # informative test:

    N_components = 0
    
    component_color = [
        
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
        Navy	    ,  	
        Light_grey  , 
        Magenta	    , 	
        Gray	    , 
        Purple 	    , 
    ]
    SP = 0


    font = pygame.font.Font('freesansbold.ttf',22)
    text = font.render("count",True,Dark_yellow)                        
    screen.blit(text,text.get_rect(center = (920,50)))
    
    font = pygame.font.Font('freesansbold.ttf',18)
    text = font.render("connected components",True,Dark_yellow)                        
    screen.blit(text,text.get_rect(center = (890,70)))

    font = pygame.font.Font('freesansbold.ttf',18)
    pygame.draw.circle(screen,memory_color, (845,220),7)
    text = font.render("memory stack",True,memory_color)
    screen.blit(text,text.get_rect(center = (920,220)))                             
    text = font.render("(pilha de processamento)",True,memory_color)
    screen.blit(text,text.get_rect(center = (890,245)))

    font = pygame.font.Font('freesansbold.ttf',20)


    pygame.draw.circle(screen,  (255,255,255), (845,170) , 7)
    pygame.draw.circle(screen,visited_color,(845,170),5)
    text = font.render("seen (visto)",True,visited_color)                               # informative node       
    screen.blit(text,text.get_rect(center = (925,170)))

    pygame.draw.circle(screen,current_color,(845,195),7)
    text = font.render("current (atual)",True,current_color)                            # informative node   
    screen.blit(text,text.get_rect(center = (925,195)))




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


    pause = True
    current = source
    process_stack =  stack()
    seen = list(False for _ in range(len(graph)))
    
    process_stack.insert(source)
    displayed = False

    component_dict = {}

    node = 0
    
    while True :

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

        
        # if we still have  nodes to see
        if node < len(graph): 


            # still in the same component
            if process_stack.not_empty():
                
                if not displayed:
                    font = pygame.font.Font('freesansbold.ttf',20)
                    pygame.draw.rect(screen, component_color[SP], (862,327 , 70, 25))
                    text = font.render("DFS",True,Dark_yellow)                        
                    screen.blit(text,text.get_rect(center = (895,340)))
                    displayed = True

                current = process_stack.pop()
                component_dict[current] = True
            

            # new connected components
            elif not seen[node]:
            
                
                print(component_dict)

                print_component(component_dict,component_color,SP)
                SP = SP+1 if SP < len(component_color)-1 else 0 

                component_dict.clear()


                N_components += 1
             
                displayed = False
                font = pygame.font.Font('freesansbold.ttf',20)
             
                pygame.draw.rect(screen, Black, (800,350 ,300, 100))
                pygame.draw.rect(screen, Black, (862,327 , 70, 25))
                text = font.render("N° components = " + str(N_components) ,True,  component_color[SP])                   # informative node       
                screen.blit(text,text.get_rect(center = (895,400)))
                pygame.display.update()

                current = node
                component_dict[current] = True
                time.sleep(1)
                

            # searching next component
            else:
                node += 1
 

            #  iteration of dfs:
            if not seen[current]:

                visit(current,Time)

                seen[current] = True
                

                for neighbour in graph[current]:

                    if seen[neighbour]:
                        continue
                    
                    else:
                        memorize(neighbour,Time)
                        process_stack.insert(neighbour)


                visited(current,Time)


            pygame.display.update()

        else: #node ==len(graph)
            N_components += 1
            font = pygame.font.Font('freesansbold.ttf',20)
            
            pygame.draw.rect(screen, Black, (800,350 ,300, 100))
            text = font.render("N° components = " + str(N_components) ,True,  component_color[SP])                   # informative node       
            screen.blit(text,text.get_rect(center = (895,400)))
            print_component(component_dict,component_color,SP)
            pygame.display.update()
            pause = True





if __name__ == "__main__":
    source = 0

    from test_graph import graph,node_position,edge_dict

    

    dfs_connected_components( graph,node_position,source,speed = 0)