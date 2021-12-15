import pygame, time, random


pygame.init()


screen_height = 700
screen_width = 1200
screen = pygame.display.set_mode((screen_width,screen_height))

screen.fill((0,0,0))


precision  = 1
N = 128


white = (255,255,255)
black = ( 0 , 0 , 0 )

labirinth = list(  list( (0,0,0) for _ in range(N) )  for _ in range(N))



def display_maze():

    for k in range(N):
        labirinth[0][k] = labirinth[k][0] = labirinth[k][N-1] = labirinth[N-1][k] = (255,255,255)

    for x in range(N):
        j = x
        for y in range(N):
            i = y
            pygame.draw.rect(screen ,  labirinth[ N-1 - i][j]  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )


    pygame.display.update()
    time.sleep(2)

    labirinth[N-1][0] = labirinth[N-1][1] =  labirinth[N-1][2] = labirinth[N-1][3] =labirinth[N-1][4] =  (0,0,0)
    for k in range(5):
        pygame.draw.rect(screen , labirinth[N-1][k],(50,50,0,0))
    pygame.display.update() 





def paint_position(x,y,wall):

    i,j = y,x

    if i < 0 or j < 0 or i > N or j > N:
        return 

    if labirinth[N-1-i][j] == ( 255 , 255 , 255 ):
        return

    if wall:
        labirinth[N -1- i][j] = (255,255,255)
    else: 
        labirinth[N -1- i][j] = ( 0 , 0 , 0 )

    pygame.draw.rect(screen ,  labirinth[ N -1- i][j]  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
    pygame.display.update()








def cur_position(x,y,wall):

    i,j = y,x

    if labirinth[N-1-i][j] == ( 255 , 255 , 255 ):
        return

    if wall:
        pygame.draw.rect(screen ,  (  0  , 150  , 0 ) , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
    else:
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
                time.sleep(0.1)
    
        

    
            if event.key == pygame.K_RIGHT:
                right = True
                
            if event.key == pygame.K_UP:   
                up = True
    
            if event.key == pygame.K_DOWN:
                down = True

            if event.key == pygame.K_LEFT: 
                left = True
        

#        if event.type == pygame.KEYUP:
#
#            if event.key == pygame.K_RIGHT:
#                right = False
#                
#            if event.key == pygame.K_UP:   
#                up = False
#    
#            if event.key == pygame.K_DOWN:
#                down = False
#
#            if event.key == pygame.K_LEFT: 
#                left = False
        
            
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



print('\nlabirinth = ', labirinth)