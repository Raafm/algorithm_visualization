from algorithms.data_struct.priority_queue import Heap
from graph.Create_Graph.Maze_islands_maker.randomHumanizedweightMaze import  assign_weights
from graph.maze_diagonal_good import labirinth as maze     
import pygame,time,random
from graph.color import *
from math import inf as INFINITY, hypot,exp

#COLS = 60
#ROWS = 60
#rect_size = 8
#maze = assign_weights(list(list( White for _ in range(COLS) ) for _ in range(ROWS)),rect_size = rect_size,  end_animation = True,N_loops = 100)



pygame.init()


screen_height = 700
screen_width = 1250
screen = pygame.display.set_mode((screen_width,screen_height))

screen.fill( Black ) # background color

weights = [
    Black,  
    brown, 
    royal_blue ,
    
]

def peso(color):
    return 1*(color == weights[0]) + 10*(color == weights[1]) + 100*(color == weights[2])

def altura(color): 
    return 0*(color == weights[0]) + 1*(color == weights[1]) + 2*(color == weights[2])

square_counter = {weights[0] : 0, weights[1] : 0, weights[2] : 0, Green : 0}

ROWS = len(maze)
COLS = len(maze[0])
rect_size = 7

for i in range(ROWS):
    for j in range(COLS):
        if maze[i][j] == Green:
            maze[i][j] = Black


# choose random obstacles' positions
i,j = random.randint(1, ROWS-1), random.randint(1, COLS-1)

while maze[i][j] == White:
    i,j = random.randint(1, ROWS-1), random.randint(1, COLS-1)
    # if is not an obstacle
    
target = (i,j)

maze[ i ][ j ] = Green



maze[0][0] = Black
maze[0][1] = Black
maze[1][0] = Black
maze[1][1] = Black





predecessor =  list( list( ( -1 , -1 ) for _ in range(COLS) ) for _ in range(ROWS) )
dist        =  list( list( INFINITY for _ in range(COLS) ) for _ in range(ROWS) )



PQ = Heap(comp = lambda a,b: a[1] > b[1])

