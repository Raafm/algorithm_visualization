import math 
cor = (255,255,255)
peso = 1
raio  =12
White = (255,255,255)
cor_aresta = White
width = 2

nodes = [
    [ cor, (50 , 30), raio ],  # node 0 
    [ cor, (130 ,20), raio ],  # node 1
    [ cor, (80 ,100), raio ],  # node 2
    [ cor, (65 ,180), raio ],  # node 3
    [ cor, (180,120), raio ],  # node 4
    [ cor, (280 ,50), raio ],  # node 5
    [ cor, (130,320), raio ],  # node 6
    [ cor, (330,110), raio ],  # node 7
    [ cor, (380,220), raio ],  # node 8
    [ cor, (180,235), raio ],  # node 9
    [ cor, (220,400), raio ],  # node 10
    [ cor, (288,520), raio ],  # node 11
    [ cor, (280,180), raio ],  # node 12
    [ cor, (470,410), raio ],  # node 13
    [ cor, (465, 70), raio ],  # node 14
    [ cor, (260,300), raio ],  # node 15
    [ cor, (450,540), raio ],  # node 16
    [ cor, (60 ,380), raio ],  # node 17
    [ cor, (160,483), raio ],  # node 18
    [ cor, (340,360), raio ],  # node 19
    [ cor, (485,330), raio ],  # node 20
    [ cor, (440,270), raio ],  # node 21
    [ cor, (330,460), raio ],  # node 22
    [ cor, (580,459), raio ],  # node 23
    [ cor, (560,240), raio ],  # node 24
    [ cor, (640,150), raio ],  # node 25
    [ cor, (650,366), raio ],  # node 26
    [ cor, (630, 20), raio ],  # node 27
    [ cor, (760,380), raio ],  # node 28
    [ cor, (800,310), raio ],  # node 29
    [ cor, (787,110), raio ],  # node 30
    [ cor, (760,210), raio ],  # node 31
    [ cor, (860, 60), raio ],  # node 32
    [ cor, (860,210), raio ],  # node 33
    [ cor, (910,330), raio ],  # node 34
    [ cor, (840,450), raio ],  # node 35
    [ cor, (720,510), raio ],  # node 36
    [ cor, (940,480), raio ],  # node 37
    [ cor, (540,140), raio ],  # node 38
    [ cor, (976,580), raio ]   # node 39
  ] 

# como coloquei os pesos
#def distance(node1,node2):
#    _,(x1,y1),_ = nodes[node1]
#    _,(x2,y2),_ = nodes[node2]
#    
#    return math.hypot(x2 - x1, y2 - y1)
#
#for edge in lista_arestas:
#    _,node1,node2 = edge
#    
#    print(distance(node1,node2))
 
