
import pygame,time
from graph.color import *
from algorithms.data_struct.ChildUnionFind import Matrix_ChildUnionFind as Disjoint_Sets_datastruct_optimized
from algorithms.data_struct.queue import queue
import pygame, time, random,numpy as np         

pygame.init()
screen_height = 700
screen_width = 1200
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill((0,0,0))


ROWS = COLS = 100
grid = list(list( Black for _ in range(COLS)) for _ in range(ROWS))

temp = np.random.permutation(list(range(ROWS*COLS)))
random_order = list((i%COLS,i//COLS) for i in temp)

UF = Disjoint_Sets_datastruct_optimized(ROWS+1,COLS)


def paint_position(screen,x,y,color,grid = grid, show = False):

    grid[x][y] = color

    pygame.draw.rect(screen ,  grid[x][y]  , ( 50 + 5*x , 50 + 5*y , 4 , 4 ) )
    if show: pygame.display.update()

def just_paint(screen,x,y,color):
    pygame.draw.rect(screen ,  color  , ( 50 + 5*x , 50 + 5*y , 4 , 4 ) )
    pygame.display.update()


def display_grid(screen,grid):

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            just_paint(screen,y,x,grid[x][y])
    
    pygame.display.update()


def display_info(P):

    pygame.draw.rect(screen,Black,(0,0,screen_width-150,screen_height))
    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("Percolation",True,White)                      
    screen.blit(text,text.get_rect(center = (950,30)))

    pygame.draw.rect(screen, Black, (900,50 ,100, 100))    # erase what was before in the island couting

    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("P = " + str(P) +'%',True,White)                        
    screen.blit(text,text.get_rect(center = (950,100)))
    pygame.display.update()

def look_around(i,j):
    if(       (i+1 < ROWS)       and   grid[i+1][ j ] == White ): UF.Union( (i,j) , (i+1 ,  j ) ); 
    if(        (0  <  i )        and   grid[i-1][ j ] == White ): UF.Union( (i,j) , (i-1 ,  j ) ); 
    if(       (j+1 < COLS)       and   grid[ i ][j+1] == White ): UF.Union( (i,j) , ( i  , j+1) ); 
    if(        (j  > 0 )         and   grid[ i ][j-1] == White ): UF.Union( (i,j) , ( i  , j-1) ); 

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

def BFS(i,j):
    fila = queue()
    fila.insert((i,j))
    while fila.not_empty():
        i,j =fila.pop()
        if(   (i+1 < ROWS)   and   (grid[i+1][ j ] == White ) ):  grid[i+1][ j ] = Lime ;  just_paint( screen,  j , i+1 , Lime ); fila.insert( (i+1 ,  j ) ) 
        if(    (0  <  i )    and   (grid[i-1][ j ] == White ) ):  grid[i-1][ j ] = Lime ;  just_paint( screen,  j , i-1 , Lime ); fila.insert( (i-1 ,  j ) ) 
        if(   (j+1 < COLS)   and   (grid[ i ][j+1] == White ) ):  grid[ i ][j+1] = Lime ;  just_paint( screen, j+1,  i  , Lime ); fila.insert( ( i  , j+1) ) 
        if(    (j  > 0 )     and   (grid[ i ][j-1] == White ) ):  grid[ i ][j-1] = Lime ;  just_paint( screen, j-1,  i  , Lime ); fila.insert( ( i  , j-1) )



if __name__ == "__main__":

    for i in range(COLS):
        UF.Union((ROWS,0),(0,i))
        UF.Union((ROWS,1),(ROWS-1,i))

    P = 80 #porcentagem
    x = 0
    y = 0
    i=0
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

            just_paint(screen,y,x,White)
            grid[x][y] = White
            look_around(x,y)

            if UF.Find((ROWS,0)) == UF.Find((ROWS,1)):
                paint_position(screen,y,x,Yellow,show = True)

                font = pygame.font.Font('freesansbold.ttf',25)
                text = font.render("Percolation set with inverseFind()",True,Cyan)                        
                screen.blit(text,text.get_rect(center = (900,200)))
                pygame.display.update()
                time.sleep(1)
                
                node = UF.child_list((ROWS,0)).head
                while node:
                    if node.data[0] < ROWS:
                        just_paint(screen,node.data[1],node.data[0],Cyan)
                        grid[node.data[0]][node.data[1]] = Cyan
                    node = node.next
               

                for i in range(len(grid)):
                    for j in range(len(grid[0])):
                        grid[i][j] = White if (grid[i][j] != Black) else Black
                 
                time.sleep(1)
                pygame.draw.rect(screen,Black,(680,150,520,80))
                pygame.display.update()
                time.sleep(1)
                display_grid(screen,grid)
                time.sleep(1)

                pygame.draw.rect(screen,Black,(680,150,520,80))
                font = pygame.font.Font('freesansbold.ttf',30)
                text = font.render("Percolation set with BFS",True,Lime)                        
                screen.blit(text,text.get_rect(center = (930,200)))
                pygame.display.update()
                time.sleep(1)

                BFS(x,y)

                break
            
            
        

    game_loop()