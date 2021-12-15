class UnionFind:
    def __init__(self,N):
        self.parent   = list(i for i in range(N))
        self.rank     = list(0 for _ in range(N))
    
    def Find(self,element):
        if self.parent[element] == element: return element

        Patriarch = self.Find(self.parent[element])
        self.parent[element] = Patriarch

        return Patriarch
    
    def Union(self,element1,element2):
        Patriarch1 = self.Find(self.parent[element1])
        Patriarch2 = self.Find(self.parent[element2])

        if Patriarch1 == Patriarch2: return None

        if self.rank[Patriarch1] < self.rank[Patriarch2]:  
            Patriarch1,Patriarch2 =Patriarch2,Patriarch1


        self.parent[Patriarch2] = Patriarch1


        return element1


class Matrix_UnionFind:
    def __init__(self, ROWS,COLS):
        self.parent   =  list(list((x,y) for y in range(COLS)) for x in range(ROWS))
        self.rank     =  list(list(  1   for y in range(COLS)) for x in range(ROWS))
    
    def Find(self, position):
        x,y = position
        if self.parent[x][y] == (x,y): return (x,y)
        
        self.parent[x][y] = self.Find(self.parent[x][y])

        return self.parent[x][y]
    
    def Union(self,position1,position2):

        x1,y1 = position1 = self.Find(position1)
        x2,y2 = position2 = self.Find(position2)

        if position1 == position2: return None

        if self.rank[x1][y1] < self.rank[x2][y2]:  
            x1,x2 = x2,x1
            y1,y2 = y2,y1
        
        self.parent[x2][y2] = (x1,y1)


        return (x1,y1)