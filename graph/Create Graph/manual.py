# draw manually a graph on the screen.
#when exit pygame, print(edge_dict) and print(node_list)

import pygame,time
pygame.init()                   #width , height : coordinates 0,0 no canto superior esquerdo
screen = pygame.display.set_mode((800,600))
screen.fill((0,0,0))     



register = False    # register  new edge
edge_dict = {}      
node_list = []

cur = None
seted_cur = False
n_cur= 0

pointing = None         
pointing_number = -1            #info of the green node, the edges goes from him to cur
seted = False                   # when is seted, pointing dont adnvance automaticaly, but stays where we put him


#game Loop
running = True
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                
                seted = False
                if pointing  and cur  and ( (pointing,cur) not in edge_dict ):  # "not in edge_dict" beacause whe we clik space the program thinks we've touched many times
                    edge_dict[(pointing,cur)] = 1
                    pygame.draw.line(screen, (255,255,255), pointing, cur)
            
            if event.key == pygame.K_RIGHT:
                
                seted = True

                if pointing_number < len(node_list)-1:                          # avoid bugs running away the nodes list
                    
                    if pointing:                                                # avoid bugs  when there is no pointing yet (haven't put 2 nodes yet)
                        pygame.draw.circle(screen,(0,0,255),pointing,5)
                        pointing_number += 1
                        pointing = node_list[pointing_number]
                        pygame.draw.circle(screen,(0,255,0),pointing,5)

                    else:                                           
                        pointing_number = len(node_list)  -1
                        pointing = node_list[pointing_number]
                        pygame.draw.circle(screen,(0,255,0),pointing,5)

            
            if event.key == pygame.K_UP:                                        
                
                if n_cur < len(node_list)-1:
                    pygame.draw.circle(screen,(0,0,0),cur,7)
                    pygame.draw.circle(screen,(0,0,255),cur,5)
                    
                    n_cur += 1
                    cur = node_list[n_cur] 
                    pygame.draw.circle(screen,(255,0,0),cur,7)



            if event.key == pygame.K_DOWN:
                
                if n_cur > 0:
                    pygame.draw.circle(screen,(0,0,0),cur,7)
                    pygame.draw.circle(screen,(0,0,255),cur,5)
                    
                    n_cur -= 1
                    cur = node_list[n_cur] 
                    pygame.draw.circle(screen,(255,0,0),cur,7)                    


            if event.key == pygame.K_LEFT:  # same thing as RIGHT, but simpler 
                seted = True
                if pointing_number > 0:
                    if pointing:
                        pygame.draw.circle(screen,(0,0,255),pointing,5)
                        pointing_number -= 1
                        pointing = node_list[pointing_number]
                        pygame.draw.circle(screen,(0,255,0),pointing,5)
                    

            if event.key == pygame.K_SPACE:
                register = False

        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:      # put nodes on the screen

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.pos not in node_list:
                        
                        if cur:
                            pygame.draw.circle(screen,(0,0,0),cur,7)
                            pygame.draw.circle(screen,(0,0,255),cur,5)
                            

                        pygame.draw.circle(screen,(255,0,0),event.pos,7)
                        node_list.append(event.pos)

                        if not seted:   #advance pointing automaticaly
                            
                            if pointing:
                                pygame.draw.circle(screen,(0,0,255),pointing,5)
                            
                            pointing = cur

                            if pointing:
                                pygame.draw.circle(screen,(0,255,0),pointing,5)
                                pointing_number += 1

                        cur = event.pos
                        n_cur +=1
                        

                        
                #elif event.type == pygame.MOUSEBUTTONUP:
                #    print(event.pos)
        


    pygame.display.update()
    time.sleep(0.1)             # avoid bugs/repetion of actions, because the program detects too many times when we interact with it




node_dict ={}                                                                   # convert position to node's index

for index,node in enumerate(node_list):

    node_dict[node] = index


graph = []                                                                      # create graph
for x in range(len(node_list)):
    graph.append([])

for node1,node2 in edge_dict:                                               

    graph[node_dict[node1]].append(node_dict[node2])                            # fill graph
    graph[node_dict[node2]].append(node_dict[node1])


print("\n\nedge_dict = ",edge_dict)

print("\n\nnode_list =",node_list)

print("\n\ngraph = ",graph)
