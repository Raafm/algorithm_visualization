n_node = 0
cor = (255,255,255)
raio = 12
# for x in range(50,950,50):
#     print(f" [cor, ({x} , {750 - x}), raio],    # node {n_node}")
#     n_node += 1
# print("##################################################3")
# for x in range(50, 950,50): 
#     print(f"[cor, ({x} , {750 - x}), raio],    # node ")


tree_graph  = [

]


if __name__ == '__main__':

    import pygame
    number_size = 10
    number_color = (0,0,0)
    pygame.init()
    font = pygame.font.Font('freesansbold.ttf',number_size)

    screen_height = 700
    screnn_width = 1000
    screen = pygame.display.set_mode((screnn_width, screen_height))
    screen.fill((0, 0,0))

    for indice,(color, posicao,radius) in enumerate(tree_graph):
        pygame.draw.circle(screen,  color, posicao, radius)
        text = font.render(str(indice), True, number_color)    
        screen.blit(text, text.get_rect(center = posicao))
    
    pygame.display.update()
                
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                quit()                          #exit() program


        pygame.display.update()