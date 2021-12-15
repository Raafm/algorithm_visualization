import pygame,random,time
from math import log
from algorithms.colors import *
from algorithms.data_struct.priority_queue import Heap

color_list = [
Dark_red     ,   
Blue	     , 
deepskyblue	   , 
Yellow	     ,
lightsteelblue,
Lime,
Dark_yellow  ,  
Flame        ,  
Cyan 	     ,  
Magenta	     ,  
Gray	     ,  
Dark_gray    ,  
Maroon 	     ,  
skyblue	       ,
Olive  	     ,  
dodgerblue	   ,
Purple 	     ,  
cornflowerblue,
Teal	     ,  
steelblue	   ,
Navy	     ,  
cadetblue	   ,
Castanho	 ,  
mediumslateblue,
Orange	       ,
Springgreen	   ,
royalblue   	,
]
t = 0


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


def print_rect(screen,arr,i,color):

    if i >= len(arr): return
    pygame.draw.rect(   screen   ,  color   ,   (10 + (square_width+space)*i , ground - size_rate*arr[i],    square_width  ,  size_rate*arr[i])  )
    
    pygame.display.update()
    time.sleep(0.005)


def display(screen,arr,pivot_pos = None):


    pygame.draw.rect(screen,Black,(0,100,screen_width-150,screen_height))

    for i in range(len(arr)):
        pygame.draw.rect(   screen   ,  rect_color[i]    ,   (10 + (square_width+space)*i , ground - size_rate*arr[i],    square_width  ,  size_rate*arr[i])  )
    
    if pivot_pos is not None:
        i = pivot_pos
        pygame.draw.rect(   screen   ,  rect_color[i]    ,   (10 + (square_width+space)*i , ground - size_rate*arr[i],    square_width  ,  size_rate*arr[i])  )

    pygame.display.update()

def show_Heap(H):
    pygame.draw.rect(screen, Light_grey, (1150,145+100 ,80, 60))    # erase 
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render(str(H.__len__()) ,True, Black)                      
    screen.blit(text,text.get_rect(center = (1190,180+100)))
    pygame.display.update()
    time.sleep( 0.015*log(H.__len__()+1,2) )


def print_range(i,f,color):
    global t
    
    for index in range(i,f+1):
        rect_color[index] = color
        print_rect(screen,arr,index,color)
    t += 1
    if t == len(color_list):t = 0


def HeapMerge(arr,runs):
    H = Heap(comp = lambda a,b: a > b)
    
    font = pygame.font.Font('freesansbold.ttf',18)
    text = font.render( 'Heap size',True, Light_grey)                      
    screen.blit(text,text.get_rect(center = (1195,180+50)))
    show_Heap(H)
    time.sleep(1)

    
    for i,f in runs:
        H.insert((arr[i],i,f))
        show_Heap(H) 
        print_rect(screen,arr,i,Black)

    aux_arr = list( 0 for _ in range(len(arr)))
    aux = 0
    for _ in range(len(arr)):

        # coloca na Heap
        aux_arr[aux],index,last = H.pop()         
        

        print_rect(screen,aux_arr,aux,White) 
        print_rect(screen,arr,index,Light_grey)
        show_Heap(H)
        print_rect(screen,arr,index,Black)


        if index <= aux:
            print_rect(screen,aux_arr,index,White) 
        aux += 1

        # se o elemento tirado for o ultimo nao coloca o prox na Heap
        if index < last: 
            H.insert((arr[index+1],index+1,last))
            show_Heap(H)


    arr[:] = aux_arr[:]
    display(screen,arr)

def reverse(arr,start,end):
    global t
    i = start
    f = end

    while i < f:
        arr[i],arr[f] = arr[f],arr[i]
        i += 1
        f -= 1
        
    display(screen,arr)  
    print_range(i,f,Red)
    
    time.sleep(0.05)
    print_range(i,f,color_list[t])


def Sort(arr):
    global t
    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("HeapMerge Sort. ",True,Light_grey)                        
    screen.blit(text,text.get_rect(center = (400,30)))

    last = len(arr) -1
    i = 0
    f = 0
    runs = []

    while f < len(arr):
        #ascending
        if f < len(arr)-1 and arr[f] <= arr[f+1]:
            while f < last  and arr[f] <= arr[f+1]:
                f += 1

            if i <= f:
                runs.append((i,f))
                print_range(i,f,color_list[t])
            
            display(screen,arr)
            f += 1
            i = f
        if f == len(arr):break
        #descending
        while f < last and arr[f] >= arr[f+1]:
            f += 1


        i0,f0 = i,f
        reverse(arr,i0,f0)
        
        if i <= f:
            if f < last and arr[f] > arr[f+1]:
                runs.append((i,f))
                print_range(i,f,color_list[t])
            
            elif f == last:
                runs.append((i,f))
                print_range(i,f,color_list[t])
            
            else:
                continue


        f += 1
        i  = f


    display(screen,arr)
    time.sleep(1.5)
    HeapMerge(arr, runs)


if __name__ == "__main__":
    N = 200
    arr        = list(random.randint(5,200) for _ in range(N))
    rect_color = list(White for _ in range(N))

    display(screen,arr)
    time.sleep(1)
    
    Sort(arr)
    print(arr)
    
    f, last = 0,N-1
    while f < last  and arr[f] <= arr[f+1]:
        f += 1
    print(f,"is sorted:",f == last)
    running = True
    while running :

        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                running = False                          #exit() program    



