import pygame,time
from threading import Thread, Lock, Condition
from random import randint
from algorithms.data_struct.queue import queue
from algorithms.data_struct.stack import stack
from algorithms.colors import *


mutex_stack = Lock()
mutex_ponto = Lock() 
mutex_ponto = Condition()
mutex_display = Lock()
N_operantes = 0

Q = queue()

pygame.init()


screen_height = 700
screen_width = 1300
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
    pygame.draw.rect(   screen   ,  color   ,   (10 + (square_width+space)*i , ground - size_rate*arr[i],    square_width  ,  size_rate*arr[i])  )
    mutex_display.acquire()
    pygame.display.update()
    mutex_display.release()

def display(screen,arr,pivot_pos = None,display_name = True):

    mutex_display.acquire()
    pygame.draw.rect(screen,Black,(0,0,screen_width-150,screen_height))
    if display_name:
        font = pygame.font.Font('freesansbold.ttf',30)
        text = font.render("QuickSort",True,White)                  
        screen.blit(text,text.get_rect(center = (400,30)))

    for i in range(len(arr)):
        pygame.draw.rect(   screen   ,  rect_color[i]    ,   (10 + (square_width+space)*i , ground - size_rate*arr[i],    square_width  ,  size_rate*arr[i])  )
    
    if pivot_pos is not None:
        i = pivot_pos
        pygame.draw.rect(   screen   ,  rect_color[i]    ,   (10 + (square_width+space)*i , ground - size_rate*arr[i],    square_width  ,  size_rate*arr[i])  )

    pygame.display.update()
    mutex_display.release()
   

def take_possession(id,left,right):
    for i in range(left,right+1):
        rect_color[i] = thread_color[id]


def ordenar(*args):
    global N_operantes
    arr,N,id = args
    print("thread: "+str(id)+ " criada")
    

        
    while(Q.not_empty() or N_operantes > 0):
       
        # mutex para pegar um trecho 
        # para particionar (trabalhar/ bater ponto)
        mutex_ponto.acquire()

        # se nao tem particao pronta,
        # mas tem thread operando (produtora)
        # esperamos a thread liberar
        while(N_operantes > 0 and not Q.not_empty()):
            pygame.draw.rect(screen, Light_grey, (1170,145+100*id ,80, 60))    # erase what was before in the prime 
            font = pygame.font.Font('freesansbold.ttf',20)
            text = font.render(str("wait") ,True, thread_color[id])                      
            screen.blit(text,text.get_rect(center = (1210,180+100*id)))
            mutex_display.acquire()
            pygame.display.update()
            mutex_display.release()
            mutex_ponto.wait()
        
        #acabou o trabalho (arr ordenado)
        if(not Q.not_empty()):
            mutex_ponto.release()
            break
        
        top = Q.pop() #particao para operar 
        N_operantes += 1 #um a mais trabalhando
        mutex_ponto.release()


        left,right  = top
        

        l = left
        r = right
        
        pygame.draw.rect(screen, thread_color[id], (1170,145+100*1 ,80, 60))    # erase what was before in the prime 
        font = pygame.font.Font('freesansbold.ttf',20)
        text = font.render(str(left)+","+str(right) ,True, White)                      
        screen.blit(text,text.get_rect(center = (1210,180+100*1)))
        mutex_display.acquire()
        pygame.display.update()
        mutex_display.release()

        if(left < right) :
            
            pivot_index = left
            pivot = arr[pivot_index]
            
            take_possession(id,left,right)
            display(screen,arr)
            time.sleep(0.002)
            
            while l < r:
                
                
                while l < len(arr) and arr[l] <= pivot:
                    
                    print_rect(screen,arr,l,Yellow)
                    
                    time.sleep(0.002)
                    l += 1
                    
                    
                
                while arr[r] > pivot:
                    
                    print_rect(screen,arr,r,Yellow)
                    
                    time.sleep(0.002)
                    r -= 1
                    

                
                if(l < r):
                   
                    print_rect(screen,arr,r,Red)
                    print_rect(screen,arr,l,Red)
                    
                    time.sleep(0.002)
                    arr[l], arr[r] = arr[r], arr[l]
                
                
                display(screen,arr)
                time.sleep(0.002)
                
            # Swap pivot element with element on r pointer.
            # This puts pivot on its correct sorted place.
            arr[r], arr[pivot_index] = arr[pivot_index], arr[r]
            
            

            take_possession(-2,left,right)
            display(screen,arr,pivot_pos = r)
            take_possession(-1,r,r)
            print_rect(screen,arr,r,Lime)
            time.sleep(0.006)

            trecho = (r+1,right)
            mutex_stack.acquire()
            Q.insert( trecho ) # regiao critica: colocar na stack a particao esquerda
            mutex_stack.release()

            trecho = (left, r-1)
            mutex_stack.acquire()
            Q.insert( trecho ) # regiao critica: colocar na stack a particao direita
            mutex_stack.release()

            mutex_ponto.acquire()
            N_operantes -= 1 # "fim de expediente", um "operario" a menos
            mutex_ponto.release()
            
            mutex_ponto.acquire()
            mutex_ponto.notify_all()
            mutex_ponto.release()
            
        
        else: # se temos apenas um elemento na particao
            mutex_ponto.acquire()
            N_operantes -= 1
            mutex_ponto.notify_all() #must acquire lock?
            mutex_ponto.release()

            take_possession(-1,left,right)
            print_rect(screen,arr,left,Lime)
            time.sleep(0.002)
        
    
    mutex_display.acquire()
    pygame.display.update()
    mutex_display.release()
    return None 





if __name__ == "__main__":
    
    N = 200
    k = 100

    arr = list(randint(0,200) for _ in range(N))
    rect_color = list(White for _ in range(N))
    print(arr)

    Q.insert((0,N-1)) 
    display(screen,arr,display_name = False)
    time.sleep(0.5)

    pygame.draw.rect(screen, thread_color[0], (1170,145+100*3 ,80, 60))   
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("k = " + str(k) ,True, White)                      
    screen.blit(text,text.get_rect(center = (1210,180+100*3)))
    pygame.display.update()

   
    display(screen,arr)
    time.sleep(0.5)

    t = Thread(target=ordenar,args=(arr,N,0))
    t.start()
    t.join()


    print_rect(screen,arr,k-1,thread_color[0])
    pygame.draw.rect(screen, thread_color[0], (1145,145+100*3 ,130, 60))   
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("arr[k-1]="+  str(arr[k-1]) ,True, White)                      
    screen.blit(text,text.get_rect(center = (1210,180+100*3)))
    
    pygame.display.update()

    running =  True
    while running :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                running = False                          #exit() program    





