from algorithms.data_struct.queue import queue
from algorithms.data_struct.stack import stack
from graph.Maze_Dense import labirinth as maze   
import pygame,time,random
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
Blue = (100,100,255)

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
    #improving the maze for better animation
    maze[ROWS//2][COLS//2] = maze[ROWS//2 +1][COLS//2 +1] = maze[ROWS//2 +1][COLS//2] = maze[ROWS//2][COLS//2 +1] = Green
    maze[ROWS//2+2][COLS//2+5] = maze[ROWS//2+1][COLS//2+4] = maze[ROWS//2+2][COLS//2-2] = White
    maze[ROWS//2-5][COLS//2+4] = maze[ROWS//2-2][COLS//2+6] = White
    maze[1][COLS-7] = Black
    maze[1][COLS-40] = White
    maze[14][COLS-22] = Black
    maze[40][COLS-48] = White
    maze[38][COLS-48] = White
    maze[38][COLS-42] = White

    for x in range(N):
        time.sleep(0.01)
        for y in range(N):
            pygame.draw.rect(screen ,  maze[x][y]  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
        pygame.display.update()


    time.sleep(1)
    
    
    font = pygame.font.Font('freesansbold.ttf',25)
    text = font.render("Find a path",True, Lime)                      
    screen.blit(text,text.get_rect(center = (800,50)))

    font = pygame.font.Font('freesansbold.ttf',25)
    text = font.render("from source to a corner",True, Lime)                      
    screen.blit(text,text.get_rect(center = (800,75)))
 
    pygame.display.update()
    time.sleep(3)

    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("4 Threads searching",True,White)                      
    screen.blit(text,text.get_rect(center = (800,125)))

    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("N° houses visited:",True,White)                      
    screen.blit(text,text.get_rect(center = (800,175)))

    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("BFS",True,Blue)                      
    screen.blit(text,text.get_rect(center = (50,30)))
    

    text = font.render("BFS",True,Cyan)                      
    screen.blit(text,text.get_rect(center = (560,30)))

    

    text = font.render("DFS",True,Dark_red)                      
    screen.blit(text,text.get_rect(center = (50,570)))
    

    text = font.render("DFS",True,Dark_yellow)                      
    screen.blit(text,text.get_rect(center = (560,570)))

    pygame.display.update()

    time.sleep(1)
display_maze()

seen      = list( list( False  for _ in range(COLS) ) for _ in range(ROWS) )
mutex_pos = list( list( Lock() for _ in range(COLS) ) for _ in range(ROWS) )
found = False

def runner(arg0,arg1,arg2,arg3,arg4):
    global found
    id,color , source = arg0,arg1,arg2
    predecessor =  list( list( ( -1 , -1 ) for _ in range(COLS) ) for _ in range(ROWS) )
    seen[source[0]][source[1]] = True
    Q = arg3 
    delay = arg4

    N_visited = 0
    skip = False
    I_found = False
    
    current = source
    Q.insert(source)
    see_neighbours = False

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
            time.sleep(delay)
            if Q.not_empty():
                current = Q.pop()
                N_visited += 1
                pygame.draw.rect(screen, (30,30,30), (750,225+100*id ,60, 60))    # erase what was before in the prime 
                font = pygame.font.Font('freesansbold.ttf',20)
                text = font.render(str(N_visited) ,True, color)                      
                screen.blit(text,text.get_rect(center = (780,260+100*id)))

                
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
    Q1 = queue()
    Q2 = queue()
    S1 = stack()
    S2 = stack() 

    NO = Thread(target=runner, args = ( 0, Blue,    (1,1)    ,     Q1        , 0.01 )   )
    NE = Thread(target=runner, args = ( 1, Cyan,(COLS-1,1)       ,    Q2     , 0.01 )   )
    SE = Thread(target=runner, args = ( 2, Dark_red,(1,ROWS-1)    ,     S1   , 0.01 )   )
    SO = Thread(target=runner, args = ( 3, Dark_yellow,(COLS-1,ROWS-1),   S2 , 0.01 )   )

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

        
