import pygame,time, random, string
from graph.color import *
from math import cos,sin,pi
import math

pygame.init()
screen_width,screen_height = 1200,700
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(Black)
font = pygame.font.Font('freesansbold.ttf',15)

h0 = 50
h = 20
x0 = 150

N=32
positions = list((x0, h*y+h0) for y in range(N))



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



def display(screen,positions,color=White):
    for pos in positions:
        mark(screen,pos,color)

    pygame.display.update()


def arrow(screen, start, end, lcolor = (255,255, 255), tricolor = (255,255,255),  trirad= 4, thickness=3):
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


def informative():
    font = pygame.font.Font('freesansbold.ttf',35)
    text = font.render("FFT",True, White)                         
    screen.blit(text,text.get_rect(center = (1050,50)))
    
    font = pygame.font.Font('freesansbold.ttf',25)

    pygame.draw.circle(screen,White, (1000,185),10)
    text = font.render("Coefficient",True,White)
    screen.blit(text,text.get_rect(center = (1110,183)))                             # informative node 

    pygame.draw.circle(screen,Cyan, (1000,225),10)
    text = font.render("Even",True,Cyan)
    screen.blit(text,text.get_rect(center = (1110,223)))                             # informative node 

    pygame.draw.circle(screen, White, (1000,265) , radius = 10)
    pygame.draw.circle(screen, Dark_red, (1000,265) , radius = 7)
    
    text = font.render("Odd",True,Dark_red)
    screen.blit(text,text.get_rect(center = (1110,263)))                             # informative node   

    pygame.display.update()
    



def fft_animation(positions,N,h0)->list:

    x,_ = positions[0]

    # if there is only one item in the array, return THE ARRAY
    if N <= 1:
        return

    
    # separate even and odd coefficients
    positionsEven = list((x + x0 ,     h*y + h0   )   for y, (x,_) in enumerate(positions[0::2]))
    positionsOdd  = list((x + x0 , h*(y+N//2) + h0)   for y, (x,_) in enumerate(positions[1::2]))

    display(screen, positionsEven,color = Cyan)
    display(screen, positionsOdd, color = (White,Dark_red))

    time.sleep(0.05)

    fft_animation(positionsEven, N//2, h0= h0)

    time.sleep(0.05)
    fft_animation(positionsOdd , N//2, h0= h0 + h*N//2)
    

    # middle of the array
    middle = N//2
    for k in range(middle):
        
        startEven,end = (x + x0,h*k + h0), (x,h*k + h0)
        startOdd ,end_m = (x + x0,h*(k+middle) + h0), (x,h*(k+middle) + h0)
        arrow(screen, startEven,end, Blue,Black)
        time.sleep(0.1)
        arrow(screen, startOdd,end , Red ,Black)
        
        time.sleep(0.1)

        arrow(screen,startEven,end_m, Blue  ,Black)
        time.sleep(0.1)
        arrow(screen,startOdd,end_m ,Dark_red,Black)
    
        time.sleep(0.1)
    
    
    

if __name__ == "__main__":

    display(screen,positions)
    informative()
    
    time.sleep(1)

    fft_animation(positions,N,h0)
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
        
        