import pygame,time,random
from graph.color import *
from algorithms.data_struct.linked_list import linked_list


pygame.init()


screen_height = 700
screen_width  = 1250
screen = pygame.display.set_mode((screen_width,screen_height))

screen.fill(Black)
Time = 0.05

def pow(base,exp):
    p = base
    for _ in range(exp):
        p *= base
    return p


def HashF(x,m):
    return x%m

def reHashF(table):
    pygame.draw.rect(screen,Black,(0,80,screen_width,screen_height))
    TABLE_SIZE = len(table)*2
    new_table  = list( linked_list() for _ in range(TABLE_SIZE) )
    global growths
    global last_height
    global Time
    last_height = list( 145 for _ in range(TABLE_SIZE))

    display_table(new_table,Cyan)

    for i in range(len(table)): 
        for _ in range(table[i].size):
            data = table[i].parse()
            key = HashF(data,TABLE_SIZE) 
            new_table[key].push_back(data)
            display_insertion(id,key,Blue)
            time.sleep(Time)    

    display_table(new_table,White,Creamer)
    return new_table



def display_table(table,color_arr = White, color_node = Creamer):
    pygame.draw.rect(screen,Black,(0,80,screen_width,screen_height))

    y = 125
    for i in range(len(table)):
    
        x = 10+ 19*i
        pygame.draw.rect(screen, color_arr, (x, y,18, 20))
        font = pygame.font.Font('freesansbold.ttf',13)
        text = font.render(str(i) ,True, Black)                      
        screen.blit(text,text.get_rect(center = (x+9, y+10)))
        
        for h in range(0,table[i].size):
            
            pygame.draw.line(screen,color_node,(x+9,y+40*h+20),(x+9,y+40*(h+1)+20))
            pygame.draw.circle(screen,color_node,(x+9,y+40*(h+1)+20),7)

            font = pygame.font.Font('freesansbold.ttf',7)
            text = font.render(str(table[i].parse()) ,True, Black)                      
            screen.blit(text,text.get_rect(center = (x+9, y+40*(h+1)+20)))

    pygame.display.update()

def display_calculation(id,key):
    pygame.draw.rect(screen,Black,(0,0,screen_width,80)) 
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("h(",True,White)                   
    screen.blit(text,text.get_rect(center = (screen_width//2,50)))
    text = font.render(str(id) ,True,Lime)                   
    screen.blit(text,text.get_rect(center = (screen_width//2 + 25,50)))
    text = font.render(") =",True,White)                   
    screen.blit(text,text.get_rect(center = (screen_width//2 + 55,50)))
    text = font.render( str(key),True,Dark_yellow)                   
    screen.blit(text,text.get_rect(center = (screen_width//2  + 80,50)))

def display_insertion(id,key,color_node = Creamer):
    global last_height

    y = last_height[key]
    x = 10 + 19*key

    pygame.draw.line(  screen, color_node, (x+9,y) , (x+9,y+40) )
    pygame.draw.circle(screen, color_node, (x+9,y+40) ,    7    )

    font = pygame.font.Font('freesansbold.ttf',7)
    text = font.render(str(id) ,True, Black)                      
    screen.blit(text,text.get_rect(center = (x+9, y+40)))
    pygame.display.update()

    last_height[key] += 40

font = pygame.font.Font('freesansbold.ttf',30)
text = font.render("Hash animation",True,Creamer)                   
screen.blit(text,text.get_rect(center = (screen_width//2,50)))
pygame.display.update()
time.sleep(1)


growths     = 1
TABLE_SIZE  = 8
table       = list( linked_list() for _ in range(TABLE_SIZE) )
last_height = list(      145      for _ in range(TABLE_SIZE) )

display_table(table)
time.sleep(2)


for i in range(250):

    if i == 4*TABLE_SIZE:

        if growths == 1:Time = 0.05
        if growths == 2:Time = 0.06
        if growths == 3:Time = 0.07

        pygame.draw.rect(screen,Black,(0,0,screen_width,screen_height)) 
        font = pygame.font.Font('freesansbold.ttf',20)
        text = font.render("ReHash",True,Cyan)                   
        screen.blit(text,text.get_rect(center = (screen_width//2,50)))
        pygame.display.update()
        
        time.sleep(0.1)   

        table = reHashF(table)
        TABLE_SIZE *= 2   
        growths += 1

                   


    id = random.randint(0,999)
    key = HashF(id,TABLE_SIZE)
    table[key].push_back(id)


    display_calculation(id,key)
    time.sleep(Time)
    display_insertion(id,key)
    #display_table(table)

    x = 10+19*key
    y = 125
    pygame.draw.rect(screen,Dark_yellow,(x,y,18,20))
    pygame.display.update()

    time.sleep(Time)

    pygame.draw.rect(screen, White, (x, y,18, 20))
    font = pygame.font.Font('freesansbold.ttf',13)
    text = font.render(str(key) ,True, Black)                      
    screen.blit(text,text.get_rect(center = (x+9, y+10)))
    pygame.display.update()

    


time.sleep(0.5)
pygame.draw.rect(screen,Black,(0,0,screen_width,80)) 
display_table(table)

pause = True
running =  True
while running :

    # pygame stuff:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                   #exit pygame,
            running = False                          #exit() program