lista_arestas = [
[cor_aresta, 0, 1, 80.62257748298549] ,
[cor_aresta, 0, 2, 76.15773105863909] ,
[cor_aresta, 1, 4, 111.80339887498948] ,
[cor_aresta, 2, 3, 81.39410298049853] ,
[cor_aresta, 2, 4, 101.9803902718557] ,
[cor_aresta, 3, 9, 127.47548783981962] ,
[cor_aresta, 4, 5, 122.06555615733703] ,
[cor_aresta, 4, 9, 115.0] ,
[cor_aresta, 5, 12, 130.0] ,
[cor_aresta, 5, 14, 186.07794065928394] ,
[cor_aresta, 6, 10, 120.41594578792295] ,
[cor_aresta, 6, 17, 92.19544457292886] ,
[cor_aresta, 6, 9, 98.6154146165801] ,
[cor_aresta, 7, 8, 120.83045973594571] ,
[cor_aresta, 7, 12, 86.02325267042627] ,
[cor_aresta, 8, 14, 172.4093964956667] ,
[cor_aresta, 8, 38, 178.88543819998318] ,
[cor_aresta, 8, 21, 78.10249675906655] ,
[cor_aresta, 9, 15, 103.07764064044152] ,
[cor_aresta, 10, 11, 137.92751719653336] ,
[cor_aresta, 10, 18, 102.41581909060729] ,
[cor_aresta, 11, 16, 163.22989922192565] ,
[cor_aresta, 13, 19, 139.2838827718412] ,
[cor_aresta, 13, 22, 148.66068747318505] ,
[cor_aresta, 13, 16, 131.52946437965903] ,
[cor_aresta, 13, 26, 185.29975715040752] ,
[cor_aresta, 38, 25, 100.4987562112089] ,
[cor_aresta, 38, 27, 150.0] ,
[cor_aresta, 16, 22, 144.22205101855957] ,
[cor_aresta, 16, 23, 153.16984037335808] ,
[cor_aresta, 17, 18, 143.55835050598762] ,
[cor_aresta, 19, 20, 148.07092894960846] ,
[cor_aresta, 19, 21, 134.5362404707371] ,
[cor_aresta, 19, 15, 100.0] ,
[cor_aresta, 19, 22, 100.4987562112089] ,
[cor_aresta, 20, 24, 117.15374513859983] ,
[cor_aresta, 23, 36, 149.0] ,
[cor_aresta, 24, 26, 154.8418548067673] ,
[cor_aresta, 24, 31, 202.23748416156684] ,
[cor_aresta, 25, 30, 152.34500319997372] ,
[cor_aresta, 25, 31, 134.1640786499874] ,
[cor_aresta, 26, 28, 110.8873302050329] ,
[cor_aresta, 26, 29, 160.11246047700348] ,
[cor_aresta, 27, 30, 180.96684779262748] ,
[cor_aresta, 27, 32, 233.45235059857504] ,
[cor_aresta, 28, 34, 158.11388300841898] ,
[cor_aresta, 28, 36, 136.01470508735446] ,
[cor_aresta, 29, 31, 107.70329614269009] ,
[cor_aresta, 30, 33, 123.81033882515628] ,
[cor_aresta, 30, 31, 103.58088626768938] ,
[cor_aresta, 33, 34, 130.0] ,
[cor_aresta, 34, 35, 138.92443989449805] ,
[cor_aresta, 35, 37, 104.40306508910551] ,
[cor_aresta, 35, 36, 134.1640786499874] ,
[cor_aresta, 36, 37, 222.0360331117452] ,
[cor_aresta, 37, 39, 106.28264204469137] 
]

graph = [
    (1, 2),  
    (0, 4),  
    (0, 3, 4),  
    (2, 9),  
    (1, 2, 5, 9),  
    (4, 12, 14),  
    (10, 17, 9),  
    (8, 12),  
    (7, 14, 38, 21),  
    (3, 4, 6, 15),  
    (6, 11, 18),  
    (10, 16),  
    (5, 7),  
    (19, 22, 16, 26),  
    (5, 8),  
    (9, 19),  
    (11, 13, 22, 23),  
    (6, 18),  
    (10, 17),  
    (13, 20, 21, 15, 22),  
    (19, 24),  
    (8, 19),  
    (13, 16, 19),  
    (16, 36),  
    (20, 26, 31),  
    (38, 30, 31),  
    (13, 24, 28, 29),  
    (38, 30, 32),  
    (26, 34, 36),  
    (26, 31),  
    (25, 27, 33, 31),  
    (24, 25, 29, 30),  
    (27),  
    (30, 34),  
    (28, 33, 35),  
    (34, 37, 36),  
    (23, 28, 35, 37),  
    (35, 36, 39),  
    (8, 25, 27), 
    (37)
]

# como eu fiz: 
#edge_dict = dict()
#for cor, node1,node2,peso in lista_arestas:
#    if (node1,node2) in edge_dict:
#        continue
#    else:
#        edge_dict[(node1,node2)] = (cor,peso)
#
#
#for edge in edge_dict:
#   print(edge,":", edge_dict[edge],",")

