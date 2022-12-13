
class Node:
    def __init__(self,value,next=None) -> None:
        self.value = value 
        self.next = next
        
class CLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def __iter__(self):
        temp = self.head
        
        while temp.next ==self.head:
            yield temp
            temp =temp.next
    
    def insertLL(self,value,index):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.tail.next = node
        else:
            if index==0:
                if self.head==self.tail:
                    self.head = node
                    self.tail = node
                    self.head.next= node
                else:
                    node.next = self.head
                    self.tail.next= node
            elif index==1:
                if self.head==self.tail:
                    self.head = node
                    self.tail = node
                    self.tail.next= node                    
                    