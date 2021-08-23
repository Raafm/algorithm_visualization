from data_struct.queue import queue
from graph.color import *
from threading import Thread,Lock
from graph.Maze_Dense import labirinth as maze
import pygame,time,random


pygame.init()


screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))





COLS = len(maze[0])
ROWS = len(maze)

Nt = 4
own_queue = []
QP = 0
thread = []
initial_position = [(1,1),(98,1), (1,98),(98,98)]
thread_color = [Cyan,Dark_yellow,Red,Blue]
mutex = Lock()





def display_maze():
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
    
    font = pygame.font.Font('freesansbold.ttf',15)
    text = font.render("Entry (Entrada).",True, Cyan)                        
    screen.blit(text,text.get_rect(center = (100,30)))

    font = pygame.font.Font('freesansbold.ttf',15)
    text = font.render("Exit (Saida)" ,True, Green)                         
    screen.blit(text,text.get_rect(center = (560,570)))



def insert_queue(i,j,colour):
    if i < 0 or j < 0 or i >99 or j > 99: return
    if maze[i][j] != Green:
        maze[i][j] = colour
    pygame.draw.rect(screen ,  maze[i][j]  , ( 50 + 5*i , 50 + 5*j , 5 , 5 ) )
    pygame.display.update()


def runner(args):

    id = args
    colour = thread_color[id]
    process_list = own_queue[id]

    process_list.insert(initial_position[id])
    print(process_list.front())
    print("thread",id,"on")
    
    time.sleep(1)

    running =  True
    pause = False           
    
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
        


        if process_list.not_empty():
            print(process_list.front())
            time.sleep(0.01)
            i,j = process_list.pop()

            if(    (i+1 < ROWS)   and   (maze[i+1][ j ] == Black or maze[i+1][ j ] == Green) ): insert_queue( i+1 ,  j  , colour ); process_list.insert((i+1 ,  j ))
            if(     (0  <  i )    and   (maze[i-1][ j ] == Black or maze[i-1][ j ] == Green) ): insert_queue( i-1 ,  j  , colour ); process_list.insert((i-1 ,  j ))
            if(    (j+1 < COLS)   and   (maze[ i ][j+1] == Black or maze[ i ][j+1] == Green) ): insert_queue(  i  , j+1 , colour ); process_list.insert(( i  , j+1))
            if(     (j  > 0 )     and   (maze[ i ][j-1] == Black or maze[ i ][j-1] == Green) ): insert_queue(  i  , j-1 , colour ); process_list.insert(( i  , j-1))

        else:
            return

        



if __name__ == "__main__":

    for id in range(Nt):
        Q = queue()
        own_queue.append(Q)

    display_maze()


    thread0 = Thread(target= runner, args = (0,) )

    thread1 = Thread(target= runner, args = (1,) )

    thread2 = Thread(target= runner, args = (2,) )
  
    thread3 = Thread(target= runner, args = (3,) )
    

    #
    #thread4 = Thread(target= runner, args = (4,) )
    #thread4.start()

    
    thread3.start() 
    thread2.start()
    thread1.start()
    thread0.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread0.join()