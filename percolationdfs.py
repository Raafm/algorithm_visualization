from graph.color import *
from algorithms.data_struct.UnionFind import Matrix_UnionFind as Disjoint_Sets_datastruct_normal
from algorithms.data_struct.queue import queue
import pygame, time, random,numpy as np         

pygame.init()
screen_height = 700
screen_width = 1200
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill((0,0,0))


ROWS = COLS = 10
grid = list(list( Black for _ in range(COLS)) for _ in range(ROWS))

temp = np.random.permutation(list(range(ROWS*COLS)))
random_order = list((i%COLS,i//COLS) for i in temp)

UF = Disjoint_Sets_datastruct_normal(ROWS+1,COLS)


def paint_position(screen,x,y,color,grid = grid, show = False):

    grid[x][y] = color

    pygame.draw.rect(screen ,  grid[x][y]  , ( 100 + 32*x , 100 + 32*y , 30 , 30 ) )
    if show: pygame.display.update()



def display_grid(screen,grid):

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            paint_position(screen,x,y,grid[x][y])
    
    pygame.display.update()


def display_info(P):

    pygame.draw.rect(screen,Black,(0,0,screen_width-150,screen_height))
    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("Perco ",True,Lime)                        
    screen.blit(text,text.get_rect(center = (960,30)))
    text = font.render("lation ",True,Cyan)                        
    screen.blit(text,text.get_rect(center = (1045,30)))

    pygame.draw.rect(screen, Black, (950,50 ,100, 100))    # erase what was before in the island couting

    font = pygame.font.Font('freesansbold.ttf',30)
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
    paint_position(screen,i,j,color,show=True)
    while fila.not_empty():
        i,j = fila.pop()
        if(   (i+1 < ROWS)   and   grid[i+1][ j ] != Black and grid[i+1][ j ] != color ):  paint_position( screen, i+1 ,  j , color , show = True); fila.insert( (i+1 ,  j ) ) 
        if(    (0  <  i )    and   grid[i-1][ j ] != Black and grid[i-1][ j ] != color ):  paint_position( screen, i-1 ,  j , color , show = True); fila.insert( (i-1 ,  j ) ) 
        if(   (j+1 < COLS)   and   grid[ i ][j+1] != Black and grid[ i ][j+1] != color ):  paint_position( screen,  i  , j+1, color , show = True); fila.insert( ( i  , j+1) ) 
        if(    (j  > 0 )     and   grid[ i ][j-1] != Black and grid[ i ][j-1] != color ):  paint_position( screen,  i  , j-1, color , show = True); fila.insert( ( i  , j-1) )

def trace_back(node,color): 
    flag = True
    while flag:
        x,y = node
        if x == 0: flag = False
        paint_position(screen, x, y, color,show = True)
        node = parent[x][y]

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
    i = 0
    display_info(P)
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
        
         
            if(   (x+1 < ROWS)  and  grid[x+1][ y ] != Black ): UF.Union( (x,y) , (x+1 ,  y ) )
            if(    (0  <  x )   and  grid[x-1][ y ] != Black ): UF.Union( (x,y) , (x-1 ,  y ) )
            if(   (y+1 < COLS)  and  grid[ x ][y+1] != Black ): UF.Union( (x,y) , ( x  , y+1) )
            if(    (0  <  y )   and  grid[ x ][y-1] != Black ): UF.Union( (x,y) , ( x  , y-1) )

            
            if   UF.Find((ROWS,0)) == UF.Find((ROWS,1)):
                paint_position(screen,x,y,Yellow,show = True)
                font = pygame.font.Font('freesansbold.ttf',30)
                text = font.render("Percolated!",True,Yellow)                        
                screen.blit(text,text.get_rect(center = (1000,200)))
                pygame.display.update()
                time.sleep(5)

                for i in range(ROWS):
                    for j in range(COLS):
                        if grid[i][j] == Cyan or grid[i][j] == Lime:
                            grid[i][j] = Springgreen


                parent = list(list( (-1,-1) for _ in range(COLS)) for _ in range(ROWS))               
                fila = queue()
                for j in range(COLS):
                    fila.insert((0,j))
                    parent[0][j] = 0,j
                color = Springgreen
                                
                i,j = 0,0
                
                while fila.not_empty():
                    i,j = fila.pop()
                    if i == ROWS-1: break
                    if(   (i+1 < ROWS)   and  grid[i+1][ j ] == color and parent[i+1][ j ] == (-1,-1)):parent[i+1][ j ] = (i,j);  paint_position( screen, i+1 ,  j , color , show = True); fila.insert( (i+1 ,  j ) ) 
                    if(    (0  <  i )    and  grid[i-1][ j ] == color and parent[i-1][ j ] == (-1,-1)):parent[i-1][ j ] = (i,j);  paint_position( screen, i-1 ,  j , color , show = True); fila.insert( (i-1 ,  j ) ) 
                    if(   (j+1 < COLS)   and  grid[ i ][j+1] == color and parent[ i ][j+1] == (-1,-1)):parent[ i ][j+1] = (i,j);  paint_position( screen,  i  , j+1, color , show = True); fila.insert( ( i  , j+1) ) 
                    if(    (j  > 0 )     and  grid[ i ][j-1] == color and parent[ i ][j-1] == (-1,-1)):parent[ i ][j-1] = (i,j);  paint_position( screen,  i  , j-1, color , show = True); fila.insert( ( i  , j-1) )                
                
                trace_back((i,j),Yellow)
                
                
            if   UF.Find((x,y)) == UF.Find((ROWS,0)): BFS(x,y,Lime)
            if UF.Find((x,y)) == UF.Find((ROWS,1)): BFS(x,y,Cyan)

            
            time.sleep(0.01)
            
            
           
        

    game_loop()