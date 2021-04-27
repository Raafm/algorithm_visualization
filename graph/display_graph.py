import pygame
def show_weight(screen, weight, position, font):
    
    weight_color = (200, 50, 50)
    text = font.render(str(weight), True, weight_color)
    screen.blit(text, position)

def median_point(p1, p2):
    return ((p1[0] + p2[0])/2,  (p1[1] + p2[1])/2)

def display_graph(screen, graph, nodes, edge_dict, number_size, font):
    

    number_color = (255, 0, 255)
    for edge in edge_dict:

        n1, n2 = edge
        posicao1, posicao2 = nodes[n1][1], nodes[n2][1]

        color_edge, weight, _ = edge_dict[edge]

        pygame.draw.line(screen, color_edge, posicao1, posicao2, 2)
        show_weight(screen, int(weight), median_point(posicao1, posicao2), font)


    for indice, (color,  posicao, raio)  in enumerate(nodes):
        pygame.draw.circle(screen,  color, posicao, raio)
        text = font.render(str(indice), True, number_color)
        screen.blit(text, text.get_rect(center = posicao))

    pygame.display.update()

def modify_node(screen,   nodes,  color,  node_number, number_color,  font, radius = 7,  update = False):
    nodes[node_number][0] = color
    nodes[node_number][2] = radius
    
    if update:
        
        color,  posicao, raio = nodes[node_number]
        pygame.draw.circle(screen,  color, posicao, raio)
        text = font.render(str(node_number), True, number_color, )
        screen.blit(text, text.get_rect(center = posicao))
        pygame.display.update()

def modify_edge(screen,   edge_dict,   nodes,   color,   edge,  font, width = 2, update = False):   
    
    radius = 7
    
    edge_dict[edge] = ( color ,  edge_dict[edge][1] ,  width)
    color_edge,  weight , width = edge_dict[edge]
    
    if update:
        n1, n2 = edge
        posicao1, posicao2 = nodes[n1][1],  nodes[n2][1]

        color_edge,  weight = edge_dict[edge]

        pygame.draw.line(screen, color_edge, posicao1, posicao2, width)
        show_weight(screen, int(weight), median_point(posicao1, posicao2), font)

        modify_node(screen,   nodes,   nodes[n1][0],   n1,  font, radius,  update = True)
        modify_node(screen,   nodes,   nodes[n2][0],   n2,  font, radius,  update = True)
         
        pygame.display.update()



if __name__ == '__main__':




    from grafo import graph, edge_dict, nodes
    import time
    number_size = 10
    radius = 7
    weight_color = (255,  0, 0)
    screen_color = (0, 0, 0)
    number_color =(50, 150, 200)
    green = (0,   200,   80)
    default_node_color = (100, 200, 255)
    yellow = (255, 200, 100)

    color_cur_node = green
    color_neighbour_node = yellow
    source = 1 #int(input("fonte (int de 0 a 39): "))                                      # recebe fonte
    speed = 2.5 #float(input("speed (numero quebrado ou nao de 0 ate 3): "))
    
    pygame.init()
        
    screen_height = 700
    screnn_width = 1000
    screen = pygame.display.set_mode((screnn_width, screen_height))
    font = pygame.font.Font('freesansbold.ttf', number_size)

    display_graph(screen, graph, nodes, edge_dict, number_size)
    sono =2
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame, 
                quit()                          #exit() program


