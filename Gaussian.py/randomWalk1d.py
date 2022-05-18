import pygame,time,random,math,numpy as np
from colors import *

pygame.init()


screen_height = 700
screen_width = 1300
screen = pygame.display.set_mode((screen_width,screen_height))
ground = 600
init_pos = 200

def arrow(screen, start, end, lcolor = (255,255, 255), tricolor = (255,255,255),  trirad= 6, thickness=3):
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






def update_histogram(distribuicao_dict,show = True):
    ground_hist = screen_height -50
    for x,freq in distribuicao_dict.items():
        pygame.draw.rect(screen,Green,(x,ground- 10*freq,10,10*freq)) 
    if show:pygame.display.update()

class walker:
    def __init__(self,init_pos = (screen_width/2,ground - 15), probabilities = (0.5,0.5),color = Cyan):
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.p = probabilities
        self.show = True
        self.color = color
        pygame.draw.circle(screen,self.color,(self.x,self.y),10)

    def update(self,last_pos):
        pos = self.x ,self.y
        
        pygame.draw.circle(screen,   Black  ,last_pos,11)
        
        pygame.draw.circle(screen,self.color,pos     ,10)
        
        if self.show:pygame.display.update()
        

    def move(self,pos = None):
        y0 = ground
        x0 = init_pos

        #arrow(screen,(x0,y0),(1000,y0))
        #arrow(screen, (x0,y0),(x0,50))

        last = self.x,self.y
        if pos: self.x = pos[0]
        else:self.x += 10*np.random.choice([-1,1],p= self.p)
        self.update(last)
        return self.x,self.y

N_bebados = 10
bebados = []
for _ in range(1,N_bebados):
    bebado = walker();bebado.show = False
    bebados.append(bebado)
bebado = walker();bebado.show = False
bebados.append(bebado)

dist = {}

y0 = ground
x0 = init_pos   

arrow(screen,(x0,y0),(1000,y0))
arrow(screen, (x0,y0),(x0,50))
pygame.draw.rect(screen,Cyan,(screen_width/2,ground +2,5,5))
pygame.display.update()
time.sleep(2)

N_steps = 50

font = pygame.font.Font('freesansbold.ttf',30)
text = font.render(f"{N_steps} moves",True,White)                  
screen.blit(text,text.get_rect(center = (100,100)))
text = font.render(f"{N_bebados} particles",True,White)                  
screen.blit(text,text.get_rect(center = (100,200)))
pygame.display.update()
time.sleep(2)

pause = False
while pause:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:        
            if event.key == pygame.K_SPACE:     #press breakspace to  play
                pause = False   
                time.sleep(0.2)
        


running = True
while running:
    for step in range(N_steps):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
   
        for bebado in bebados:
            bebado.move()
        update_histogram(dist,show = True)
        time.sleep(0.01)
        

    for bebado in bebados:
        if bebado.x in dist: dist[bebado.x] += 1 
        else: dist[bebado.x] = 1
        pygame.draw.circle(screen, Lime,(bebado.x,bebado.y),10)
    pygame.display.update();time.sleep(0.3)
    update_histogram(dist)
    for bebado in bebados:
        bebado.move((screen_width/2,ground - 15))