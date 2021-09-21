
import pygame,time,random

Black	     =	    (0,0,0)
White	     =	    (235,235,235)
Lime	     =	    (0,255,0)
Blue	     =	    (0,0,200)
Yellow	     =	    (255,255,0)
Cyan 	     =	    (0,255,255)
Light_sky    = 		(135,206,250)
Red  	     =	    (255,0,0)
Dark_yellow  =      (250,200,0)
Dark_red     =     	(150,0,0)
pygame.init()

h = 60
x0 = 20
y0 = 20
screen_height = 700
screen_width = 1300
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(White)

def mark(screen,node_center,color,radius=4,show=True,Time = 0.03,text = None,text_color = (226, 88, 34)):

    pygame.draw.circle(screen, color, node_center , radius)
    
    if text is not None:
        font = pygame.font.Font('freesansbold.ttf',15)
        text = font.render(text,True,text_color)                        
        screen.blit(text,text.get_rect(center = node_center))
    if show:
        pygame.display.update()
        time.sleep(Time)

def inserting(screen,position,Time):
    mark(screen,position,Lime,Time = Time)

def visiting(screen,position,Time):
    mark(screen,position,Dark_yellow,Time = Time)

RED = True
BLACK = False
class Node:
    def __init__(self,key,val,color):
        self.key = key
        self.val = val
        self.color = color
        self.right = None
        self.left = None

class Red_Black_Tree:
    def __init__(self,screen,Time):
        self.root = None
        self.N_nodes = 0
        self.screen = screen
        self.time = Time

    def isRed(self,node):
        if node is None: return False
        return node.color == RED

    def LeftRotate(self,node):
        assert node is not None and self.isRed(node.right)

        RIGHT = node.right
        node.right,RIGHT.left = RIGHT.left,node
        RIGHT.color = node.color
        node.color = RED
        return RIGHT
    def RightRotate(self,node):
        assert node is not None and self.isRed(node.left)

        LEFT = node.left
        node.left,LEFT.right = LEFT.right,node
        LEFT.color = node.color
        node.color = RED
        return LEFT
    def FlipColors(self,node):
        assert (not self.isRed(node)) and self.isRed(node.left) and self.isRed(node.right)
        node.color,node.left.color,node.right.color = RED,BLACK,BLACK
            
    def insert(self,key):    
        
        position = (x0,screen_width-100,y0)
        
        self.root = self._insert(self.root,key,position)
        self.root.color = Black

    def _insert(self,node,key,position):

        l,r,y = position
        m = (l+r)//2
        position = (m,y)

        if node is None:    
            inserting(self.screen,position,self.time+0.1)
            return Node(key, position, RED)
        
        visiting(self.screen,position,self.time)
        
        
        if         key  < node.key:
            if node.left is None:
                pygame.draw.line(self.screen,Black,(m,y),((m+l)//2,y+h),1)    
            node.left  = self._insert(node.left,  key, (l,m,y+h)) 
            pygame.display.update()
        elif   node.key <    key  :
            if node.right is None:
                pygame.draw.line(self.screen,Black,(m,y),((m+r)//2,y+h),1) 
                pygame.display.update()   
            node.right = self._insert(node.right, key, (m,r,y+h)) 
        else:              node.val   = position

        if self.isRed(node.right) and (not self.isRed(node.left))     : node = self.LeftRotate(node)
        self.display_tree()
        if self.isRed(node.left)  and     self.isRed(node.left.left)  : node = self.RightRotate(node)
        self.display_tree()
        if self.isRed(node.left)  and     self.isRed(node.right)      :        self.FlipColors(node)
        self.display_tree()

        return node
    




    def display_tree(self):
        pygame.draw.rect(self.screen,White,(0,0,screen_width-100,2000))
        self._display_tree(self.root,x0,screen_width-100,y0)

        font = pygame.font.Font('freesansbold.ttf',25)
        text = font.render("Red-Black Tree",True,Dark_red)                         
        screen.blit(text,text.get_rect(center = (1000,20)))

        pygame.display.update()
        time.sleep(self.time)
        
    def _display_tree(self,node,l,r,y):
        if node:
            m = (l+r)//2
            mr,ml = (m+r)//2,(l+m)//2
            #print node
            if self.isRed(node):
                mark(self.screen,(m,y),Red,show=False)
            else:
                mark(self.screen,(m,y),Black,show=False)
            #print edges
            if node.right:
                if   self.isRed(node.right):
                    pygame.draw.line(self.screen,Red,(m,y),(mr,y+h),1)
                else:
                    pygame.draw.line(self.screen,Black,(m,y),(mr,y+h),1)

                self._display_tree(node.right,m, r, y+h)
            if node.left:
                if   self.isRed(node.left):
                    pygame.draw.line(self.screen,Red,(m,y),(ml,y+h),1)
                else:              
                    pygame.draw.line(self.screen,Black,(m,y),(ml,y+h),1)
            
                self._display_tree(node.left ,l, m, y+h)




treeSlow = Red_Black_Tree(screen,0.5)
treeFast = Red_Black_Tree(screen,0)
number = list(range(1,16))


#game loop
slow = True
fast = False
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

    if slow:
        number = []
        if len(number):
            r=random.randint(0, len(number)-1)
            num = number[r]
            number.pop(r)
            treeSlow.insert(num)
            treeSlow.display_tree()
            
        else:
            number = list(range(0,251))
            slow = False
            fast = True
            
            pygame.draw.rect(screen,White,(0,0,screen_width-100,2000))# clear screen
            font = pygame.font.Font('freesansbold.ttf',25)
            text = font.render("Red-Black Tree",True,Dark_red)                         
            screen.blit(text,text.get_rect(center = (1000,40)))

            font = pygame.font.Font('freesansbold.ttf',50)
            text = font.render("Fast animation",True,Dark_red)                         
            screen.blit(text,text.get_rect(center = ((screen_width-100)//2,screen_height//2)))
            text = font.render("random insertions",True,Red)                         
            screen.blit(text,text.get_rect(center = ((screen_width-100)//2,screen_height//2+50)))
            pygame.display.update()
            time.sleep(3)
            pygame.draw.rect(screen,White,(0,0,screen_width-100,2000))
            pygame.display.update()
        time.sleep(0.5)
    
    if fast:

        if len(number):
            r=random.randint(0, len(number)-1)
            num = number[r]
            number.pop(r)
            treeFast.insert(num)
            treeFast.display_tree()
            
        else:
            pause = True


        time.sleep(0.01)

    