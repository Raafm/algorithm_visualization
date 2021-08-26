import pygame,time,random

number = []
rectangle = []
doubled =0 

def generate_array(N):
    
    while len(number) < N:
        n = random.randint(1,N)
        if n not in number:
            number.append(n)

    number.insert(random.randint(0,N-1),random.randint(1,N))
    print(number)
    sum = 0
    for x in range(1,N+1):
        sum += number[x] - x
    print(sum + number[0])
    

def Find_positions(N):

    sum = 0
    for x in range(1,N+1):
        sum += number[x] - x
    
    sum += number[0]
    
    position = []
    for x in range(N+1):
        if number[x] == sum:
            position.append(x)
    
    return position[0],position[1]


def reinitialize():
    for i in range(N+1):
        pygame.draw.rect(   screen   ,  numb_color    ,   (100 + (square_width+space)*i , ground - size_rate*number[i],    square_width  ,  size_rate*number[i])  )
        pygame.draw.rect(   screen   ,  const_color   ,   (100 + (square_width+space)*i , ground              ,    square_width  ,     size_rate*i     )  )
    pygame.display.update()


N = 60
generate_array(N)



pygame.init()


screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))
square_width = 8
space = 4
index_color = (0,200,0)
index2_color = (200,200,0)
numb_color = (50,50,250)
const_color = (255,255,255)
sum_color = (250,250,0)
duplicate_color = (255,0,0)
ground = 150
size_rate = 1

for i in range(N+1):
    rectangle.append((100 + (square_width+space)*i , ground - size_rate*number[i],   square_width,  size_rate*number[i]))
    pygame.draw.rect(   screen   ,  numb_color    ,   (100 + (square_width+space)*i , ground - size_rate*number[i],    square_width  ,  size_rate*number[i])  )
    pygame.draw.rect(   screen   ,  const_color   ,   (100 + (square_width+space)*i , ground              ,    square_width  ,     size_rate*i     )  )
    pygame.display.update()
 



sum_rectangle = (100,450,0,0)
index = 0
index2 = 1

part_algorithm = 1

pause =False
running =  True
while running :

    # pygame stuff:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                   #exit pygame,
            running = False                          #exit() program


        if event.type == pygame.KEYDOWN:        
            if event.key == pygame.K_SPACE:     #press breakspace to pause or play
                pause = not pause   
                time.sleep(0.2)

    if pause:
        continue


    if part_algorithm == 2:
        if index == N+1: 
            pause = True

            _ , _ ,   width ,   high      =   rectangle[0]
            _ , _ ,     _   , sum_high    =   sum_rectangle         
            sum_rectangle                 =   rectangle[N][0] , ground , width , high + sum_high
            pygame.draw.rect(screen, duplicate_color , sum_rectangle)
            pygame.display.update()
            print((high + sum_high)/size_rate)
            
            i1,i2 = Find_positions(N)

            pygame.draw.rect(   screen   ,  duplicate_color,   (100 + (square_width+space)*i1 , ground - size_rate*number[i1],    square_width  ,  size_rate*number[i1])  )
            pygame.draw.rect(   screen   ,  duplicate_color,   (100 + (square_width+space)*i2 , ground - size_rate*number[i2],    square_width  ,  size_rate*number[i2])  )
            pygame.display.update()


            part_algorithm = 2
            index  = 0
            index2 = 1
            continue



        x , _ ,   width ,   high      =   rectangle[index]
        _ , _ ,     _   , sum_high    =   sum_rectangle         
        sum_rectangle                 =   x , ground , width , high + sum_high - size_rate*index

        pygame.draw.rect(screen, sum_color , sum_rectangle)


        index += 1
        pygame.display.update()
        time.sleep(0.1)
    


    if part_algorithm == 1:
        
        if number[index] == number[index2]:
            
            pygame.draw.rect( screen , duplicate_color, (100 + (square_width+space)*index  , ground - size_rate*number[index] ,   square_width  ,  size_rate*number[index])  )
            pygame.draw.rect( screen , duplicate_color, (100 + (square_width+space)*index2 , ground - size_rate*number[index2],   square_width  ,  size_rate*number[index2]) )
            part_algorithm = 2  
            index = 1
            
            pause = True
            pygame.display.update()
            time.sleep(1)
            reinitialize()
            continue

        else:
            if index2 > index+1 :
                pygame.draw.rect( screen , numb_color, (100 + (square_width+space)*(index2-1) , ground - size_rate*number[index2-1],   square_width  ,  size_rate*number[index2-1]) )
            else:
                pygame.draw.rect( screen , numb_color, (100 + (square_width+space)*(N) , ground - size_rate*number[N],   square_width  ,  size_rate*number[N]) )

            pygame.draw.rect( screen , index_color , (100 + (square_width+space)*index  , ground - size_rate*number[index] ,   square_width  ,  size_rate*number[index])  )
            pygame.draw.rect( screen , index2_color, (100 + (square_width+space)*index2 , ground - size_rate*number[index2],   square_width  ,  size_rate*number[index2]) )


        index2 +=1
        if index2 == N+1:
            
            index += 1
            index2 = index+1
            
            

            if index == N:
                part_algorithm = 2
                index = 1


        
        
        
        pygame.display.update()
        time.sleep(0.01)

