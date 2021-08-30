class Node:
    def __init__(self,DATA):
        self.data = DATA
        self.next = None
        self.prev = None
    



class circular_linked_list:
    def __init__(self):
        self.head = None        
    
    def insert(self,element):
        if self.head is None:
            self.head = Node(element)
            (self.head).prev = self.head
            (self.head).next = self.head
            
        else:
            Next = (self.head).next
            node = Node(element)

            node.next = Next
            Next.prev = node

            (self.head).next = node
            node.prev = self.head

            self.head = node
    
    def remove(self):
        if self.head is None: return

        Prev = (self.head).prev
        Next = (self.head).next

        if self.head == Next:
            self.head = None
            return

        Prev.next = Next 
        Next.prev = Prev
        self.head = Next


    def print_list(self):
        if self.head is None:
            print("None")
            return

        temp = self.head
        beggining = True

        while (temp != self.head) or beggining:
            beggining = False
            print(temp.data, end = " ---> ")
            temp = temp.next
        
        print((self.head).data)
        


if __name__ == '__main__':

    CL = circular_linked_list()
    entrada = 1
    while entrada:

        print("\n1 para insert\n2 para remover\n0 para sair")
        try:
            entrada = int(input("entrada: "))
        except:
            print("digitou errado")
            continue

        if entrada == 1:
            element = input("your input: ")
            CL.insert(element)
        elif entrada == 2:
            CL.remove()

        CL.print_list()