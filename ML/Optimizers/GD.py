import pygame,time,random,math
from color import *

import numpy as np
from numpy import sin,cos,exp,pi,hypot

from threading import Thread, Lock


mutex = Lock()
def show_info(screen, n_id, n_iter, cost, color = Purple):
    
    cost = np.round(cost,1)
    
    pygame.draw.rect(screen, Gray, (1140,145+100*n_id ,60, 60))    # erase what was before in the prime 
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render(str(n_iter) ,True, color)                      
    screen.blit(text,text.get_rect(center = (1170,180+100*n_id)))
    
    pygame.draw.rect(screen, Gray, (1030,145+100*n_id ,80, 60))    # erase what was before in the prime 
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render(str(cost) ,True, color)                      
    screen.blit(text,text.get_rect(center = (1070,180+100*n_id)))
    
    pygame.display.update()
        

def arrow(screen, start, end, lcolor = (255,255, 255), tricolor = (255,255,255),  trirad= 2, thickness=2):
    
    start = 50 + 3*start[0] , 10 + 3*start[1]
    end   = 50 + 3*end[0]   , 10 + 3*end[1]
    
    pygame.draw.line(screen, lcolor, start, end, thickness) 
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + pi/2
    rad = 180/pi
    pygame.draw.polygon(screen, tricolor, (
            (end[0] + trirad * sin(      rotation    ), end[1] + trirad * cos(     rotation     )),                    
            (end[0] + trirad * sin(rotation - 120*rad), end[1] + trirad * cos(rotation - 120*rad)),
            (end[0] + trirad * sin(rotation + 120*rad), end[1] + trirad * cos(rotation + 120*rad))
        )
    )
    mutex.acquire();pygame.display.update();mutex.release()


pygame.init()
screen_width,screen_height = 1300,700
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(Black)
font = pygame.font.Font('freesansbold.ttf',20)
text = font.render("iteration" ,True, Gray)                      
screen.blit(text,text.get_rect(center = (1170,180+100*(-1))))
text = font.render("cost" ,True, Gray)                      
screen.blit(text,text.get_rect(center = (1070,180+100*(-1))))
text = font.render("optimizer" ,True, Gray)                      
screen.blit(text,text.get_rect(center = (940,180+100*(-1))))

for i,nome,color in zip(list(range(5)),["GD", "momentum", "nesterov","spsa","adam"],[White,Lime,Yellow,Black,dark_green]):
    pygame.draw.rect(screen, Gray, (880,145+100*i ,120, 60))  
    text = font.render(nome ,True, color)                      
    screen.blit(text,text.get_rect(center = (940,180+100*i)))


#np.random.seed(42)
def J_1(x1,x2):
    return np.abs(2.5*N -2*(x1+x2 + 1e-2*np.random.random()) )

def J_2(x1,x2):
    r = hypot(N/2 - x1, N/2 - x2)
    return 3*r - 2*x1

def J_3(x1,x2):
    r = hypot(N-60 - x1, N-60 - x2)
    return ((4*(0.5*cos(x1/5)+1) + 2*(0.5*cos(x2/5)+1)) + 100)* r**(0.8)

def J_4(x1,x2):
    r = hypot(N-60 - x1, N/2 - x2)
    if 51 <= x1 and x1 <= 130 and 50 <= x2 and x2 <= 120: return 20_000
    return 100*r  - 30*x2



def grad_J(w,delta_x = 1e-3, J = J_2):
    x1,x2 = w

    dJdx1 = ( J(x1 + delta_x,x2) - J(x1 - delta_x,x2) )/(2*delta_x)
    dJdx2 = ( J(x1,x2 + delta_x) - J(x1,x2 - delta_x) )/(2*delta_x)
    
    return np.array([dJdx1,dJdx2])


def create_grid(J = J_2, N = 230):
    cost_grid = np.array([[J(x1,x2) for x2 in range(N)] for x1 in range(N)])
    cost_grid = 254*(cost_grid - cost_grid.min())/(cost_grid.max() - cost_grid.min())+1e-3    
    return cost_grid

