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

class queue:
    def __init__(self): 
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self,data): 
        if self.length == 0:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1

    def pop(self): 
        if self.length == 0:
            return None 
        
        else:
            returned = self.head.val 
            self.head = self.head.next
            self.length -= 1
            return returned
    
    def front(self):
        if self.length == 0:
            return None
        else:
            return self.head.val

    def not_empty(self):
        return bool(self.length)

pygame.init()

screen_height = 700
screen_width = 1000
screen = pygame.display.set_mode((screen_width,screen_height))

White = (255,255,255)
Creamer = (220,220,220)
Black = ( 0 , 0 , 0 ) 

screen.fill(Creamer)

pygame.display.update()
time.sleep(1.5)

font = pygame.font.Font('freesansbold.ttf',30)
text = font.render("Random Maze generator",True,Black)                   
screen.blit(text,text.get_rect(center = (800,50)))

pygame.display.update()

ROWS = 100
COLS = 100
N = ROWS*COLS

maze = list(list(White for _ in range(COLS)) for _ in range(ROWS))



def print_square(i,j):
    maze[i][j] = Black
    pygame.draw.rect(screen ,  Black  , ( 50 + 5*i , 50 + 5*j , 5 , 5 ) ) 
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

        

        if     (i+1 < ROWS) and maze[i+1][ j ] == Black and parent[i][j] != (i+1 ,  j  ):continue
        if     (0  <  i )   and maze[i-1][ j ] == Black and parent[i][j] != (i-1 ,  j  ):continue
        if     (j+1 < COLS) and maze[ i ][j+1] == Black and parent[i][j] != ( i  , j+1 ):continue
        if     (j  > 0 )    and maze[ i ][j-1] == Black and parent[i][j] != ( i  , j-1 ):continue 
        print_square(i,j)

        to_stack = []
        if     (i+1 < ROWS) and seen[i+1][ j ] == False: seen[i+1][ j ] = True; to_stack.append( (i+1 ,  j  ) ); parent[i+1][ j ] = (i,j)
        if      (0  <  i )  and seen[i-1][ j ] == False: seen[i-1][ j ] = True; to_stack.append( (i-1 ,  j  ) ); parent[i-1][ j ] = (i,j)
        if     (j+1 < COLS) and seen[ i ][j+1] == False: seen[ i ][j+1] = True; to_stack.append( ( i  , j+1 ) ); parent[ i ][j+1] = (i,j)
        if      (j  > 0 )   and seen[ i ][j-1] == False: seen[ i ][j-1] = True; to_stack.append( ( i  , j-1 ) ); parent[ i ][j-1] = (i,j)

        while len(to_stack):
            S.insert(   to_stack.pop(randint( 0, len(to_stack)-1) )   )

        time.sleep(0.003)
