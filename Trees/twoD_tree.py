class Node:
    def __init__(self,position):
        self.left  = None
        self.right = None
        self.x = position[0]
        self.y = position[1]

points = [
    (484, 67),  # 0
    (241, 344), # 1
    (818, 145), #2
    (193, 176),  #3
    (367, 580), #4
    (664, 456), #5
    (942, 97),  #6
    (754, 555), #7 
    (586, 628), #8
    (148, 487), #9
    (160, 107),  #10
    (431, 278), #11
    (542, 408), #12
    (882, 523), #13
    (205, 599), #14
    (347, 76),  #15
    (669, 236), #16
    (972, 368), #17
    (986, 30),  #18
    (700,120),  #19
    (990,620),  #20
    (750,300),  #21
    (50,450),   #22
    (153, 236), #23
    (510,200),  #24

]        


vintequatro = Node(points[24])
vintetres   = Node(points[23])
vintedois   = Node(points[22])
vinteum     = Node(points[21])
vinte       = Node(points[20])
dezenove    = Node(points[19])
dezoito     = Node(points[18])
dezessete   = Node(points[17])
dezesseis   = Node(points[16])
quinze      = Node(points[15])
quatorze    = Node(points[14])
treze       = Node(points[13])
doze        = Node(points[12])
onze        = Node(points[11])
dez         = Node(points[10])
nove        = Node(points[9])
oito        = Node(points[8])
sete        = Node(points[7])
seis        = Node(points[6])
cinco       = Node(points[5])
quatro      = Node(points[4])
tres        = Node(points[3])
dois        = Node(points[2])
um          = Node(points[1])
zero        = Node(points[0])


root = doze

vintequatro.left = zero

dezessete.right = sete
dezessete.left = dois

dezesseis.right = vinteum
dezesseis.left = dezenove

quinze.right = vintequatro
quinze.left = tres

quatorze.left  = nove
quatorze.right = quatro

treze.right = vinte

doze.left  = onze
doze.right = dezessete

onze.left  = quinze
onze.right = quatorze

nove.left= vintedois

sete.left  = cinco
sete.right = treze

seis.left = dezoito

cinco.right = oito

quatro.left = um

tres.right= vintetres
tres.left= dez

dois.left  = dezesseis
dois.right =  seis



def reverse_tree(cur):
    if cur is not None:
        cur.left,cur.right = cur.right,cur.left
        
        reverse_tree(cur.left)  
        reverse_tree(cur.right)



if __name__ == "__main__":
    import pygame
    White = (255,255,255)
    Black = (0,0,0)
    Blue = (0,0,255)

    pygame.init()
    screen_width,screen_height = 1200,700
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill(Black)

    def print_point(position, color= White,radius = 4, index=-1):
        pygame.draw.circle(screen,color,position,radius)
        if index > -1:
            font = pygame.font.Font('freesansbold.ttf',14)
            text = font.render( str(index),True, White)    
            screen.blit(text,text.get_rect(center = position))
        
        pygame.display.update()


    for index,P in enumerate(points):
        print_point(P,radius = 10,color = Blue, index = index)

    

   

    running =  True
    while running :

        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                running = False                          #exit() program
