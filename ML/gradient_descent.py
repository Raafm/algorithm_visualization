import pygame,time,random,math
from color import *

import numpy as np
from numpy import sin,exp,pi


screen_width,screen_height = 1300,700
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(Black)


def arrow(screen, start, end, lcolor = (255,255, 255), tricolor = (255,255,255),  trirad= 6, thickness=3):
    pygame.draw.line(screen, lcolor, start, end, thickness)
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi/2
    rad = 180/math.pi
    pygame.draw.polygon(screen, tricolor, (
            (end[0] + trirad * math.sin(      rotation    ), end[1] + trirad * math.cos(     rotation     )),                    
            (end[0] + trirad * math.sin(rotation - 120*rad), end[1] + trirad * math.cos(rotation - 120*rad)),
            (end[0] + trirad * math.sin(rotation + 120*rad), end[1] + trirad * math.cos(rotation + 120*rad))
        )
    )
    #pygame.display.update()





def print_point(position, color= White,radius = 5, index=-1,show = True):
    pygame.draw.circle(screen,color,position,radius)
    if index > -1:
        font = pygame.font.Font('freesansbold.ttf',14)
        text = font.render( str(index),True, White)    
        screen.blit(text,text.get_rect(center = position))
    
    if show: pygame.display.update()



def h(theta,X):
    return (theta.T*X).sum(axis = 1)

def J(theta,X,y):
    
    return ((h(theta,X) - y)**2).sum()/(2*len(y))

def dJ_dtheta(theta,X,y):
    return ((h(theta,X) - y)*X.T).sum(axis= 1)/len(y)




def train_test_split(X,y):
    m = len(y)
    indices = np.arange(m)
    
    X_train = X[indices%5 != 0]
    y_train = y[indices%5 != 0]

    X_test  = X[indices%5 == 0]
    y_test  = y[indices%5 == 0]

    return X_train,X_test,y_train,y_test

def show_contador(num,show = True):
    pygame.draw.rect(screen, Light_grey, (1000,145 ,80, 60))    # erase what was before in the prime 
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render(str(num) ,True, Black)                      
    screen.blit(text,text.get_rect(center = (1040,180)))
    
    if show: pygame.display.update()


def show_points(X,y,color = White, tempo = 0,radius = 4,show = True):
    
    for point in zip(800*X +50 ,screen_height/2 - 40*y + 60):
        
        print_point(point,color,show= False,radius = radius)
    
    if show: pygame.display.update()
    if tempo: time.sleep(tempo)



def show_cost(cost_list):
    x0,y0 = (900 ,600 )

    displacement = 1.8#0.6
 
    first = 0 if len(cost_list) < 1000 else-1000 
    
    first = 0

    displacement_y = 20#/np.var(cost_list)#max(min(cost_list),0.001)
    last = y0-displacement_y*cost_list[first]-5
    

    pygame.draw.rect(screen,White,(880,240,screen_width-300,screen_height))
    arrow(screen, (x0,y0),(x0      ,250), lcolor = Dark_gray, tricolor = Dark_gray)
    arrow(screen, (x0,y0),(x0 + 370,y0) , lcolor = Dark_gray, tricolor = Dark_gray)

    


    cost_arr = np.array(cost_list[first:])
    cost_arr = cost_arr/(np.sqrt((cost_arr**2).mean())) 

    i = first +1
    for x,cost in enumerate(cost_arr):
        if x == 0: continue
        cur = y0 - displacement_y*cost-5
        pygame.draw.line(screen,Maroon,(displacement*x+x0+10,last),(displacement*(x+1)+x0+10,cur),2)
        #print_point((x0 + displacement*x,y0-10*cost),royal_blue,show=False,radius = 1)
        last = cur
        i += 1

    pygame.display.update()




def treino(X,y,n_iterations = 1000, alpha = 0.1, theta0 = None,info_rate = 1,tempo = 0, stochastic_flag = False, batch_size = 30):

    global it_total

    if X.ndim > 1:
        x = X[:,1]
        
    else:
        x = X
        

    theta = theta0 if theta0 is not None else 2*np.random.random((X.shape)[1])
    

    global cost_list
    
    m = len(y)
    

    for it in range(n_iterations+1):

        if stochastic_flag:
            indices = np.random.randint(0,m,batch_size)
            X_batch = X[indices]
            y_batch = y[indices]
            
        else:
            X_batch = X
            y_batch = y

           
        

        ######################################################################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                quit()                          #exit() program
        ######################################################################

        

        if it%info_rate == 0:
            #print(f"it {it} | cost: {np.round(cost,3)} | theta: {np.round(theta,3)}")
            cost = J(theta,X,y)
            cost_list.append(cost)
            pygame.draw.rect(screen,Black,(0,90,screen_width-430,screen_height))
            show_points(x,h(theta,X),color = royal_blue,radius = 8, show = False)
            
            if stochastic_flag:    
                show_points(X_batch[:,1],y_batch, show = False, color = White,radius =6)
            else:
                show_points(x      ,y, show = False)

            
            show_contador(it + it_total,show = False)
            show_cost(cost_list)
            time.sleep(tempo)
            
        theta = theta - alpha*dJ_dtheta(theta,X_batch,y_batch)

    it_total += it   

    pygame.draw.rect(screen,Black,(0,80,screen_width-430,screen_height))
    show_points(x,h(theta,X),color = Blue,radius = 8)
    show_points(x,y)
    pygame.draw.rect(screen,White,(880,280,screen_width-300,screen_height))
    
    show_cost(cost_list)
    return theta

