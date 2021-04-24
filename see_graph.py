import pygame
from grafo import nodes, lista_arestas

pygame.init()

altura_tela = 700
largura_tela = 1000
tamanho_numero_indice =10
cor_numero_indice =(50,150,200)
screen = pygame.display.set_mode((largura_tela,altura_tela))

screen.fill((0,0,0))
font = pygame.font.Font('freesansbold.ttf',tamanho_numero_indice)

for cor, inicio, fim, peso in lista_arestas:
    pygame.draw.line(screen,cor,nodes[inicio][1],nodes[fim][1],2)
    print(cor)

for indice,(cor, posicao,raio)  in enumerate(nodes):
    pygame.draw.circle(screen, cor,posicao,raio)
    text = font.render(str(indice),True,cor_numero_indice)
    screen.blit(text,text.get_rect(center = posicao))



while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                   #exit pygame,
            quit()                          #exit() program


    pygame.display.update()
