
class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.prev = None
        self.next = None

class DoubleCircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node == self.tail:
                break
            node = node.next
            
    def createDCLL(self,value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = node
        node.prev = node
        
    def insert(self,value,location):
        if self.head is None:
            return "Linked List is Empty!!"
        else:
            node = Node(value)
            if location==0:
                node.next = self.head
                node.prev = self.tail
                self.head.prev = node
                self.tail.next = node
                self.head = node
            elif location==1:
                node.prev = self.tail
                node.next = self.head
                self.tail.next = node
                self.head.prev = node
                self.tail = node
            else:
                index = 0
                temp = self.head
                while index<location-1:
                    temp = temp.next
                    index+=1
                node.prev = temp
                node.next = temp.next
                temp.next.prev = node
                temp.next = node
                
    def traversal(self):
        temp = self.head
        while temp:
            print(temp.value,end=" ")
            if temp.next ==self.head:
                break
            temp = temp.next
        print()
        
    def reverseTraversal(self):
        last = self.tail
        while last:
            print(last.value,end=" ")
            if last.prev ==self.tail:
                break
            last = last.prev
        print()   
    
    def search(self,element):
            node =self.head
            while node:
                if node.value==element:
                    print(f"{element} is present in Doubly Linked List")
                    return
                node= node.next
                if node.next==self.head:
                    print(f"{element} is not present in Doubly Linked List")  
                    return
                    
    def delete(self,location):
        if self.head is None:
            return "Doubly Circular Linked List is Empty!!"
        else:
            if location==0:
                if self.head==self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.tail = None
                    self.head = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail                     
                    self.tail.next = self.head
            elif location==1:
                if self.head==self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.tail = None
                    self.head = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                index = 0 
                temp = self.head
                while index<location-1:
                    temp =temp.next
                    index+=1
                
                temp.next = temp.next.next
                temp.next.prev= temp
                    
    def deleteEntireList(self):
        # self.head.prev=None
        # self.head.next=None
        # self.tail.prev = None
        # self.tail.next = None
        self.head = None
        self.tail = None
                      
dcll = DoubleCircularLinkedList()
dcll.createDCLL(12)
dcll.insert(1,0) # 1 12 12 89 15 46 29 64
dcll.insert(12,1)
dcll.insert(15,1)
dcll.insert(46,1)
dcll.insert(29,1)
dcll.insert(89,3)
dcll.insert(64,1)

# dcll.traversal()
# dcll.reverseTraversal()
# dcll.search(123)
print([node.value for node in dcll])
# dcll.delete(1)
# dcll.delete(1)
# dcll.delete(1)
# dcll.delete(1)  
dcll.deleteEntireList()

print(dcll.head.value)
# print([node.value for node in dcll])