class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        temp = self.head
        
        while temp:
            yield temp
            temp = temp.next
    
    def __str__(self) -> str:
        value = [str(item.data) for item in self]
        return " -> ".join(value)
   
    def insertLL(self,value,index):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            temp = self.head
            if index==0:
                node.next = temp
                self.head = node
            elif index==1:
                while temp.next:
                    temp = temp.next
                temp.next = node
                self.tail= temp
                
            else:
                temp = self.head
                location=0
            
                while  location <index-1:
                    temp = temp.next
                    location+=1
                node.next = temp.next
                temp.next = node
   
class Node:
    def __init__(self,data) -> None:
        self.data  =data
        self.next = None
        
        
firstList = LinkedList()
firstList.insertLL(1,1)
firstList.insertLL(2,1)
firstList.insertLL(3,1)
firstList.insertLL(4,1)
firstList.insertLL(0,0)
firstList.insertLL(10,5)


print(firstList)
