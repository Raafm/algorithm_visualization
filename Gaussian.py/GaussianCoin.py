import pandas as pd 
import numpy as np
from math import comb
def throws(N_dices = 10,n_faces = 2):
    " faces go from 0 to n_faces"
    maximo = (n_faces-1)*N_dices
    
    results = np.array(list( int(comb(N_dices,k)) for k in range(maximo+1)))

    df_res = pd.DataFrame(results)
    df_res.columns = ["N° formas"]

    return df_res
    
for _,i in throws(10).iterrows():
    print(int(i))


import pygame,time
from random import randint
from colors import *


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
ground = 600
size_rate = 1
init_pos = 400


def print_rect(screen,arr,i,color):

    if i >= len(arr): return
    pygame.draw.rect(   screen   ,  color   ,   (init_pos + (square_w2th+space)*i , ground - size_rate*arr[i],    square_w2th  ,  size_rate*arr[i])  )
    
    pygame.display.update()
    

def display(screen,arr,pivot_pos = None, display_name = True):
    size_rate = 400/max(arr)
    pygame.draw.rect(screen,Black,(0,0,screen_w2th-150,screen_height))
    if display_name:
        font = pygame.font.Font('freesansbold.ttf',30)
        text = font.render(f"{len(arr)-1} coins",True,White)                  
        screen.blit(text,text.get_rect(center = (400,30)))
    for i in range(len(arr)):
        pygame.draw.rect(   screen   ,  White    ,   (init_pos + (square_w2th+space)*i , ground - size_rate*arr[i],    square_w2th  ,  size_rate*arr[i])  )
    
    if pivot_pos is not None:
        i = pivot_pos
        pygame.draw.rect(   screen   ,  White    ,   (init_pos + (square_w2th+space)*i , ground - size_rate*arr[i],    square_w2th  ,  size_rate*arr[i])  )

    pygame.display.update()

print(throws(10)["N° formas"].tolist())
display(screen, throws(100)["N° formas"].tolist())

i = 1
running = True
pause = False
while running:
            # pygame stuff:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                   #exit pygame,
            running = False                          #exit() program    
        if event.type == pygame.KEYDOWN:        
            if event.key == pygame.K_SPACE:     #press breakspace to pause or play
                pause = not pause   
                time.sleep(0.2)
        
        if pause:
            continue

    if pause: continue
    time.sleep(0.1)
    display(screen, throws(i)["N° formas"].tolist())
    i+=1
