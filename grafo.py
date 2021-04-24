cor = (255,255,255)
peso = 1
raio =12
nodes = [
    [cor,(50,30),raio],   #node 0 
    [cor,(130,20),raio],  #node 1
    [cor,(80,100),raio],  #node 2
    [cor,(65,180),raio],  #node 3
    [cor,(180,120),raio], #node 4
    [cor,(280,50),raio],  #node 5
    [cor,(130,320),raio], #node 6
    [cor,(330,110),raio], #node 7
    [cor,(380,220),raio], #node 8
    [cor,(180,235),raio], #node 9
    [cor,(220,400),raio], #node 10
    [cor,(288,520),raio], #node 11
    [cor,(280,180),raio], #node 12
    [cor,(470,410),raio], #node 13
    [cor,(465,70),raio],  #node 14
    [cor,(260,300),raio], #node 15
    [cor,(450,540),raio], #node 16
    [cor,(60,380),raio],  #node 17
    [cor,(160,483),raio], #node 18
    [cor,(340,360),raio], #node 19
    [cor,(485,330),raio], #node 20
    [cor,(440,270),raio], #node 21
    [cor,(330,460),raio], #node 22
    [cor,(580,459),raio], #node 23
    [cor,(560,240),raio], #node 24
    [cor,(640,150),raio], #node 25
    [cor,(650,366),raio], #node 26
    [cor,(630,20),raio],  #node 27
    [cor,(760,380),raio], #node 28
    [cor,(800,310),raio], #node 29
    [cor,(787,110),raio], #node 30
    [cor,(760,210),raio], #node 31
    [cor,(860,60),raio],  #node 32
    [cor,(860,210),raio], #node 33
    [cor,(910,330),raio], #node 34
    [cor,(840,450),raio], #node 35
    [cor,(720,510),raio], #node 36
    [cor,(940,480),raio], #node 37
    [cor,(540,140),raio], #node 38
    [cor,(976,580),raio]  #node 39
  ] 


lista_arestas = [
   [ cor, 0  , 1 , peso],
   [ cor, 0  , 2 , peso],
   [ cor, 1  , 4 , peso],
   [ cor, 2  , 3 , peso],
   [ cor, 2  , 4 , peso],
   [ cor, 3  , 9 , peso],
   [ cor, 4  , 5 , peso],
   [ cor, 4  , 9 , peso],
   [ cor, 5  , 12, peso],
   [ cor, 5  , 14, peso],
   [ cor, 6  , 10, peso],
   [ cor, 6  , 17, peso],
   [ cor, 7  , 8 , peso],
   [ cor, 7  , 12, peso],
   [ cor, 8  , 14, peso],
   [ cor, 8  , 38, peso],
   [ cor, 8  , 21, peso],
   [ cor, 9  ,  6, peso],
   [ cor, 9  , 15, peso],
   [ cor, 10 , 11, peso],
   [ cor, 10 , 18, peso],
   [ cor, 11 , 16, peso],
   [ cor, 13 , 19, peso],
   [ cor, 13 , 22, peso],
   [ cor, 13 , 16, peso],
   [ cor, 13 , 26, peso],
   [ cor, 38 , 25, peso],
   [ cor, 38 , 27, peso],
   [ cor, 16 , 22, peso],
   [ cor, 16 , 23, peso],
   [ cor, 17 , 18, peso],
   [ cor, 19 , 20, peso],
   [ cor, 19 , 21, peso],
   [ cor, 19 , 15, peso],
   [ cor, 19 , 22, peso],
   [ cor, 20 , 24, peso],
   [ cor, 23 , 36, peso],
   [ cor, 24 , 26, peso],
   [ cor, 24 , 31, peso],
   [ cor, 25 , 30, peso],
   [ cor, 25 , 31, peso],
   [ cor, 26 , 28, peso],
   [ cor, 26 , 29, peso],
   [ cor, 27 , 30, peso],
   [ cor, 27 , 32, peso],
   [ cor, 28 , 34, peso],
   [ cor, 28 , 36, peso],
   [ cor, 29 , 31, peso],
   [ cor, 30 , 33, peso],
   [ cor, 30 , 31, peso],
   [ cor, 33 , 34, peso],
   [ cor, 34 , 35, peso],
   [ cor, 35 , 37, peso],
   [ cor, 35 , 36, peso],
   [ cor, 36 , 37 ,peso],
   [ cor, 37 , 39, peso]
]

grafo = [
    [1, 2],
    [0, 4],
    [0, 3, 4],
    [2, 9],
    [1, 2, 5, 9],
    [4, 12, 14],
    [10, 17, 9],
    [8, 12],
    [7, 14, 38, 21],
    [3, 4, 6, 15],
    [6, 11, 18],
    [10, 16],
    [5, 7],
    [19, 22, 16, 26],
    [5, 8],
    [9, 19],
    [11, 13, 22, 23],
    [6, 18],
    [10, 17],
    [13, 20, 21, 15, 22],
    [19, 24],
    [8, 19],
    [13, 16, 19],
    [16, 36],
    [20, 26, 31],
    [38, 30, 31],
    [13, 24, 28, 29],
    [38, 30, 32],
    [26, 34, 36],
    [26, 31],
    [25, 27, 33, 31],
    [24, 25, 29, 30],
    [27],
    [30, 34],
    [28, 33, 35],
    [34, 37, 36],
    [23, 28, 35, 37],
    [35, 36, 39],
    [8, 25, 27],
    [37]
]

