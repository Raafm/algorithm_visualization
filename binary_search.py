from graph.Continental import M
import pygame,time,random


COLS = len(M[0])
ROWS = len(M)
partes = 1
COLS //= partes

N = ROWS*COLS
print(N)



target =  random.randint(0,1020)
beggining = 0
end = N-1
middle = (beggining+end)//2

middle_color = (0,200,0)
end_color = (255,0,0)
beggining_color = (0, 0, 255)
target_color = (0, 255, 0)


pygame.init()


screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))

search_array = []
for _ in range(N):
    x = random.randint(0,10000)
    search_array.append(x)

search_array.sort()


def print_square(element,color=False,show = True):

    if color is False:
            color = (search_array[element]//40,0,255 - search_array[element]//40)

    i = element//ROWS               
    j = element%ROWS

    pygame.draw.rect(screen, color, (M[j][i][0],M[j][i][1] ,4, 4))
    
    if show:
        pygame.display.update()





for element in range(N):
    print_square(element,False,random.randint(0,10)==0)

pygame.display.update()



font = pygame.font.Font('freesansbold.ttf',30)
text = font.render("Binary search. ",True,(150,150,150))                        
screen.blit(text,text.get_rect(center = (400,30)))

font = pygame.font.Font('freesansbold.ttf',20)
text = font.render("target: " ,True, (150,150,150))                         
screen.blit(text,text.get_rect(center = (875,100)))

pygame.draw.rect(screen, (0, 65, 255), (840,170 ,60, 60))    # erase what was before in the island couting
font = pygame.font.Font('freesansbold.ttf',20)
text = font.render(str(target) ,True, (255,255,255))                      
screen.blit(text,text.get_rect(center = (870,200)))


font = pygame.font.Font('freesansbold.ttf',20)
text = font.render("actual: " ,True, (150,150,150))                         
screen.blit(text,text.get_rect(center = (870,280)))

time.sleep(1)



running = True
pause =       False   
N_search = 10
new_search = True
while running:



    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_SPACE:         # click breakspace for pause
                pause = not pause                   # if it is paused, click breakspace for play(resume)
                time.sleep(0.2)
    
    if pause:
        continue

    
    if new_search:
        
        if N_search:
            N_search -= 1
        else:
            new_search = False
            pause = True
            continue


        target = random.randint(0,1020)
        for element in range(N):
            if search_array[element] == target:
                print_square(element,target_color,False)
                continue
            print_square(element,False,False)
        
       
        new_search = False
        

    
        pygame.draw.rect(screen, (0, 65, 255), (840,170 ,60, 60))    # erase what was before in the island couting
        font = pygame.font.Font('freesansbold.ttf',20)
        text = font.render(str(target) ,True, (255,255,255))                      
        screen.blit(text,text.get_rect(center = (870,200)))
        pygame.display.update()

        beggining, end = 0,N-1
        time.sleep(2)


    print_square(beggining,(255,255,0))
    print_square(end,(255,255,255))

    middle = (beggining+end)//2
    pygame.draw.rect(screen, (0, 255, 0), (840,365 ,60, 60))    # erase what was before in the island couting
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render(str(search_array[middle]) ,True, (255,255,255))                      
    screen.blit(text,text.get_rect(center = (870,400)))
    print_square(middle,(255,255,0))
    

    if  target < search_array[middle]:

        for x in range(end,middle-1,-1):
            print_square(x,(255,255,0),random.randint(0,500)==0)
        end = middle -1;        
        print_square(end,end_color) # erro quando middle -1 < 0


    elif target > search_array[middle]:
    
       
        for x in range(beggining,middle+1):
            print_square(x,(255,255,0),random.randint(0,500)==0)
        beggining = middle + 1 ;
        print_square(beggining,(255,255,255))  #erro quando middle+1 >= N


    else:
        for x in range(beggining,middle):
            print_square(x,(255,255,0),random.randint(0,500)==0)
        for x in range(end,middle,-1):
            print_square(x,(255,255,0),random.randint(0,500)==0)

        end = middle + 1
        beggining = middle -1
        print_square(end,end_color)  #erro quando middle+1 >= N
        print_square(beggining,beggining_color) 


        print_square(middle,middle_color);
        #pause = True;
        pygame.draw.rect(screen, (0, 255, 0), (840,365 ,60, 60))    # erase what was before in the island couting
        font = pygame.font.Font('freesansbold.ttf',20)
        text = font.render(str(search_array[middle]) ,True, (255,255,255))                      
        screen.blit(text,text.get_rect(center = (870,400)))
        print_square(middle,middle_color)
        new_search = True


    if end < beggining : new_search = True

    time.sleep(0.5)