edge_dict = {
    (0, 1) : (cor_aresta, 80.62257748298549 , width) ,
    (0, 2) : (cor_aresta, 76.15773105863909 , width) ,
    (1, 4) : (cor_aresta, 111.80339887498948 , width) ,
    (2, 3) : (cor_aresta, 81.39410298049853 , width) ,
    (2, 4) : (cor_aresta, 101.9803902718557 , width) ,
    (3, 9) : (cor_aresta, 127.47548783981962 , width) ,
    (4, 5) : (cor_aresta, 122.06555615733703 , width) ,
    (4, 9) : (cor_aresta, 115.0 , width) ,
    (5, 12) : (cor_aresta, 130.0 , width) ,
    (5, 14) : (cor_aresta, 186.07794065928394 , width) ,
    (6, 10) : (cor_aresta, 120.41594578792295 , width) ,
    (6, 17) : (cor_aresta, 92.19544457292886 , width) ,
    (6, 9) : (cor_aresta, 98.6154146165801 , width) ,
    (7, 8) : (cor_aresta, 120.83045973594571 , width) ,
    (7, 12) : (cor_aresta, 86.02325267042627 , width) ,
    (8, 14) : (cor_aresta, 172.4093964956667 , width) ,
    (8, 38) : (cor_aresta, 178.88543819998318 , width) ,
    (8, 21) : (cor_aresta, 78.10249675906655 , width) ,
    (9, 15) : (cor_aresta, 103.07764064044152 , width) ,
    (10, 11) : (cor_aresta, 137.92751719653336 , width) ,
    (10, 18) : (cor_aresta, 102.41581909060729 , width) ,
    (11, 16) : (cor_aresta, 163.22989922192565 , width) ,
    (13, 19) : (cor_aresta, 139.2838827718412 , width) ,
    (13, 22) : (cor_aresta, 148.66068747318505 , width) ,
    (13, 16) : (cor_aresta, 131.52946437965903 , width) ,
    (13, 26) : (cor_aresta, 185.29975715040752 , width) ,
    (38, 25) : (cor_aresta, 100.4987562112089 , width) ,
    (38, 27) : (cor_aresta, 150.0 , width) ,
    (16, 22) : (cor_aresta, 144.22205101855957 , width) ,
    (16, 23) : (cor_aresta, 153.16984037335808 , width) ,
    (17, 18) : (cor_aresta, 143.55835050598762 , width) ,
    (19, 20) : (cor_aresta, 148.07092894960846 , width) ,
    (19, 21) : (cor_aresta, 134.5362404707371 , width) ,
    (19, 15) : (cor_aresta, 100.0 , width) ,
    (19, 22) : (cor_aresta, 100.4987562112089 , width) ,
    (20, 24) : (cor_aresta, 117.15374513859983 , width) ,
    (23, 36) : (cor_aresta, 149.0 , width) ,
    (24, 26) : (cor_aresta, 154.8418548067673 , width) ,
    (24, 31) : (cor_aresta, 202.23748416156684 , width) ,
    (25, 30) : (cor_aresta, 152.34500319997372 , width) ,
    (25, 31) : (cor_aresta, 134.1640786499874 , width) ,
    (26, 28) : (cor_aresta, 110.8873302050329 , width) ,
    (26, 29) : (cor_aresta, 160.11246047700348 , width) ,
    (27, 30) : (cor_aresta, 180.96684779262748 , width) ,
    (27, 32) : (cor_aresta, 233.45235059857504 , width) ,
    (28, 34) : (cor_aresta, 158.11388300841898 , width) ,
    (28, 36) : (cor_aresta, 136.01470508735446 , width) ,
    (29, 31) : (cor_aresta, 107.70329614269009 , width) ,
    (30, 33) : (cor_aresta, 123.81033882515628 , width) ,
    (30, 31) : (cor_aresta, 103.58088626768938 , width) ,
    (33, 34) : (cor_aresta, 130.0 , width) ,
    (34, 35) : (cor_aresta, 138.92443989449805 , width) ,
    (35, 37) : (cor_aresta, 104.40306508910551 , width) ,
    (35, 36) : (cor_aresta, 134.1640786499874 , width) ,
    (36, 37) : (cor_aresta, 222.0360331117452 , width) ,
    (37, 39) : (cor_aresta, 106.28264204469137, width) 
}