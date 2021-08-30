import random,pygame
from math import hypot


WHITE = (255,255,255)
blue = (0,0,255)

def middle(x,y):
    return abs((985-hypot(x-(745/2),y-(645/2))))//100 # maximum is 9

def up(x,y): 
    return (160 - y)//20            # max is 8

def down(x,y):                      # max is 8
    return y//20

def right(x,y):                     # max is 8
    return (170 - x)//20

def left(x,y):                      # max is 8
    return x//20

def make_new_matrix(save_graph = False):

    screen_height = 700
    screnn_width = 1000
    screen = pygame.display.set_mode((screnn_width,screen_height))

    screen.fill((0,0,0))

    M = []
    node_color = []

    foi_branco = 10
    m=0
    for x in range(50,750,5):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        M.append([])
        node_color.append([])

        ROWS = len(M)
        COLS = len(M[0])

        for y in range(50,650,5):

            i , j = (x-50)//5 , (y-50)//5

            if(        (0  <  i )              and   node_color[i-1][ j ] == WHITE   ): foi_branco += 2     # up
            if( (0 <  i) and (j+1 < COLS)      and   node_color[i-1][j+1] == WHITE   ): foi_branco += 2     # up right
            if( (0 <  i) and ( j  >  0 )       and   node_color[i-1][j-1] == WHITE   ): foi_branco += 2     # up left
            if(        (j  > 0 )               and   node_color[ i ][j-1] == WHITE   ): foi_branco += 2     # left
            # os outros quadrados vizinhos ainda nao foram gerados
            
            Color = blue
            if random.randint(0, 10 - middle(x,y) ) < random.randint( 0 , foi_branco ):
                Color = WHITE


            M[(x-50)//5].append((x,y))
            node_color[(x-50)//5].append(Color)
            pygame.draw.rect(screen, Color , ( x , y , 4 , 4))
            
            foi_branco = 1
    

        pygame.display.update()



    # infromation
    print("ROWS = ",ROWS,"COLS = ",COLS,"\nNumber of squares: ",ROWS*COLS)

    if save_graph:
        with open("MATRIX.py","w") as f:            # save the graph in other file

            f.write("M = "+ str(M))                      
            f.write("\n\n\n")                          
            f.write("node_color = "+str(node_color))   



        
    running =  True
    while running:
    
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False


make_new_matrix()