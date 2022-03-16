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

Black = ( 0 , 0 , 0 ) 
Red  = (255,0, 0 )

Dark_yellow =      (250,200,0)
dark_green	        =	    (0,100,0)
Navy	            =	    (0,0,128)
forest_green	    =	    (34,139,34)
brown	            =  	    (165,42,42)
royal_blue	=	(65, 105, 225)
weights = [
    Black ,
    brown, 
    royal_blue, 
    
]

Green = (0,255,0)
Cyan = (0,255,255)

background_color = White
screen.fill(background_color)

pygame.display.update()
time.sleep(0.5)

font = pygame.font.Font('freesansbold.ttf',30)
text = font.render("Random Maze generator",True,Black)                   
screen.blit(text,text.get_rect(center = (screen_width -200,50)))

pygame.display.update()




maze_size = 80
maze = list( list(background_color for _ in range(maze_size)) for _ in range(maze_size) )


cur_color = weights[0]
color_counter = 0   

def assign_weights(maze,rect_size = 8, end_animation = False, N_loops = 20, show_cycles = False):

    ROWS = len(maze)
    COLS = len(maze[0])
    N = ROWS*COLS
 

    def print_square(i,j, unprint = False, color = False):
        
        if unprint:
            maze[i][j] =  (background_color[0]-1,background_color[1],background_color[2])
        else:
            global color_counter
            global cur_color

            if color: maze[i][j] = color
            else: 
                if color_counter == 20:
                    color_counter = 0
                    cur_color = weights[randint(0,len(weights)-1)]
                
                
                maze[i][j] = cur_color
                color_counter += 1

        pygame.draw.rect(screen ,  maze[i][j]  , ( 50 + rect_size*i , 50 + rect_size*j , rect_size , rect_size  ) ) 
        pygame.display.update()

    seen = list(list(False for _ in range(COLS)) for _ in range(ROWS)  )
    parent = list(list((-1,-1) for _ in range(COLS)) for _ in range(ROWS)  )

    left  = 0
    right = 1
    up    = 2
    down  = 3

    S = stack()
    S.insert(  (1,1, randint(0,3) ) )
    walk_counter = 0
    

    seen[1][1] = True

    pause = False
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
            if walk_counter == 0:
                i,j,orientation = S.pop()
                walk_counter = randint(2,15)

            while walk_counter:
                walk_counter -= 1
                if   not ( (i+1 < ROWS) and (0  <  i )  and  (j+1 < COLS) and  (j  > 0 ) ) : continue
                
                 
                if     (i+1 < ROWS-1) and maze[i+1][ j ] != background_color and parent[i][j] != (i+1 ,  j  ): continue
                if     (1  <  i )     and maze[i-1][ j ] != background_color and parent[i][j] != (i-1 ,  j  ): continue
                if     (j+1 < COLS-1) and maze[ i ][j+1] != background_color and parent[i][j] != ( i  , j+1 ): continue
                if     (j  > 1 )      and maze[ i ][j-1] != background_color and parent[i][j] != ( i  , j-1 ): continue 

                to_stack = []
                promising = False

                # right
                if     (i+1 < ROWS-1) and seen[i+1][ j ] == False: seen[i+1][ j ] = True; to_stack.append( (i+1 ,  j , right ) ); parent[i+1][ j ] = (i,j);  promising = True
                # left
                if      (1  <  i )    and seen[i-1][ j ] == False: seen[i-1][ j ] = True; to_stack.append( (i-1 ,  j , left ) ); parent[i-1][ j ]  = (i,j);  promising = True
                # down
                if     (j+1 < COLS-1) and seen[ i ][j+1] == False: seen[ i ][j+1] = True; to_stack.append( ( i  , j+1 , down ) ); parent[ i ][j+1] = (i,j);  promising = True
                # up
                if      (j  > 1 )     and seen[ i ][j-1] == False: seen[ i ][j-1] = True; to_stack.append( ( i  , j-1  , up )  ); parent[ i ][j-1] = (i,j);  promising = True

            
                print_square(i,j,unprint = not promising)

                while len(to_stack):
                    S.insert(   to_stack.pop(randint( 0, len(to_stack)-1) )   )
                    time.sleep(0.0001)

                i = (i+1)*(right == orientation) + (i-1)*(left == orientation)  + (orientation == down or orientation == up)*i
                j = (j+1)*(down == orientation) + (j-1)*(up == orientation)  + (orientation == left or orientation == right)*j



        # create loops
        if not S.not_empty():

            # everything that is not a path becomes a obstacle
            for i in range(ROWS):
                for j in range(COLS):
                    if maze[i][j] not in weights and maze[i][j] != background_color:
                        maze[i][j] = background_color
            
            while N_loops:
                N_loops -= 1
              
                
                # create loops
                loop_done = False
                while  not loop_done:

                    # choose random obstacles' positions
                    i,j = randint(3, ROWS-3), randint(3, COLS-3)

                    # if is not an obstacle
                    if maze[i][j] != background_color: continue

                    # remove obstacles
                    cor_do_lado =  maze[i + randint(-1,1)][j]
                    
                    # create a loop by connecting two paths with fixed i
                    if  maze[ i ][j-1] != background_color  and maze[ i ][j+1] != background_color and maze[ i -1][j] == background_color and maze[i+1][j] == background_color: 
                        if show_cycles: print_square(i,j,color = Green)
                        else:           print_square(i,j,color = cor_do_lado)
                        loop_done = True                        

                    # create a loop by connecting two paths with fixed j  
                    elif maze[ i ][j-1] == background_color  and maze[ i ][j+1] == background_color and maze[ i -1][j] != background_color and maze[i+1][j] != background_color: 
                        if show_cycles: print_square(i,j,color = Green)
                        else:           print_square(i,j,color = cor_do_lado)
                        loop_done = True
                        
                    time.sleep(0.01)
    
        if end_animation and not S.not_empty(): 
            running = False
            pygame.quit()

    return maze                


if __name__ == "__main__":
    assign_weights(maze,N_loops = 30,rect_size = 5)
    print(maze)