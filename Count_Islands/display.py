from algorithms.data_struct.ChildUnionFind import *
import pygame,time,random
from graph.Continental import M, node_color
from  graph.matriz import WHITE, blue
from graph.color import *

ROWS = len(M)
COLS = len(M[0])

N_islands = 0

print(ROWS,COLS)
pygame.init()

forget = (1,0,0)

screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))


def display_islands_map(done,speed= 10):
    if(done): return

    for y in range(len(M[0])):
        for x in range(len(M)):
            Colour = node_color[x][y]
            if node_color[x][y][0] < 200 and node_color[x][y][1] < 200 and node_color[x][y][2]  <200:
                Colour = (node_color[x][y][0] + 50,node_color[x][y][1]+50,node_color[x][y][2]+50)
            pygame.draw.rect(screen,Colour , (M[x][y][0],M[x][y][1] ,4, 4))
            if node_color[x][y]==forget:
                pygame.draw.rect(screen,(0,0,0) , (M[x][y][0],M[x][y][1] ,4, 4))
    
    pygame.display.update()

def print_square(i,j):
    pygame.draw.rect(screen, node_color[i][j], (M[i][j][0],M[i][j][1] ,4, 4))
    pygame.display.update()
    

def display_islands_numbers(N_islands):
    pygame.draw.rect(screen, (0,0,0), (760,10 ,300, 200))    # erase what was before in the island couting

    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("N° islands = " + str(N_islands) ,True,(255,255,0))                   # print counting      
    screen.blit(text,text.get_rect(center = (855,100)))
