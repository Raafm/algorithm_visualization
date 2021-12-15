import pygame,time,random
from graph.color import *
#from graph.points import pointsMany as points
from Trees.twoD_tree import points,root
import math

screen_width,screen_height = 1200,700
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(Black)
if __name__ == "__main__":
    pygame.init()

    N = 50
    Max_width  = screen_width  - 100
    Max_height = screen_height - 100

#points = list( (random.randint(50,Max_width),random.randint(50,Max_height)) for _ in range(N))


def print_point(position, color= White,radius = 4, index=-1,show = True):
    pygame.draw.circle(screen,color,position,radius)
    if index > -1:
        font = pygame.font.Font('freesansbold.ttf',14)
        text = font.render( str(index),True, White)    
        screen.blit(text,text.get_rect(center = position))
    
    if show: pygame.display.update()


def print_lines(pos,orientation,X0 = 10,Y0 = 10,X1 = screen_width-200,Y1 = screen_height-50,show= True):
    x,y = pos

    if orientation: pygame.draw.line(screen,Cyan,(X0,y),(X1,y))
    else:           pygame.draw.line(screen,Red ,(x,Y0),(x,Y1))
    if show: pygame.display.update()


class rectangle:
    
    def __init__(self,x,y,width=200,height=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self,display = True,color = Dark_yellow):
        pygame.draw.rect(screen,color,(1+self.x,1+self.y,self.width,self.height))
        if display: pygame.display.update()

    # left: -1, inside: 0, right: 1,
    # up:   -1, inside: 0, down:  1,
    # orientation == 0: horizontal, 
    # orientation == 1: vertical
    def compare_position(self,point,orientation)->int:
        xP,yP = point
        if orientation == 0:
            return int(self.x < xP) - int(self.x + self.width  > xP ) 
        if orientation == 1:
            return int(self.y < yP) - int(self.y + self.height > yP )    
    
    def extremes(self):

        xL,xR = self.x,self.x + self.width
        yD,yU = self.y,self.y + self.height
        return xL,xR,yU,yD


def arrow(screen, start, end, lcolor = Light_grey, tricolor = Black,  trirad= 4, thickness=2,show = True):
    pygame.draw.line(screen, lcolor, start, end, thickness)
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi/2
    rad = 180/math.pi
    pygame.draw.polygon(screen, tricolor, (
            (end[0] + trirad * math.sin(      rotation    ), end[1] + trirad * math.cos(     rotation     )),                    
            (end[0] + trirad * math.sin(rotation - 120*rad), end[1] + trirad * math.cos(rotation - 120*rad)),
            (end[0] + trirad * math.sin(rotation + 120*rad), end[1] + trirad * math.cos(rotation + 120*rad))
        )
    )
    if show: pygame.display.update()


def print_points(tree = False,rect = None,erase_screen = True,delay = 0):

    if erase_screen:
        pygame.draw.rect(screen,Black,(10,10,1000,800))
    if rect:
        rect.show(display = (delay!=0))
    for index,P in enumerate(points):
        print_point(P,radius = 5,color = White, show = (delay!= 0))

    if tree:
        show_tree(delay)
    
    pygame.display.update()
    
def show_tree(delay = 0.1):
    from algorithms.data_struct.queue import queue
    xL,yD,xR,yU = 10,10,screen_width,screen_height
    vertical = False

    Q = queue()

    Q.insert( (root,xL,yD,xR,yU, vertical) )

    pause = False
    running =  True
    while running :

        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                running = False                          #exit() program

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not pause
                    time.sleep(0.2)
        
        if pause:
            continue

        if Q.not_empty():
            cur,xL,yD,xR,yU,vertical = Q.pop()
        else:
            if delay!=0: time.sleep(1)
            break

        
        print_point((cur.x,cur.y),(vertical)*Cyan + (not vertical)*Red,radius = 6,show= (delay!=0))
        print_lines((cur.x,cur.y),vertical,xL,yD,xR,yU,show= (delay!=0))
        time.sleep(delay)

        if vertical == True:
            
            if cur.right:
                Q.insert( (cur.right, xL, cur.y , xR ,  yU   , not vertical)  )
                arrow(screen, (cur.x,cur.y),(cur.right.x,cur.right.y),show= (delay!=0))
                
                time.sleep(delay/2)
            if cur.left :
                Q.insert( (cur.left , xL,   yD  , xR , cur.y , not vertical ) )
                arrow(screen, (cur.x,cur.y),(cur.left .x,cur.left .y),show= (delay!=0))
                
                time.sleep(delay/2) 
        else:
            
            if cur.right: 
                Q.insert( (cur.right,cur.x,yD,xR,yU, not vertical) )
                arrow(screen, (cur.x,cur.y),(cur.right.x,cur.right.y),show= (delay!=0))
                
                time.sleep(delay/2)
            if cur.left : 
                Q.insert( (cur.left ,xL,yD,cur.x,yU, not vertical) )
                arrow(screen, (cur.x,cur.y),(cur.left .x,cur.left .y),show= (delay!=0))
                
                time.sleep(delay/2)
        

