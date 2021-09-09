import pygame,time
from math import hypot
import math

def arrow(screen, start, end, lcolor = (255,255, 255), tricolor = (255,255,255),  trirad= 8, thickness=5):
    pygame.draw.line(screen, lcolor, start, end, thickness)
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi/2
    rad = 180/math.pi
    pygame.draw.polygon(screen, tricolor, (
            (end[0] + trirad * math.sin(      rotation    ), end[1] + trirad * math.cos(     rotation     )),                    
            (end[0] + trirad * math.sin(rotation - 120*rad), end[1] + trirad * math.cos(rotation - 120*rad)),
            (end[0] + trirad * math.sin(rotation + 120*rad), end[1] + trirad * math.cos(rotation + 120*rad))
        )
    )
    pygame.display.update()


def distance(node1,node2):
    return hypot(node1[0]-node2[0], node1[1]-node2[1])


def show_weight(screen,peso,position,font,peso_color = (0,255,255),radius = 10):
    text = font.render(str(peso),True,peso_color,radius)
    screen.blit(text,position)


def median_point(p1,p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)


def memorize(screen,node_center,radius=10,Time = 0.1,show=True):
    pygame.draw.circle(screen,(255,0,0),node_center,radius)

    if show:
        pygame.display.update()
        time.sleep(Time)


def visit(screen,node_center,visit_color = (0,255,0),radius = 10,show=True,Time = 0.1):

    pygame.draw.circle(screen,visit_color,node_center,radius)

    if show:
        pygame.display.update()
        time.sleep(Time)



def visited(screen,node_center,radius = 10,show=True,Time = 0.1):
    Cyan 	     =	    (0,255,255)
    pygame.draw.circle(screen, Cyan , node_center , radius)

    

    if show:
        pygame.display.update()
        time.sleep(Time)



def mark(screen,node_center,color,radius,show=True,Time = 0.1):

    pygame.draw.circle(screen, color, node_center , radius)
    if show:
        pygame.display.update()
        time.sleep(Time)


# name of the algorithm
def top_info(screen,info_text,center_position = (400,30),size = 30):
    font = pygame.font.Font('freesansbold.ttf',size)
    text = font.render(info_text,True,(150,150,150))                        
    screen.blit(text,text.get_rect(center = center_position))
    pygame.display.update()



def informative_nodes(screen,
                    memory_color  = (255, 0 , 0 ), memory_text ="memorized nodes",
                    visited_color = ( 0 ,255,255), visited_text ="visited nodes",
                    current_color = ( 0 ,255, 0 ), current_text = "current"):

    font = pygame.font.Font('freesansbold.ttf',15)
    pygame.draw.circle(screen,memory_color, (850,200),7)
    text = font.render(memory_text,True,memory_color)
    screen.blit(text,text.get_rect(center = (915,200)))                             


    font = pygame.font.Font('freesansbold.ttf',15)


    pygame.draw.circle(screen,  (255,255,255), (850,150) , 7)
    pygame.draw.circle(screen,visited_color,(850,150),5)
    text = font.render(visited_text,True,visited_color)                               # informative node       
    screen.blit(text,text.get_rect(center = (925,150)))

    pygame.draw.circle(screen,current_color,(850,175),7)
    text = font.render(current_text,True,current_color)                            # informative node   
    screen.blit(text,text.get_rect(center = (925,175)))

    pygame.display.update()

def display_graph(screen, node_position,graph,
                node_color   = (0, 0 ,255),node_radius = 5 ,
                source = 0, source_color = (0,255,127),source_radius = 8,
                target = 1,target_color = (0,255, 0 ),target_radius = 8):
    #Springgreen	 =      (0,255,127)
    #Green  	     =	    (0,180,0)
    
    #draw lines (edges)
    for node in range(len(graph)):
        for neighbour in graph[node]:
            pygame.draw.line(screen,(255,255,255), node_position[node], node_position[neighbour],2)
    
    #draw circles (nodes)
    for node_number in range(len(graph)):                                                          # draw nodes
        if node_number == source:
            pygame.draw.circle(screen,source_color,node_position[node_number],source_radius)
        elif node_number == target:
            pygame.draw.circle(screen,target_color,node_position[node_number],target_radius)
        else:
            pygame.draw.circle(screen, node_color, node_position[node_number], node_radius)
    
    pygame.display.update()


def see_position(screen,position,color = (0,255,0)):
    pygame.draw.circle(screen,color,position,5)
    pygame.display.update()

if __name__ == "__main__":


    pause = True
    while True:

        
            # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                quit()                          #exit() program


            
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_SPACE:     #press breakspace to pause or play
                    pause = not pause   
                    time.sleep(0.2)
        
        if pause:
            continue


