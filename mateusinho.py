import pygame,time

edge_dict =  {
 ((303, 324), (265, 245)): 1,
  ((265, 245),(170, 210)): 1,
  ((170, 210),(171, 163)): 1,
  ((171, 163),(114, 107)): 1,
  ((114, 107),(78, 54)):   1,
  (( 78, 54 ),(35, 45)):   1,
  ((303, 324),(263, 314)): 1,
  ((263, 314),(198, 297)): 1,
  ((198, 297),(155, 304)): 1,
  ((155, 304),(113, 272)): 1,
  ((113, 272),(107, 226)): 1,
  ((107, 226),(66, 219)):  1,
  ((66, 219),(34, 243)):   1,
  ((303, 324),(258, 360)): 1,
  ((258, 360),(210, 369)): 1,
  ((210, 369),(147, 362)): 1,
  ((147, 362),(119, 390)): 1,
  ((119, 390),(60, 332)):  1,
  ((60, 332),(37, 384)):   1,
  ((303, 324),(320, 349)): 1,
  ((320, 349),(349, 360)): 1,
  ((349, 360),(370, 397)): 1,
  ((370, 397),(406, 400)): 1,
  ((406, 400),(409, 446)): 1,
  ((409, 446),(442, 467)): 1,
  ((442, 467),(433, 510)): 1,
  ((433, 510),(392, 518)): 1,
  ((303, 324),(342, 288)): 1,
  ((342, 288),(336, 235)): 1,
  ((336, 235),(318, 197)): 1,
  ((318, 197),(296, 156)): 1,
  ((296, 156),(290, 94)):  1,
  ((318, 197),(362, 169)): 1,
  ((362, 169),(372, 129)): 1,
  ((372, 129),(390, 89)):  1,
  ((390, 89),(438, 85)):   1,
  ((362, 169),(439, 162)): 1,
  ((439, 162),(465, 196)): 1,
  ((342, 288),(388, 296)): 1,
  ((388, 296),(446, 268)): 1,
  ((446, 268),(475, 318)): 1,
  ((446, 268),(495, 256)): 1,
  ((495, 256),(515, 207)): 1,
  ((442, 467),(492, 455)): 1,
  ((492, 455),(505, 408)): 1,
  ((505, 408),(539, 465)): 1,
  ((505, 408),(562, 372)): 1,
  ((392, 518),(340, 496)): 1,
  ((320, 349),(305, 390)): 1,
  ((305, 390),(234, 432)): 1,
  ((234, 432),(229, 474)): 1,
  ((229, 474),(193, 486)): 1,
  ((193, 486),(120, 458)): 1,
  ((120, 458),(102, 498)): 1,
  ((102, 498),(42, 517)):  1,
  ((42, 517),(76, 551)):   1,
  ((193, 486),(224, 540)): 1,
  ((224, 540),(272, 552)): 1,
  ((171, 163),(194, 92)):  1,
  ((194, 92),(251, 57)):   1,
  ((251, 57),(309, 29)):   1,
  ((114, 107),(140, 53)):  1,
  ((140, 53),(174, 22)):   1,
  ((114, 107),(65, 129)):  1,
  ((65, 129),(73, 160)):   1,
  ((372, 129),(346, 86)):  1,
  ((346, 86),(380, 46)):   1,
  ((296, 156),(255, 158)): 1,
  ((255, 158),(219, 121)): 1,
  ((255, 158),(244, 186)): 1,
  ((244, 186),(277, 208)): 1,
  ((388, 296),(404, 343)): 1,
  ((404, 343),(449, 366)): 1,
  ((449, 366),(503, 338)): 1,
  ((475, 318),(540, 283)): 1,
  ((540, 283),(548, 323)): 1,
  ((446, 268),(409, 228)): 1,
  ((392, 518),(386, 473)): 1,
  ((386, 473),(348, 450)): 1,
  ((392, 518),(373, 545)): 1,
  ((373, 545),(347, 565)): 1,
  ((347, 565),(417, 550)): 1
}


node_list = [(303, 324),
 (265, 245),
 (170, 210),
 (171, 163),
 (114, 107),
 (78, 54),
 (35, 45),
 (263, 314),
 (198, 297),
 (155, 304),
 (113, 272),
 (107, 226),
 (66, 219),
 (34, 243),
 (258, 360),
 (210, 369),
 (147, 362),
 (119, 390),
 (60, 332),
 (37, 384),
 (320, 349),
 (349, 360),
 (370, 397),
 (406, 400),
 (409, 446),
 (442, 467),
 (433, 510),
 (392, 518),
 (342, 288),
 (336, 235),
 (318, 197),
 (296, 156),
 (290, 94),
 (362, 169),
 (372, 129),
 (390, 89),
 (438, 85),
 (439, 162),
 (465, 196),
 (388, 296),
 (446, 268),
 (475, 318),
 (495, 256),
 (515, 207),
 (492, 455),
 (505, 408),
 (539, 465),
 (562, 372),
 (340, 496),
 (305, 390),
 (234, 432),
 (229, 474),
 (193, 486),
 (120, 458),
 (102, 498),
 (42, 517),
 (76, 551),
 (224, 540),
 (272, 552),
 (194, 92),
 (251, 57),
 (309, 29),
 (140, 53),
 (174, 22),
 (65, 129),
 (73, 160),
 (346, 86),
 (380, 46),
 (255, 158),
 (219, 121),
 (244, 186),
 (277, 208),
 (404, 343),
 (449, 366),
 (503, 338),
 (540, 283),
 (548, 323),
 (409, 228),
 (386, 473),
 (348, 450),
 (373, 545),
 (347, 565),
 (417, 550)]


