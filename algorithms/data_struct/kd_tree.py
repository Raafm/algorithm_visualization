class Node:
    def __init__(self,position):
        self.left  = None
        self.right = None
        self.x = position[0]
        self.y = position[1]

class two_d_tree:

    def __init__(self):
        self.root = None
    
    def insert(self,position):
        xP,yP = position

        if self.root is None:
            self.root = Node(position)
        
        else:
            vertical = True
            cur = self.root
            while True:
                if vertical:
                    if cur.y < yP:
                        if cur.right: cur = cur.right
                        else: cur.right = Node(position)
                    else:
                        if cur.left:  cur = cur.left
                        else: cur.left  = Node(position)
                else:
                    if cur.x < xP:
                        if cur.right: cur = cur.right
                        else: cur.right = Node(position)
                    else:
                        if cur.left:  cur = cur.left
                        else: cur.left  = Node(position)

                vertical = not vertical

  

    def _range_count(self,cur,xL,xR,yU,yD,vertical):
        if cur is None: return 0
        if vertical:
            if   cur.y < yD: return self._range_count(cur.right ,xL,xR,yU,yD,False)
            elif cur.y < yU: 
                Im_in = int ((xL < cur.x) and (cur.x < xR)) 
                return Im_in + self._range_count(cur.left  ,xL,xR,yU,yD,False) + self._range_count(cur.right ,xL,xR,yU,yD,False)
            else:            return self._range_count(cur.left  ,xL,xR,yU,yD,False)
        else:
            if   cur.x < xL: return self._range_count(cur.right ,xL,xR,yU,yD,True)
            elif cur.x < xR: 
                Im_in = int((yD < cur.y) and (cur.x < xR))
                return Im_in + self._range_count(cur.left  ,xL,xR,yU,yD,True) + self._range_count(cur.right ,xL,xR,yU,yD,True)
            else:            return self._range_count(cur.left  ,xL,xR,yU,yD,True)


    def range_count(self,position,width,height):
        xP,yP = position
        xL,xR = xP,xP + width
        yD,yU = yP,yP + height
        vertical = False
        cur = self.root
        return self._range_count(cur,xL,xR,yU,yD,vertical)

        