import pygame,time,random
from graph.Continental import M, node_color
from  graph.matriz import WHITE, blue,red,ciano,color,SP


ROWS = len(M)
COLS = len(M[0])

pygame.init()


screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))


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
    



def Find(position):

    x,y = position
    print(x,y)
    print(len(node_color[0]))
    _,Xparent,Yparent = node_color[x][y]
    Xparent = 254-Xparent,
    Yparent = 254

    if (Xparent ==  x) and (Yparent == y): return (x,y)
    
    
    Xparent,Yparent = Find((Xparent,Yparent))

    node_color[x][y] = ( Xparent,254, Yparent)
    print_square(x,y)

    return (Xparent,Yparent)


def Union(position1,position2):
    
    x1,y1 = Find(position1)
    x2,y2 = Find(position2)

    if x1 == x2 and y1 == y2: return

    if node_color[x1][y1][0] == node_color[x2][y2][0]: node_color[x1][y1] = (node_color[x1][y1][0]+1, 254-x1, 254-y1)
    elif node_color[x1][y1][0] < node_color[x2][y][0]: 
        i  , j  = x1 , y1
        x1 , y1 = x2 , y2
        x2 , y2 = i  , j
    
    
    node_color[x2][y2] = (  0  , 254 - x1  , 254 - y1  ) 

    #print_square( x2,y2)
    pygame.draw.rect(screen,ciano,(M[x2][y2][0],M[x2][y2][1],4,4))
    pygame.draw.circle(screen,(255, 255, 0,),M[x1][y1],3)
    pygame.display.update()

    #pygame.draw.rect(screen,(0,0,0),(M[x2][y2][0],M[x2][y2][1],4,4))
    pygame.draw.circle(screen,(0, 0, 0,),M[x1][y1],3)

def look_around(i,j):
    

    if(       (i+1 < ROWS)             and   node_color[i+1][ j ] != blue   and   node_color[i+1][ j ] != ciano):    Union( (i,j) , (i+1 ,  j ) ); 
    if(        (0  <  i )              and   node_color[i-1][ j ] != blue   and   node_color[i-1][ j ] != ciano):    Union( (i,j) , (i-1 ,  j ) ); 
    if(       (j+1 < COLS)             and   node_color[ i ][j+1] != blue   and   node_color[ i ][j+1] != ciano):    Union( (i,j) , ( i  , j+1) ); 
    if(        (j  > 0 )               and   node_color[ i ][j-1] != blue   and   node_color[ i ][j-1] != ciano):    Union( (i,j) , ( i  , j-1) ); 
    if( (i+1 < ROWS)  and (j+1 < COLS) and   node_color[i+1][j+1] != blue   and   node_color[i+1][j+1] != ciano):    Union( (i,j) , (i+1 , j+1) ); 
    if( (i+1 < ROWS)  and (j > 0)      and   node_color[i+1][j-1] != blue   and   node_color[i+1][j-1] != ciano):    Union( (i,j) , (i+1 , j-1) ); 
    if( (0 <  i) and (j+1 < COLS)      and   node_color[i-1][j+1] != blue   and   node_color[i-1][j+1] != ciano):    Union( (i,j) , (i-1 , j+1) ); 
    if( (0 <  i) and ( j  >  0 )       and   node_color[i-1][j-1] != blue   and   node_color[i-1][j-1] != ciano):    Union( (i,j) , (i-1 , j-1) ); 




display_islands_map(False)





font = pygame.font.Font('freesansbold.ttf',30)
text = font.render("How many islands? (quantas ilhas)",True,WHITE)                        
screen.blit(text,text.get_rect(center = (300,30)))
display_islands_map(False)

N_islands = 0
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
            
        pygame.draw.rect(screen, (0,0,0), (755,425,300, 400))    # erase what was before in the island couting

        font = pygame.font.Font('freesansbold.ttf',20)

        text = font.render("part "+str(part_algorithm) ,True,(255,255,255))                   # print counting      
        screen.blit(text,text.get_rect(center = (850,450)))        
        
        string = ""
        if part_algorithm == 1:
            string = "parent(x,y) = (x,y)"
        if part_algorithm == 2:
            string = "Unions"    
        if part_algorithm == 3:
            string = "Search Patriarches"

        text = font.render(string ,True,(255,255,255))                   # print counting      
        screen.blit(text,text.get_rect(center = (850,500)))

        time.sleep(1)



    if part_algorithm == 1:

        if node_color[x][y] == WHITE:
            node_color[x][y]  = (  0  , 254 - x, 254 - y )
        else:
            node_color[x][y] = ciano
        
        print_square(x,y)



    if part_algorithm == 2:         

        if node_color[x][y] != ciano:
            look_around(x,y)

        pygame.draw.rect(screen, blue, (751, (4*y)+50, 4,4))    # erase what was before in the island couting
        pygame.display.update()
    
    if part_algorithm == 3:


        if node_color[x][y][1] == 254- x   and   node_color[x][y][2] == 254-  y:
            
            N_islands +=  1 
            
            if SP == len(color):
                SP =1
            pygame.draw.circle(screen, color[SP] , M[x][y], 5)
            SP+=1

            pygame.draw.rect(screen, (0,0,0), (760,10 ,300, 200))    # erase what was before in the island couting

            font = pygame.font.Font('freesansbold.ttf',20)
            text = font.render("N° islands = " + str(N_islands) ,True,node_color[x][y])                   # print counting      
            screen.blit(text,text.get_rect(center = (855,100)))

            pygame.display.update()
        
        else:
            node_color[x][y] = WHITE        
            print_square(x,y)


    x += 1   #next column
