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


N = 100
n = 500


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


def show_signal(signal,color_dot,altura,N = N,displacement = 10,show_points = False):

    last = signal(0)+altura
    mark(screen,(displacement*(N)+20,signal(N-1)+altura),color_dot,radius = 4,show=False)
    
    for t in range(N):
        cur = signal(t) + altura
        pygame.draw.line(screen,color_dot,(displacement*t+20,last),(displacement*(t+1)+20,cur),3)
        if show_points:
            mark(screen,(20*(t  )+20,last),White,radius = 4,show = False)
            mark(screen,(20*(t+1)+20,cur ),White,radius = 4,show = False)
        last = cur  


def noise(x):
    global random_noise
    L = random_noise.size
    return random_noise[x%L]


if __name__ == "__main__":
    
    random_noise = (np.random.rand(N)-0.5)*(80)

    f1 = lambda x: 35*cos(2*pi*5*x/N)
    f2 = lambda x: 20*cos(2*pi*10*x/N)
    f3 = lambda x: 50*sin(2*pi*2*x/N)


    f = lambda x: f1(x) + f2(x) + f3(x) + noise(x)


    power_distribution = abs(np.fft.fft(np.array(list(f(x) for x in range(N)))))
    PD = lambda x : power_distribution[x%(N//2+1)]
    
   # show_signal(lambda x: - PD(x)/7,indian_red,14*screen_height//15,N//2+1,displacement=10)
   # pygame.display.update()


    font = pygame.font.Font('freesansbold.ttf',20)

    t = 0
    vez = 0
    pause = False
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

        if vez == 0:
            text = font.render("Denoise",True,Cyan)
            screen.blit(text,text.get_rect(center = (1110,153)))
            text = font.render("the",True,Cyan)
            screen.blit(text,text.get_rect(center = (1110,183)))
            text = font.render("signal",True,Cyan)
            screen.blit(text,text.get_rect(center = (1110,213)))
            show_signal(lambda x: f(x+t),Cyan,screen_height//6)
        
        if vez == 1:
            text = font.render("Fourier Transform",True,indian_red)
            screen.blit(text,text.get_rect(center = (1110,223)))
            text = font.render("FFT",True,indian_red)
            screen.blit(text,text.get_rect(center = (1110,253)))
            text = font.render("and",True,indian_red)
            screen.blit(text,text.get_rect(center = (1110,293)))
            text = font.render("Pick the peaks",True,indian_red)
            screen.blit(text,text.get_rect(center = (1110,323)))

            text = font.render("f1",True,Green)
            screen.blit(text,text.get_rect(center = (50,15*screen_height//16)))
            
            text = font.render("f2",True,Yellow)
            screen.blit(text,text.get_rect(center = (80,15*screen_height//16)))
            
            text = font.render("f3",True,Red)
            screen.blit(text,text.get_rect(center = (130,15*screen_height//16)))

            show_signal(lambda x: f(x+t),Cyan,screen_height//6)
            show_signal(lambda x: - PD(x)/7,indian_red,14*screen_height//15,N//2+1,displacement=10)

        if vez == 2:
            t += 1
            text = font.render("First",True,Green)
            screen.blit(text,text.get_rect(center = (1110,223)))
            f = lambda x: f2(x)+ f1(x) + noise(x)
            show_signal(lambda x: f(x+t),Cyan,screen_height//6)
            show_signal(lambda x: f3(x+t),Green,300)
        
        if vez == 3:
            t += 1
            f = lambda x: f2(x) + noise(x)
            show_signal(lambda x: f(x+t),Cyan,screen_height//6)
            show_signal(lambda x: f3(x+t),Green   ,400)
            show_signal(lambda x: f1(x+t),Yellow  ,300)
        
        if vez == 4:
            text = font.render("Noise",True,Cyan)
            screen.blit(text,text.get_rect(center = (1110,113)))
            text = font.render("First frequency",True,Green)
            screen.blit(text,text.get_rect(center = (1110,503)))
            text = font.render("Second frequency",True,Yellow)
            screen.blit(text,text.get_rect(center = (1110,403)))
            text = font.render("Third frequency",True,Red)
            screen.blit(text,text.get_rect(center = (1110,300)))
            f = lambda x: noise(x)
            show_signal(lambda x: f(x+t),Cyan,screen_height//6)
            show_signal(lambda x: f1(x+t),Yellow ,400)
            show_signal(lambda x: f2(x+t),Red,300)
            show_signal(lambda x: f3(x+t),Green ,500)
        
        if vez == 5:
            text = font.render("Clean signal",True,White)
            screen.blit(text,text.get_rect(center = (1110,303)))
            text = font.render("noise removed",True,White)
            screen.blit(text,text.get_rect(center = (1110,333)))
            time.sleep(0.03)
            screen.blit(text,text.get_rect(center = (1110,333)))
            f = lambda x: f1(x+t) + f2(x+t) + f3(x+t)
            show_signal(lambda x: f(x+t),White,300)
            
        pygame.display.update()
        time.sleep(0.01)
        pygame.draw.rect(screen,Black,(0,0,screen_width,screen_height))
        t+=1
        if t == n:
            vez += 1 
            t = 0
            if vez == 2:
                vez = 4
            if vez==6:
                vez = 0
                f = lambda x: f1(x) + f2(x) + f3(x) + noise(x)
            