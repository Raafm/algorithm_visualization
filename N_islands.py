import pygame, time
from graph.matriz import M,node_color,color,WHITE, blue,ciano

#for x in range(50,800,50):
#    print( list((x,y) for y in range(50, 1000,50)))
        

ROWS = len(M)
COLS = len(M[0])

SP = 0

print("tamamnho = " ,len(M)*len(M[0]),"\nROWS: ",len(M),"\nCOLS: ",len(M[0]))

print("tamamnho = " ,len(node_color)*len(node_color[0]),"\nROWS: ",len(node_color),"\nCOLS: ",len(node_color[0]))

pygame.init()                   #width , height : coordinates 0,0 no canto superior esquerdo
screen = pygame.display.set_mode((950,720))
screen.fill((0,0,0)) 



def display_islands_map(done,speed= 1):
    if(done): return

    for y in range(len(M[0])):
        for x in range(len(M)):
          
            pygame.draw.rect(screen, node_color[x][y], (M[x][y][0],M[x][y][1] ,45, 45))

    pygame.display.update()
    time.sleep(0.15/speed)


def DFS(source):
    i,j=source

    if(       (i+1 < ROWS)             and   node_color[i+1][ j ] == WHITE ):  node_color[i+1][ j ] = node_color[i][j] ; display_islands_map(False,2); DFS((i+1, j )) 
    if(        (0  <  i )              and   node_color[i-1][ j ] == WHITE ):  node_color[i-1][ j ] = node_color[i][j] ; display_islands_map(False,2); DFS((i-1, j )) 
    if(       (j+1 < COLS)             and   node_color[ i ][j+1] == WHITE ):  node_color[ i ][j+1] = node_color[i][j] ; display_islands_map(False,2); DFS(( i ,j+1)) 
    if(        (j  > 0 )               and   node_color[ i ][j-1] == WHITE ):  node_color[ i ][j-1] = node_color[i][j] ; display_islands_map(False,2); DFS(( i ,j-1)) 
    if( (i+1 < ROWS)  and (j+1 < COLS) and   node_color[i+1][j+1] == WHITE ):  node_color[i+1][j+1] = node_color[i][j] ; display_islands_map(False,2); DFS((i+1,j+1)) 
    if( (i+1 < ROWS)  and (j > 0)      and   node_color[i+1][j-1] == WHITE ):  node_color[i+1][j-1] = node_color[i][j] ; display_islands_map(False,2); DFS((i+1,j-1)) 
    if( (0 <  i) and (j+1 < COLS)      and   node_color[i-1][j+1] == WHITE ):  node_color[i-1][j+1] = node_color[i][j] ; display_islands_map(False,2); DFS((i-1,j+1)) 
    if( (0 <  i) and ( j  >  0 )       and   node_color[i-1][j-1] == WHITE ):  node_color[i-1][j-1] = node_color[i][j] ; display_islands_map(False,2); DFS((i-1,j-1)) 


font = pygame.font.Font('freesansbold.ttf',30)
text = font.render("How many islands? (quantas ilhas)",True,WHITE)                   # informative node       
screen.blit(text,text.get_rect(center = (300,30)))
display_islands_map(False)

N_islands = 0
x=y=0

running =  True
end_algorithm = False
pause = True
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
                time.sleep(0.2)
    
    if pause:
        
        continue



    #for y in range(len(M[0])):
    #    for x in range(len(M)):


    if x == len(M):
        x = 0
        y += 1
    if y == len(M[0]):
        end_algorithm = True    

    if end_algorithm: continue    

    if node_color[x][y] == WHITE:

        N_islands +=1
        node_color[x][y] = color[SP]

        SP +=1
        if SP == len(color): SP =0

        pygame.draw.rect(screen, (0,0,0), (750,50 ,300, 100))

        font = pygame.font.Font('freesansbold.ttf',40)
        text = font.render("DFS",True,node_color[x][y])                   # informative node       
        screen.blit(text,text.get_rect(center = (860,50)))

        pygame.display.update()

        font = pygame.font.Font('freesansbold.ttf',20)
        text = font.render("N° islands = " + str(N_islands) ,True,node_color[x][y])                   # informative node       
        screen.blit(text,text.get_rect(center = (855,100)))

        display_islands_map(False,0.3)
        
        DFS((x,y))

    elif node_color[x][y] == blue:
        node_color[x][y] = ciano
        display_islands_map(False)
    
    font = pygame.font.Font('freesansbold.ttf',40)
    text = font.render("DFS",True,(0,0,0))                   # informative node       
    screen.blit(text,text.get_rect(center = (860,50)))

    x+=1
                
   #for y in range(len(M[0])):
   #    for x in range(len(M)):
   #        DFS((x,y))