node_dict ={}                                                                   # convert position to node's index

for index,node in enumerate(node_list):

    node_dict[node] = index


graph = []                                                                      # create graph
for x in range(len(node_list)):
    graph.append([])

for node1,node2 in edge_dict:                                               

    graph[node_dict[node1]].append(node_dict[node2])                            # fill graph
    graph[node_dict[node2]].append(node_dict[node1])



import pygame,time,random


pygame.init()


screen_height = 700
screnn_width = 1000
screen = pygame.display.set_mode((screnn_width,screen_height))

screen.fill((0,0,0))

for node1,node2 in edge_dict:                                                   # draw edges
    pygame.draw.line(screen,(255,255,255), node1, node2, 2)

for node in node_list:                                                          # draw nodes
    pygame.draw.circle(screen,  (0,0,255), node, 5)


font = pygame.font.Font('freesansbold.ttf',15)


cor_A = (255,150,100)
cor_B = (100,250,155)






font = pygame.font.Font('freesansbold.ttf',18)
text = font.render("Escolha metade ou menos dos nodes",True,(0,255,0))                   # informative node       
screen.blit(text,text.get_rect(center = (820,50)))

font = pygame.font.Font('freesansbold.ttf',20)
text = font.render(" para formar um conjunto",True,(0,255,0))                   # informative node       
screen.blit(text,text.get_rect(center = (820,70)))

font = pygame.font.Font('freesansbold.ttf',20)
text = font.render("de modo que todos os outros nodes",True,(0,255,0))                   # informative node       
screen.blit(text,text.get_rect(center = (820,90)))


font = pygame.font.Font('freesansbold.ttf',20)
text = font.render(" estejam conectados a este conjunto",True,(0,255,0))                   # informative node       
screen.blit(text,text.get_rect(center = (820,110)))


font = pygame.font.Font('freesansbold.ttf',15)
pygame.draw.circle(screen,(0,0,255), (850,130),5)
text = font.render("V",True,(0,0,255))
screen.blit(text,text.get_rect(center = (915,130)))                             # informative node 

font = pygame.font.Font('freesansbold.ttf',20)

text = font.render("Number of nodes:" + str(len(graph)),True,(255,255,255))
screen.blit(text,text.get_rect(center = (890,280)))                             # informative node 

font = pygame.font.Font('freesansbold.ttf',15)
pygame.draw.circle(screen,cor_A, (850,160),10)
text = font.render("A",True,cor_A)
screen.blit(text,text.get_rect(center = (915,160)))                             # informative node   

pygame.draw.circle(screen,cor_B, (850,200),10)
text = font.render("B",True,cor_B)
screen.blit(text,text.get_rect(center = (915,200)))                             # informative node   

pygame.display.update()                                                         # display graph and infos before algorithm 


V = list(  node_id for node_id in range(len(graph)))

A = []  
B = [] 

current = 0

pause = True            # doesn't start until press play (breakspace)
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                   #exit pygame,
            quit()                          #exit() program


        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
                time.sleep(0.2)
    
    if pause:
        continue


    if len(V): 

        current = V.pop(random.randint(0, len(V)-1))        
        pygame.draw.circle(screen,  (255,255,255), node_list[current] , 10)


        all_in_A = True
        for neighbour in graph[current]:

            if (neighbour in A):
                continue
            else:
                all_in_A = False

            if(neighbour in B):
                continue

            pygame.draw.circle(screen,  cor_B, node_list[neighbour] , 10)
            B.append(neighbour)
            V.remove(neighbour)
        
        if all_in_A:
            B.append(current)
            pygame.draw.circle(screen,  cor_B, node_list[current] , 10)
        else:
            A.append(current)
            pygame.draw.circle(screen,  cor_A, node_list[current] , 10)
            

    else:
        font = pygame.font.Font('freesansbold.ttf',20)
        qtd_A = "number of elements in A: " + str(len(A))
        text = font.render(qtd_A,True,cor_A)                      
        screen.blit(text,text.get_rect(center = (800,350)))
        
        font = pygame.font.Font('freesansbold.ttf',20)
        qtd_B = "number of elements in B: " + str(len(B))
        text = font.render(qtd_B,True,cor_B)                         
        screen.blit(text,text.get_rect(center = (800,405)))

        font = pygame.font.Font('freesansbold.ttf',30)
        awnser= "awnser " + str(min(len(A),len(B)))
        text = font.render(awnser,True,(0,255,0))                   # informative node       
        screen.blit(text,text.get_rect(center = (800,500)))

    pygame.display.update()
    time.sleep(0.7)