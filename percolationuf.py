from graph.color import *
from algorithms.data_struct.ChildUnionFind import Matrix_ChildUnionFind as Disjoint_Sets_datastruct_optimized
from algorithms.data_struct.queue import queue
import pygame, time, random,numpy as np         

pygame.init()
screen_height = 700
screen_width = 1200
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill((0,0,0))


ROWS = COLS = 50
grid = list(list( Black for _ in range(COLS)) for _ in range(ROWS))

temp = np.random.permutation(list(range(ROWS*COLS)))
random_order = list((i%COLS,i//COLS) for i in temp)

UF = Disjoint_Sets_datastruct_optimized(ROWS+1,COLS)


def paint_position(screen,x,y,color,grid = grid, show = False):

    grid[x][y] = color

    pygame.draw.rect(screen ,  grid[x][y]  , ( 50 + 12*x , 50 + 12*y , 10 , 10 ) )
    if show: pygame.display.update()



def display_grid(screen,grid):

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            paint_position(screen,x,y,grid[x][y])
    
    pygame.display.update()


def display_probabilities(P):
    pygame.draw.rect(screen, Black, (850,10 ,300, 200))    # erase what was before in the island couting

    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("P = " + str(P) +'%',True,White)                        
    screen.blit(text,text.get_rect(center = (1000,100)))
    pygame.display.update()

def look_around(i,j):
    if(    (i+1 < ROWS)   and   grid[i+1][ j ] == White ): UF.Union( (i,j) , (i+1 ,  j ) ); 
    if(     (0  <  i )    and   grid[i-1][ j ] == White ): UF.Union( (i,j) , (i-1 ,  j ) ); 
    if(    (j+1 < COLS)   and   grid[ i ][j+1] == White ): UF.Union( (i,j) , ( i  , j+1) ); 
    if(     (j  > 0 )     and   grid[ i ][j-1] == White ): UF.Union( (i,j) , ( i  , j-1) ); 

def game_loop():
    running =  True
    pause = False           # start paused, press breakspace to start playing
    while running:
    
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            
            if event.type == pygame.KEYDOWN:            
                if event.key == pygame.K_SPACE:         # click breakspace for pause
                    pause = not pause                   # if it is paused, click breakspace for play(resume)
                    time.sleep(0.2)
        
        if pause:
            break

def BFS(i,j, color):
    fila = queue()
    fila.insert((i,j))
    color_bfs = Dark_yellow
    while fila.not_empty():
        i,j = fila.pop()
        if(   (i+1 < ROWS)   and   grid[i+1][ j ] == color  ):  grid[i+1][ j ] = color_bfs ;  paint_position( screen, i+1 ,  j , grid[i+1][ j ] , show = True); fila.insert( (i+1 ,  j ) ) 
        if(    (0  <  i )    and   grid[i-1][ j ] == color  ):  grid[i-1][ j ] = color_bfs ;  paint_position( screen, i-1 ,  j , grid[i-1][ j ] , show = True); fila.insert( (i-1 ,  j ) ) 
        if(   (j+1 < COLS)   and   grid[ i ][j+1] == color  ):  grid[ i ][j+1] = color_bfs ;  paint_position( screen,  i  , j+1, grid[ i ][j+1] , show = True); fila.insert( ( i  , j+1) ) 
        if(    (j  > 0 )     and   grid[ i ][j-1] == color  ):  grid[ i ][j-1] = color_bfs ;  paint_position( screen,  i  , j-1, grid[ i ][j-1] , show = True); fila.insert( ( i  , j-1) )


def print_set(x,y,color):
    node = UF.child_list((x,y)).head
    while node:
        if node.data[0] < ROWS-1 and 0 < node.data[0]:
            paint_position(screen,node.data[0],node.data[1],color,show = True)
        node = node.next
    


if __name__ == "__main__":
    
    for i in range(COLS):
        UF.Union((ROWS,0),(0,i))
        UF.Union((ROWS,1),(ROWS-1,i))
        pygame.draw.rect(screen ,  Lime  , ( 50 - 12 , 50 + 12*i , 10 , 10 ) )
        pygame.draw.rect(screen ,  Cyan  , ( 50 + COLS*12 , 50 + 12*i , 10 , 10 ) )
        pygame.display.update()

    P = 70 #porcentagem
    x = 0
    y = 0
    i=0
    running =  True
    pause = False           # start paused, press breakspace to start playing
    while running:
    
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

            
            if event.type == pygame.KEYDOWN:            
                if event.key == pygame.K_SPACE:         # click breakspace for pause
                    pause = not pause                   # if it is paused, click breakspace for play(resume)
                    time.sleep(0.2)
        
        if pause:
            continue

        if len(random_order):
            x,y = random_order.pop()   
        else:
            break
             

        if random.randint(1,100) <= P:

            
            if x == ROWS-1:  
                paint_position(screen,x,y,Cyan,show = True)
            elif x == 0:
                paint_position(screen,x,y,Lime,show = True)
            else:
                paint_position(screen,x,y,White,show = True)
        

            if(   (x+1 < ROWS)  and  grid[x+1][ y ] != Black ):  
                UF.Union( (x,y) , (x+1 ,  y ) ); 

            if(    (0  <  x )   and  grid[x-1][ y ] != Black ):                                     
                UF.Union( (x,y) , (x-1 ,  y ) ); 

            if(   (y+1 < COLS)  and  grid[ x ][y+1] != Black ):              
                UF.Union( (x,y) , ( x  , y+1) ); 

            if(    (0  <  y )   and  grid[ x ][y-1] != Black ):                                         
                UF.Union( (x,y) , ( x  , y-1) ); 

            
            if   UF.Find((ROWS,0)) == UF.Find((ROWS,1)):
                node = UF.child_list((x,y)).head
                while node:
                    if node.data[0] < ROWS:
                        paint_position(screen,node.data[0],node.data[1],Springgreen,show = True)
                        
                    node = node.next
                paint_position(screen,x,y,Dark_yellow,show = True)
                
                
            

               # for i in range(len(grid)):
               #     for j in range(len(grid[0])):
               #         grid[i][j] = White if (grid[i][j] != Black) else Black
               # 
               # display_grid(screen,grid)
#
               # BFS(x,y,White)

                break

            if   UF.Find((x,y)) == UF.Find((ROWS,0)):print_set(x,y,Lime)
            elif UF.Find((x,y)) == UF.Find((ROWS,1)):print_set(x,y,Cyan)
     
            
            
           
        

    game_loop()