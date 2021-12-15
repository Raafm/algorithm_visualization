import pygame,time,random
from graph.color import *
#from graph.points import pointsMany as points
from Trees.twoD_tree import points,root
import math
from algorithms.data_struct.queue import queue

pygame.init()
screen_width,screen_height = 1200,700
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(Black)


def print_lines(pos,vertical,XL = 10,YD = 10,XR = screen_width-200,YU = screen_height-50):
    x,y = pos

    if vertical: pygame.draw.line(screen,Cyan,(XL,y),(XR,y))
    else:        pygame.draw.line(screen,Red ,(x,YD),(x,YU))
    pygame.display.update()



def print_point(position, color= White,radius = 4, index=-1):
    pygame.draw.circle(screen,color,position,radius)
    if index > -1:
        font = pygame.font.Font('freesansbold.ttf',14)
        text = font.render( str(index),True, White)    
        screen.blit(text,text.get_rect(center = position))
    
    pygame.display.update()

def arrow(screen, start, end, lcolor = Light_grey, tricolor = Black,  trirad= 4, thickness=2):
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



for point in points:
    print_point(point)

xL,yD,xR,yU = 10,10,screen_width,screen_height
vertical = False

Q = queue()

Q.insert( (root,xL,yD,xR,yU, vertical) )

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

    if Q.not_empty():
        cur,xL,yD,xR,yU,vertical = Q.pop()
    else: continue

    print(cur.x,cur.y)
    print_point((cur.x,cur.y),(vertical)*Cyan + (not vertical)*Red,radius = 6)
    print_lines((cur.x,cur.y),vertical,xL,yD,xR,yU)
    time.sleep(0.5)

    if vertical == True:
        #print_point((cur.x,cur.y),Cyan,radius = 6)
        if cur.right:
            Q.insert( (cur.right, xL, cur.y , xR ,  yU   , not vertical)  )
            arrow(screen, (cur.x,cur.y),(cur.right.x,cur.right.y))
            #print_point((cur.right.x,cur.right.y),Red,radius = 6)
            time.sleep(0.2)
        if cur.left :
            Q.insert( (cur.left , xL,   yD  , xR , cur.y , not vertical ) )
            arrow(screen, (cur.x,cur.y),(cur.left .x,cur.left .y))
            #print_point((cur.left.x,cur.left.y),Red,radius = 6)
            time.sleep(0.2) 
    else:
        #print_point((cur.x,cur.y),Red,radius = 6)
        if cur.right: 
            Q.insert( (cur.right,cur.x,yD,xR,yU, not vertical) )
            arrow(screen, (cur.x,cur.y),(cur.right.x,cur.right.y))
            #print_point((cur.right.x,cur.right.y),Cyan,radius = 6)
            time.sleep(0.2)
        if cur.left : 
            Q.insert( (cur.left ,xL,yD,cur.x,yU, not vertical) )
            arrow(screen, (cur.x,cur.y),(cur.left .x,cur.left .y))
            #print_point((cur.left.x,cur.left.y),Cyan,radius = 6)
            time.sleep(0.2)
    


    