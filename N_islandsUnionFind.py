from graph.goodIslands import goodIslands as Map
import pygame,time,random
from graph.color import *
from algorithms.data_struct.ChildUnionFind import Matrix_ChildUnionFind as Disjoint_Sets_datastruct_optimized
from   algorithms.data_struct.UnionFind    import    Matrix_UnionFind   as Disjoint_Sets_datastruct_normal




print(len(Map),len(Map[0]))


color_list = [
Dark_red     ,
maroon	     ,
brown	     ,  	
firebrick	 ,	  	 
Flame        ,
Gray	     ,
Lime	     ,
Dark_gray    ,
Maroon 	     ,
Olive  	     ,
Green  	     ,
Purple 	     ,
Teal	     ,
Castanho	 ,
Carmesim	 ,
Some_grey    ,
Orange	     ,
Springgreen	 ,	    
crimson	     ,	   
tomato	     ,
coral	     ,
indian_red	 ,
light_coral  ,
dark_salmon	 ,
salmon	     ,
light_salmon ,
orange_red	 ,
dark_olive_green,
olive_drab	    ,
lawn_green	    ,
chart_reuse	    ,
green_yellow	,
dark_green	    ,
forest_green	,
saddle_brown	,   
sienna	        ,   
chocolate	    ,   
peru	        ,   
wheat	        ,   
sandy_brown	    ,   
burly_wood	    ,   
]
INDEX = 0



global IslandSet


def display_islands_numbers(N_islands):
    pygame.draw.rect(screen, Black, (850,10 ,300, 200))    # erase what was before in the island couting

    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("N° islands = " + str(N_islands) ,True,White)                   # print counting      
    screen.blit(text,text.get_rect(center = (1000,100)))
    pygame.display.update()

def paint_position(screen,x,y,color,IslandsMap = Map, show = False):

    IslandsMap[x][y] = color

    pygame.draw.rect(screen ,  IslandsMap[x][y]  , ( 50 + 5*x , 50 + 5*y , 4 , 4 ) )
    if show: pygame.display.update()



def display_islands_map(screen,IslandsMap):
    print(len(Map),len(Map[0]))
    for x in range(len(IslandsMap)):
        for y in range(len(IslandsMap[0])):
            paint_position(screen,x,y,IslandsMap[x][y])
        pygame.display.update() #display a cada fila (linha ou coluna)
        time.sleep(0.001)



def initialize_islands_map(screen,IslandsMap):
    display_islands_numbers(0)
    # make water Blue and land White
    for x in range(len(Map)):
        for y in range(len(Map[0])):
            if Map[x][y] == Navy or Map[x][y] == Blue or Map[x][y] == Black:
                Map[x][y] = Blue
            else: Map[x][y] = White
            paint_position(screen,x,y,Map[x][y],show = False)
        pygame.display.update() #display a cada fila (linha ou coluna)



def check_Num_Islands(IslandsMap):
    N_I = 0
    for y in range(len(IslandsMap[0])):
        for x in range(len(IslandsMap)): 
            if IslandSet.Find((x,y)) == (x,y) and IslandsMap[x][y] != Navy and IslandsMap[x][y] != Blue: N_I += 1
    print(N_I)
              

water = Blue
land = White
def N_islandsUnionFind(screen,Unite_Islands,IslandsMap = Map,just_half = False):
    
    ROWS  = len(IslandsMap)
    COLS  = len(IslandsMap[0])


    def look_around(screen,i,j):
        if(       (i+1 < ROWS)             and   IslandsMap[i+1][ j ] != Blue and IslandsMap[i+1][ j ] != Navy ): Unite_Islands( screen, (i,j) , (i+1 ,  j ) ); 
        if(        (0  <  i )              and   IslandsMap[i-1][ j ] != Blue and IslandsMap[i-1][ j ] != Navy ): Unite_Islands( screen, (i,j) , (i-1 ,  j ) ); 
        if(       (j+1 < COLS)             and   IslandsMap[ i ][j+1] != Blue and IslandsMap[ i ][j+1] != Navy ): Unite_Islands( screen, (i,j) , ( i  , j+1) ); 
        if(        (j  > 0 )               and   IslandsMap[ i ][j-1] != Blue and IslandsMap[ i ][j-1] != Navy ): Unite_Islands( screen, (i,j) , ( i  , j-1) ); 
        if( (i+1 < ROWS)  and (j+1 < COLS) and   IslandsMap[i+1][j+1] != Blue and IslandsMap[i+1][j+1] != Navy ): Unite_Islands( screen, (i,j) , (i+1 , j+1) ); 
        if( (i+1 < ROWS)  and (j > 0)      and   IslandsMap[i+1][j-1] != Blue and IslandsMap[i+1][j-1] != Navy ): Unite_Islands( screen, (i,j) , (i+1 , j-1) ); 
        if( (0 <  i) and (j+1 < COLS)      and   IslandsMap[i-1][j+1] != Blue and IslandsMap[i-1][j+1] != Navy ): Unite_Islands( screen, (i,j) , (i-1 , j+1) ); 
        if( (0 <  i) and ( j  >  0 )       and   IslandsMap[i-1][j-1] != Blue and IslandsMap[i-1][j-1] != Navy ): Unite_Islands( screen, (i,j) , (i-1 , j-1) ); 
        
    
    global INDEX
    global N_islands
    N_islands = 0
    
    x = y = 0
    running =  True
    pause = False           # start paused, press breakspace to start playing
    while running:
    
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            
            if event.type == pygame.KEYDOWN:            
                if event.key == pygame.K_SPACE:         # click breakspace for pause
                    pause = not pause                   # if it is paused, click breakspace for play(resume)
                    time.sleep(0.2)
        
        if pause:
            break

        if x == len(IslandsMap):
            x,y = 0, y+1
        if y ==len(IslandsMap[0]):
            break
        
        if IslandsMap[x][y] == water:         
            paint_position(screen,x,y,Navy,show = True)
        else:
            if IslandsMap[x][y] == land:
                IslandsMap[x][y] = color_list[INDEX]
                INDEX =  INDEX+1 if INDEX < len(color_list) -1 else  0; 
                N_islands += 1 #nova ilha encontrada
                display_islands_numbers(N_islands)
            look_around(screen,x,y)
        x+=1

  
    check_Num_Islands(IslandsMap)#check resposta ao final

        
                

