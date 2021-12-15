import pygame,time
from random import randint
from algorithms.colors import *


pygame.init()


screen_height = 700
screen_w2th = 1300
screen = pygame.display.set_mode((screen_w2th,screen_height))

screen.fill((0,0,0))
square_w2th    =       3
space = 2
index_color     =   (0,200,0)
index2_color    =   (200,200,0)
numb_color      =   (50,50,250)
const_color     =   (255,255,255)
sum_color       =   (250,250,0)
duplicate_color =   (255,0,0)
ground = 500
size_rate = 2
rect_color = []

thread_color = [
    Teal,
    Flame,
    Castanho,
    (0,0,255),
    Magenta,
    White,
    Lime
]

def print_rect(screen,arr,i,color):

    if i >= len(arr): return
    pygame.draw.rect(   screen   ,  color   ,   (10 + (square_w2th+space)*i , ground - size_rate*arr[i],    square_w2th  ,  size_rate*arr[i])  )
    
    pygame.display.update()
    

def display(screen,arr,pivot_pos = None,display_name=True):

    pygame.draw.rect(screen,Black,(0,0,screen_w2th-150,screen_height))
    if display_name:
        font = pygame.font.Font('freesansbold.ttf',30)
        text = font.render("QuickSelect",True,White)                  
        screen.blit(text,text.get_rect(center = (400,30)))

    for i in range(len(arr)):
        pygame.draw.rect(   screen   ,  rect_color[i]    ,   (10 + (square_w2th+space)*i , ground - size_rate*arr[i],    square_w2th  ,  size_rate*arr[i])  )
    
    if pivot_pos is not None:
        i = pivot_pos
        pygame.draw.rect(   screen   ,  rect_color[i]    ,   (10 + (square_w2th+space)*i , ground - size_rate*arr[i],    square_w2th  ,  size_rate*arr[i])  )

    pygame.display.update()
   

def take_possession(id,left,right):
    for i in range(left,right+1):
        rect_color[i] = thread_color[id]


def QuickSelect(arr,N,k):

    
    print("k = ",k)
    
    trecho = 0,N-1
        
    while(True):    
        
        left,right  = trecho
        take_possession(5,0,N-1)
        take_possession(3,left,right)

        l = left
        r = right
        
        pygame.draw.rect(screen, (0,0,255), (1170,145+100*2 ,80, 60))    # erase what was before in the prime 
        font = pygame.font.Font('freesansbold.ttf',20)
        text = font.render(str(left)+","+str(right) ,True, White)                      
        screen.blit(text,text.get_rect(center = (1210,180+100*2)))

        pygame.display.update()

        if(left < right) :
            
            pivot_index = left
            pivot = arr[pivot_index]
            
            display(screen,arr)
            time.sleep(0.003)
            
            while l < r:
                
                while l < len(arr) and arr[l] <= pivot:
                    
                    print_rect(screen,arr,l,Yellow)
                    
                    time.sleep(0.003)
                    l += 1
                    
                                    
                while arr[r] > pivot:
                    
                    print_rect(screen,arr,r,Yellow)
                    
                    time.sleep(0.003)
                    r -= 1
                    

                if(l < r):
                   
                    print_rect(screen,arr,r,Red)
                    print_rect(screen,arr,l,Red)
                    
                    time.sleep(0.003)
                    arr[l], arr[r] = arr[r], arr[l]
                
                
                display(screen,arr)
                time.sleep(0.003)
                
            # Swap pivot element with element on r pointer.
            # This puts pivot on its correct sorted place.
            arr[r], arr[pivot_index] = arr[pivot_index], arr[r]
            

            display(screen,arr,pivot_pos = r)
            

            if   k-1 > r : trecho = (r+1,right); print_rect(screen,arr,r,Lime); time.sleep(0.01); print_rect(screen,arr,r,White); 
            elif k-1 < r : trecho = (left, r-1); print_rect(screen,arr,r,Lime); time.sleep(0.01); print_rect(screen,arr,r,White); 
            else: 
                print('r = ',r)
                print_rect(screen,arr,r,Lime)
                break

            print_rect(screen,arr,r,White)
            
        else: # se temos apenas um elemento na particao

            print_rect(screen,arr,left,Lime)
            time.sleep(0.1)
            break
        
    pygame.draw.rect(screen, Blue, (1145,145+100*3 ,130, 60))   
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("arr[k-1]="+  str(arr[r]) ,True, Lime)                      
    screen.blit(text,text.get_rect(center = (1210,180+100*3)))
    
    pygame.display.update()
    
    return None 




if __name__ == "__main__":
    
    N = 200
    
    arr = list(randint(0,200) for _ in range(N))
    rect_color = list(White for _ in range(N))

    print(arr)
    k = 100
    
    display(screen,arr,display_name = False)
    time.sleep(0.5)

    pygame.draw.rect(screen, (0,0,255), (1170,145+100*3 ,80, 60))   
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("k = " + str(k) ,True, White)                      
    screen.blit(text,text.get_rect(center = (1210,180+100*3)))
    
    pygame.display.update()

    display(screen,arr)
    time.sleep(0.5)

    QuickSelect(arr,N,k)

    running =  True
    while running :

        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                running = False                          #exit() program    








