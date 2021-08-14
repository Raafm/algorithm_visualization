import pygame,time,random
from graph.Continental import M, node_color
from  graph.matriz import WHITE, blue,red,ciano,color,SP
from data_struct.stack import stack
from math import hypot

ROWS = len(M)
COLS = len(M[0])
print(ROWS,COLS)
pygame.init()

forget = (1,0,0)

screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))


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
    pygame.draw.rect(screen, node_color[i][j], (M[i][j][0],M[i][j][1] ,4, 4));
    
    if random.randint(0,1):         # print sometimes to seem faster
        pygame.display.update()
    

#
#
#def Find(position):
#
#    x,y = position
#
#    _,Xparent,Yparent = node_color[x][y]
#
#    if (Xparent == x) and (Yparent == y): return (x,y)
#    
#    
#    Xparent,Yparent = Find((Xparent,Yparent))
#
#    node_color[x][y] = (0,Xparent,Yparent)
#    print_square(x,y)
#
#    return (Xparent,Yparent)


def Union(position1,position2):
    
    S = stack()
    x1,y1 = position1
    while node_color[x1][y1][1] != x1 or node_color[x1][y1][2] != y1: 
        S.insert((x1,y1))
        x1,y1 =  node_color[x1][y1][1],node_color[x1][y1][2]

    x2 , y2 = position2
    while node_color[x2][y2][1] != x2 or node_color[x2][y2][2] != y2: 
        S.insert((x2,y2))
        x2,y2 = node_color[x2][y2][1], node_color[x2][y2][2]



    #x1,y1 = Find(position1)
    #x2,y2 = Find(position2)

    if x1 == x2 and y1 == y2: return

    if node_color[x1][y1][0] == node_color[x2][y2][0]: node_color[x1][y1] = (node_color[x1][y1][0]+0.3, x1, y1)
    elif node_color[x1][y1][0] < node_color[x2][y2][0]: 
        i  , j  = x1 , y1
        x1 , y1 = x2 , y2
        x2 , y2 = i  , j
    
    S.insert((x2,y2))
    while S.not_empty():
        x,y = S.pop()
        node_color[x][y] = node_color[x1][y1]



    #print_square( x2,y2)
    #pygame.draw.rect(screen,ciano,(M[x2][y2][0],M[x2][y2][1],4,4))
    #pygame.draw.circle(screen,(255, 255, 0,),M[x1][y1],3)
    display_islands_map(random.randint(0,20))

    #pygame.draw.rect(screen,(0,0,0),(M[x2][y2][0],M[x2][y2][1],4,4))
    pygame.draw.circle(screen,(225, 225, 0,),M[x1][y1],3)

def look_around(i,j):
    

    if(       (i+1 < ROWS)             and   node_color[i+1][ j ] != blue   and   node_color[i+1][ j ] != forget ):    Union( (i,j) , (i+1 ,  j ) ); 
    if(        (0  <  i )              and   node_color[i-1][ j ] != blue   and   node_color[i-1][ j ] != forget ):    Union( (i,j) , (i-1 ,  j ) ); 
    if(       (j+1 < COLS)             and   node_color[ i ][j+1] != blue   and   node_color[ i ][j+1] != forget ):    Union( (i,j) , ( i  , j+1) ); 
    if(        (j  > 0 )               and   node_color[ i ][j-1] != blue   and   node_color[ i ][j-1] != forget ):    Union( (i,j) , ( i  , j-1) ); 
    if( (i+1 < ROWS)  and (j+1 < COLS) and   node_color[i+1][j+1] != blue   and   node_color[i+1][j+1] != forget ):    Union( (i,j) , (i+1 , j+1) ); 
    if( (i+1 < ROWS)  and (j > 0)      and   node_color[i+1][j-1] != blue   and   node_color[i+1][j-1] != forget ):    Union( (i,j) , (i+1 , j-1) ); 
    if( (0 <  i) and (j+1 < COLS)      and   node_color[i-1][j+1] != blue   and   node_color[i-1][j+1] != forget ):    Union( (i,j) , (i-1 , j+1) ); 
    if( (0 <  i) and ( j  >  0 )       and   node_color[i-1][j-1] != blue   and   node_color[i-1][j-1] != forget ):    Union( (i,j) , (i-1 , j-1) ); 




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
            
        pygame.draw.rect(screen, (0,0,0), (755,425,300, 400))    # erase 
        pygame.draw.rect(screen, (0,0,0), (755,305,300, 400))


        font = pygame.font.Font('freesansbold.ttf',20)

        text = font.render("part "+str(part_algorithm) ,True,(255,255,255))                   # print counting      
        screen.blit(text,text.get_rect(center =(870,350) ))        
        
        

        string = ""
        if part_algorithm == 1:
            string = "parent(x,y) = (x,y)"
        if part_algorithm == 2:
            string = "     Unions"    
        if part_algorithm == 3:
            string = "Search Patriarches:"
            for n,colour in enumerate(color):
                pygame.draw.circle(screen, colour , (780+15*n,380), 5)
                

        text = font.render(string ,True,(255,255,255))                   # print counting      
        screen.blit(text,text.get_rect(center = (850,410)))

        time.sleep(1)



    if part_algorithm == 1:

        if node_color[x][y] == WHITE:
            node_color[x][y]  = (  0  , x,  y )
        else:
            node_color[x][y] = forget 
        
        print_square(x,y)



    if part_algorithm == 2:         
        tx,ty = x,y
        x,y = ROWS-1-x,COLS-y-1
        if node_color[x][y] != forget:
            look_around(x,y)

        pygame.draw.rect(screen , (50 + y , 50 + y  ,  20) , (751, (5*y)+50, 4,4))    # erase what was before in the island couting
        
        if random.randint(0,4) == 0:
            pygame.display.update()
        x,y = tx,ty
    



    if part_algorithm == 3:

        if node_color[x][y] == forget:
            node_color[x][y] = blue        
            print_square(x,y)

        elif node_color[x][y][1] == x   and   node_color[x][y][2] ==  y:
            
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
