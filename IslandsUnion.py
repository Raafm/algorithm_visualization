import pygame,time,random
from graph.Continental import M, node_color
from  graph.matriz import WHITE, blue
from graph.color import *

ROWS = len(M)
COLS = len(M[0])

N_islands = 0

print(ROWS,COLS)
pygame.init()

forget = (1,0,0)

screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))

parent = list(  list( (x,y) for y in range(len(M[0]))  ) for x in range(len(M)))
size = list(  list( 1 for _ in range(len(M[0]))  ) for _ in range(len(M)))


def display_islands_map(done,speed= 10):
    if(done): return

    max_rank =-1
    for y in range(len(M[0])):
        for x in range(len(M)):
            Colour = node_color[x][y]
            if node_color[x][y][0] < 200 and node_color[x][y][1] < 200 and node_color[x][y][2]  <200:
                Colour = (node_color[x][y][0] + 50,node_color[x][y][1]+50,node_color[x][y][2]+50)
            pygame.draw.rect(screen,Colour , (M[x][y][0],M[x][y][1] ,4, 4))
            if node_color[x][y]==forget:
                pygame.draw.rect(screen,(0,0,0) , (M[x][y][0],M[x][y][1] ,4, 4))
    #print(max_rank) #smaior foi de 275         
    pygame.display.update()
    #time.sleep(0.001/speed)

def print_square(i,j):
    #print(node_color[x][y])
    pygame.draw.rect(screen, node_color[i][j], (M[i][j][0],M[i][j][1] ,4, 4))
    
    if not random.randint(0,100):         # print sometimes to seem faster
        pygame.display.update()
    

def display_islands_numbers(N_islands):
    pygame.draw.rect(screen, (0,0,0), (760,10 ,300, 200))    # erase what was before in the island couting

    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("N° islands = " + str(N_islands) ,True,(255,255,0))                   # print counting      
    screen.blit(text,text.get_rect(center = (855,100)))
    



def Find(position):

    x,y = position

    Xparent,Yparent = parent[x][y]

    if (Xparent == x) and (Yparent == y): return (x,y)
    
    
    Xparent,Yparent = Find((Xparent,Yparent))

    parent[x][y] = (Xparent,Yparent)

    return (Xparent,Yparent)


def Union(position1,position2):


    x1,y1 = Find(position1)
    x2,y2 = Find(position2)

    if x1 == x2 and y1 == y2: return

    global N_islands
    N_islands -= 1


    if size[x1][y1] < size[x2][y2]:
        xt,yt = x1,y1
        x1,y1 = x2,y2        
        x2,y2 = xt,yt

    size[x1][y1] += size[x2][y2]

    
    for x in range(len(M)):
        for y in range(len(M[0])):
            if Find((x,y)) == parent[x2][y2]:
                node_color[x][y] = node_color[x1][y1]
                parent[x][y] = (x1,y1)
                pygame.draw.rect(screen,node_color[x1][y1],(M[x][y][0],M[x][y][1],4,4))




def look_around(i,j):
    

    if(       (i+1 < ROWS)             and   node_color[i+1][ j ] != blue   and   node_color[i+1][ j ] != forget ):    Union( (i,j) , (i+1 ,  j ) ); 
    if(        (0  <  i )              and   node_color[i-1][ j ] != blue   and   node_color[i-1][ j ] != forget ):    Union( (i,j) , (i-1 ,  j ) ); 
    if(       (j+1 < COLS)             and   node_color[ i ][j+1] != blue   and   node_color[ i ][j+1] != forget ):    Union( (i,j) , ( i  , j+1) ); 
    if(        (j  > 0 )               and   node_color[ i ][j-1] != blue   and   node_color[ i ][j-1] != forget ):    Union( (i,j) , ( i  , j-1) ); 
    if( (i+1 < ROWS)  and (j+1 < COLS) and   node_color[i+1][j+1] != blue   and   node_color[i+1][j+1] != forget ):    Union( (i,j) , (i+1 , j+1) ); 
    if( (i+1 < ROWS)  and (j > 0)      and   node_color[i+1][j-1] != blue   and   node_color[i+1][j-1] != forget ):    Union( (i,j) , (i+1 , j-1) ); 
    if( (0 <  i) and (j+1 < COLS)      and   node_color[i-1][j+1] != blue   and   node_color[i-1][j+1] != forget ):    Union( (i,j) , (i-1 , j+1) ); 
    if( (0 <  i) and ( j  >  0 )       and   node_color[i-1][j-1] != blue   and   node_color[i-1][j-1] != forget ):    Union( (i,j) , (i-1 , j-1) ); 

    #pygame.display.update()


