
class Node:
    def __init__(self,value,next=None) -> None:
        self.value = value 
        self.next = next
        
class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next  == self.head:
                break
            node = node.next
            
    def createCLL(self,value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        
    def insert(self,value,location):
        if self.head is None:
            return "Linked List is Empty !!"
        else:
            newNode = Node(value)
        
            if location==0:
                newNode.next = self.head
                self.tail.next = newNode
                self.head = newNode
                
            elif location==1:
                self.tail.next = newNode
                newNode.next = self.head
                self.tail = newNode
                
            else:
                index = 0
                temp = self.head
                while index < location-1:
                    temp = temp.next
                    index+=1
                newNode.next = temp.next
                temp.next = newNode
            
    def traversal(self):

        if self.head is None:
            return "Linked List does not exist!!"
        else:
            node = self.head
            while node:
                print(node.value)
                if node.next == self.tail.next:
                    break
                node = node.next
    
    def search(self,element):
        if self.head is None:
            return "Linked List is empty!!"
        else:
            node = self.head
            while node:
                if node.value ==element:
                    print (f"{element} is present in Linked List")
                    return
                    
                node = node.next
                
                if node == self.tail.next:
                    print(f"{element} is not present in Linked List")
                    return
                
    def deleteNode(self,location):
        if self.head is None:
            return "Linked List is Empty!!"
        else:
            if location==0:
                if self.head==self.tail:
                    first  =self.head
                    first.next = None # self.head.next = None 
                    self.head=None
                    self.tail=None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
                    
            elif location==1:
                if self.head==self.tail:
                    first  =self.head
                    first.next = None
                    self.head=None
                    self.tail=None
                else:
                    temp =self.head
                    while temp is not None:
                        if temp.next == self.tail:
                            break
                        temp = temp.next
                    temp.next = self.head
                    self.tail = temp
            
            else:
                index = 0
                temp =self.head
                
                while index < location-1:
                    temp = temp.next
                    index+=1
                
                temp.next = temp.next.next

    def deleteEntire(self):
        self.tail.next = None
        self.head = None
        self.tail = None

cll = CircularLinkedList()
cll.createCLL(1)   # 56 23 2 47 35 10 
cll.insert(0,0)
cll.insert(2,1)
cll.insert(20,1)
cll.insert(37,1)
cll.insert(3,1)
cll.insert(2,2)
cll.insert(200,1)

# cll.search(200)

print([node.value for node in cll])
# cll.deleteNode(5)
cll.deleteEntire()

print([node.value for node in cll])
# cll.traversal()