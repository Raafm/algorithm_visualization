import pygame,time
from random import randint
from algorithms.colors import *


pygame.init()


screen_height = 700
screen_w2th = 1300
screen = pygame.display.set_mode((screen_w2th,screen_height))

screen.fill((0,0,0))
square_w2th    =       3
space = 2
index_color     =   (0,200,0)
index2_color    =   (200,200,0)
numb_color      =   (50,50,250)
const_color     =   (255,255,255)
sum_color       =   (250,250,0)
duplicate_color =   (255,0,0)
ground = 500
size_rate = 2
rect_color = []


def print_rect(screen,arr,i,color):

    if i >= len(arr): return
    pygame.draw.rect(   screen   ,  color   ,   (10 + (square_w2th+space)*i , ground - size_rate*arr[i],    square_w2th  ,  size_rate*arr[i])  )
    
    pygame.display.update()
    

def display(screen,arr,pivot_pos = None, display_name = True):
    
    pygame.draw.rect(screen,Black,(0,0,screen_w2th-150,screen_height))
    if display_name:
        font = pygame.font.Font('freesansbold.ttf',30)
        text = font.render("SelectionSort",True,White)                  
        screen.blit(text,text.get_rect(center = (400,30)))
    for i in range(len(arr)):
        pygame.draw.rect(   screen   ,  rect_color[i]    ,   (10 + (square_w2th+space)*i , ground - size_rate*arr[i],    square_w2th  ,  size_rate*arr[i])  )
    
    if pivot_pos is not None:
        i = pivot_pos
        pygame.draw.rect(   screen   ,  rect_color[i]    ,   (10 + (square_w2th+space)*i , ground - size_rate*arr[i],    square_w2th  ,  size_rate*arr[i])  )

    pygame.display.update()
   

def take_possession(color,left,right):
    for i in range(left,right+1):
        rect_color[i] = color

if __name__ == '__main__':
    N = 200
    
    arr = list(randint(0,200) for _ in range(N))
    rect_color = list(White for _ in range(N))

    k = 100

    display(screen,arr,display_name = False)
    time.sleep(1)

    pygame.draw.rect(screen, Green, (1170,145+100*3 ,80, 60))   
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("k = " + str(k) ,True, White)                      
    screen.blit(text,text.get_rect(center = (1210,180+100*3)))
    
    pygame.display.update()

    time.sleep(1)
    display(screen,arr)
    time.sleep(1)

    i,f,Max_pos = 0,N-1,0
    Max = arr[0]

    running = True
    pause = False
    while running:
                # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                running = False                          #exit() program    

        if pause: continue

    
        if arr[i] > Max:
            print_rect(screen,arr,i,Red)
            print_rect(screen,arr,Max_pos,Green)
            Max_pos = i
            Max = arr[i]
        else:
            print_rect(screen,arr,i,Green)

        time.sleep(0.0005)

        
        if i == f:
            print_rect(screen,arr,Max_pos,Green)
            #put max at the end of the section
            arr[Max_pos],arr[f] = arr[f], arr[Max_pos] #swap
            rect_color[f] = Dark_red
            time.sleep(0.001)
            
            
            if f == k-1:
                
                print_rect(screen,arr,f,White)
                
                pygame.draw.rect(screen, Green, (1145,145+100*3 ,130, 60))   
                font = pygame.font.Font('freesansbold.ttf',20)
                text = font.render("arr[k-1]="+  str(arr[Max]) ,True, White)                      
                screen.blit(text,text.get_rect(center = (1210,180+100*3)))
                
                pygame.display.update()

                pause = True
                continue


            f-=1
            i = 0
            Max_pos,Max = 0,arr[0]
            
            pygame.draw.rect(screen, Dark_red, (1170,145+100*1 ,80, 60))   
            font = pygame.font.Font('freesansbold.ttf',20)
            text = font.render("f = " + str(f)  ,True, White)                      
            screen.blit(text,text.get_rect(center = (1210,180+100*1)))
            display(screen,arr)

        else:
            i += 1
