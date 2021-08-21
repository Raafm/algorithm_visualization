from data_struct.queue import queue
from graph.Maze import labirinth as maze   
import pygame,time
from graph.color import Red,Cyan,Blue,Yellow 


pygame.init()


screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))




ROWS = len(maze)
COLS = len(maze[0])

White = (255,255,255)
Black = ( 0 , 0 , 0 )

Q = queue()

def remove_queue(i,j):
    maze[i][j] = Cyan
    pygame.draw.rect(screen ,  Cyan  , ( 50 + 5*i , 50 + 5*j , 5 , 5 ) ) 
    pygame.display.update()
    time.sleep(0.001)

def insert_queue(i,j):
    maze[i][j] = Blue
    pygame.draw.rect(screen ,  Blue  , ( 50 + 5*i , 50 + 5*j , 5 , 5 ) )
    pygame.display.update()
    time.sleep(0.001)




def display_maze():
    N = len(maze)


    for x in range(N):
        for y in range(N):
            pygame.draw.rect(screen ,  maze[x][y]  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )

    maze[0][0] = maze[0][1] = maze[0][2] = maze[0][3] = Yellow

    pygame.display.update()
    time.sleep(1.5)

    for k in range(5):
        pygame.draw.rect(screen , maze[99][k],(50,50,0,0))
    pygame.display.update() 
    time.sleep(1)


display_maze()

source = (0,0)
current = source
Q.insert(source)
see_neighbours = False
pause = True
running =  True
while running :

    # pygame stuff:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                   #exit pygame,
            running = False                          #exit() program


        
        if event.type == pygame.KEYDOWN:        
            if event.key == pygame.K_SPACE:     #press breakspace to pause or play
                pause = not pause   
                time.sleep(0.2)
    
    if pause:
        continue

    if not see_neighbours:
        if Q.not_empty():
            current = Q.pop()
            
        else:
            pause = True
        i,j = current
        if maze[i][j] == Yellow:
            continue
        remove_queue(i,j)
        see_neighbours = True
        

    if see_neighbours:
        i,j = current
        if(       (i+1 < ROWS)             and   maze[i+1][ j ] == Black ): insert_queue(i+1 ,  j ); Q.insert((i+1 ,  j ))
        if(        (0  <  i )              and   maze[i-1][ j ] == Black ): insert_queue(i-1 ,  j ); Q.insert((i-1 ,  j ))
        if(       (j+1 < COLS)             and   maze[ i ][j+1] == Black ): insert_queue( i  , j+1); Q.insert(( i  , j+1))
        if(        (j  > 0 )               and   maze[ i ][j-1] == Black ): insert_queue( i  , j-1); Q.insert(( i  , j-1))
        if( (i+1 < ROWS)  and (j+1 < COLS) and   maze[i+1][j+1] == Black ): insert_queue(i+1 , j+1); Q.insert((i+1 , j+1))
        if( (i+1 < ROWS)  and (j > 0)      and   maze[i+1][j-1] == Black ): insert_queue(i+1 , j-1); Q.insert((i+1 , j-1))
        if( (0 <  i) and (j+1 < COLS)      and   maze[i-1][j+1] == Black ): insert_queue(i-1 , j+1); Q.insert((i-1 , j+1))
        
        see_neighbours = False
    