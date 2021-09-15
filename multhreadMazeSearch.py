from algorithms.data_struct.queue import queue
from graph.Maze_Dense import labirinth as maze   
import pygame,time
from graph.color import *
from threading import Thread,Lock



pygame.init()


screen_height = 700
screen_width = 1000
screen = pygame.display.set_mode((screen_width,screen_height))

screen.fill((0,0,0))




ROWS = len(maze)
COLS = len(maze[0])

White = (255,255,255)
Black = ( 0 , 0 , 0 )


def remove_queue(i,j,color):
    if maze[i][j] != Lime:

        maze[i][j] = color
        pygame.draw.rect(screen ,  color  , ( 50 + 5*i , 50 + 5*j , 5 , 5 ) ) 
    

def insert_queue(i,j,color):
    if i < 0 or j < 0 or i >99 or j > 99: return
    if maze[i][j] != Lime:
        if maze[i][j] != Green:
            maze[i][j] = color
        pygame.draw.rect(screen ,  color  , ( 50 + 5*i , 50 + 5*j , 5 , 5 ) )
    
   




def display_maze():
    N = len(maze)
    print(N)
    maze[ROWS//2][COLS//2] = maze[ROWS//2 +1][COLS//2 +1] = maze[ROWS//2 +1][COLS//2] = maze[ROWS//2][COLS//2 +1] = Green
    for x in range(N):
        time.sleep(0.01)
        for y in range(N):
            pygame.draw.rect(screen ,  maze[x][y]  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
        pygame.display.update()


    time.sleep(1)
    
    
    font = pygame.font.Font('freesansbold.ttf',25)
    text = font.render("Find shortest path",True, Lime)                      
    screen.blit(text,text.get_rect(center = (800,100)))

    font = pygame.font.Font('freesansbold.ttf',25)
    text = font.render("from source to a corner",True, Lime)                      
    screen.blit(text,text.get_rect(center = (800,150)))
 
    pygame.display.update()
    time.sleep(3)

    font = pygame.font.Font('freesansbold.ttf',25)
    text = font.render("4 Threads searching",True,White)                      
    screen.blit(text,text.get_rect(center = (800,200)))

    pygame.display.update()

    time.sleep(1)
display_maze()

seen      = list( list( False  for _ in range(COLS) ) for _ in range(ROWS) )
mutex_pos = list( list( Lock() for _ in range(COLS) ) for _ in range(ROWS) )
found = False

def runner(arg1,arg2):
    global found
    N_layer = 1
    missing = 0
    color , source = arg1,arg2
    predecessor =  list( list( ( -1 , -1 ) for _ in range(COLS) ) for _ in range(ROWS) )
    seen[source[0]][source[1]] = True
    Q = queue() 

    skip = False
    I_found = False
    
    current = source
    Q.insert(source)
    see_neighbours = False
    delay = 0.025
    pause = False
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

            pygame.display.update()
            time.sleep(0.01)
            if Q.not_empty():
                missing -= 1
                current = Q.pop()

                
            else:
                running = False

            i,j = current
            
            if maze[i][j] == Green:
                
                I_found = found = True
                continue

            remove_queue(i,j,color)
            see_neighbours = True
            

        if see_neighbours and not found:
            i,j = current
            
            if(       (i+1 < ROWS)        and   not seen[i+1][ j ] and maze[i+1][ j ] != White):
                mutex_pos[i+1][ j ].acquire()
                if(not seen[i+1][ j ]): seen[i+1][ j ] = True
                else: skip = True
                mutex_pos[i+1][ j ].release()
                if not skip:
                    insert_queue(i+1 ,  j ,color); Q.insert((i+1 ,  j ))
                    predecessor[i+1][ j ] = ( i , j )
                else:
                    skip = False

            
            if(        (0  <  i )         and   not seen[i-1][ j ] and maze[i-1][ j ] != White):
                mutex_pos[i-1][ j ].acquire()
                if(not seen[i-1][ j ]): seen[i-1][ j ] = True
                else: skip = True
                mutex_pos[i-1][ j ].release()
                if not skip:
                    insert_queue(i-1 ,  j ,color); Q.insert((i-1 ,  j ))
                    predecessor[i-1][ j ] = ( i , j )
                else:
                    skip = False

            
            if(       (j+1 < COLS)        and   not seen[ i ][j+1] and maze[ i ][j+1] != White):
                mutex_pos[ i ][j+1].acquire()
                if(not seen[ i ][j+1]): seen[ i ][j+1] = True
                else: skip = True
                mutex_pos[ i ][j+1].release()
                if not skip:
                    insert_queue( i  , j+1,color); Q.insert(( i  , j+1))
                    predecessor[ i ][j+1] = ( i , j )
                
                else:
                    skip = False

            
            if(        (j  > 0 )          and   not seen[ i ][j-1] and maze[ i ][j-1] != White):
                mutex_pos[ i ][j-1].acquire()
                if(not seen[ i ][j-1]): seen[ i ][j-1] = True
                else: skip = True
                mutex_pos[ i ][j-1].release()
                if not skip:
                    insert_queue( i  , j-1,color); Q.insert(( i  , j-1))
                    predecessor[ i ][j-1] = ( i , j )
                else:
                    skip = False
            


            see_neighbours = False

            time.sleep(0.001)

        if found:
            if I_found:
                time.sleep(0.025)
                (x,y) = current
                if( current != source ):
                    pygame.draw.rect(screen ,  Lime  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
                    maze[x][y] = Lime
                    x,y = predecessor[x][y]
                    pygame.draw.rect(screen ,  Lime  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
                    pygame.display.update()

                    current = (x,y)

                if current == source:
                    pygame.draw.rect(screen ,  Green  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
                    pygame.display.update()
                    running = False
                    continue
            else:
                running = False


if __name__ == "__main__":

    NO = Thread(target=runner, args = (Blue,(1,1))           )
    NE = Thread(target=runner, args = (Cyan,(COLS-1,1))        )
    SE = Thread(target=runner, args = (Dark_red,(1,ROWS-1)) )
    SO = Thread(target=runner, args = (Dark_yellow,(COLS-1,ROWS-1))        )

    NO.start()
    NE.start()
    SE.start()
    SO.start()

    NO.join()
    NE.join()
    SE.join()
    SO.join()

    running =  True
    while running :

        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                running = False                          #exit() program

        
