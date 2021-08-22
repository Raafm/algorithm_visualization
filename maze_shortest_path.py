from data_struct.queue import queue
from graph.Maze_Dense import labirinth as maze   
import pygame,time,random
from graph.color import Green,Cyan,Blue,Lime,Yellow


pygame.init()


screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))




ROWS = len(maze)
COLS = len(maze[0])

predecessor =  list( list( ( -1 , -1 ) for _ in range(COLS) ) for _ in range(ROWS) )

White = (255,255,255)
Black = ( 0 , 0 , 0 )

Q = queue()

def remove_queue(i,j):
    maze[i][j] = Cyan
    pygame.draw.rect(screen ,  Cyan  , ( 50 + 5*i , 50 + 5*j , 5 , 5 ) ) 
    

def insert_queue(i,j):
    if i < 0 or j < 0 or i >99 or j > 99: return
    if maze[i][j] != Green:
        maze[i][j] = Blue
    pygame.draw.rect(screen ,  Blue  , ( 50 + 5*i , 50 + 5*j , 5 , 5 ) )
    
   




def display_maze():
    N = len(maze)
    print(N)
    for x in range(N):
        time.sleep(0.001)
        for y in range(N):
            pygame.draw.rect(screen ,  maze[x][y]  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
        pygame.display.update()

    #maze[0][1] = maze[0][2] = maze[0][3] = maze[0][4] = Yellow
    maze[99][95] = maze[99][96] = maze[99][97] = maze[99][98] = maze[99][99] = Green

    
    time.sleep(1)
    
    font = pygame.font.Font('freesansbold.ttf',15)
    text = font.render("Entry (Entrada).",True, Cyan)                        
    screen.blit(text,text.get_rect(center = (100,30)))

    font = pygame.font.Font('freesansbold.ttf',15)
    text = font.render("Exit (Saida)" ,True, Green)                         
    screen.blit(text,text.get_rect(center = (560,570)))

    pygame.display.update()

display_maze()

N_layer = 1
missing = 0

found = False

source = (0,0)
current = source
Q.insert(source)
see_neighbours = False
delay = 0.02
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

    if not see_neighbours and not found:

        if missing == 0:
            missing = N_layer
            N_layer = 0
            pygame.display.update()
            time.sleep(delay)

        if Q.not_empty():
            missing -= 1
            current = Q.pop()
            
        else:
            pause = True
            continue

        i,j = current
        
        if maze[i][j] == Green:
            
            font = pygame.font.Font('freesansbold.ttf',40)
            text = font.render("Found",True,(0,235,0))                   # informative node       
            screen.blit(text,text.get_rect(center = (860,50)))
            pygame.display.update()
            
            found = True
            continue

        remove_queue(i,j)
        see_neighbours = True
        

    if see_neighbours and not found:
        i,j = current
        if(       (i+1 < ROWS)             and   (maze[i+1][ j ] == Black or maze[i+1][ j ] == Green) ): insert_queue(i+1 ,  j ); Q.insert((i+1 ,  j )); N_layer += 1 ; predecessor[i+1][ j ] = ( i , j )
        if(        (0  <  i )              and   (maze[i-1][ j ] == Black or maze[i-1][ j ] == Green) ): insert_queue(i-1 ,  j ); Q.insert((i-1 ,  j )); N_layer += 1 ; predecessor[i-1][ j ] = ( i , j )
        if(       (j+1 < COLS)             and   (maze[ i ][j+1] == Black or maze[ i ][j+1] == Green) ): insert_queue( i  , j+1); Q.insert(( i  , j+1)); N_layer += 1 ; predecessor[ i ][j+1] = ( i , j )
        if(        (j  > 0 )               and   (maze[ i ][j-1] == Black or maze[ i ][j-1] == Green) ): insert_queue( i  , j-1); Q.insert(( i  , j-1)); N_layer += 1 ; predecessor[ i ][j-1] = ( i , j )
        
        see_neighbours = False

        time.sleep(0.001)

    if found:
        time.sleep(0.01)
        (x,y) = current
        if( current != source ):
            pygame.draw.rect(screen ,  Green  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
            x,y = predecessor[x][y]
            pygame.draw.rect(screen ,  Lime  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
            pygame.display.update()

            current = (x,y)

        if current == source:
            pygame.draw.rect(screen ,  Green  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
            pygame.display.update()
            pause = True
            found = False
            continue

        