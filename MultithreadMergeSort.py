import pygame,time
from random import randint
from threading import Thread, Lock, Condition


from algorithms.colors import *


mutex_stack = Lock()
mutex_ponto = Lock() 
mutex_display = Lock()
N_operantes = 0

pygame.init()


screen_height = 700
screen_width = 1250
screen = pygame.display.set_mode((screen_width,screen_height))

screen.fill((0,0,0))
square_width    =       3
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

N_active = 0
mutex = Lock()


def display_Nthreads(color):
    pygame.draw.rect(screen, Dark_gray, (1140,145+150 ,80, 60))    # erase what was before in the prime 
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render(str(N_active) ,True, color)                      
    screen.blit(text,text.get_rect(center = (1180,180+150)))
    mutex_display.acquire()
    pygame.display.update()
    mutex_display.release()

def print_rect(screen,arr,i,color):
    mutex_display.acquire()
    if i >= len(arr): return
    pygame.draw.rect(   screen   ,  color   ,   (10 + (square_width+space)*i , ground - size_rate*arr[i],    square_width  ,  size_rate*arr[i])  )
    
    pygame.display.update()
    mutex_display.release()

def display(screen,arr):

    mutex_display.acquire()
    pygame.draw.rect(screen, Black,(0,0,screen_width-150,screen_height))
    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("Multithread MergeSort.",True,Green)                        
    screen.blit(text,text.get_rect(center = (400,30)))
    for i in range(len(arr)):
        pygame.draw.rect(   screen   ,  rect_color[i]    ,   (10 + (square_width+space)*i , ground - size_rate*arr[i],    square_width  ,  size_rate*arr[i])  )
    
    pygame.display.update()
    mutex_display.release()


def Merge(arr,start,end):
    temp_arr = list(range(start,end+1))
    middle = (start+end)//2

    i1,i2 = start,middle+1
    i3 = 0

    while i1 <= middle and i2 <= end:

        if arr[i2] < arr[i1]:
            print_rect(screen,arr,i2,Dark_yellow)
            time.sleep(0.02)
            temp_arr[i3] = arr[i2]
            i2 += 1
            i3 += 1
            
        else:
            print_rect(screen,arr,i1,Dark_yellow)
            time.sleep(0.02)
            temp_arr[i3] = arr[i1]
            i1 += 1
            i3 += 1
            
    
    while i1 <= middle:
        print_rect(screen,arr,i1,Dark_yellow)
        time.sleep(0.02)
        temp_arr[i3] = arr[i1]
        i1 += 1
        i3 += 1

    while i2 <= end:
        print_rect(screen,arr,i2,Dark_yellow)
        time.sleep(0.02)
        temp_arr[i3] = arr[i2]
        i2 += 1
        i3 += 1

    
    for i,x in enumerate(temp_arr):
        arr[i+start] = x
        print_rect(screen,arr,i+start,Lime)
        time.sleep(0.01)
    

def MergeSort(*args):

    arr,start,end,Nthreads = args
    
    print(start,end)
    print(arr[start:end+1],"\n")

    global N_active


    if start < end:
        r = 255*(N_active/200) if  N_active > 160 else(  ( 255*(N_active/200) if N_active > 100 else ( 50 if N_active > 8 else 10*N_active) )  )
        color = ( r , 255*(1-N_active/200), 255*(1-N_active/400) )
        print(color)
        mutex.acquire()
        N_active += 1
        mutex.release()

        display_Nthreads(color)

        rect_color[start:end+1] = list( color for _ in range(start,end+1))
        rect_color[start] = rect_color[end] =  Green 
        display(screen,arr)
        
        time.sleep(1)
    
    
        middle = (start + end)//2

        


        #t1 = Thread(target= MergeSort,args=(arr, start, middle, Nthreads))
        t2 = Thread(target= MergeSort,args=(arr, middle+1, end, Nthreads))

        #t1.start()
        t2.start()
        
        MergeSort(arr, start, middle, Nthreads)
        #t1.join()
        t2.join()
        
        rect_color[start:end+1] = list(color for _ in range(start,end+1))
        rect_color[start] = rect_color[end] =  Green 
        display(screen,arr)
        time.sleep(1)

        Merge(arr, start, end)

        rect_color[start:end+1] = list(Lime for _ in range(start,end+1))
        rect_color[start] = rect_color[end] =  Lime 
        display(screen,arr)

        mutex.acquire()
        N_active -= 1
        mutex.release()

        display_Nthreads(color)

        time.sleep(0.5)

        
        print('sorted:',arr[start:end+1])





if __name__ == "__main__":
    
    Nthreads = 4     # max number of threads
    N = 200
    arr = list(randint(5,205) for _ in range(N))
    rect_color = list(White for _ in range(N))
    display(screen,arr)
    time.sleep(1)

    print(arr)
    
    start,end = 0,len(arr)-1

    
    font = pygame.font.Font('freesansbold.ttf',17)
    text = font.render('N° of threads:' ,True, White)                      
    screen.blit(text,text.get_rect(center = (1180,180+95)))
    pygame.display.update()

    display_Nthreads(Black)

    t = Thread(target= MergeSort,args=(arr,start, end, Nthreads))
    t.start()
    t.join()
    
    print(arr)
    running = True
    while running :

        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                running = False                          #exit() program    



