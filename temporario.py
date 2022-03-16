#from graph.weighted_human_maze import labirinth as maze   
import pygame,time,random
from graph.color import *
from graph.Create_Graph.Maze_islands_maker.randomHumanizedweightMaze import  assign_weights


COLS = 80
ROWS = 80
rect_size = 8

maze = assign_weights(list(list( White for _ in range(COLS) ) for _ in range(ROWS)),rect_size = rect_size,  end_animation = True,N_loops = 300)



pygame.init()


screen_height = 700
screen_width = 1250
screen = pygame.display.set_mode((screen_width,screen_height))

screen.fill( Black ) # background color



weights = [
    royal_blue,
    brown, 
    Black,    
]




for i in range(ROWS):
    for j in range(COLS):
        if maze[i][j] in weights:
            if i > ROWS/2 and j < COLS/2:
                maze[i][j] = royal_blue
            elif j > ROWS/2 and i < COLS/2:
                maze[i][j] = brown

            else: maze[i][j] = Black

def display_maze():
    N = len(maze)
    print(N)
    for x in range(N):
        time.sleep(0.01)
        for y in range(N):
            pygame.draw.rect(screen ,  maze[x][y]  , ( 50 + rect_size*x , 50 + rect_size*y , rect_size , rect_size ) )
        pygame.display.update()

    maze[0][1]  = maze[1][1]  = weights[0]
    
    time.sleep(1)
    
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Entry (Entrada).",True, Dark_yellow)                        
    screen.blit(text,text.get_rect(center = (100,30)))

    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Exit (Saida)" ,True, Green)                         
    screen.blit(text,text.get_rect(center = (560,570)))

    
    font = pygame.font.Font('freesansbold.ttf',40)
    text = font.render("in Heap",True, Blue)                      
    screen.blit(text,text.get_rect(center = (800,250)))

    
    font = pygame.font.Font('freesansbold.ttf',40)
    text = font.render("seen",True, Dark_yellow)                      
    screen.blit(text,text.get_rect(center = (800,350)))

    pygame.display.update()

display_maze()

with open("temp.txt","w") as f:
    f.write("labirinth = [")
    for line in maze:
        f.write(str(line)+ ',\n')
    f.write("]")
    
print("labirinth = ",maze)


pause = True
running =  True
while running :

    # pygame stuff:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                   #exit pygame,
            running = False                          #exit() program


        
        if event.type == pygame.KEYDOWN:        
            if event.key == pygame.K_SPACE:     #press breakspace to pause or play
                pause = not pause   
                time.sleep(0.2)
    
    if pause:
        continue
    

