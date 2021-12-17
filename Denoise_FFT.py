import numpy as np
import pygame,time, random, string
from graph.color import *
from math import cos,sin,pi
import math

pygame.init()
screen_width,screen_height = 1200,700
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(Black)
font = pygame.font.Font('freesansbold.ttf',15)


N = 80
n = 600


def mark(screen,node_center,colors,radius=8,show=True,Time = 0.05,text = None,text_color = (226, 88, 34)):

    if len(colors) == 2:
        pygame.draw.circle(screen, colors[0], node_center , radius = 8)
        pygame.draw.circle(screen, colors[1], node_center , radius=5)
    else:
        pygame.draw.circle(screen, colors, node_center , radius)

    
    if text is not None:
        font = pygame.font.Font('freesansbold.ttf',15)
        text = font.render(text,True,text_color)                        
        screen.blit(text,text.get_rect(center = node_center))
    if show:
        pygame.display.update()
        time.sleep(Time)


def show_signal(signal,color_dot,altura,N = N,displacement = 15):

    last = signal(0)+altura
    mark(screen,(20*(0)+20,last),color_dot,radius = 4,show=False)
    
    for t in range(1,N):
        cur = signal(t) + altura
        pygame.draw.line(screen,color_dot,(displacement*t+20,last),(displacement*(t+1)+20,cur))
       # mark(screen,(20*(t  )+20,last),color_dot,radius = 4,show = False)
       # mark(screen,(20*(t+1)+20,cur ),color_dot,radius = 4,show = False)
        last = cur  


def noise(x):
    global random_noise
    L = random_noise.size
    return random_noise[x%L]


if __name__ == "__main__":


    
    random_noise = (np.random.rand(N)-0.5)*20

    signal_random = list( 0*random.randint(10,50) for _ in range(N))
    # show_signal(signal_random,Red,50)

    f1 = lambda x: 20*cos(2*pi*5*x/N)
    f2 = lambda x: 10*cos(2*pi*10*x/N)
    f3 = lambda x: 50*cos(2*pi*35*x/N)


    f = lambda x: f1(x) + f2(x) + f3(x) + noise(x)


    power_distribution = abs(np.fft.fft(np.array(list(f(x) for x in range(N)))))
    PD = lambda x : power_distribution[x%(N//2+1)]
    
    show_signal(lambda x: - PD(x)/4,indian_red,9*screen_height//10,N//2+1,displacement=25)
    pygame.display.update()
    time.sleep(2)

    t = 0
    vez = True
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

        if vez:
        
            show_signal(lambda x: f(x-t),Cyan,screen_height//2)
        

        else:
            
            show_signal(lambda x: f1(x-t),Red   ,400)
            show_signal(lambda x: f2(x-t),Yellow,400)
            show_signal(lambda x: f3(x-t),Green ,400)
           
            
            
        pygame.display.update()
        time.sleep(0.01)
        pygame.draw.rect(screen,Black,(0,0,screen_width,screen_height))
        t+=1
        if t == n:
            vez = not vez
            t = 0
            