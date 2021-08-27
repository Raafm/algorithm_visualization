from graph.bst import children,root
from data_struct.TreeNode import TreeNode
from data_struct.stack import stack
import pygame,time
from graph.color import *


pygame.init()

forget = (1,0,0)

screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))

cur_color = Red
memory_color = Flame
seen_color = Yellow
node_size  = 5
rootNode   = TreeNode(root)

def print_treeNode(treeNode,colour):
    if treeNode is None: return
    print(treeNode.data)
    pygame.draw.circle(screen,colour,treeNode.data,node_size)
    pygame.display.update()

def convert_to_tree(sub_root):
    if sub_root is not None:

        if children[sub_root.data][0] is not None:
            Rnode = TreeNode(children[sub_root.data][0])
            pygame.draw.line(screen,White,sub_root.data,Rnode.data,2)
        else: Rnode = None
        if children[sub_root.data][1] is not None:
            Lnode = TreeNode(children[sub_root.data][1])
            pygame.draw.line(screen,White,sub_root.data,Lnode.data,2)
        else: Lnode = None
        sub_root.link(Rnode,False)
        sub_root.link(Lnode,True)
        convert_to_tree(sub_root.right)
        convert_to_tree(sub_root.left)
        

        print_treeNode(sub_root,Blue)
        print(sub_root.data)    


convert_to_tree(rootNode)






S = stack()
S.insert(rootNode)
cur = None

seen = {}


running =  True
pause = False
while running:
       
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_SPACE:         # click breakspace for pause
                pause = not pause                   # if it is paused, click breakspace for play(resume)
                time.sleep(0.2)
    
    if pause:
        continue


    if S.not_empty():
        if cur is not None:
            print_treeNode(cur,seen_color)
        cur = S.pop()
        
        print_treeNode(cur,cur_color)
        
        if cur.right is not None: S.insert(cur.right); print_treeNode(cur.right,memory_color)
        if cur.left is not None: S.insert(cur.left)  ; print_treeNode(cur.left,memory_color)
    


    else:# S is empty
        pause = True




    
    time.sleep(0.5)