display_islands_map(False)





font = pygame.font.Font('freesansbold.ttf',30)
text = font.render("How many islands? (quantas ilhas)",True,WHITE)                        
screen.blit(text,text.get_rect(center = (300,30)))
display_islands_map(False)


x,y = ROWS,COLS-1

running =  True
part_algorithm = 0  # this is for the running keep True but the algorithm stop, so we can see the final screen
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
   
#walk through the matrix

    if x == ROWS:                 # if we are in this "column" it means we are outside the matrix, so go to next row
        x = 0
        y += 1

    if y == COLS:              # end of rows
        
        part_algorithm += 1 
        
        if part_algorithm < 4:
            x = y = 0

        else:
            x , y = ROWS+1, COLS+1  
            pause = True  
            
        pygame.draw.rect(screen, (0,0,0), (755,425,300, 400))    # erase 
        pygame.draw.rect(screen, (0,0,0), (755,305,300, 400))


        font = pygame.font.Font('freesansbold.ttf',20)

        text = font.render("part "+str(part_algorithm) ,True,(255,255,255))                   # print counting      
        screen.blit(text,text.get_rect(center =(870,350) ))        
        
        

        string = ""
        if part_algorithm == 1:
            string = "parent(x,y) = (x,y)="
            pygame.draw.rect(screen, (255,255,0), (950,407, 10, 10))
        if part_algorithm == 2:
            string = "     Unions"  
        if part_algorithm == 3:
            string = " representatives: "
            pygame.draw.circle(screen, (255,255,0) , (950,409), 8)  

                

        text = font.render(string ,True,(255,255,255))                   # print counting      
        screen.blit(text,text.get_rect(center = (850,410)))

        time.sleep(1)


    # disconsidering water and: parent(x,y) = (x,y)
    if part_algorithm == 1: 

        if node_color[x][y] == WHITE:
            
            node_color[x][y]  = (  2*y  , 0.8*(x+y)  , 255 - 0.8*(x+y))
            pygame.draw.rect(screen, (255,255,0), (M[x][y][0],M[x][y][1] ,4, 4))
            N_islands += 1

        else:
            node_color[x][y] = forget 
            pygame.draw.rect(screen, forget, (M[x][y][0],M[x][y][1] ,4, 4))

        
        if random.randint(0,20) == 0:
            pygame.display.update()
        


    #Unions
    if part_algorithm == 2:         
        tx,ty = x,y

        #x,y = ROWS-1-x,COLS-y-1 #olhar de baixo para cima
        

        if node_color[x][y] != forget:
            
            look_around(x,y)
            
        display_islands_numbers(N_islands)

        if random.randint(0,20) == 0:
            pygame.display.update()
        x,y = tx,ty
    


    # search the representatives
    if part_algorithm == 3:

        if node_color[x][y] == forget:
            node_color[x][y] = blue        
            print_square(x,y)

        elif parent[x][y] == (x,y):
            pygame.draw.circle(screen, (255,255,0) , M[x][y], 8)
        
        else:
            node_color[x][y] = WHITE        
            print_square(x,y)

        if x == ROWS -1 and y == COLS -1 :
            display_islands_numbers(N_islands)
            pygame.display.update()

        if random.randint(0,20) == 0:
            pygame.display.update() 

    x += 1   #next column
