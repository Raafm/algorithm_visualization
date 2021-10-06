def dfs(graph, node_position, source = 0,steps_mode = False):
    
    from algorithms.data_struct.stack import stack
    import pygame,time
    from algorithms.colors import Springgreen,Cyan,Red,Green,Yellow,Lime,Black,White,Flame,Navy
    process_list = stack()
    seen = list(False for x in range(len(graph)))                                   # haven't seen anyone yet
    parent = list(-1 for _ in range(len(graph))) 

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


    font = pygame.font.Font('freesansbold.ttf',35)
    text = font.render("DFS",True,Dark_yellow)                   # informative node       
    screen.blit(text,text.get_rect(center = (1050,50)))
    
    font = pygame.font.Font('freesansbold.ttf',25)
    
    pygame.draw.circle(screen,Red, (1000,185),10)
    text = font.render("memory stack",True,Red)
    screen.blit(text,text.get_rect(center = (1110,183)))                             # informative node   
    text = font.render("(pilha de processamento)",True,Red)
    screen.blit(text,text.get_rect(center = (1080,220)))

    pygame.draw.circle(screen,  Yellow,(1000,250)  ,10 )
    pygame.draw.circle(screen,  Dark_yellow, (1000,250)  ,7 )
    text = font.render("seen",True,Dark_yellow,20)
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
            
            current = process_list.pop()
            seen[current] = True
            
            pygame.draw.circle(screen, Lime , node_position[current] , 6)
            pygame.display.update()
            time.sleep(0.5)

            for neighbour in graph[current]:
                if seen[neighbour]:
                    time.sleep(0.02)
                    continue
                else:
                 
                    pygame.draw.circle(screen,  Red, node_position[neighbour] , 5)
                    pygame.display.update()
                    time.sleep(0.3)
                    parent[neighbour] = current 
                    process_list.insert(neighbour)
                    seen[neighbour] = True



            if process_list.not_empty():
                next_node = process_list.top()
                pred = parent[next_node] #predecessor
                pygame.draw.line(screen,Yellow,node_position[pred],node_position[next_node],3)
                pygame.draw.circle(screen,  Yellow, node_position[pred] ,8 )
                pygame.draw.circle(screen,  Dark_yellow, node_position[pred] ,6 )

            pygame.draw.circle(screen,  Yellow, node_position[current] ,8 )
            pygame.draw.circle(screen,  Dark_yellow, node_position[current] ,6 )
            pygame.display.update()
            
