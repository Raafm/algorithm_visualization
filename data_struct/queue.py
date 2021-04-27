class Node:
    def __init__(self,value = None):
        self.val = value
        self.next = None
class queue:
    def __init__(self): 
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self,data): 
        if self.length == 0:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1

    def pop(self): 
        if self.length == 0:
            return None 
        
        else:
            returned = self.head.val 
            self.head = self.head.next
            self.length -= 1
            return returned

    def not_empty(self):
        return bool(self.length)