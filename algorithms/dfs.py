def dfs(screen, node_list,graph,source = 0, steps_mode = False):

    import pygame,time
    from data_struct.stack import stack

    process_stack = stack()
    seen = list(False for x in range(len(graph)))                                   # haven't seen anyone yet

    screen_height = 700
    screnn_width = 1000
    screen = pygame.display.set_mode((screnn_width,screen_height))

    screen.fill((0,0,0))

    pygame.init()

    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("DFS",True,(0,255,0))                   # informative node       
    screen.blit(text,text.get_rect(center = (950,50)))

    font = pygame.font.Font('freesansbold.ttf',15)
    pygame.draw.circle(screen,(255,0,0), (850,200),10)
    text = font.render("memory stack",True,(255,0,0))
    screen.blit(text,text.get_rect(center = (915,200)))                             # informative node   
    text = font.render("(pilha de processamento)",True,(255,0,0))
    screen.blit(text,text.get_rect(center = (910,220)))

    pause = True            # doesn't start until press play (breakspace)
    current = source
    process_stack.insert(source)

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                quit()                          #exit() program


            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not pause
                    time.sleep(0.2)
        
        if pause:
            continue
        
        if steps_mode: #pause every step of the algorithm
            pause = True  #when this iteration ends,the animation is paused

        if process_stack.not_empty(): 

            
            pygame.draw.circle(screen,  (255,255,255), node_list[current] , 10)
            pygame.draw.circle(screen,  (0,255,0), node_list[current] , 5)

            current = process_stack.pop()
            seen[current] = True

            pygame.draw.circle(screen,  (0,255,0), node_list[current] , 10)

            for neighbour in graph[current]:
                if seen[neighbour]:
                    continue
                else:
                    pygame.draw.circle(screen,  (255,0,0), node_list[neighbour] , 10)
                    process_stack.insert(neighbour)


        pygame.display.update()
        time.sleep(0.05)