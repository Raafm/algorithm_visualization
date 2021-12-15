class Node:

    def __init__(self,DATA):
        self.data = DATA
        self.next = None
        self.prev = None
    
def link(node1,node2):
    if node1: node1.next = node2
    if node2: node2.prev = node1

class linked_list:
    def __init__(self):
        self.head   = None
        self.tail   = None
        self.cursor = None
        self.size   = 0

    def push_back(self,data):
        if self.size > 0:
            node = Node(data)
            link(self.tail,node)
            self.tail = self.tail.next
        else:
            self.head = self.tail = Node(data)
        
        self.size += 1

    def push_front(self,data):
        if self.size > 0:
            node = Node(data)
            link(node,self.head)
            self.head = node
        else:
            self.head = self.tail = Node(data)
        
        self.size += 1

    def pop_front(self,data):
        if self.size > 0:
            self.head = self.head.next
            self.size -=1
    
    def pop_back(self,data):
        if self.size > 0:
            self.tail = self.tail.prev
            self.size -=1

    def front(self,data):
        if self.size > 0:
            return self.head.data
    def back(self,data):
        if self.size > 0:
            return self.tail.data
    
    def parse(self):
        if self.cursor is None:
            self.cursor = self.head

        element = self.cursor.data
        self.cursor = self.cursor.next
        
        return element
