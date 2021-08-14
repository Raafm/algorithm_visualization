from graph.Continental import M
import pygame,time
from threading import Thread, Lock
from math import sqrt
import random


walk = (30,30,30)
false = (80,80,80)
true = (235, 235, 235)

COLS = len(M[0])
ROWS = len(M)
partes = 1
COLS //= partes

N = ROWS*COLS
print(N)
advantage = 4

printed = False

is_prime = list(  true for _ in range(N)  )
is_prime[0] = is_prime[1] = false


one_operation = 0.00000001 #time for one multiplication or division 


pygame.init()


screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))





def print_square(element,color=False):

    if color is False:
        color = is_prime[element]

    i = element//ROWS               
    j = element%ROWS
    pygame.draw.rect(screen, color, (M[j][i][0],M[j][i][1] ,4, 4))
    
    if random.randint(0,8)==0:
        pygame.display.update()





def eliminate(element,id):
    is_prime[element] = false
    print_square(element,thread_color[id])
    time.sleep(one_operation)



def next_element(element):

    if element + 1 < N:
        print_square(element+1,walk)
        time.sleep(one_operation)

    return element+1




for x in range(ROWS):
    for y in range(COLS):
    
        pygame.draw.rect(screen, is_prime[x+ROWS*y], (M[x][y][0],M[x][y][1] ,4, 4))

    pygame.display.update()



font = pygame.font.Font('freesansbold.ttf',30)
text = font.render("Multi thread Sieve. ",True,(150,150,150))                        
screen.blit(text,text.get_rect(center = (400,30)))

font = pygame.font.Font('freesansbold.ttf',20)
text = font.render("threads: " ,True, (150,150,150))                         
screen.blit(text,text.get_rect(center = (875,100)))


T = 5        #number of threads

prime_list_sieve = [1]

in_execution = [0 for _ in range(T)]

thread_color = [

    
    (230,40,40),
    (180,20,20),
    (20,20,180),
    (40,40,230), 
    (20,130,10),
    (255,220,220),
    
]




def find_next_prime(id,element):

    
    if element >= N: return element
    
    
    real_prime = False
    while real_prime is False:

        while element+1 <N and is_prime[element] == false:
            print("thread",id,"searching next prime. Now in ",element+1)
            element = next_element(element)
        
        if element == N:
            return element

        for in_course in in_execution:  # see if other thread 
            real_prime = True
            if in_course >0 and element%in_course == 0:  # is going to take it
                real_prime = False
                break
    
        if real_prime:
            return element
        







mutex = Lock()
def crive_operator(args):


    global printed   
    id = args
    eliminating = False  
    element = 1
    multiple = 1
    print("thread",id)

    time.sleep(1)
    

    
    running =  True
    pause = False           
    
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
        
        if printed:
            
            return

        if not eliminating:

            if printed:
                return

            print("thread",id,"tries  to lock")
            mutex.acquire()                            # LOCK()
            print("thread",id,"acquired")
            
            element = prime_list_sieve[-1] + 1  # go search next prime

            element = find_next_prime(id,element)

            if element >= N:
                mutex.release()  
                if printed:
                    return
                else:
                    printed = True

                print("siege prime list:", prime_list_sieve)
                pause = True
                in_execution[id]=-1
                            
                return
              
    
                
            prime_list_sieve.append(element)
            in_execution[id] = element
            multiple = 2*element
            eliminating = True

            print("thread",id,"released, and working on:",element)
            mutex.release()                    # UNLOCK()


            if is_prime[element] == true:
                pygame.draw.rect(screen, walk, (840,145+100*id ,60, 60))    # erase what was before in the island couting
                font = pygame.font.Font('freesansbold.ttf',20)
                text = font.render(str(element) ,True, thread_color[id])                      
                screen.blit(text,text.get_rect(center = (870,180+100*id)))
                print_square(element)

            if element  >= N:
                if printed:
                    return
                else:
                    printed = True

                in_execution[id] = -1
                print("siege prime list:", prime_list_sieve)
                pause = True

                return




        if multiple + 1  <  N:
            eliminate(multiple,id)
            multiple += element
        
        else:
            eliminating = False





time.sleep(3.5)
thread0 = Thread(target= crive_operator, args = (0,) )
thread0.start()
time.sleep(2)

thread1 = Thread(target= crive_operator, args = (1,) )
thread1.start()
time.sleep(1)

thread2 = Thread(target= crive_operator, args = (2,) )
thread2.start()
time.sleep(2)

thread3 = Thread(target= crive_operator, args = (3,) )
thread3.start()
time.sleep(1)
#
#thread4 = Thread(target= crive_operator, args = (4,) )
#thread4.start()
time.sleep(1)

thread1.join()
thread2.join()
thread3.join()
thread0.join()

running =  True
pause = False
prime =2
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

    if prime< N:
        print_square(prime)
        prime+=1
    else: pause=True