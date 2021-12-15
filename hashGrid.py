import pygame,time,random, math
from graph.color import *
from algorithms.data_struct.linked_list import linked_list
from Trees.twoD_tree import points,root
from countPoints_inrect import rectangle


# pega os elementos nas extremidades  O(N)
# acha os elementos da extremidade e cria um retangulo 
# divide em um grid de setores iguais 
# coloca cada elemento no setor correspondente O(N)
# consulta


# queremos: tempo constante para pegar
# o tempo para pegar == 1 + N/M, 
# que deve ser cte (hash) ---> N ~ M
# M = Lx*Ly/sector_size   ---> sector_size = Lx*Ly/M 
# sector_size = Lx*Ly/N 
# number of sectorsX: Lx/sector_size  
# number of sectorsY: Ly/sector_size 


# achar os quatros pontos,
# e ver os setores entre os pontos, 
# print_point() para cada sector, 
# checa se o ponto esta no rect ou nao


pygame.init()

screen_height = 700
screen_width  = 1250
screen = pygame.display.set_mode((screen_width,screen_height))

screen.fill(Black)

N = 300

points = list( (random.randint(50,screen_width-300),random.randint(50,screen_height-100))  for _ in range(N) )




def print_lines(pos,orientation,X0 = 50,Y0 = 50,X1 = screen_width-200,Y1 = screen_height-50,show= True):
    x,y = pos

    if orientation: pygame.draw.line(screen,Cyan,(X0,y),(X1,y))
    else:           pygame.draw.line(screen,Red ,(x,Y0),(x,Y1))
    if show: pygame.display.update()


def print_point(position, color= White,radius = 4, index=-1,show = True):
    pygame.draw.circle(screen,color,position,radius)
    if index > -1:
        font = pygame.font.Font('freesansbold.ttf',14)
        text = font.render( str(index),True, White)    
        screen.blit(text,text.get_rect(center = position))
    
    if show: pygame.display.update()


def print_lines(pos,color = Red, X0 = 10,Y0 = 10,X1 = screen_width-300,Y1 = screen_height-100,show= True):
    x,y = pos

    pygame.draw.line(screen,color, (X0,y),(X1,y),2)
    pygame.draw.line(screen,color, (x,Y0),(x,Y1),2)
    if show: pygame.display.update()


def find_extremes(points):

    pygame.draw.rect(screen, Black, (1000,145+100 , 250, 60))   
    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render(str("Find extremes") ,True, Red)                      
    screen.blit(text,text.get_rect(center = (1130,180+100)))
    pygame.display.update()

    x,y = points[0]
    left,right,top,bottom = x,x,y,y
    point_left   = (x,y)
    point_right  = (x,y)  
    point_top    = (x,y)
    point_bottom = (x,y)

    print_point(points[0],Red)

    for point in points:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                exit()
        
        print_point(point,White,radius = 5)

        x,y = point
        if x < left:   left    = x; print_point(point_left  ,color = Black,radius = 8); print_point(point_left  ,color = White,radius = 5); point_left   = point
        if x > right:  right   = x; print_point(point_right ,color = Black,radius = 8); print_point(point_right ,color = White,radius = 5); point_right  = point
        if y > top:    top     = y; print_point(point_top   ,color = Black,radius = 8); print_point(point_top   ,color = White,radius = 5); point_top    = point
        if y < bottom: bottom  = y; print_point(point_bottom,color = Black,radius = 8); print_point(point_bottom,color = White,radius = 5); point_bottom = point
 
        print_point(point_left  ,Red,radius = 8)
        print_point(point_right ,Red,radius = 8)
        print_point(point_top   ,Red,radius = 8)
        print_point(point_bottom,Red,radius = 8)
 
        time.sleep(0.03) 
        

    print_lines(  (left,bottom)  )
    print_lines(    (left,top)   )
    print_lines(  (right,bottom) )
    print_lines(   (right,top)   )

    pygame.draw.rect(screen, Black, (1000,145+100 , 250, 60)) 
    pygame.display.update()

    return left,right,top,bottom


