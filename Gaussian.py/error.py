import pygame,time,random,math,numpy as np
from math import cos,sin,pi,hypot
from colors import *

pygame.init()
screen_height = 700
screen_width = 1300
screen = pygame.display.set_mode((screen_width,screen_height))

init_pos = 200

def update_histogram(distribuicao_dict,show = True):
    
    for x,freq in distribuicao_dict.items():
        if x == 0: freq /=2
        pygame.draw.rect(screen,Dark_yellow,(3*x+900, y0 + 300 - 2*freq,2,2*freq)) 
    if show:pygame.display.update()

def arrow(screen, start, end, lcolor = (255,255, 255), tricolor = (255,255,255),  trirad= 6, thickness=3,show = False):
    pygame.draw.line(screen, lcolor, start, end, thickness)
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi/2
    rad = 180/math.pi
    pygame.draw.polygon(screen, tricolor, (
            (end[0] + trirad * math.sin(      rotation    ), end[1] + trirad * math.cos(     rotation     )),                    
            (end[0] + trirad * math.sin(rotation - 120*rad), end[1] + trirad * math.cos(rotation - 120*rad)),
            (end[0] + trirad * math.sin(rotation + 120*rad), end[1] + trirad * math.cos(rotation + 120*rad))
        )
    )
    if show: pygame.display.update()

x0,y0 = screen_width/5,screen_height/2
print(x0,y0)
arrow(screen,(x0-250,y0),(500,y0))
arrow(screen, (x0,y0+200),(x0,y0-200))

pygame.draw.circle(screen,Cyan,(x0,y0),3)
pygame.draw.circle(screen,Cyan,(900,y0+5),3)


pygame.draw.rect(screen,Cream,(0,0,550,1000))
arrow(screen,(x0-250,y0),(500,y0) , Black,Black)
arrow(screen, (x0,y0+250),(x0,y0-250),Black,Black)   
pygame.draw.circle(screen,Black,(x0,y0),5)
pygame.display.update()
time.sleep(1)

results = {}
N_throws = 10
N_show = 10
running = True
while running:
    pygame.draw.rect(screen,Cream,(0,0,550,1000))
    arrow(screen,(x0-250,y0),(500,y0) , Black,Black)
    arrow(screen, (x0,y0+250),(x0,y0-250),Black,Black)   
    pygame.draw.circle(screen,Black,(x0,y0),5)
    Xm = 0
    for step in range(N_throws):
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        t = 2*pi*random.random()
        r = random.randint(0,150)
        x,y = r*cos(t)+x0,r*sin(t)+y0
        pygame.draw.circle(screen,Dark_red,(x,y),3)
        #pygame.display.update()
        #time.sleep(0.1)

        Xm +=  x
    
    Xm = Xm/N_throws

    pygame.draw.circle(screen,Dark_yellow,(Xm,y0),5)
    pygame.display.update()
    time.sleep(0.01)

    dx = int(Xm-x0)
  
    if dx in results: results[dx] += 1
    else: results[dx] = 1
    N_show -= 1
    if N_show==0: update_histogram(results);N_show = 10
    