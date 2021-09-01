from graph.Continental import M
import pygame,time
from math import sqrt
import random
false = (55,55,55)
true = (0,225,255)

COLS = len(M[0])
ROWS = len(M)
partes = 2
COLS //= partes

N = ROWS*COLS
print(N)
advantage = 4





is_prime = list(  true for _ in range(N)  )
is_prime[0] = is_prime[1] = false


one_operation = 0.0000001 #time for one multiplication or division 




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
    
    pygame.display.update()





def eliminate(element):
    is_prime[element] = false
    print_square(element,(205,0,0))
#    time.sleep(one_operation)
    #print_square(element)


def next_element(element):

    if element + 1 < N:
        print_square(element+1,(255,255,255))
        #print_square(element)

    #    time.sleep(one_operation)
    return element+1



def check_prime(element):

    i = 2
    root = sqrt(element)
    while( i <= root ):
        if element%i == 0:
            return False 
        print_square(element,(205,0,0))
    #    time.sleep(one_operation)
        print_square(element,(255,255,255))
        i += 1

    return True


font = pygame.font.Font('freesansbold.ttf',18)
text = font.render("Find primes, divide by all less than sqrt approach (Ache os primos, dividindo por todos < sqrt). ",True,(50,225,50))                        
screen.blit(text,text.get_rect(center = (430,30)))
font = pygame.font.Font('freesansbold.ttf',20)
text = font.render("last prime: " ,True, true)                         
screen.blit(text,text.get_rect(center = (875,100)))
for x in range(ROWS):
    for y in range(COLS):
    
        pygame.draw.rect(screen, (205, 205,0), (M[x][y][0],M[x][y][1] ,4, 4))
        
    pygame.display.update()

time.sleep(2)
pause = True


prime_list_all = []
prime_list_sieve = []
primes_found = 0
element = 1
multiple = 1
eliminating = False

try_all_divisions = True
Sieve = False
beggining_sieve = False

running =  True
#pause = False           # start paused, press breakspace to start playing
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
    
    if Sieve:
        #print("eliminating = ",eliminating,"\nmultiple = ",multiple)
        
        if beggining_sieve:

            pygame.draw.rect(screen, (245,245,245),(0,0,1000,47))
            font = pygame.font.Font('freesansbold.ttf',30)
            text = font.render("Sieve of Eratosthenes (crivo de Erastotenes)",True,(55,55,55))                        
            screen.blit(text,text.get_rect(center = (500,20)))
            pygame.display.update()
            time.sleep(2)
            is_prime[0] = is_prime[1] = false
            print_square(0)
            print_square(1)

            for x in range(2,N):
                is_prime[x] = true
                if x not in prime_list_all:
                    print_square(x)
            beggining_sieve = False   
            one_operation = one_operation*10
            element=1



        if not eliminating:

            if element+1< N :
            
                element = next_element(element)

                if is_prime[element] == true:
                    
                    prime_list_sieve.append(element)
                    multiple = 2*element
                    eliminating = True
                    pygame.draw.rect(screen, (55,55,55), (820,130 ,100, 100))    # erase what was before in the island couting
                    font = pygame.font.Font('freesansbold.ttf',20)
                    text = font.render(str(element) ,True, (225,225,225))                      
                    screen.blit(text,text.get_rect(center = (870,180)))

                else:
                    print_square(element)
            else:
                print("siege prime list:", prime_list_sieve)
                Sieve = False
                pause = True




        if multiple +1< N:
            eliminate(multiple)
            multiple += element
        
        else:
            eliminating = False
    
    
    if try_all_divisions:
        
        element = next_element(element)

        if element +1< N//advantage:
        
            if check_prime(element):
                print_square(element,(0,255,0))
                prime_list_all.append(element)
                pygame.draw.rect(screen, (245,245,245), (820,130 ,100, 100))    # erase what was before in the island couting
                font = pygame.font.Font('freesansbold.ttf',20)
                text = font.render(str(element) ,True, (0,225,0))                      
                screen.blit(text,text.get_rect(center = (870,180)))

                
                
        
        else:
            try_all_divisions = False
            #pause = True
            Sieve = True
            beggining_sieve = True
            print("try_all_divisions prime list:",prime_list_all)
            prime_list_all.clear()

    

    if try_all_divisions== False and Sieve == False:
        ok =True
        for x in range(0,len(prime_list_all)):
            print(prime_list_all[x],prime_list_sieve[x])
            if prime_list_all[x] != prime_list_sieve[x]:
                ok = False
        print(ok)