def remove_queue(i,j):
    #maze[i][j] = Dark_yellow
    pygame.draw.circle(screen ,  Dark_yellow  ,  (50 + rect_size//2 + rect_size*i , 50 + rect_size//2 + rect_size*j ), rect_size//3  ) 
    #pygame.display.update()


def insert_queue(i,j):
    if i < 0 or j < 0 or i >99 or j > 99: return
    #if maze[i][j] != Green:
    #    maze[i][j] = Blue
    pygame.draw.circle(screen ,     Flame     ,  (50 + rect_size//2 + rect_size*i , 50 + rect_size//2 + rect_size*j ), rect_size//3  )
    #pygame.display.update()
   
 
def estimative(current,target,C = 1e6):
    i  , j   = current
    it , jt  = target
    return C*hypot( (i - it) , (j - jt) ) **5


def display_maze():
    N = len(maze)
    print(N)
    for x in range(N):
        time.sleep(0.01)
        for y in range(N):
            pygame.draw.rect(screen ,  maze[x][y]  , ( 50 + rect_size*x , 50 + rect_size*y , rect_size , rect_size ) )
        pygame.display.update()

    maze[0][1]  = maze[1][1]  = weights[0]
    
    time.sleep(1)
    
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Entry (Entrada).",True, Dark_yellow)                        
    screen.blit(text,text.get_rect(center = (100,30)))

    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Exit (Saida)" ,True, Green)                         
    screen.blit(text,(50+ROWS*rect_size ,50+COLS*rect_size))

    
    font = pygame.font.Font('freesansbold.ttf',40)
    text = font.render("in Heap",True, Flame)                      
    screen.blit(text,text.get_rect(center = (800,250)))

    
    font = pygame.font.Font('freesansbold.ttf',40)
    text = font.render("seen",True, Dark_yellow)                      
    screen.blit(text,text.get_rect(center = (800,350)))

    pygame.display.update()

display_maze()


found = False

source = (0,0)
current = source

PQ.insert((source,1))
dist[source[0]][source[1]] = 0

C = 1

see_neighbours = False
delay = 0.025
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
    
    

    if not found:


        if PQ.not_empty():
            
            current,_ = PQ.pop()
            
        else:
            pause = True
            continue

        i,j = current
        W = peso(maze[i][j])
        square_counter[maze[i][j]] += 1
        pygame.draw.rect(screen, maze[i][j], (screen_width - 200,145+100*altura(maze[i][j]) ,80, 60))    # erase what was before in the prime 
        font = pygame.font.Font('freesansbold.ttf',20)
        text = font.render(str(square_counter[maze[i][j]]) ,True, White)                      
        screen.blit(text,text.get_rect(center = (screen_width - 160,180+100*altura(maze[i][j]))))
        pygame.display.update()

        if maze[i][j] == Green:
            
            font = pygame.font.Font('freesansbold.ttf',40)
            text = font.render("Found",True,(0,235,0))                   # informative node       
            screen.blit(text,text.get_rect(center = (860,50)))
            pygame.display.update()
            
            found = True
            continue

        remove_queue(i,j)
        

    if not found:
        i,j = current
        if(       (i+1 < ROWS)             and   ( (maze[i+1][ j ] in weights) or maze[i+1][ j ] == Green) ):
            
            if dist[i+1][ j ] > (dist[i][j] + W) + estimative(current,target,C):
                dist[i+1][ j ] = (dist[i][j] + W) + estimative(current,target,C)
                predecessor[i+1][ j ] = ( i , j )
                insert_queue( i+1 ,  j  ); PQ.insert(((i+1 ,  j ),dist[i+1][ j ]))
                
            
        if(        (0  <  i )              and   ( (maze[i-1][ j ] in weights) or maze[i-1][ j ] == Green) ):
            
            if dist[i-1][ j ] > (dist[i][j] + W) + estimative(current,target,C):
                dist[i-1][ j ] = (dist[i][j] + W) + estimative(current,target,C)
                predecessor[i-1][ j ] = ( i , j )
                insert_queue( i-1 ,  j  ); PQ.insert(((i-1 ,  j ),dist[i-1][ j ]))
                
            
        if(       (j+1 < COLS)             and   ( (maze[ i ][j+1] in weights) or maze[ i ][j+1] == Green) ):
            
            if dist[ i ][j+1] > (dist[i][j] + W) + estimative(current,target,C):
                dist[ i ][j+1] = (dist[i][j] + W) + estimative(current,target,C)
                predecessor[ i ][j+1] = ( i , j )
                insert_queue(  i  , j+1 ); PQ.insert((( i  , j+1),dist[ i ][j+1]))
                
            
        if(        (j  > 0 )               and   ( (maze[ i ][j-1] in weights) or maze[ i ][j-1] == Green) ):
            
            if dist[ i ][j-1] > (dist[i][j] + W) + estimative(current,target,C):
                dist[ i ][j-1] = (dist[i][j] + W) + estimative(current,target,C)
                predecessor[ i ][j-1] = ( i , j )
                insert_queue(  i  , j-1 ); PQ.insert((( i  , j-1),dist[ i ][j-1]))

        
        pygame.display.update()      
        time.sleep(0.01)
        #C *= (random.randint(0,9) == 0)*1000
        

    if found:
        time.sleep(0.01)
        (x,y) = current
        if( current != source ):
            pygame.draw.circle(screen ,  Lime   ,  (50 + rect_size//2 + rect_size*x , 50 + rect_size//2 + rect_size*y ), rect_size//3  )
            x,y = predecessor[x][y]
            pygame.draw.circle(screen ,  Green  ,  (50 + rect_size//2 + rect_size*x , 50 + rect_size//2 + rect_size*y ), rect_size//3  )
            pygame.display.update()

            current = (x,y)

        if current == source:
            pygame.draw.circle(screen ,  Green  ,  (50 + rect_size//2 + rect_size*x , 50 + rect_size//2 + rect_size*y ), rect_size//3  )
            pygame.display.update()
            pause = True
            found = False
            continue