def legenda(titulo):
    pygame.draw.rect(screen,Black,(0,0,screen_width-430,95))
    font = pygame.font.Font('freesansbold.ttf',25)
    text = font.render(titulo ,True, White)                      
    screen.blit(text,text.get_rect(center = (400,50)))
    pygame.display.update()

it_total = 0
cost_list = []

if __name__ == "__main__":
    pygame.init()

    m = 300
    x = np.linspace(0,2*pi,m)
    y = 8*exp(-x/(2*pi))*sin(x) + 1.5*(2*np.random.random(m) -1)

    n_params = 2
    w0 = np.zeros(n_params)

    X = np.column_stack([x**k for k in range(n_params)])
    X_casted = X / X.max(axis = 0)
    X_train,X_test,y_train,y_test = train_test_split(X_casted,y)

    x_lin_train,x_lin_test,y_lin_train,y_lin_test = train_test_split(X_casted[(x > np.pi/2) & (x < 3*np.pi/2) ],y[(x > np.pi/2) & (x < 3*np.pi/2)])



    
    pygame.draw.rect(screen,Black,(0,90,screen_width-430,screen_height))
    show_points(x_lin_train[:,1],h(w0,x_lin_train),color = Blue,radius = 8, show = False)
    show_points(x_lin_train[:,1]      ,y_lin_train, show = True)
    
    time.sleep(1)
    
    show_cost([0])
    font = pygame.font.Font('freesansbold.ttf',18)
    text = font.render("cost" ,True, Maroon)                      
    screen.blit(text,text.get_rect(center = (950,250)))
    text = font.render("iteration" ,True, Maroon)                      
    screen.blit(text,text.get_rect(center = (1250,650)))


    font = pygame.font.Font('freesansbold.ttf',18)
    text = font.render("N° iterations:" ,True, White)                      
    screen.blit(text,text.get_rect(center = (1045,130)))
    show_contador(0)

    time.sleep(2)

    legenda(f"linear regression, Gradient Descent, {n_params} parameters")
    time.sleep(2)

    """ simple linear regression (2 parametros, ou seja, reta)"""

    tempo_fullset = 0.05*0.75/3
    w = treino(x_lin_train,y_lin_train,n_iterations = 50,     theta0 = w0,                          tempo = tempo_fullset);time.sleep(0.5*0.75/3)
    w = treino(x_lin_train,y_lin_train,n_iterations = 950    ,info_rate=10,  theta0 = w,  tempo = tempo_fullset);time.sleep(0.5*0.75/3)
    w = treino(x_lin_train,y_lin_train,n_iterations = 1000    ,info_rate=100,  theta0 = w,  tempo = tempo_fullset);time.sleep(0.5*0.75/3)
    w = treino(x_lin_train,y_lin_train,n_iterations = 1000    ,info_rate=100,  theta0 = w,  tempo = tempo_fullset);time.sleep(0.5*0.75/3)

    time.sleep(2)



    cost_list = []
    it_total = 0



    """ 3 parametros """


    n_params = 3
    w0 = np.zeros(n_params)
    X = np.column_stack([x**k for k in range(n_params)])
    X_casted = X / X.max(axis = 0)
    X_train,X_test,y_train,y_test = train_test_split(X_casted,y)



    ### inicio ###
    
    pygame.draw.rect(screen,Black,(0,90,screen_width-430,screen_height))
    show_points(X_train[:,1],h(w0,X_train),color = Blue,radius = 8, show = False)

    show_points(X_train[:,1],y_train)

   
    font = pygame.font.Font('freesansbold.ttf',18)
    text = font.render("N° iterations:" ,True, White)                      
    screen.blit(text,text.get_rect(center = (1045,130)))

    show_contador(0)


   # pygame.draw.rect(screen,White,(880,280,screen_width-300,screen_height))
    show_cost([0])

    font = pygame.font.Font('freesansbold.ttf',18)
    text = font.render("cost" ,True, Maroon)                      
    screen.blit(text,text.get_rect(center = (950,250)))
    text = font.render("iteration" ,True, Maroon)                      
    screen.blit(text,text.get_rect(center = (1250,650)))
    

    pygame.display.update()

    time.sleep(1)
    legenda(f"linear regression, Gradient Descent, {n_params} parameters")

    time.sleep(2)

    tempo_fullset = 0.05*0.75
    w = treino(X_train,y_train,n_iterations = 50,                   theta0 = w0, tempo = tempo_fullset);time.sleep(0.5*0.75)
    w = treino(X_train,y_train,n_iterations = 250    ,info_rate=10,  theta0 = w,  tempo = tempo_fullset);time.sleep(0.5*0.75)
    w = treino(X_train,y_train,n_iterations = 1_700  ,info_rate=50,  theta0 = w,  tempo = tempo_fullset);time.sleep(0.5*0.75)
    w = treino(X_train,y_train,n_iterations = 18_000 ,info_rate=500, theta0 = w,  tempo = tempo_fullset);time.sleep(0.5*0.75)
    w = treino(X_train,y_train,n_iterations = 280_000,info_rate=40_000,theta0 = w,  tempo = 0)


    time.sleep(1)

    """ 8 parametros """

    n_params = 8
    w0 = np.zeros(n_params)

    X = np.column_stack([x**k for k in range(n_params)])
    X_casted = X / X.max(axis = 0)
    X_train,X_test,y_train,y_test = train_test_split(X_casted,y)


    ### inicio ###
    
    pygame.draw.rect(screen,Black,(0,90,screen_width-430,screen_height))
    show_points(X_train[:,1],h(w0,X_train),color = Blue,radius = 8, show = False)
    

    show_points(X_train[:,1],y_train)

    cost_list = []
    it_total = 0




    
    show_cost([0])

    font = pygame.font.Font('freesansbold.ttf',18)
    text = font.render("cost" ,True, Maroon)                      
    screen.blit(text,text.get_rect(center = (950,250)))
    text = font.render("iteration" ,True, Maroon)                      
    screen.blit(text,text.get_rect(center = (1250,650)))

    show_contador(0)
    time.sleep(1)
    legenda(f"linear regression, Gradient Descent, {n_params} parameters")
    
    time.sleep(1)

    tempo_fullset = 0.1
    w = treino(X_train,y_train,n_iterations = 50,                    theta0 = w0, tempo = tempo_fullset);time.sleep(1)
    w = treino(X_train,y_train,n_iterations = 250    ,info_rate=10,  theta0 = w,  tempo = tempo_fullset);time.sleep(1)
    w = treino(X_train,y_train,n_iterations = 1_700  ,info_rate=50,  theta0 = w,  tempo = tempo_fullset);time.sleep(1)
    w = treino(X_train,y_train,n_iterations = 18_000 ,info_rate=500, theta0 = w,  tempo = tempo_fullset);time.sleep(1)
    w = treino(X_train,y_train,n_iterations = 280_000,info_rate=10_000,theta0 = w,  tempo = tempo_fullset)


    """ stochastic gradient descent """

    tempo_stochastic = 0.01

    ################ legendas #################
    time.sleep(3)

    cost_list = []
    it_total = 0
    show_contador(0)
    
    pygame.draw.rect(screen,Black,(0,90,screen_width-430,screen_height))
    show_points(X_train[:,1],h(w0,X_train),color = Blue,radius = 8, show = False)
    show_points(X_train[:,1],y_train)

    show_cost([0])

    font = pygame.font.Font('freesansbold.ttf',18)
    text = font.render("cost" ,True, Maroon)                      
    screen.blit(text,text.get_rect(center = (950,250)))
    text = font.render("iteration" ,True, Maroon)                      
    screen.blit(text,text.get_rect(center = (1250,650)))
    
    time.sleep(1)
    legenda(f"linear regression, SGD, {n_params} parameters")
    time.sleep(1)

    w = treino(X_train,y_train,n_iterations = 50, theta0 = w0, tempo = tempo_stochastic,stochastic_flag= True);time.sleep(0.1)
    w = treino(X_train,y_train,n_iterations = 250    ,info_rate=10,  theta0 = w,  tempo = tempo_stochastic,stochastic_flag= True);time.sleep(0.1)
    w = treino(X_train,y_train,n_iterations = 1_700  ,info_rate=50, theta0 = w,  tempo = tempo_stochastic ,stochastic_flag= True);time.sleep(0.1)
    w = treino(X_train,y_train,n_iterations = 18_000,info_rate=500,theta0 = w,  tempo = tempo_stochastic  ,stochastic_flag= True);time.sleep(0.1)
    w = treino(X_train,y_train,n_iterations = 280_000,info_rate=10_000,theta0 = w,  tempo = tempo_stochastic,stochastic_flag= True)



    pause = False
    while True:
        
        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                quit()                          #exit() program


            
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_SPACE:     #press breakspace to pause or play
                    pause = not pause   
                    time.sleep(0.2)
        
        if pause:
            continue