import pygame,time,random
from graph.color import *

pygame.init()

forget = (1,0,0)

h = 80
x0 = 20
y0 = 20
screen_height = 700
screen_width = 1300
screen = pygame.display.set_mode((screen_width,screen_height))

screen.fill((0,0,0))

def mark(screen,node_center,color,radius=4,show=True,Time = 0.02,text = None,text_color = (226, 88, 34)):

    pygame.draw.circle(screen, color, node_center , radius)
    
    if text is not None:
        font = pygame.font.Font('freesansbold.ttf',15)
        text = font.render(text,True,text_color)                        
        screen.blit(text,text.get_rect(center = node_center))
    if show:
        pygame.display.update()
        time.sleep(Time)

def inserting(screen,position):
    mark(screen,position,Lime)

def visiting(screen,position):
    mark(screen,position,Blue)

class Node:
    def __init__(self,key,position):
        self.key = key
        self.position = position
        self.right = None
        self.left = None
        self.height = 1


class AVLtree:
    def __init__(self,screen):
        self.root = None
        self.N_nodes = 0
        self.screen = screen

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
            inserting(self.screen,position)

            return Node(key,position),True
        
        root.position = position
        position = (l,r,y)

        if root.key < key:
            
            l,r,y = position
            m = (l+r)//2
            visiting(self.screen,(m,y))
            y += h
            position = m,r,y
            root.right,valid = self._internalInsertion(root.right,key,position,valid)

        elif root.key > key:
            
            l,r,y = position
            m = (l+r)//2
            visiting(self.screen, (m,y) )
            y += h
            position = l,m,y
            root.left,valid = self._internalInsertion(root.left,key,position,valid)
        else: return root,not valid #don't allow 2 nodes with same key
        
        if valid == False: return root,False #don't allow 2 nodes with same key


        self._updateHeight(root)
        balance = self._getBalance(root)
        
        #left
        if balance < -1:
            if key > root.left.key: #left-right, else: left-left
                root.left =  self._leftRotate(root.left)
            return self._rightRotate(root),True
        #right
        if balance > 1:
            if key < root.right.key: #right-left, else: right-right
               root.right = self._rightRotate(root.right)
            return self._leftRotate(root),True
        
        return root,True

    def display_tree(self):
        pygame.draw.rect(self.screen,Black,(0,0,screen_width-100,2000))
        self._display_tree(self.root,x0,screen_width-100,y0)
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




tree = AVLtree(screen)

number = list(range(1,251))

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
    
    if len(number):
        r=random.randint(0, len(number)-1)
        num = number[r]
        number.pop(r)
        tree.insert(num)
        tree.display_tree()
    else: pause = True
        
