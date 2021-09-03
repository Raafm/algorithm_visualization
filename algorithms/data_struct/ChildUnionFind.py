class Node:

    def __init__(self,DATA):
        self.data = DATA
        self.next = None
    

class linked_list:
    def __init__(self,firstNode):
        self.head = firstNode
        self.tail = firstNode
        self.size = 1
    
    def concat(self,other):
        self.tail.next = other.head     # concat the other list to this list
        self.tail = other.tail          # the end of the other list is the new end
        self.size  += other.size 
       

class UnionFind:
    def __init__(self,N):
        self.parent   = list(i for i in range(N))
        self.children = list(linked_list(Node(i)) for i in range(N))
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

        if self.children[Patriarch1].size < self.children[Patriarch2].size:  #this class is made for N_islands Union Find where I need to upgrade everyone
            Patriarch1,Patriarch2 =Patriarch2,Patriarch1


        self.parent[Patriarch2] = Patriarch1

        self.children[Patriarch1].concat(self.children[Patriarch2])

        return element1

    def child_list(self, element):
        elemement = self.Find(element)
        return self.children[elemement]# retorns the linked list  












class Matrix_ChildUnionFind:
    def __init__(self, ROWS,COLS):
        self.parent   =  list(list((x,y) for y in range(COLS)) for x in range(ROWS))
        self.children =  list(list(linked_list(Node((x,y))) for y in range(COLS)) for x in range(ROWS))

    
    def Find(self, position):
        x,y = position
        if self.parent[x][y] == (x,y): return (x,y)
        
        self.parent[x][y] = self.Find(self.parent[x][y])

        return self.parent[x][y]
    
    def Union(self,position1,position2):

        x1,y1 = position1 = self.Find(position1)
        x2,y2 = position2 = self.Find(position2)

        if position1 == position2: return None

        if self.children[x1][y1].size < self.children[x2][y2].size:  #this class is made for N_islands Union Find where I need to upgrade everyone
            x1,x2 = x2,x1
            y1,y2 = y2,y1
        
        self.parent[x2][y2] = (x1,y1)

        self.children[x1][y1].concat(self.children[x2][y2])

        return (x1,y1)

    def child_list(self, position):
        x,y = self.Find(position)
        return self.children[x][y] # retorns the linked list  



#test code
if __name__ == '__main__':

    def print_set(childrenList):
        temp  = childrenList.head
        SIZE = childrenList.size
        print("{",end=" ")
        for _ in range(SIZE):
            print(temp.data, end=", ")
            temp = temp.next
        print("}")

    test = Matrix_ChildUnionFind(5,5)
    option = 1
    while option:
        print("0 to exit\n1 to Union\n2 to find")
        try:
            option = int(input("Enter your option: "))
        except:
            continue

        if option == 1:
            x1 = int(input("x1 = "))
            x2 = int(input("x2 = "))
            y1 = int(input("y1 = "))
            y2 = int(input("y2 = "))

            test.Union((x1,y1),(x2,y2))
            print_set(test.child_list((x1,y1)))
        
        if option == 2:
            x  = int(input("x = "))
            y  = int(input("y = "))
            print("representative:", test.Find((x,y)))
            print_set(test.child_list((x,y)))