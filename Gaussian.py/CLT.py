import pandas as pd 
import numpy as np
from math import comb,exp, factorial
def throws(N_dices = 10,n_faces = 2):
    " faces go from 0 to n_faces"
    maximo = (n_faces-1)*N_dices
    
    results = np.array(list( int(comb(N_dices,k)) for k in range(maximo+1)))

    df_res = pd.DataFrame(results)
    df_res.columns = ["N° formas"]

    return df_res
    


import pygame,time,math,random
from statistics import mean
from colors import *
from math import pi

pygame.init()


screen_height = 700
screen_width = 1300
screen = pygame.display.set_mode((screen_width,screen_height))

screen.fill((0,0,0))
square_w2th    =       3
space =7
index_color     =   (0,200,0)
index2_color    =   (200,200,0)
numb_color      =   (50,50,250)
const_color     =   (255,255,255)
sum_color       =   (250,250,0)
duplicate_color =   (255,0,0)
ground = 300
size_rate = 1000
init_pos = 100

def discreto(distribuicao,N_pontos):
    probabilities = np.array(list(distribuicao(x) for x in range(N_pontos)), dtype = float)
    soma = probabilities.sum()
    k = 1/soma
    return k*probabilities 

def arrow(screen, start, end, lcolor = (255,255, 255), tricolor = (255,255,255),  trirad= 5, thickness=3,show =False):
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




def plot_dist(distribuicao,N_dots = 60,N_samples = 15,show = True,erase = True):
    y0 = ground
    x0 = init_pos
    if erase: pygame.draw.rect(screen,Black,(0,0,810,ground+ 10))
    
    arrow(screen,(x0,y0),(700,y0))
    arrow(screen, (x0,y0),(x0,50))

    
    for x in range(0,N_dots):
        pygame.draw.line(screen , Cyan ,(10*x+x0,y0-size_rate*distribuicao(x)) , (10*(x+1)+x0,y0 - size_rate*distribuicao(x+1)))
    
    probabilities = discreto(distribuicao, N_dots)

    samples = []
    for x in range(N_samples):
        sample =  np.random.choice(np.arange(N_dots),p = probabilities)
        samples.append(sample)

    media = int(mean(samples))
    pygame.draw.rect(screen,Green,(10*media+x0,ground-10,5,10))    

    for x in samples:
        pygame.draw.circle(screen , Lime ,(10*x+x0,y0-size_rate*distribuicao(x)),5)    

    if show:
        pygame.display.update()

    
    return media

def update_histogram(distribuicao_dict,show = True):
    ground_hist = screen_height -50
    for media,freq in distribuicao_dict.items():
        pygame.draw.rect(screen,Green,(10*media+init_pos,ground_hist- 5*freq,5,5*freq)) 
    if show:pygame.display.update()


distribuicoes = [
    (lambda x: 0.02 if x <= 500 else 0,                 "uniform" ) ,# uniforme de 0 a 10
    (lambda x: exp(-x/10)/10,                           "exp(-x)" ) ,# exponencial
    (lambda x: 2*exp(-((x-30)**2)/100)/math.sqrt(100*pi),"gaussian" ), # gaussiana
]

N_means = 300
running = True
pause = False
while running:
            # pygame stuff:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                   #exit pygame,
            running = False                          #exit() program    

    if pause: continue

    
    for distribuicao,nome in distribuicoes:
        pygame.draw.rect(screen,Black,(screen_width//2+200,0,200,200))
        font = pygame.font.Font('freesansbold.ttf',30)
        text = font.render(nome,True,White)                  
        screen.blit(text,text.get_rect(center = (screen_width//2+300,50)))
        pygame.display.update()
        time.sleep(1)
        
        distribuicao_medias = {}
        for _ in range(N_means):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()                   #exit pygame,
                    running = False                          #exit() program 
                
            update_histogram(distribuicao_medias,show = False)
            
            media = plot_dist(distribuicao,erase = True)
            if media in distribuicao_medias: distribuicao_medias[media] += 1
            else: distribuicao_medias[media] = 1 
            time.sleep(0.04)
        pygame.draw.rect(screen,Black,(0,ground+10,810,screen_height))
            
            
            
        

