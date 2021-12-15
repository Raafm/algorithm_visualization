from algorithms.data_struct.stack import stack
from graph.Maze_Dense import labirinth as maze   
import pygame,time,random
from graph.color import *


pygame.init()


screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))


delay = 0.005

ROWS = len(maze)
COLS = len(maze[0])

predecessor =  list( list( ( -1 , -1 ) for _ in range(COLS) ) for _ in range(ROWS) )

White = (255,255,255)
Black = ( 0 , 0 , 0 )

S = stack()

def remove_stack(i,j):
    maze[i][j] = Cyan
    pygame.draw.rect(screen ,  Dark_yellow, ( 50 + 5*i , 50 + 5*j , 5 , 5 ) ) 
    time.sleep(delay)

def insert_stack(i,j):
    if i < 0 or j < 0 or i >99 or j > 99: return
    if maze[i][j] != Green:
        maze[i][j] = Blue
    pygame.draw.rect(screen ,  Red  , ( 50 + 5*i , 50 + 5*j , 5 , 5 ) )
    
    pygame.display.update()




def display_maze():
    N = len(maze)

    for x in range(N):
        for y in range(N):
            pygame.draw.rect(screen ,  maze[x][y]  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
        pygame.display.update()

    #maze[0][1] = maze[0][2] = maze[0][3] = maze[0][4] = Yellow
    maze[99][95] = maze[99][96] = maze[99][97] = maze[99][98] = maze[99][99] = Green

    
    time.sleep(1)
    
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Entry (Entrada).",True, Cyan)                        
    screen.blit(text,text.get_rect(center = (100,30)))

    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Exit (Saida)" ,True, Green)                         
    screen.blit(text,text.get_rect(center = (560,570)))

    font = pygame.font.Font('freesansbold.ttf',40)
    text = font.render("in stack",True, Red)                      
    screen.blit(text,text.get_rect(center = (800,250)))

    
    font = pygame.font.Font('freesansbold.ttf',40)
    text = font.render("seen",True, Dark_yellow)                      
    screen.blit(text,text.get_rect(center = (800,350)))

    pygame.display.update()

display_maze()


found = False

source = (0,0)
current = source
S.insert(source)
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

    if not see_neighbours and not found:


        if S.not_empty():
           
            current = S.pop()
            
        else:
            pause = True
            continue

        i,j = current
        
        if maze[i][j] == Green:
            
            font = pygame.font.Font('freesansbold.ttf',40)
            text = font.render("Found",True,(0,235,0))                   # informative node       
            screen.blit(text,text.get_rect(center = (800,50)))
            pygame.display.update()
            
            found = True
            continue

        remove_stack(i,j)
        see_neighbours = True
        

    if see_neighbours and not found:
        i,j = current
        if(   (i+1 < ROWS)     and   (maze[i+1][ j ] == Black or maze[i+1][ j ] == Green) ): insert_stack(i+1 ,  j ) ; S.insert((i+1 ,  j )) ; predecessor[i+1][ j ] = ( i , j )
        if(    (0  <  i )      and   (maze[i-1][ j ] == Black or maze[i-1][ j ] == Green) ): insert_stack(i-1 ,  j ) ; S.insert((i-1 ,  j )) ; predecessor[i-1][ j ] = ( i , j )
        if(   (j+1 < COLS)     and   (maze[ i ][j+1] == Black or maze[ i ][j+1] == Green) ): insert_stack( i  , j+1) ; S.insert(( i  , j+1)) ; predecessor[ i ][j+1] = ( i , j )
        if(    (j  > 0 )       and   (maze[ i ][j-1] == Black or maze[ i ][j-1] == Green) ): insert_stack( i  , j-1) ; S.insert(( i  , j-1)) ; predecessor[ i ][j-1] = ( i , j )
       
        see_neighbours = False

        time.sleep(0.001)

    if found:
        time.sleep(0.01)
        (x,y) = current
        if( current != source ):
            pygame.draw.rect(screen ,  Lime  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
            x,y = predecessor[x][y]
            pygame.draw.rect(screen ,  Green  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
            pygame.display.update()

            current = (x,y)

        if current == source:
            pygame.draw.rect(screen ,  Green  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
            pygame.display.update()
            pause = True
            found = False
            continue

        