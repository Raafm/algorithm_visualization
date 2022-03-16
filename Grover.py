import pygame,time,numpy as np
from math import sqrt,cos,sin,asin
from random import randint
from algorithms.data_struct.queue import queue
from algorithms.data_struct.stack import stack
from algorithms.colors import *



pygame.init()


screen_height = 700
screen_width = 1300
screen = pygame.display.set_mode((screen_width,screen_height))

screen.fill((0,0,0))
square_width    =       2
space = 1
index_color     =   (0,200,0)
index2_color    =   (200,200,0)
numb_color      =   (50,50,250)
const_color     =   (255,255,255)
sum_color       =   (250,250,0)
duplicate_color =   (255,0,0)
ground = 450
size_rate = 500
rect_color = []


def print_rect(screen,arr,i,color):

    if i >= len(arr): return
    pygame.draw.rect(   screen   ,  color   ,   (10 + (square_width+space)*i , ground - size_rate*arr[i],    square_width  ,  size_rate*arr[i])  )
   
    pygame.display.update()
  

def display(screen,arr):

    pygame.draw.rect(screen,Black,(0,0,screen_width-150,screen_height))
    
    for i in range(len(arr)):
        x = 10 + (square_width+space)*i
        y = ground - size_rate*arr[i] if arr[i] > 0 else ground+2
        square_height = abs(size_rate*arr[i])

        pygame.draw.rect(   screen   ,  rect_color[i]    ,   (x, y,   square_width  ,  square_height)  )
    

    pygame.display.update()
    
   

def take_possession(color,left,right):
    for i in range(left,right+1):
        rect_color[i] = color

n = 8
N = 2**n


theta = asin(1/sqrt(N))
fi = theta
initial_amplitude = sin(fi)


rect_color = list(White for _ in range(N))
amplitude = np.array(list(sin(fi) for _ in range(N)))


display(screen,amplitude)

# line of 0
pygame.draw.line(screen,Cyan,(10,ground+1), (10+N*(space+square_width),ground+1) )
pygame.draw.line(screen,Cyan,(10,ground+1-size_rate*(initial_amplitude) - 1), (10+N*(space+square_width),ground+1-size_rate*(initial_amplitude) - 1) )
pygame.display.update()

time.sleep(0.5)

amplitude[N//2] *= -1
display(screen,amplitude)

# line of 0
pygame.draw.line(screen,Cyan,(10,ground+1), (10+N*(space+square_width),ground+1) )
pygame.draw.line(screen,Cyan,(10,ground+1-size_rate*(initial_amplitude) - 1), (10+N*(space+square_width),ground+1-size_rate*(initial_amplitude) - 1) )

pygame.display.update()

fi += 2*theta

amplitude       = np.array([cos(fi)/sqrt(N) for _ in range(N)])
amplitude[N//2] = sin(fi)


time.sleep(0.5)

display(screen,amplitude)

# line of 0
pygame.draw.line(screen,Cyan,(10,ground+1), (10+N*(space+square_width),ground+1) )
pygame.draw.line(screen,Cyan,(10,ground+1-size_rate*(initial_amplitude) - 1), (10+N*(space+square_width),ground+1-size_rate*(initial_amplitude) - 1) )

pygame.display.update()

r = int(sqrt(N/2))


running =  True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                   #exit pygame,
            running = False                          #exit() program    


    
    if r == 0:
        time.sleep(1)
        r = 0
        continue
    r-=1

    display(screen,amplitude)

    # line of 0
    pygame.draw.line(screen,Cyan,(10,ground+1), (10+N*(space+square_width),ground+1) )
    pygame.draw.line(screen,Cyan,(10,ground+1-size_rate*(initial_amplitude) - 1), (10+N*(space+square_width),ground+1-size_rate*(initial_amplitude) - 1) )
    pygame.display.update()

    time.sleep(1)

    amplitude[N//2]   *= -1
    amplitude[N//2+5] *= -1
   
    display(screen,amplitude)

    # line of 0
    pygame.draw.line(screen,Cyan,(10,ground+1), (10+N*(space+square_width),ground+1) )
    pygame.draw.line(screen,Cyan,(10,ground+1-size_rate*(initial_amplitude) - 1), (10+N*(space+square_width),ground+1-size_rate*(initial_amplitude) - 1) )

    pygame.display.update()

    fi += 2*theta

    amplitude       = np.array([cos(fi)/sqrt(N-1) for _ in range(N)])
    amplitude[N//2]   = sin(fi)/sqrt(2)
    amplitude[N//2+5] = sin(fi)/sqrt(2)

    time.sleep(1)

    display(screen,amplitude)

    # line of 0
    pygame.draw.line(screen,Cyan,(10,ground+1), (10+N*(space+square_width),ground+1) )
    pygame.draw.line(screen,Cyan,(10,ground+1-size_rate*(initial_amplitude) - 1), (10+N*(space+square_width),ground+1-size_rate*(initial_amplitude) - 1) )

    pygame.display.update()



