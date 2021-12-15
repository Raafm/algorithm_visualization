IslandsMap = []
if __name__ == "__main__":
    import pygame, time, random
    pygame.init()
    screen_height = 700
    screen_width = 1200
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill((0,0,0))

    precision  = 2
    


    white = (255,255,255)
    black = ( 0 , 0 , 0 )

    N = len(IslandsMap)
        
        
    def DFS(x,y):
        i,j = y,x
        pygame.draw.rect(screen ,  (  255  , 255  , 255 ) , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
        IslandsMap[N-1-i][j] = ( 255 , 255 , 255 )
        pygame.display.update()
        
        if(       (i+1 < N)             and   IslandsMap[N -1- (i+1)][ j ] == (0,0,0) ):   DFS(  j  , i+1  ); 
        if(        (0  <  i )           and   IslandsMap[N -1- (i-1)][ j ] == (0,0,0) ):   DFS(  j  , i-1  ); 
        if(       (j+1 < N)             and   IslandsMap[N -1- ( i )][j+1] == (0,0,0) ):   DFS( j+1 ,  i   ); 
        if(        (j  > 0 )            and   IslandsMap[N -1- ( i )][j-1] == (0,0,0) ):   DFS( j-1 ,  i   ); 
        if( (i+1 < N)  and (j+1 < N)    and   IslandsMap[N -1- (i+1)][j+1] == (0,0,0) ):   DFS( j+1 , i+1  ); 
        if( (i+1 < N)  and (j > 0)      and   IslandsMap[N -1- (i+1)][j-1] == (0,0,0) ):   DFS( j-1 , i+1  ); 
        if( (0 <  i) and (j+1 < N)      and   IslandsMap[N -1- (i-1)][j+1] == (0,0,0) ):   DFS( j+1 , i-1  ); 
        if( (0 <  i) and ( j  >  0 )    and   IslandsMap[N -1- (i-1)][j-1] == (0,0,0) ):   DFS( j-1 , i-1  ); 


    def display_maze():

        for k in range(N):
            IslandsMap[0][k] = IslandsMap[k][0] = IslandsMap[k][N-1] = IslandsMap[N-1][k] = (255,255,255)

        for x in range(N):
            j = x
            for y in range(N):
                i = y
                pygame.draw.rect(screen ,  IslandsMap[ N-1 - i][j]  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )


        pygame.display.update()
        time.sleep(2)

        IslandsMap[N-1][0] = IslandsMap[N-1][1] =  IslandsMap[N-1][2] = IslandsMap[N-1][3] =IslandsMap[N-1][4] =  (0,0,0)
        for k in range(5):
            pygame.draw.rect(screen , IslandsMap[N-1][k],(50,50,0,0))
        pygame.display.update() 





    def paint_position(x,y,wall):

        i,j = y,x

        if i < 0 or j < 0 or i > N or j > N:
            return 

        if IslandsMap[N-1-i][j] == ( 255 , 255 , 255 ):
            return

        if wall:
            IslandsMap[N -1- i][j] = (255,255,255)
            DFS(x,y)
        else: 
            IslandsMap[N -1- i][j] = ( 0 , 0 , 0 )

        pygame.draw.rect(screen ,  IslandsMap[ N -1- i][j]  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
        pygame.display.update()








    def cur_position(x,y,wall):

        i,j = y,x

        if IslandsMap[N-1-i][j] == ( 255 , 255 , 255 ):
            return

    
        pygame.draw.rect(screen ,  (  0  , 255  , 0 ) , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
        pygame.display.update()




    x = y = 0

    right = left = up = down = False

    running =  True
    wall  = False           # color

    display_maze()

    while running: 
    
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            
            if event.type == pygame.KEYDOWN:            
                
        
                if event.key == pygame.K_SPACE:             # click breakspace for change color
                    wall = not wall                     # if it is paused, click breakspace for play(resume)
                    #DFS(x,y)
                    time.sleep(0.1)
        
            

        
                if event.key == pygame.K_RIGHT:
                    right = True
                    
                if event.key == pygame.K_UP:   
                    up = True
        
                if event.key == pygame.K_DOWN:
                    down = True

                if event.key == pygame.K_LEFT: 
                    left = True
            
                
        if right:   

            for x0 in range(x,x+precision):
                paint_position(x0,y,wall)

            x += ( precision if ( x < N-1-precision ) else 0 )


        if up:   

            for y0 in range(y,y-precision,-1):
                paint_position(x,y0,wall)

            y -= ( precision if ( y > precision  ) else 0 )


        if down:
            
            for y0 in range(y,y+precision):
                paint_position(x,y0,wall)

            y += ( precision if ( y < N-1-precision ) else 0 )


        if left:
            
            for x0 in range(x,x-precision,-1):
                paint_position(x0,y,wall)

            x -= ( precision if ( x > precision  ) else 0 )



        cur_position(x,y,wall)


        right = left = up = down = False



    with open("algorithm_visualization\graph\Create Graph\\temp.txt","w") as file:
        file.write("IslandsMap = [\n")
        for lista in IslandsMap:
            file.write(str(lista)+",\n")
        file.write("\n]")