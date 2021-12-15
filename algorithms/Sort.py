import pygame,time
from random import randint
from threading import Thread, Lock, Condition
from algorithms.data_struct.queue import queue
from algorithms.data_struct.stack import stack 

from algorithms.colors import *

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


def print_rect(screen,arr,i,color):
    if i >= len(arr): return
    pygame.draw.rect(   screen   ,  color   ,   (10 + (square_width+space)*i , ground - size_rate*arr[i],    square_width  ,  size_rate*arr[i])  )
    
    pygame.display.update()
    

def display(screen,arr):
    pygame.draw.rect(screen, Black,(0,0,screen_width-150,screen_height))
    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("TimSort",True,Green)                        
    screen.blit(text,text.get_rect(center = (400,30)))
    for i in range(len(arr)):
        pygame.draw.rect(   screen   ,  rect_color[i]    ,   (10 + (square_width+space)*i , ground - size_rate*arr[i],    square_width  ,  size_rate*arr[i])  )
    
    pygame.display.update()
    

def reverse(arr,start,end):
    i = start
    f = end

    while i < f:
        arr[i],arr[f] = arr[f],arr[i]
        i += 1
        f -= 1


def Merge(arr,start,middle,end):
    
    temp_arr = list(range(start,end+1))

    i1,i2 = start,middle+1
    i3 = 0

    while i1 <= middle and i2 <= end:

        if arr[i2] < arr[i1]:
            #print_rect(screen,arr,i2,Dark_yellow)
            #time.sleep(0.02)
            temp_arr[i3] = arr[i2]
            i2 += 1
            i3 += 1
            
        else:
            #print_rect(screen,arr,i1,Dark_yellow)
            #time.sleep(0.02)
            temp_arr[i3] = arr[i1]
            i1 += 1
            i3 += 1
            
    
    while i1 <= middle and i3 < len(temp_arr):
        #print_rect(screen,arr,i1,Dark_yellow)
        #time.sleep(0.02)
        
        temp_arr[i3] = arr[i1]
        i1 += 1
        i3 += 1

    while i2 <= end and i3 < len(temp_arr):
        #print_rect(screen,arr,i2,Dark_yellow)
        #time.sleep(0.02)
        temp_arr[i3] = arr[i2]
        i2 += 1
        i3 += 1

    
    for i,x in enumerate(temp_arr):
        arr[i+start] = x
        #print_rect(screen,arr,i+start,Lime)
        #time.sleep(0.01)

    print("tam =",len(temp_arr),"  (",start,end,") = ",temp_arr)

def ascending(arr,start):
    if start == len(arr) -1: return (start, start)
    if arr[start] > arr[start+1]: return (start,start)
    
    i = start
    while i < len(arr) - 1 and arr[i] <= arr[i+1]:
        i += 1
    
    return (start,i)


def  descending(arr,start):
    if start == len(arr) -1: return (start, start)
    if arr[start] < arr[start+1]: return (start,start)
    
    i = start
    while i < len(arr) - 1 and arr[i] >= arr[i+1]:
        i += 1
    
    return (start,i)


def TimSort(arr):
    
    i = 0
    runs = queue()
    while i < len(arr):
        start,end = ascending(arr,i)
        if start == end:
            start,end = descending(arr,i)
            reverse(arr,start,end)
            
        runs.insert((start,end))
        print("insert the queue: ",(start,end))
        i = end+1
    
    while runs.not_empty():
        run1 = runs.pop()
        run2 = runs.pop()

        if run1 and run2:

            if run1 > run2:
                runs.insert(run1)
                run1 = runs.pop()
                run1,run2 = run2,run1

            start,middle = run1
            s2,end = run2
            print("Merge:" ,(start,middle),(s2,end))
            Merge(arr,start,middle,end)
            runs.insert((start,end))
    


if __name__ == "__main__":
    N = 20
    arr = list(range(N))
    for i in range(0,N,5):
        run = list(randint(5,20) for _ in range(5))
        run.sort()
        arr[i:i+5] = run[:]
        
    rect_color = list(White for _ in range(N))

    print(arr)
    TimSort(arr)
    print(arr)