def print_square(i,j,cost_grid,color=None,show = True):
    if color is None:
        c = cost_grid[i][j]
        color = (c,  0, 255-c)
    
    pygame.draw.rect(screen, color, (50 + 3*i, 10 + 3*j, 3, 3))
    if show: mutex.acquire();pygame.display.update();mutex.release()

def print_point(w, color = Lime, show = True):
    x1,x2 = w[0],w[1]
    pygame.draw.circle(screen,color,(3*x1+50,3*x2+10),2)
    if show: mutex.acquire();pygame.display.update();mutex.release()


def show_grid(cost_grid,N = 230):
    for i in range(N):
        for j in range(N):
            print_square(i,j,cost_grid,show = False)
    mutex.acquire();pygame.display.update();mutex.release()


# para J_1
alpha = 2e-1
betha = 8e-1

# para J_2s
# alpha = 5e-1
# betha = 9e-1

# para J_3
# alpha = 3e-1
# betha = 7e-1

# para J_4
# alpha = 2.5e-1
# betha = 6e-1

alphas = [5e-1,    1.5e-1, 3e-1]
bethas = [ 9.3e-1, 8e-1,     6e-1]

def gradient_descent(x1,x2,N_iter = 100, J = J_2,alpha = alpha,delay = 0.1, n_id =-1):
    w = np.array([x1,x2]) 
    print_point(w)
    time.sleep(1)
    
    for it in range(N_iter):
        w_antes = w[:].copy()
        w -= alpha*grad_J(w,J = J)
       
        arrow(screen,(w_antes[0],w_antes[1]),(w[0],w[1]), White, White)
        show_info(screen,n_id,it, J(w[0],w[1]),White)
        time.sleep(delay)
        
        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                        
        

def gradient_descent_momentum(x1,x2,N_iter = 100,J = J_2,alpha = alpha, betha = betha, delay = 0.1, n_id = -1):
    w = np.array([x1,x2])
    delta_w = 0
    print_point(w)
    time.sleep(1)
    
    for it in range(N_iter):
        delta_w = -alpha*grad_J(w,J = J) + betha*delta_w
        w_antes = w[:].copy()
        w += delta_w
        arrow(screen,(w_antes[0],w_antes[1]),(w[0],w[1]), Lime, Lime)
        show_info(screen,n_id,it, J(w[0],w[1]),Lime)
        time.sleep(delay)

        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()             

            

def nesterov_momentum(x1,x2,N_iter = 100, J = J_2,alpha = alpha, betha = betha, delay = 0.1, n_id = -1):
    w = np.array([x1,x2])
    delta_w = 0
    print_point(w)
    time.sleep(1)
    
    for it in range(N_iter):
        delta_w = -alpha*grad_J(w + betha*delta_w, J = J) + betha*delta_w
        w_antes = w[:].copy()
        w += delta_w
        
        arrow(screen,(w_antes[0],w_antes[1]),(w[0],w[1]), Yellow, Yellow)#print_point(w,color = Yellow)
        show_info(screen,n_id,it, J(w[0],w[1]),Yellow)
        time.sleep(delay)
        
        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,

