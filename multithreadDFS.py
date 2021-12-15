from graph.bigGraph import graph,node_list as node_position
from algorithms.data_struct.stack import stack
import pygame,time
from algorithms.colors import Springgreen,Cyan,Red,Green,Lime,Black,White,Flame,Navy,Dark_yellow, Teal,Blue,Light_grey
from threading import Thread, Lock,Condition

#source = 72 node degree 4
source = 0
process_list = stack()
seen = list(False for _ in range(len(graph)))                                   # haven't seen anyone yet
parent = list(-1 for _ in range(len(graph))) 
original_color = list(Blue for _ in range(len(graph)))

screen_height = 700
screen_width = 1300
screen = pygame.display.set_mode((screen_width,screen_height))

screen.fill(Black)

pygame.init()



source_color = Green
node_color = Blue
current_color = Lime
source_radius = 5    
node_radius = 5


font = pygame.font.Font('freesansbold.ttf',30)
text = font.render("Multithread DFS",True,Dark_yellow)                   # informative node       
screen.blit(text,text.get_rect(center = (1090,50)))

font = pygame.font.Font('freesansbold.ttf',25)

pygame.draw.circle(screen,Red, (1000,125),10)
text = font.render("memory stack",True,Red)
screen.blit(text,text.get_rect(center = (1110,123)))                             # informative node   
text = font.render("(pilha de processamento)",True,Red)
screen.blit(text,text.get_rect(center = (1080,160)))

font = pygame.font.Font('freesansbold.ttf',30)
text = font.render("Thread node:",True,White)                   # informative node       
screen.blit(text,text.get_rect(center = (1090,220)))

pygame.display.update()


for node in range(len(graph)):
    for neighbour in graph[node]:
        node1 = node_position[node]
        node2 = node_position[neighbour]
        pygame.draw.line(screen,(255,255,255), node1, node2,2)
        

#draw circles (nodes)
for node_number in range(len(graph)):                                                          # draw nodes
    if node_number == source:
        pygame.draw.circle(screen,source_color,node_position[node_number],source_radius)

    else:
        pygame.draw.circle(screen, node_color, node_position[node_number], node_radius)

pygame.display.update()



N_operating = 0
mutex = Condition()
see_mtx = Lock()
def dfs(graph, node_position,color,id):

    global N_operating
    global node_color
    current = None

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                quit()                          #exit() program
        
        if current is None:

            mutex.acquire()
            while process_list.empty() and N_operating > 0:
                mutex.wait()

            if process_list.empty():
                mutex.release()
                return    

            current = process_list.pop()

            see_mtx.acquire()
            if seen[current]:
                see_mtx.release()
                mutex.release()
                continue

            seen[current] = True
            N_operating += 1
            
            see_mtx.release()
            mutex.release()

        
        original_color[current] = color
        pred = parent[current]
        pygame.draw.line(  screen, color,node_position[current],node_position[pred],4)
        pygame.draw.circle(screen, color , node_position[current] , 8)
        pygame.draw.circle(screen, original_color[pred] , node_position[pred] , 8)
        
        pygame.draw.rect(screen, color, (1060,245+100*id ,80, 60))    # erase what was before in the prime 
        font = pygame.font.Font('freesansbold.ttf',20)
        text = font.render(str(current) ,True, Black)                      
        screen.blit(text,text.get_rect(center = (1100,280+100*id)))
        

        see_mtx.acquire()
        pygame.display.update()
        see_mtx.release()

        time.sleep(0.2)

        local_list = []
        for neighbour in graph[current]:
            
            see_mtx.acquire()
            
            if seen[neighbour]:
                see_mtx.release()
                time.sleep(0.02)
                continue

            else:
                
                pygame.draw.circle(screen,  Red, node_position[neighbour] , 5)
                pygame.display.update()
                
                if parent[neighbour] < 0: parent[neighbour] = current 
                local_list.append(neighbour)
                seen[neighbour] = True

                see_mtx.release()
                time.sleep(0.1)

        mutex.acquire()  
        for neighbour in local_list:
            process_list.insert(neighbour)
        
        if process_list.not_empty():
            current = process_list.pop()
            seen[current] = True
        else:
            current = None
            N_operating -= 1
        mutex.notify()
        mutex.release()
            



if __name__ == "__main__":
    Nt = 3
    thread = []
    color  = [Springgreen,Dark_yellow,Teal,Cyan]

    process_list.insert(source)
    parent[source] = source
    
    time.sleep(2)
    for i in range(Nt):
        t = Thread(target = dfs, args = (graph,node_position,color[i],i))
        thread.append(t)

    for i in range(Nt):
        time.sleep(1)
        thread[i].start()
        

    for i in range(Nt):
        thread[i].join()

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                quit()                          #exit() program

