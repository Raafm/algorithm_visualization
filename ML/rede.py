import pygame,time
from color import *

screen_height = 700
screen_width = 1300
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill((0,0,0))

pygame.init()


dist_layer = 150
dist_neuron = 150
layer_size = [2,3,4,2,1]

neuron_position = [
                    [(x, dist_neuron*y + 0 + dist_neuron*(6-layer_size[layer_index])/2) for y in range(layer_size[layer_index])]  
                        for layer_index,x in enumerate(range(100,dist_layer*len(layer_size) + 100,dist_layer))
                 ]

def mark(layer_index,neuron_index,color = White,radius = 8,show = False):

    pygame.draw.circle(screen, color, neuron_position[layer_index][neuron_index] , radius)
    if show: pygame.display.update()
    
    
        
for n_layer in range(1,len(layer_size)):
    for neuron_index in range(layer_size[n_layer]):
        for w_index in range(layer_size[n_layer - 1]):
            cur_neuron  = neuron_position[n_layer][neuron_index]
            last_neuron = neuron_position[n_layer-1][w_index]
            pygame.draw.line(screen, White, cur_neuron, last_neuron, 2)

x_out,y_out = neuron_position[-1][0]
pygame.draw.line(screen, White, (x_out+50, y_out),(x_out, y_out), 2)
for x_in,y_in in neuron_position[0]:
    pygame.draw.line(screen, White, (x_in-50, y_in),(x_in, y_in), 2)

for n_layer in range(len(layer_size)):
    for neuron_index in range(layer_size[n_layer]):
        mark(n_layer,neuron_index,White,show = True)

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

