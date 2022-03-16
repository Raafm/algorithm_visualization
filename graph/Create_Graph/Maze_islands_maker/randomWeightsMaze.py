import pygame,time
from random import randint

class Node:
    def __init__(self, value = None, next_element = None):
        self.val = value
        self.next = next_element

class stack:
    def __init__(self): 
        self.head = None
        self.length = 0

    def insert(self,data): 
        self.head = Node(data,self.head)
        self.length += 1

    def pop(self): 
        if self.length == 0:
            return None 
        
        else:
            returned = self.head.val 
            self.head = self.head.next
            self.length -= 1
            return returned

    def not_empty(self):
        return bool(self.length)
    
    def top(self):
        return self.head.val
pygame.init()

screen_height = 700
screen_width = 1200
screen = pygame.display.set_mode((screen_width,screen_height))

White = (255,255,255)
Creamer = (220,220,220)
Black = ( 0 , 0 , 0 ) 
Red  = (255,0, 0 )
Water = ( 0 ,255,255)
Sand = (193,147,107)
Mud = (43,37,34)
Dark_yellow =      (250,200,0)

weights = [
    Sand ,
    Mud, 
    Water, 
    
]

Green = (0,0,255)
Cyan = (0,255,255)
screen.fill((250,250,250))

pygame.display.update()
time.sleep(0.5)

font = pygame.font.Font('freesansbold.ttf',30)
text = font.render("Random Maze generator",True,Black)                   
screen.blit(text,text.get_rect(center = (800,50)))

pygame.display.update()





def display_maze(maze):
    N = len(maze)
    print(N)
    for x in range(N):
        time.sleep(0.01)
        for y in range(N):
            pygame.draw.rect(screen ,  maze[x][y]  , ( 50 + 5*x , 50 + 5*y , 5 , 5 ) )
        pygame.display.update()

    #maze[0][1] = maze[0][2] = maze[0][3] = maze[0][4] = Yellow
    maze[99][95] = maze[99][96] = maze[99][97] = maze[99][98] = maze[99][99] = Green

    
    time.sleep(1)
    
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Entry (Entrada).",True, Cyan)                        
    screen.blit(text,text.get_rect(center = (100,30)))

    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Exit (Saida)" ,True, Green)                         
    screen.blit(text,text.get_rect(center = (560,570)))

    
    font = pygame.font.Font('freesansbold.ttf',40)
    text = font.render("in Heap",True, Water)                      
    screen.blit(text,text.get_rect(center = (800,250)))

    
    font = pygame.font.Font('freesansbold.ttf',40)
    text = font.render("seen",True, Cyan)                      
    screen.blit(text,text.get_rect(center = (800,350)))

    pygame.display.update()



maze_size = 50
maze = list( list(Creamer for _ in range(maze_size)) for _ in range(maze_size) )


cur_color = weights[0]
color_counter = 0   

def assign_weights(maze,rect_size = 10):

    ROWS = len(maze)
    COLS = len(maze[0])
    N = ROWS*COLS
 

    def print_square(i,j):

        global color_counter
        global cur_color

        if color_counter == 20:
            color_counter = 0
            cur_color = weights[randint(0,len(weights)-1)]

        maze[i][j] = cur_color
        color_counter += 1

        pygame.draw.rect(screen ,  maze[i][j]  , ( 50 + rect_size*i , 50 + rect_size*j , rect_size , rect_size  ) ) 
        pygame.display.update()

    seen = list(list(False for _ in range(COLS)) for _ in range(ROWS)  )
    parent = list(list((-1,-1) for _ in range(COLS)) for _ in range(ROWS)  )
            
    S = stack()
    S.insert((1,1))


    pause = True
    running =  True
    while running :

        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                running = False                          #exit() program


            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_SPACE:    
                    pause = not pause   
                    time.sleep(0.2)

        if pause:
            continue

        if S.not_empty():
            #print(S.top())
            i,j = S.pop()
            
            seen[i][j] = True    

            if     (i+1 < ROWS) and maze[i+1][ j ] != Creamer and parent[i][j] != (i+1 ,  j  ):continue
            if     (0  <  i )   and maze[i-1][ j ] != Creamer and parent[i][j] != (i-1 ,  j  ):continue
            if     (j+1 < COLS) and maze[ i ][j+1] != Creamer and parent[i][j] != ( i  , j+1 ):continue
            if     (j  > 0 )    and maze[ i ][j-1] != Creamer and parent[i][j] != ( i  , j-1 ):continue 
            print_square(i,j)

            to_stack = []
            if     (i+1 < ROWS) and seen[i+1][ j ] == False: seen[i+1][ j ] = True; to_stack.append( (i+1 ,  j  ) ); parent[i+1][ j ] = (i,j)
            if      (0  <  i )  and seen[i-1][ j ] == False: seen[i-1][ j ] = True; to_stack.append( (i-1 ,  j  ) ); parent[i-1][ j ] = (i,j)
            if     (j+1 < COLS) and seen[ i ][j+1] == False: seen[ i ][j+1] = True; to_stack.append( ( i  , j+1 ) ); parent[ i ][j+1] = (i,j)
            if      (j  > 0 )   and seen[ i ][j-1] == False: seen[ i ][j-1] = True; to_stack.append( ( i  , j-1 ) ); parent[ i ][j-1] = (i,j)

            while len(to_stack):
                S.insert(   to_stack.pop(randint( 0, len(to_stack)-1) )   )

            time.sleep(0.003)


assign_weights(maze)