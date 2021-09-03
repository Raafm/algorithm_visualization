
from  graph.matriz import color,WHITE, blue,ciano
#from fios_de_agua import M,node_color
from graph.Continental import M, node_color

import pygame
import time,random


pygame.init()


screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))
SP = 0
screen.fill((0,0,0))


ROWS = len(M)
COLS = len(M[0])



def display_islands_map(done,speed= 10):
    if(done): return

    for y in range(len(M[0])):
        for x in range(len(M)):
          
            pygame.draw.rect(screen, node_color[x][y], (M[x][y][0],M[x][y][1] ,4, 4))

    pygame.display.update()
    #time.sleep(0.001/speed)





def print_square(i,j):
    pygame.draw.rect(screen, node_color[i][j], (M[i][j][0],M[i][j][1] ,4, 4));
    
    if random.randint(0,1):         # print sometimes to seem faster
        pygame.display.update()
    






def DFS(i,j):
    
    time.sleep(0.003*(random.randint(0,10) == 0))

    if(       (i+1 < ROWS)             and   node_color[i+1][ j ] == WHITE ):  node_color[i+1][ j ] = node_color[i][j] ;  print_square( i+1 ,  j  ); DFS( i+1 ,  j  ); 
    if(        (0  <  i )              and   node_color[i-1][ j ] == WHITE ):  node_color[i-1][ j ] = node_color[i][j] ;  print_square( i-1 ,  j  ); DFS( i-1 ,  j  ); 
    if(       (j+1 < COLS)             and   node_color[ i ][j+1] == WHITE ):  node_color[ i ][j+1] = node_color[i][j] ;  print_square(  i  , j+1 ); DFS(  i  , j+1 ); 
    if(        (j  > 0 )               and   node_color[ i ][j-1] == WHITE ):  node_color[ i ][j-1] = node_color[i][j] ;  print_square(  i  , j-1 ); DFS(  i  , j-1 ); 
    if( (i+1 < ROWS)  and (j+1 < COLS) and   node_color[i+1][j+1] == WHITE ):  node_color[i+1][j+1] = node_color[i][j] ;  print_square( i+1 , j+1 ); DFS( i+1 , j+1 ); 
    if( (i+1 < ROWS)  and (j > 0)      and   node_color[i+1][j-1] == WHITE ):  node_color[i+1][j-1] = node_color[i][j] ;  print_square( i+1 , j-1 ); DFS( i+1 , j-1 ); 
    if( (0 <  i) and (j+1 < COLS)      and   node_color[i-1][j+1] == WHITE ):  node_color[i-1][j+1] = node_color[i][j] ;  print_square( i-1 , j+1 ); DFS( i-1 , j+1 ); 
    if( (0 <  i) and ( j  >  0 )       and   node_color[i-1][j-1] == WHITE ):  node_color[i-1][j-1] = node_color[i][j] ;  print_square( i-1 , j-1 ); DFS( i-1 , j-1 ); 





#main:


font = pygame.font.Font('freesansbold.ttf',30)
text = font.render("How many islands? (quantas ilhas)",True,WHITE)                        
screen.blit(text,text.get_rect(center = (300,30)))
display_islands_map(False)

N_islands = 0
x=y=0

running =  True
end_algorithm = False  # this is for the running keep True but the algorithm stop, so we can see the final screen
pause = True            # start paused, press breakspace to start playing
while running:
   
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_SPACE:         # click breakspace for pause
                pause = not pause                   # if it is paused, click breakspace for play(resume)
                time.sleep(0.2)
    
    if pause:
        continue

 

    #for y in range(len(M[0])):
    #    for x in range(len(M)):


    if x == len(M):                 # if we are in this "column" it means we are outside the matrix, so go to next row
        x = 0
        y += 1
    if y == len(M[0]):              # end of rows
        end_algorithm = True    

    if end_algorithm: continue    # just to keep the screen of pygame

    if node_color[x][y] == WHITE:
   
        N_islands +=1
        node_color[x][y] = color[SP]
        pygame.draw.rect(screen, node_color[x][y], (M[x][y][0],M[x][y][1] ,4, 4));
        SP +=1
        if SP == len(color): SP =0

        
        pygame.draw.rect(screen, (0,0,0), (760,10 ,300, 200))    # erase what was before in the island couting

        font = pygame.font.Font('freesansbold.ttf',20)
        text = font.render("N° islands = " + str(N_islands) ,True,node_color[x][y])                   # print counting      
        screen.blit(text,text.get_rect(center = (855,100)))



        font = pygame.font.Font('freesansbold.ttf',40)
        text = font.render("DFS",True,node_color[x][y])                   # print DFS  in top       
        screen.blit(text,text.get_rect(center = (860,50)))
        
        DFS(x,y)

        font = pygame.font.Font('freesansbold.ttf',40)
        text = font.render("DFS",True,(0,0,0))                           # erase DFS 
        screen.blit(text,text.get_rect(center = (860,50)))

    elif node_color[x][y] == blue:
        node_color[x][y] = ciano
        pygame.draw.rect(screen, node_color[x][y], (M[x][y][0],M[x][y][1] ,4, 4));
        time.sleep(0.001*(random.randint(0,15) == 0))
    pygame.display.update()
    
    x += 1   #next column
                
