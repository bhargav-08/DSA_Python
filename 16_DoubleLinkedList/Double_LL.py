import sys
class Node:
    def __init__(self,value) -> None:
        self.value = value 
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail= None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            
            if node.next==self.head:
                break
            node = node.next
    
    def createDLL(self,value):
        node = Node(value)
        self.head = node
        self.tail = node
        return "Doubly Linked List is Created"
    
    def insert(self,value,location):
        if self.head is None:
            return "Linked List is Empty!!"
        else:
            node = Node(value)
            if location==0:
                node.next =self.head
                self.head.prev = node
                self.head = node
            elif location==1:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                
            else:
                index = 0
                temp = self.head
                while index < location-1:
                    temp =temp.next
                    index+=1
                node.next = temp.next
                temp.next.prev = node
                temp.next = node
                node.prev = temp
                
    def traversal(self):
        if self.head is None:
            print("Linked List is Empty!!")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next   
        
    def reverseTraversal(self):
        if self.head is None:
            print("Linked List is Empty!!")
        else:
            node = self.tail
            while node:
                print(node.value)
                node = node.prev
    
    def search(self,element):
        node =self.head
        while node:
            if node.value==element:
                print(f"{element} is present in Doubly Linked List")
                return
            node= node.next
        print(f"{element} is not presenet in Doubly Linked List")  
         
    def delete(self,location):
        if self.head is None:
            print("Linked List is Empty!!")
            return
        else:
            if location==0:
                if self.head==self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head= self.head.next
                    self.head.prev = None
            elif location==1:
                if self.head==self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next= None
            else:
                index = 0
                temp = self.head
                while index<location-1:
                    temp = temp.next
                    index+=1
                currentNode = temp.next.next
                temp.next = temp.next.next
                currentNode.prev = temp
                    
    def deleteEntire(self):
        self.tail.next = None
        temp = self.head.next
        while temp==self.tail:
            temp.prev = None
            temp = temp.next
        temp.prev = None
        self.head = None
        self.tail = None
        
dll = DoublyLinkedList()
dll.createDLL(5)

dll.insert(12,0)    
dll.insert(20,1)
dll.insert(34,1)
dll.insert(55,2)
dll.insert(22,2)
dll.insert(11,2)

# dll.reverseTraversal()
# dll.search(22)
print([node.value for node in dll])
# dll.delete(0)

# dll.delete(4)
dll.deleteEntire()


print([node.value for node in dll])

# dll.traversal()
        
        
        