def spsa(x1,x2,N_iter = 100, J = J_2,delay = 0.1, n_id = - 1):
    alpha=0.602
    gamma=0.101
    
    w = np.array([x1,x2]) 
    print_point(w)
    time.sleep(1)
    
    def grad(L, w, ck):
        # number of parameters
        p = len(w)
        # bernoulli-like distribution
        deltak = np.random.choice([-1, 1], size=p)
        # simultaneous perturbations
        ck_deltak = ck * deltak
        # gradient approximation
        DELTA_L = L(w + ck_deltak) - L(w - ck_deltak)
        return (DELTA_L) / (2 * ck_deltak)

    c = 5e-2   # a small number

    # A is <= 10% of the number of iterations
    A = N_iter*0.1
    if N_iter == 251:
        A = 5*A
    

    # order of magnitude of first gradients
    magnitude_g0 = np.abs(grad(lambda w: J(w[0],w[1]), w, c).mean())+1

    # the number 2 in the front is an estimative of
    # the initial changes of the parameters,
    # different changes might need other choices
    a = ((A+1)**alpha)/magnitude_g0

    if N_iter == 250:
        a = 8    

    elif N_iter == 120:
        a = 9
    
    elif N_iter == 180:
        a = 2
    
    elif N_iter == 50:
        a = 3

    print(N_iter,a,"a")

    for k in range(1,N_iter):

        # update ak and ck
        ak = a/((k+A)**(alpha))
        ck = c/(k**(gamma))

        # estimate gradient
        gk = grad(lambda w: J(w[0],w[1]), w, ck)
        
        w_antes = w[:].copy()
        # update parameters
        w -= ak*gk        
        arrow(screen,(w_antes[0],w_antes[1]),(w[0],w[1]), Black, Black)
        show_info(screen,n_id,k, J(w[0],w[1]),Black)
        time.sleep(delay)
        
        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                        
        
            
def adam(x1,x2,N_iter = 100, J = J_2, alpha = 1e-1, betha1 = 9e-1, betha2 = 99e-1, delay = 0.1, n_id = -1):
    color = dark_green
    w= np.array([x1,x2])
    m_dw, v_dw = 0, 0
    print_point(w,color = color)
    for it in range(1,N_iter):
        
        dw=grad_J((w[0],w[1]), J = J)
        
        ## dw, db are from current minibatch
        ## momentum betha 1
        # *** weights *** #
        m_dw = betha1*m_dw + (1-betha1)*dw


        ## rms betha 2
        # *** weights *** #
        v_dw = betha2*v_dw + (1-betha2)*(dw**2)

        m_dw_corr = m_dw/(1-betha1**it + 1e-10)
        v_dw_corr = v_dw/(1-betha2**it + 1e-10)
        
        w_antes = w[:].copy()
        
        ## update weights
        w -= alpha*(m_dw_corr/(np.sqrt(v_dw_corr)+1e-8))
        
        
        arrow(screen,(w_antes[0],w_antes[1]),(w[0],w[1]), color, color)
        show_info(screen,n_id,it, J(w[0],w[1]),color)
        time.sleep(delay)
        

N = 265

init_pos_list = [(50.,50.),(1.,1.),(1.,1.),(1.,1.)]
N_iter_list   = [ 250, 120, 180,50]

for J,a,b,pos0,n_iter in zip([J_1, J_2, J_3, J_4],[alpha] + alphas,[betha] + bethas, init_pos_list, N_iter_list):
    cost_grid = create_grid(J,N)
    show_grid(cost_grid,N)
    
    x01, x02 = pos0
    
    threads = [
        Thread(target= gradient_descent,          args=(x01,x02, n_iter, J,a, 0.1, 0)),
        Thread(target= gradient_descent_momentum, args=(x01,x02, n_iter, J,a,b, 0.1, 1)),
        Thread(target= nesterov_momentum,         args=(x01,x02, n_iter, J,a,b, 0.1, 2)),
        Thread(target= spsa,                      args=(x01,x02, n_iter, J, 0.1, 3)),
        Thread(target= adam,                      args=(x01,x02, n_iter, J,15*a,0.9,0.999, 0.1, 4))
    ]

    for t in threads:
        t.start()
            
    for t in threads:
        t.join()

    time.sleep(2)

# gradient_descent(1,1,N_iter = 80, J = J_2_2, delay = 0.1)
# gradient_descent_momentum(1,1,N_iter = 80, J = J_2_2, delay = 0.1)
# nesterov_momentum(1,1,N_iter = 80, J = J_2_2, delay = 0.1)


pause = True
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

    