def rect_list(N,left,right,top,bottom):
    rects = []
    for i in range(N):
        x,y = random.randint(50,screen_width-500), random.randint(50,screen_height-200) 
        lx,ly = random.randint(30,screen_width//10),random.randint(30,screen_height//5)
        rects.append(rectangle(x,y,width = lx,height = ly))

    return rects


def display_grid(points):
    N = len(points)
    left,right,top,bottom = find_extremes(points)
    Lx = right -  left
    Ly =  top  - bottom
    

    font = pygame.font.Font('freesansbold.ttf',30)
    text = font.render("Hash" ,True, Lime)                      
    screen.blit(text,text.get_rect(center = (1130,180+100)))
    pygame.display.update()

    time.sleep(0.5)

    sector_sizeX = int(Lx/(math.sqrt(N)))
    sector_sizeY = int(Ly/(math.sqrt(N)))

    nX,nY = 1,1

    for i in range(left,right,sector_sizeX):
        print_lines((i,bottom), color = White)
        time.sleep(0.03)
        nX += 1
        #time.sleep(0.05)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                exit()


    for j in range(bottom, top,sector_sizeY):
        print_lines((left,j),color = White)
        time.sleep(0.03)
        nY += 1
        #time.sleep(0.05)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                exit()

    print_lines(  (left,bottom)  )
    print_lines(    (left,top)   )
    print_lines(  (right,bottom) )
    print_lines(   (right,top)   )

    sector_table = list( list(linked_list() for _ in range(nY+1)) for _ in range(nX+1))
    print("len sector_table = ",len(sector_table))
    for point in points:
        x,y = point
        print_point(point,color= Lime,radius = 5)
        sector_table[int((x-left)/sector_sizeX)][int((y-bottom)/sector_sizeY)].push_back(point)
        time.sleep(0.03)

    pygame.draw.rect(screen, Black, (1000,145+100 , 250, 60)) 
    pygame.display.update()

    for point in points:
        print_point(point,color = White,radius = 5,show = False)

    pygame.display.update()
    time.sleep(0.05)
    return sector_table,sector_sizeX,sector_sizeY,left,right,top,bottom


def Hash(point,sector_sizeX,sector_sizeY):
    global left,bottom
    x,y = point
    index_x = int((x-left)/sector_sizeX) 
    index_y = int((y-bottom)/sector_sizeY)
    
    return index_x,index_y


def intersects(rect: rectangle, sector_sizeX, sector_sizeY,show = True):
    xL,xR,yU,yD= rect.extremes()
    global left, bottom
    index_left   = int((xL-left)/sector_sizeX)
    index_right  = int((xR-left)/sector_sizeX)
    index_top    = int((yU-bottom)/sector_sizeY)
    index_bottom = int((yD-bottom)/sector_sizeY)
    
    if show:
        for y in range(index_bottom,index_top+1):
            for x in range(index_left,index_right+1):
                rect = rectangle(left+x*sector_sizeX, bottom + y*sector_sizeY,  sector_sizeX, sector_sizeY)
                rect.show(color=Dark_red)
                time.sleep(0.05)
        
    return index_left, index_right, index_top, index_bottom


point_color = list(White for _ in range(N))


if __name__ == '__main__':

    

    C = 6 # numero de consultas
    rects = [rectangle(80,80),
            rectangle(450,400,width = 30),
            rectangle(700,200,width=300,height = 40),
            rectangle(80,350,width = 150,height = 50),
            rectangle(700,450,width = 150,height = 150),
            rectangle(350,80,width = 200,height = 250)
    ]#rect_list(C,100,screen_width-100,screen_height-100,100)

    for point in points:
        print_point(point,radius = 6)

    gridHash = False
    brute = True
    i = 0
    running =  True
    while running :

        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   # exit pygame,
                running = False                 # exit() program

        if brute:

            if i == C:
                brute = False
                gridHash = True
                i = 0
                point_color = list(White for _ in range(N))
                
                
                pygame.draw.rect(screen,Black,(0,0,1500,1500))
                font = pygame.font.Font('freesansbold.ttf',50)
                text = font.render("Grid_Hash",True,White)                         
                screen.blit(text,text.get_rect(center = ((screen_width-100)//2,screen_height//2   - 100)))
                pygame.display.update()
                time.sleep(1.5)
               
                pygame.draw.rect(screen,Black,(0,0,screen_width,screen_height))
                pygame.display.update()
                time.sleep(0.5)

                color_dict = dict()

                sector_table, sector_sizeX, sector_sizeY, left, right, top, bottom = display_grid(points)   

                continue         
                
            time.sleep(0.5)

            rect = rects[i]
            rect.show(color = Flame)
            for index,point in enumerate(points):
                    print_point(point,color = point_color[index],radius = 6, show = False)
                    
            pygame.display.update()

            time.sleep(0.5)

            for index,point in enumerate(points):

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()                   # exit pygame,
                        running = False                 # exit() program
                        break

                if point_color[index] != Yellow:
                    if rect.compare_position(point,True) or rect.compare_position(point,False):
                        print_point(point,Lime,radius = 6)
                        
                    else: print_point(point,Yellow,radius = 6); point_color[index] = Yellow

                time.sleep(0.03)

            

        if gridHash:
            if i == C: continue      

            time.sleep(0.5)

            rect = rects[i]
            
            index_left, index_right, index_top, index_bottom = intersects(rect,sector_sizeX,sector_sizeY)
            rect.show(color = Flame) 
            
            for point in points:    
                if point in color_dict: print_point(point, color = Yellow, radius = 6, show = False)
                else: print_point(point, color = White,radius = 6, show = False)

            pygame.display.update()

            time.sleep(0.5)

            for y in range(index_bottom, index_top + 1):
                for x in range(index_left, index_right + 1):
                    
                    if x >= len(sector_table) or y >= len(sector_table[0]): continue

                    for _ in range(sector_table[x][y].size):
                    
                        point = sector_table[x][y].parse()

                        if not (point in color_dict):
                            if rect.compare_position(point,True) or rect.compare_position(point,False):
                                print_point(point,Lime,radius = 6)
                                
                            else:
                                print_point(point,Yellow,radius = 6)
                                color_dict[point] = Yellow


                            
                        time.sleep(0.03)
        

        i += 1



        