def Unite_Islands_Brute(screen,position1,position2,IslandsMap = Map):
    global N_islands
    #junto as ilhas numa so
    if IslandSet.Union(position1,position2) is None: return

    if IslandsMap[position2[0]][position2[1]] != land: N_islands -= 1;display_islands_numbers(N_islands)
    
    patriarch       = IslandSet.Find(position1)
    patriarch_color = Map[patriarch[0]][patriarch[1]] 

    #busco por todos as posicoes que pertencem a ilha 
    for y in range(len(Map[0])):
        for x in range(len(Map)):
            if IslandSet.Find((x,y)) == patriarch and IslandsMap[x][y] != patriarch_color: #pertence a ilha
                paint_position(screen,x,y,patriarch_color,show = False) #recebe a cor do patriarca
               
    pygame.display.update()
    


def Unite_Islands_Optimized(screen,position1,position2, IslandsMap = Map):
    global N_islands
    #pega as listas pequenas
    lista1 = IslandSet.child_list(position1)
    lista2 = IslandSet.child_list(position2)
    
    #une as duas ilhas
    patriarch = IslandSet.Union(position1,position2) 
    if patriarch is None: return # se nao houve union (ja era da mesma ilha)
    
    if IslandsMap[position2[0]][position2[1]] != land: N_islands -= 1;display_islands_numbers(N_islands)

    patriarch_color = Map[patriarch[0]][patriarch[1]] 
   
    #pega a ilha menor
    elements = lista1 if lista1.size < lista2.size else lista2
   
   #muda a cor dela
    element_node =  elements.head
    

    #itera somente sobre a antiga menor ilha
    for _ in range(elements.size):
        paint_position(screen,  element_node.data[0], element_node.data[1]  , patriarch_color, show = False)
        element_node = element_node.next

    pygame.display.update()


def game_loop():
    running =  True
    pause = False           # start paused, press breakspace to start playing
    while running:
    
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            
            if event.type == pygame.KEYDOWN:            
                if event.key == pygame.K_SPACE:         # click breakspace for pause
                    pause = not pause                   # if it is paused, click breakspace for play(resume)
                    time.sleep(0.2)
        
        if pause:
            break


if __name__ == "__main__":

    import pygame, time, random
    pygame.init()
    screen_height = 700
    screen_width = 1200
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill((0,0,0))

   # make water Blue and land White
    initialize_islands_map(screen,Map)
    IslandSet = Disjoint_Sets_datastruct_normal(len(Map),len(Map[0]))
    N_islandsUnionFind(screen, Unite_Islands_Brute)    
    


    time.sleep(1)
    pygame.draw.rect( screen , Black, (40,40, screen_width-100,screen_height))
    font = pygame.font.Font('freesansbold.ttf',50)
    text = font.render("Optimized implementation",True,Dark_yellow)                         
    screen.blit(text,text.get_rect(center = ((screen_width-100)//2,screen_height//2)))
    pygame.display.update()
    game_loop()
    pygame.draw.rect( screen , Black, (40,40, screen_width-100,screen_height))


    # make water Blue and land White
    initialize_islands_map(screen,Map)    
    IslandSet = Disjoint_Sets_datastruct_optimized(len(Map),len(Map[0]))
    N_islandsUnionFind(screen,Unite_Islands_Optimized)



game_loop()