def range_count(cur,xL,xR,yU,yD,vertical,lines = False,delay=0.2):
    if cur is None: return 0
    if lines: print_lines((cur.x,cur.y),vertical)

    print_point((cur.x,cur.y),color = Lime,radius=9)
    time.sleep(delay)

    if vertical:
        if   cur.y < yD: return range_count(cur.right ,xL,xR,yU,yD,False,delay=delay)
        elif cur.y < yU: 
            if ((xL < cur.x) and (cur.x < xR)) :print_point((cur.x,cur.y),color = Yellow, radius = 10)
            Im_in = int ((xL < cur.x) and (cur.x < xR)) 
            return Im_in + range_count(cur.left  ,xL,xR,yU,yD,False,delay=delay) + range_count(cur.right ,xL,xR,yU,yD,False,delay=delay)
        else:            return range_count(cur.left  ,xL,xR,yU,yD,False,delay=delay)
    else:
        if   cur.x < xL: return range_count(cur.right ,xL,xR,yU,yD,True,delay=delay)
        elif cur.x < xR: 
            if ((yD < cur.y) and (cur.y < yU)):print_point((cur.x,cur.y),color = Yellow, radius = 10)
            Im_in = int((yD < cur.y) and (cur.y < yU))
            return Im_in + range_count(cur.left  ,xL,xR,yU,yD,True,delay=delay) + range_count(cur.right ,xL,xR,yU,yD,True,delay=delay)
        else:            return range_count(cur.left  ,xL,xR,yU,yD,True,delay=delay)
    

##### MAIN #####

if __name__ == "__main__":

    rects = [
    rectangle(630,220,width = 150,height = 90),
    rectangle(100,100,100,40),
    rectangle(900,500,100,100),
    rectangle(800,90,200,40),
    rectangle(130,480,100,130),
    rectangle(200,400,400,400)
    ]



    print_points(tree = False)
    time.sleep(2)
    show_tree(delay=0.2)
    time.sleep(2)

    rect = rects[0] 
    rect.show()
    show_tree(delay=0)
    xL,xR,yU,yD = rect.extremes()
    range_count(root,xL,xR,yU,yD,False,delay=0.6)
    time.sleep(1)


    for rect in rects[1:-3]:
        print_points(erase_screen = True,tree=True,rect=rect)
        time.sleep(0.6)
        xL,xR,yU,yD = rect.extremes()
        range_count(root,xL,xR,yU,yD,False,delay=1)
        time.sleep(0.4)

    pygame.draw.rect(screen,Black,(0,0,1500,1500))
    font = pygame.font.Font('freesansbold.ttf',50)
    text = font.render("Comparison",True,White)                         
    screen.blit(text,text.get_rect(center = ((screen_width-100)//2,screen_height//2   - 100)))
    text = font.render("Check All X Tree",True,White)                         
    screen.blit(text,text.get_rect(center = ((screen_width-100)//2,screen_height//2   - 50)))
    pygame.display.update()
    time.sleep(3)

    for rect in rects:

        print_points(erase_screen = True,rect=rect)
        for point in points:
            print_point(point,Lime,radius = 10)
            time.sleep(0.15)
            if rect.compare_position(point,True) == 0 and rect.compare_position(point,False) == 0:        
                print_point(point,Yellow,radius = 12)
        
        time.sleep(0.2)
            

    time.sleep(1)
    print_points(tree = False)
    time.sleep(1)

    show_tree(delay = 0.1)
    for rect in rects:
        print_points(erase_screen = True,tree=True,rect=rect)
        time.sleep(0.2)
        xL,xR,yU,yD = rect.extremes()
        range_count(root,xL,xR,yU,yD,False,delay=0.2)
        


    running =  True
    while running :

        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                running = False                          #exit() program



        

