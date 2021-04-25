import pygame
from grafo import graph,edge_dict,nodes
import time
number_size = 10
radius = 7
weight_color = (255, 0,0)
screen_color = (0,0,0)
number_color =(50,150,200)

pygame.font.init()

font = pygame.font.Font('freesansbold.ttf',number_size)

def show_weight(weight,position):
    text = font.render(str(weight),True,weight_color)
    screen.blit(text,position)

def median_point(p1,p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

def display_graph(screen,graph,nodes,edge_dict):

    for edge in edge_dict:

        n1,n2 = edge
        posicao1,posicao2 = nodes[n1][1],nodes[n2][1]

        color_edge,weight = edge_dict[edge]

        pygame.draw.line(screen,color_edge,posicao1,posicao2,2)
        show_weight(int(weight),median_point(posicao1,posicao2))


    for indice,(color, posicao,raio)  in enumerate(nodes):
        pygame.draw.circle(screen, color,posicao,raio)
        text = font.render(str(indice),True,number_color)
        screen.blit(text,text.get_rect(center = posicao))

    pygame.display.update()

def set_node_color(screen,  nodes, color, node_number,  update =False):
    nodes[node_number][0] = color

    if update:
        
        color, posicao,raio = nodes[node_number]
        pygame.draw.circle(screen, color,posicao,raio)
        text = font.render(str(node_number),True,number_color,)
        screen.blit(text,text.get_rect(center = posicao))
        pygame.display.update()

def set_edge_color(screen,  edge_dict,  nodes,  color,  edge,  update =False):
    
    print()
    print(edge_dict[edge])
    edge_dict[edge] = ( color , edge_dict[edge][1] )
    color_edge, weight = edge_dict[edge]
    print("\ncolor_edge: ",color_edge)
    print("\nweight: ",weight)
    print(edge_dict[edge])
    
    if update:
        n1,n2 = edge
        posicao1,posicao2 = nodes[n1][1], nodes[n2][1]

        color_edge, weight = edge_dict[edge]

        pygame.draw.line(screen,color_edge,posicao1,posicao2,2)
        show_weight(int(weight),median_point(posicao1,posicao2))

        set_node_color(screen,  nodes,  nodes[n1][0],  n1,  update = True)
        set_node_color(screen,  nodes,  nodes[n2][0],  n2,  update = True)
        
        pygame.display.update()


if __name__ == '__main__':

    altura_tela = 700
    largura_tela = 1000
    tamanho_numero_indice = 10
    number_color = (50,150,200)

    screen = pygame.display.set_mode((largura_tela,altura_tela))

    display_graph(screen,graph,nodes,edge_dict)
    time.sleep(2)
    set_node_color(screen,nodes,(110,110,110),32,True)
    set_edge_color(screen,  edge_dict,  nodes,  (0,255,255), (3, 9), True )
    
   

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                quit()                          #exit() program



