import pygame,time,random

Black	     =	    (0,0,0)
White	     =	    (255,255,255)
Lime	     =	    (0,255,0)
Blue	     =	    (0,0,200)
Yellow	     =	    (255,255,0)
Cyan 	     =	    (0,255,255)
Light_sky    = 		(135,206,250)

pygame.init()

h = 70
x0 = 20
y0 = 20
screen_height = 700
screen_width = 1300
screen = pygame.display.set_mode((screen_width,screen_height))

screen.fill((0,0,0))

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
    mark(screen,position,Blue,Time = Time)

class Node:
    def __init__(self,key,position):
        self.key = key
        self.position = position
        self.right = None
        self.left = None
        self.height = 1


class AVLtree:
    def __init__(self,screen,Time):
        self.root = None
        self.N_nodes = 0
        self.screen = screen
        self.time = Time

    def insert(self,key):
        self.N_nodes+=1
        
        position = (x0,screen_width-100,y0)
        
        self.root,valid = self._internalInsertion(self.root,key,position)
        return valid # if there was already this key: return false

    def inOrder(self):
        self._inOrder(self.root)
        print()

    def _internalInsertion(self,root,key,position,valid=True):
        
        l,r,y = position
        x = (l+r)//2
        position = (x,y)

        if root is None:
            inserting(self.screen,position,self.time)
            time.sleep(0.1)
            return Node(key,position),True
        
        root.position = position
        position = (l,r,y)

        if root.key < key:
            
            l,r,y = position
            m = (l+r)//2
            visiting(self.screen,(m,y),self.time)
            y += h
            position = m,r,y
            if root.right is None: 
                pygame.draw.line(self.screen,White,(m,y-h),((m+r)//2,y),1)
                pygame.display.update()
            root.right,valid = self._internalInsertion(root.right,key,position,valid)

        elif root.key > key:
            
            l,r,y = position
            m = (l+r)//2
            visiting(self.screen, (m,y),self.time )
            y += h
            position = l,m,y
            if root.right is None: 
                pygame.draw.line(self.screen,White,(m,y-h),((m+l)//2,y),1)
                pygame.display.update()
            root.left,valid = self._internalInsertion(root.left,key,position,valid)
        else: return root,not valid #don't allow 2 nodes with same key
        
        if valid == False: return root,False #don't allow 2 nodes with same key


        self._updateHeight(root)
        balance = self._getBalance(root)
        
        #left
        if balance < -1:
            mark(self.screen,root.position,Yellow,Time=self.time)
            if key > root.left.key: #left-right, else: left-left
                root.left =  self._leftRotate(root.left)
                self.display_tree()
                time.sleep(self.time)
            return self._rightRotate(root),True
        #right
        if balance > 1:
            mark(self.screen,root.position,Light_sky,Time = self.time)
            if key < root.right.key: #right-left, else: right-right
                root.right = self._rightRotate(root.right)
                self.display_tree()
                time.sleep(self.time)
            return self._leftRotate(root),True
        
        return root,True

    def display_tree(self):
        pygame.draw.rect(self.screen,Black,(0,0,screen_width-100,2000))
        self._display_tree(self.root,x0,screen_width-100,y0)

        font = pygame.font.Font('freesansbold.ttf',25)
        text = font.render("AVL Tree",True,Cyan)                         
        screen.blit(text,text.get_rect(center = (1000,20)))

        pygame.display.update()
        

    # this functions are better to be in the avl
    # so the memory for each node is smaller,
    # otherwise each node would have a space for the function set
    def _display_tree(self,node,l,r,y):
        if node:
            m = (l+r)//2
            mr,ml = (m+r)//2,(l+m)//2
            mark(self.screen,(m,y),White,show=False)
            if node.right: pygame.draw.line(self.screen,White,(m,y),(mr,y+h),1)
            if node.left:  pygame.draw.line(self.screen,White,(m,y),(ml,y+h),1)
            self._display_tree(node.left ,l, m, y+h)
            self._display_tree(node.right,m, r, y+h)

    def _getBalance(self,node):
        if node.right is None: H_right = 0
        else: H_right = node.right.height
        if node.left is None:  H_left  = 0
        else: H_left  = node.left.height

        return H_right - H_left

    def _updateHeight(self,node):# use wisely
        if node.right is None: H_right = 0
        else: H_right = node.right.height
        if node.left is None:  H_left  = 0
        else: H_left  = node.left.height

        node.height = 1 + max(H_left, H_right)
    
    def _rightRotate(self,node):
        LEFT = node.left
        LEFT.right,node.left = node,LEFT.right

        self._updateHeight(node)
        self._updateHeight(LEFT)   

        return LEFT #return so to parent node can link to the new subroot

    def _leftRotate(self,node):
        RIGHT = node.right
        RIGHT.left,node.right = node,RIGHT.left
        
        self._updateHeight(node)
        self._updateHeight(RIGHT)


        return RIGHT

    def _inOrder(self,node):
        if node is not None:
            self._inOrder(node.left)
            print(node.val,end=" ")
            self._inOrder(node.right)



treeSlow = AVLtree(screen,0.6)
treeFast = AVLtree(screen,0.01)
number = list(range(1,16))

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
            
            pygame.draw.rect(screen,Black,(0,0,screen_width-100,2000))# clear screen
            font = pygame.font.Font('freesansbold.ttf',25)
            text = font.render("AVL Tree",True,Cyan)                         
            screen.blit(text,text.get_rect(center = (1000,40)))

            font = pygame.font.Font('freesansbold.ttf',50)
            text = font.render("Fast animation",True,Cyan)                         
            screen.blit(text,text.get_rect(center = ((screen_width-100)//2,screen_height//2)))
            text = font.render("random insertions",True,Cyan)                         
            screen.blit(text,text.get_rect(center = ((screen_width-100)//2,screen_height//2+50)))
            pygame.display.update()
            time.sleep(3)
            pygame.draw.rect(screen,Black,(0,0,screen_width-100,2000))
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

    
